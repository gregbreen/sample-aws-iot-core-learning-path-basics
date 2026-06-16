#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import argparse
import json
import os
import shutil
import sys
import time
import traceback

# Add i18n to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "i18n"))

# Add iot_helpers to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import boto3
from botocore.exceptions import ClientError
from language_selector import get_language
from loader import load_messages
from confirm_input import is_yes

# Import iot_helpers modules
from iot_helpers.cleanup.resource_identifier import ResourceIdentifier
from iot_helpers.cleanup.deletion_engine import DeletionEngine
from iot_helpers.cleanup.reporter import CleanupReporter
from iot_helpers.utils.dependency_handler import DependencyHandler
from iot_helpers.utils.naming_conventions import validate_thing_prefix

# Sample data patterns created by setup scripts
SAMPLE_THING_TYPES = ["SedanVehicle", "SUVVehicle", "TruckVehicle"]
SAMPLE_THING_GROUPS = ["CustomerFleet", "TestFleet", "MaintenanceFleet", "DealerFleet"]
SAMPLE_THING_PREFIX = "Vehicle-VIN-"  # Things created as Vehicle-VIN-001, Vehicle-VIN-002, etc.

# Global variables
USER_LANG = "en"
messages = {}
DEBUG_MODE = False


def get_message(key, *args):
    """Get localized message with optional formatting"""
    msg = messages.get(key, key)
    if args:
        return msg.format(*args)
    return msg


def debug_print(message):
    """Print debug message if debug mode is enabled"""
    if DEBUG_MODE:
        print(message)


def log_api_call(operation, description, params=None, response=None):
    """Log API call details in debug mode"""
    if not DEBUG_MODE:
        return

    print(f"\n{get_message('api_call_header', operation)}")
    print(f"{get_message('api_description', description)}")

    if params:
        print(get_message("api_input_params"))
        print(json.dumps(params, indent=2, default=str))
    else:
        print(get_message("api_no_params"))

    if response is not None:
        print(get_message("api_response"))
        if response:
            print(json.dumps(response, indent=2, default=str))
        else:
            print(get_message("api_empty_response"))


def clean_certificate(iot_client, certificate_arn):
    """Clean up a certificate and its associated policies"""
    try:
        certificate_id = certificate_arn.split("/")[-1]
        print(f"  {get_message('cleaning_certificate', certificate_id)}")

        # Step 1: List and detach policies
        print(f"    {get_message('step1_list_policies')}")
        list_params = {"target": certificate_arn}
        log_api_call(
            "list_attached_policies",
            "List policies attached to certificate",
            list_params,
        )

        policies_response = iot_client.list_attached_policies(target=certificate_arn)
        log_api_call(
            "list_attached_policies",
            "List policies attached to certificate",
            list_params,
            policies_response,
        )

        policies = policies_response.get("policies", [])
        print(f"    {get_message('found_attached_policies', len(policies))}")

        # Detach policies
        for policy in policies:
            policy_name = policy["policyName"]
            print(f"    {get_message('detaching_policy', policy_name)}")

            detach_params = {"policyName": policy_name, "target": certificate_arn}
            log_api_call("detach_policy", "Detach policy from certificate", detach_params)

            iot_client.detach_policy(policyName=policy_name, target=certificate_arn)
            log_api_call("detach_policy", "Detach policy from certificate", detach_params, {})

        # Step 2: List and detach from Things
        list_things_params = {"principal": certificate_arn}
        log_api_call(
            "list_principal_things",
            "List Things attached to certificate",
            list_things_params,
        )

        things_response = iot_client.list_principal_things(principal=certificate_arn)
        log_api_call(
            "list_principal_things",
            "List Things attached to certificate",
            list_things_params,
            things_response,
        )

        things = things_response.get("things", [])

        # Detach from Things
        for thing_name in things:
            print(f"    {get_message('detaching_cert_from_thing', thing_name)}")

            detach_thing_params = {
                "thingName": thing_name,
                "principal": certificate_arn,
            }
            log_api_call(
                "detach_thing_principal",
                "Detach certificate from Thing",
                detach_thing_params,
            )

            iot_client.detach_thing_principal(thingName=thing_name, principal=certificate_arn)
            log_api_call(
                "detach_thing_principal",
                "Detach certificate from Thing",
                detach_thing_params,
                {},
            )

        # Step 3: Deactivate certificate
        print(f"    {get_message('deactivating_certificate', certificate_id)}")

        update_params = {"certificateId": certificate_id, "newStatus": "INACTIVE"}
        log_api_call("update_certificate", "Deactivate certificate", update_params)

        iot_client.update_certificate(certificateId=certificate_id, newStatus="INACTIVE")
        log_api_call("update_certificate", "Deactivate certificate", update_params, {})

        print(f"    {get_message('certificate_deactivated', certificate_id)}")

        # Step 4: Delete certificate
        print(f"    {get_message('deleting_certificate', certificate_id)}")

        delete_params = {"certificateId": certificate_id}
        log_api_call("delete_certificate", "Delete certificate", delete_params)

        iot_client.delete_certificate(certificateId=certificate_id)
        log_api_call("delete_certificate", "Delete certificate", delete_params, {})

        return True

    except Exception as e:
        print(f"    {get_message('error_cleaning_certificate', certificate_id, str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_error')}")
            print(json.dumps(str(e), indent=2))
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return False


def cleanup_sample_things(iot_client):
    """Clean up sample Things and their certificates"""
    print(f"\n{get_message('step1_title')}")
    print(get_message("step_separator"))

    # List all Things
    print(get_message("listing_things"))

    log_api_call("list_things", "List all Things to find sample Things")

    try:
        response = iot_client.list_things()
        log_api_call("list_things", "List all Things to find sample Things", None, response)

        all_things = response.get("things", [])

        # Filter sample Things
        sample_things = [thing for thing in all_things if thing["thingName"].startswith(SAMPLE_THING_PREFIX)]

        print(get_message("found_sample_things", len(sample_things)))

        certificates_cleaned = 0

        for thing in sample_things:
            thing_name = thing["thingName"]
            print(f"\n{get_message('processing_thing', thing_name)}")

            # List principals (certificates) for this Thing
            print(f"  {get_message('listing_principals', thing_name)}")

            list_principals_params = {"thingName": thing_name}
            log_api_call(
                "list_thing_principals",
                "List certificates attached to Thing",
                list_principals_params,
            )

            try:
                principals_response = iot_client.list_thing_principals(thingName=thing_name)
                log_api_call(
                    "list_thing_principals",
                    "List certificates attached to Thing",
                    list_principals_params,
                    principals_response,
                )

                principals = principals_response.get("principals", [])
                print(f"  {get_message('found_certificates', len(principals), thing_name)}")

                # Clean up certificates
                for principal in principals:
                    if clean_certificate(iot_client, principal):
                        certificates_cleaned += 1

            except ClientError as e:
                print(f"  {get_message('error_generic', str(e))}")
                if DEBUG_MODE:
                    print(f"{get_message('debug_full_error')}")
                    print(json.dumps(e.response, indent=2, default=str))

            # Delete the Thing
            print(f"  {get_message('deleting_thing', thing_name)}")

            delete_thing_params = {"thingName": thing_name}
            log_api_call("delete_thing", "Delete Thing", delete_thing_params)

            try:
                iot_client.delete_thing(thingName=thing_name)
                log_api_call("delete_thing", "Delete Thing", delete_thing_params, {})
                print(f"  {get_message('deleted_resource', 'Thing', thing_name)}")

            except ClientError as e:
                if e.response["Error"]["Code"] == "ResourceNotFoundException":
                    print(f"  {get_message('resource_not_found', 'Thing', thing_name)}")
                else:
                    print(f"  {get_message('error_deleting_resource', 'Thing', thing_name, str(e))}")
                    if DEBUG_MODE:
                        print(f"{get_message('debug_full_error')}")
                        print(json.dumps(e.response, indent=2, default=str))

        return certificates_cleaned

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0


def cleanup_orphaned_certificates(iot_client):
    """Check for and report orphaned certificates"""
    print(f"\n{get_message('step2_title')}")
    print(get_message("step_separator"))

    print(get_message("listing_certificates"))

    log_api_call("list_certificates", "List all certificates to check for orphaned ones")

    try:
        response = iot_client.list_certificates()
        log_api_call(
            "list_certificates",
            "List all certificates to check for orphaned ones",
            None,
            response,
        )

        certificates = response.get("certificates", [])
        print(get_message("found_certificates_account", len(certificates)))

        skipped_certificates = 0

        for cert in certificates:
            cert_id = cert["certificateId"]
            cert_status = cert["status"]
            cert_arn = cert["certificateArn"]

            print(get_message("certificate_info", cert_id, cert_status))

            # Check if certificate is attached to any Things
            print(f"  {get_message('checking_certificate_things', cert_id)}")

            list_things_params = {"principal": cert_arn}
            log_api_call(
                "list_principal_things",
                "Check Things attached to certificate",
                list_things_params,
            )

            try:
                things_response = iot_client.list_principal_things(principal=cert_arn)
                log_api_call(
                    "list_principal_things",
                    "Check Things attached to certificate",
                    list_things_params,
                    things_response,
                )

                attached_things = things_response.get("things", [])

                # Check if any attached Things are sample Things
                sample_things_attached = [thing for thing in attached_things if thing.startswith(SAMPLE_THING_PREFIX)]

                if sample_things_attached:
                    print(f"  {get_message('cert_attached_sample_things', cert_id, ', '.join(sample_things_attached))}")
                    print(f"  {get_message('cert_should_cleanup_step1')}")
                else:
                    print(f"  {get_message('cert_not_attached_sample', cert_id)}")
                    skipped_certificates += 1

            except ClientError as e:
                print(f"  {get_message('could_not_check_things', cert_id, str(e))}")
                skipped_certificates += 1
                if DEBUG_MODE:
                    print(f"{get_message('debug_full_error')}")
                    print(json.dumps(e.response, indent=2, default=str))

        return skipped_certificates

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0


def cleanup_sample_policies(iot_client):
    """Clean up sample policies"""
    print(f"\n{get_message('step3_title')}")
    print(get_message("step_separator"))

    print(get_message("listing_policies"))

    log_api_call("list_policies", "List all policies to check for cleanup")

    try:
        response = iot_client.list_policies()
        log_api_call("list_policies", "List all policies to check for cleanup", None, response)

        policies = response.get("policies", [])
        print(get_message("found_policies_account", len(policies)))

        deleted_policies = 0
        skipped_policies = 0

        for policy in policies:
            policy_name = policy["policyName"]
            print(get_message("checking_policy", policy_name))

            # Check if policy matches sample patterns
            is_sample_policy = (
                policy_name.startswith("SamplePolicy")
                or policy_name.startswith("VehiclePolicy")
                or "Sample" in policy_name
                or "Vehicle" in policy_name
            )

            if not is_sample_policy:
                print(f"  {get_message('policy_no_sample_patterns', policy_name)}")
                continue

            # Check if policy is attached to any targets
            print(f"  {get_message('checking_policy_targets', policy_name)}")

            list_targets_params = {"policyName": policy_name}
            log_api_call("list_policy_targets", "Check targets for policy", list_targets_params)

            try:
                targets_response = iot_client.list_targets_for_policy(policyName=policy_name)
                log_api_call(
                    "list_policy_targets",
                    "Check targets for policy",
                    list_targets_params,
                    targets_response,
                )

                targets = targets_response.get("targets", [])

                if targets:
                    print(f"  {get_message('policy_attached_targets', policy_name, len(targets))}")
                    skipped_policies += 1
                else:
                    print(f"  {get_message('deleting_unattached_policy', policy_name)}")

                    delete_policy_params = {"policyName": policy_name}
                    log_api_call(
                        "delete_policy",
                        "Delete unattached policy",
                        delete_policy_params,
                    )

                    iot_client.delete_policy(policyName=policy_name)
                    log_api_call(
                        "delete_policy",
                        "Delete unattached policy",
                        delete_policy_params,
                        {},
                    )

                    deleted_policies += 1

            except ClientError as e:
                print(f"  {get_message('error_checking_policy', policy_name, str(e))}")
                skipped_policies += 1
                if DEBUG_MODE:
                    print(f"{get_message('debug_full_error')}")
                    print(json.dumps(e.response, indent=2, default=str))

        # Summary
        print(f"\n{get_message('policy_cleanup_summary')}")
        print(get_message("deleted_policies", deleted_policies))
        print(get_message("skipped_policies", skipped_policies))

        return deleted_policies, skipped_policies

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0, 0


def cleanup_sample_thing_groups(iot_client):
    """Clean up sample Thing Groups"""
    print(f"\n{get_message('step4_title')}")
    print(get_message("step_separator"))

    print(get_message("listing_thing_groups"))

    log_api_call("list_thing_groups", "List all Thing Groups to find sample groups")

    try:
        response = iot_client.list_thing_groups()
        log_api_call(
            "list_thing_groups",
            "List all Thing Groups to find sample groups",
            None,
            response,
        )

        all_groups = response.get("thingGroups", [])

        # Filter sample Thing Groups
        sample_groups = [group for group in all_groups if group["groupName"] in SAMPLE_THING_GROUPS]

        print(get_message("found_sample_groups", len(sample_groups)))

        for group in sample_groups:
            group_name = group["groupName"]
            print(f"{get_message('deleting_thing_group', group_name)}")

            delete_group_params = {"thingGroupName": group_name}
            log_api_call("delete_thing_group", "Delete Thing Group", delete_group_params)

            try:
                iot_client.delete_thing_group(thingGroupName=group_name)
                log_api_call("delete_thing_group", "Delete Thing Group", delete_group_params, {})
                print(f"  {get_message('deleted_resource', 'Thing Group', group_name)}")

            except ClientError as e:
                if e.response["Error"]["Code"] == "ResourceNotFoundException":
                    print(f"  {get_message('resource_not_found', 'Thing Group', group_name)}")
                else:
                    print(f"  {get_message('error_deleting_resource', 'Thing Group', group_name, str(e))}")
                    if DEBUG_MODE:
                        print(f"{get_message('debug_full_error')}")
                        print(json.dumps(e.response, indent=2, default=str))

        return len(sample_groups)

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0


def cleanup_sample_thing_types(iot_client):
    """Clean up sample Thing Types"""
    print(f"\n{get_message('step5_title')}")
    print(get_message("step_separator"))

    print(get_message("listing_thing_types"))

    log_api_call("list_thing_types", "List all Thing Types to find sample types")

    try:
        response = iot_client.list_thing_types()
        log_api_call(
            "list_thing_types",
            "List all Thing Types to find sample types",
            None,
            response,
        )

        all_types = response.get("thingTypes", [])

        # Filter sample Thing Types
        sample_types = [thing_type for thing_type in all_types if thing_type["thingTypeName"] in SAMPLE_THING_TYPES]

        print(get_message("found_sample_types", len(sample_types)))

        if not sample_types:
            print(get_message("no_sample_types"))
            return 0

        # Check status of each Thing Type
        deprecated_types = []
        active_types = []

        for thing_type in sample_types:
            type_name = thing_type["thingTypeName"]

            describe_params = {"thingTypeName": type_name}
            log_api_call("describe_thing_type", "Check Thing Type status", describe_params)

            try:
                describe_response = iot_client.describe_thing_type(thingTypeName=type_name)
                log_api_call(
                    "describe_thing_type",
                    "Check Thing Type status",
                    describe_params,
                    describe_response,
                )

                metadata = describe_response.get("thingTypeMetadata", {})
                deprecation_date = metadata.get("deprecationDate")

                if deprecation_date:
                    print(get_message("thing_type_deprecated", type_name, deprecation_date))
                    deprecated_types.append((type_name, deprecation_date))
                else:
                    print(get_message("thing_type_active", type_name))
                    active_types.append(type_name)

            except ClientError as e:
                print(get_message("could_not_check_status", type_name, str(e)))
                if DEBUG_MODE:
                    print(f"{get_message('debug_full_error')}")
                    print(json.dumps(e.response, indent=2, default=str))

        # Deprecate active Thing Types
        if active_types:
            print(f"\n{get_message('deprecating_active_types', len(active_types))}")

            for type_name in active_types:
                print(get_message("deprecating_thing_type", type_name))

                deprecate_params = {"thingTypeName": type_name}
                log_api_call("deprecate_thing_type", "Deprecate Thing Type", deprecate_params)

                try:
                    iot_client.deprecate_thing_type(thingTypeName=type_name)
                    log_api_call(
                        "deprecate_thing_type",
                        "Deprecate Thing Type",
                        deprecate_params,
                        {},
                    )

                    print(f"  {get_message('thing_type_deprecated_success', type_name)}")
                    deprecated_types.append((type_name, time.time()))

                except ClientError as e:
                    print(f"  {get_message('could_not_deprecate', type_name)}")
                    if DEBUG_MODE:
                        print(f"{get_message('debug_full_error')}")
                        print(json.dumps(e.response, indent=2, default=str))

        # Handle deletion with 5-minute constraint
        if deprecated_types:
            print(f"\n{get_message('aws_constraint_5min')}")
            print(get_message("thing_types_to_delete"))

            for type_name, dep_date in deprecated_types:
                if isinstance(dep_date, float):
                    dep_date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(dep_date))
                else:
                    dep_date_str = str(dep_date)
                print(get_message("deprecated_item", type_name, dep_date_str))

            print(f"\n{get_message('deletion_options')}")
            print(get_message("wait_5min_delete"))
            print(get_message("skip_deletion"))
            print(get_message("try_deletion_now"))

            while True:
                try:
                    choice = input(get_message("select_option_1_3")).strip()

                    if choice == "1":
                        # Wait 5 minutes
                        print(f"\n{get_message('waiting_5min')}")
                        print(get_message("constraint_explanation"))

                        try:
                            for i in range(300, 0, -1):  # 5 minutes = 300 seconds
                                minutes = i // 60
                                seconds = i % 60
                                print(
                                    f"\r{get_message('time_remaining', minutes, seconds)}",
                                    end="",
                                    flush=True,
                                )
                                time.sleep(1)

                            print(f"\n{get_message('wait_completed')}")

                        except KeyboardInterrupt:
                            print(f"\n{get_message('cleanup_interrupted')}")
                            print(get_message("types_deprecated_delete_later"))
                            return len(deprecated_types)

                        break

                    elif choice == "2":
                        print(f"\n{get_message('skipping_deletion')}")
                        print(get_message("deletion_tip"))
                        print(get_message("types_ready_deletion"))
                        return len(deprecated_types)

                    elif choice == "3":
                        print(f"\n{get_message('attempting_deletion_now')}")
                        break

                    else:
                        print(get_message("invalid_choice_1_3"))

                except KeyboardInterrupt:
                    print(f"\n{get_message('cleanup_interrupted')}")
                    print(get_message("types_deprecated_delete_later"))
                    return len(deprecated_types)

            # Delete deprecated Thing Types
            print(f"\n{get_message('deleting_deprecated_types')}")
            deleted_count = 0

            for type_name, _ in deprecated_types:
                print(get_message("attempting_delete_type", type_name))

                delete_params = {"thingTypeName": type_name}
                log_api_call("delete_thing_type", "Delete Thing Type", delete_params)

                try:
                    iot_client.delete_thing_type(thingTypeName=type_name)
                    log_api_call("delete_thing_type", "Delete Thing Type", delete_params, {})

                    print(f"  {get_message('deleted_resource', 'Thing Type', type_name)}")
                    deleted_count += 1

                except ClientError as e:
                    print(f"  {get_message('error_deleting_resource', 'Thing Type', type_name, str(e))}")
                    if DEBUG_MODE:
                        print(f"{get_message('debug_full_error')}")
                        print(json.dumps(e.response, indent=2, default=str))

            if deleted_count < len(deprecated_types):
                print(f"\n{get_message('deletion_failed_timing')}")
                for type_name, _ in deprecated_types:
                    print(get_message("type_ready_deletion", type_name))

            return deleted_count

        return 0

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0


def cleanup_device_shadows():
    """Device shadows cleanup (automatic)"""
    print(f"\n{get_message('step6_title')}")
    print(get_message("step_separator"))

    print(get_message("shadows_auto_cleanup"))
    print(get_message("no_manual_shadow_cleanup"))

    debug_print(get_message("debug_shadow_skipped"))

    print(get_message("shadow_cleanup_completed"))


def cleanup_sample_rules(iot_client):
    """Clean up sample IoT rules"""
    print(f"\n{get_message('step7_title')}")
    print(get_message("step_separator"))

    debug_print(get_message("debug_listing_rules"))

    log_api_call("list_topic_rules", "List all IoT rules")

    try:
        response = iot_client.list_topic_rules()
        log_api_call("list_topic_rules", "List all IoT rules", None, response)

        rules = response.get("rules", [])
        deleted_rules = 0

        for rule in rules:
            rule_name = rule["ruleName"]

            # Check if rule matches sample patterns
            is_sample_rule = (
                rule_name.startswith("SampleRule")
                or rule_name.startswith("VehicleRule")
                or "Sample" in rule_name
                or "Vehicle" in rule_name
                or "Learning" in rule_name
            )

            if is_sample_rule:
                debug_print(get_message("debug_deleting_rule", rule_name))

                delete_rule_params = {"ruleName": rule_name}
                log_api_call("delete_topic_rule", "Delete IoT rule", delete_rule_params)

                try:
                    iot_client.delete_topic_rule(ruleName=rule_name)
                    log_api_call("delete_topic_rule", "Delete IoT rule", delete_rule_params, {})

                    print(get_message("deleted_rule", rule_name))
                    deleted_rules += 1

                except ClientError as e:
                    print(get_message("error_deleting_rule", rule_name, str(e)))
                    if DEBUG_MODE:
                        print(f"{get_message('debug_full_error')}")
                        print(json.dumps(e.response, indent=2, default=str))

        if deleted_rules == 0:
            print(get_message("no_sample_rules"))

        print(get_message("rules_cleanup_summary", deleted_rules))
        return deleted_rules

    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
        return 0


def cleanup_iam_resources(iot_client, iam_client):
    """Clean up IAM resources by following IoT rule dependencies"""
    print(f"\n{get_message('step8_title')}")
    print(get_message("step_separator"))
    
    workshop_tag_key = "workshop"
    workshop_tag_value = "learning-aws-iot-core-basics"
    
    debug_print(get_message("debug_cleaning_iam_resources"))
    
    try:
        # Step 1: Scan all IoT rules for workshop tags
        print(get_message("scanning_rules_for_iam"))
        
        log_api_call("list_topic_rules", "List all IoT rules to find workshop-tagged rules")
        
        rules_response = iot_client.list_topic_rules()
        log_api_call("list_topic_rules", "List all IoT rules to find workshop-tagged rules", None, rules_response)
        
        all_rules = rules_response.get("rules", [])
        workshop_rules = []
        
        # Check each rule for workshop tags
        for rule in all_rules:
            rule_name = rule["ruleName"]
            
            try:
                # Get rule ARN to check tags
                region = iot_client.meta.region_name
                sts_client = boto3.client('sts')
                account_id = sts_client.get_caller_identity()['Account']
                rule_arn = f"arn:aws:iot:{region}:{account_id}:rule/{rule_name}"
                
                # Check tags
                tags_response = iot_client.list_tags_for_resource(resourceArn=rule_arn)
                tags = tags_response.get('tags', [])
                
                # Check if rule has workshop tag
                has_workshop_tag = any(
                    tag['Key'] == workshop_tag_key and tag['Value'] == workshop_tag_value
                    for tag in tags
                )
                
                if has_workshop_tag:
                    workshop_rules.append(rule_name)
                    debug_print(f"Found workshop-tagged rule: {rule_name}")
                    
            except ClientError as e:
                debug_print(f"Could not check tags for rule {rule_name}: {str(e)}")
                continue
        
        if not workshop_rules:
            print(get_message("no_workshop_rules_found"))
            print(get_message("iam_cleanup_completed"))
            return
        
        print(get_message("found_workshop_rules", len(workshop_rules)))
        
        # Step 2: Extract IAM role ARNs from rule actions
        role_arns = set()
        
        for rule_name in workshop_rules:
            debug_print(f"Inspecting rule: {rule_name}")
            
            try:
                log_api_call("get_topic_rule", f"Get rule details for {rule_name}", {"ruleName": rule_name})
                
                rule_response = iot_client.get_topic_rule(ruleName=rule_name)
                log_api_call("get_topic_rule", f"Get rule details for {rule_name}", {"ruleName": rule_name}, rule_response)
                
                rule_payload = rule_response.get("rule", {})
                actions = rule_payload.get("actions", [])
                
                # Check each action for roleArn
                for action in actions:
                    role_arn = None
                    
                    if "republish" in action:
                        role_arn = action["republish"].get("roleArn")
                    elif "s3" in action:
                        role_arn = action["s3"].get("roleArn")
                    elif "lambda" in action:
                        role_arn = action["lambda"].get("roleArn")
                    elif "kinesis" in action:
                        role_arn = action["kinesis"].get("roleArn")
                    elif "firehose" in action:
                        role_arn = action["firehose"].get("roleArn")
                    elif "dynamoDB" in action:
                        role_arn = action["dynamoDB"].get("roleArn")
                    elif "dynamoDBv2" in action:
                        role_arn = action["dynamoDBv2"].get("roleArn")
                    elif "sns" in action:
                        role_arn = action["sns"].get("roleArn")
                    elif "sqs" in action:
                        role_arn = action["sqs"].get("roleArn")
                    elif "cloudwatchMetric" in action:
                        role_arn = action["cloudwatchMetric"].get("roleArn")
                    elif "cloudwatchAlarm" in action:
                        role_arn = action["cloudwatchAlarm"].get("roleArn")
                    elif "elasticsearch" in action:
                        role_arn = action["elasticsearch"].get("roleArn")
                    elif "salesforce" in action:
                        role_arn = action["salesforce"].get("roleArn")
                    elif "iotAnalytics" in action:
                        role_arn = action["iotAnalytics"].get("roleArn")
                    elif "iotEvents" in action:
                        role_arn = action["iotEvents"].get("roleArn")
                    elif "stepFunctions" in action:
                        role_arn = action["stepFunctions"].get("roleArn")
                    
                    if role_arn:
                        role_arns.add(role_arn)
                        debug_print(f"Found role ARN in action: {role_arn}")
                        
            except ClientError as e:
                print(f"  {get_message('error_getting_rule', rule_name, str(e))}")
                if DEBUG_MODE:
                    print(f"{get_message('debug_full_error')}")
                    print(json.dumps(e.response, indent=2, default=str))
        
        if not role_arns:
            print(get_message("no_iam_roles_in_rules"))
            print(get_message("iam_cleanup_completed"))
            return
        
        # Step 3: Parse role names from ARNs and clean up
        print(f"\n{get_message('found_iam_roles', len(role_arns))}")
        
        for role_arn in role_arns:
            # Parse role name from ARN: arn:aws:iam::account:role/RoleName
            try:
                role_name = role_arn.split("/")[-1]
                print(f"\n  {get_message('processing_iam_role', role_name)}")
                
                # Check if role exists
                try:
                    iam_client.get_role(RoleName=role_name)
                    print(f"    {get_message('found_iam_role', role_name)}")
                    
                    # List and detach managed policies
                    policies_to_delete = []
                    
                    try:
                        attached_policies = iam_client.list_attached_role_policies(RoleName=role_name)
                        for policy in attached_policies.get('AttachedPolicies', []):
                            policy_arn = policy['PolicyArn']
                            policy_name = policy['PolicyName']
                            
                            # Check if this is a customer-managed policy (not AWS managed)
                            if not policy_arn.startswith('arn:aws:iam::aws:policy/'):
                                # Check tags on the policy
                                try:
                                    policy_tags_response = iam_client.list_policy_tags(PolicyArn=policy_arn)
                                    policy_tags = policy_tags_response.get('Tags', [])
                                    
                                    # Check if policy has workshop tag
                                    has_workshop_tag = any(
                                        tag['Key'] == workshop_tag_key and tag['Value'] == workshop_tag_value
                                        for tag in policy_tags
                                    )
                                    
                                    if has_workshop_tag:
                                        print(f"      ✅ {get_message('policy_has_workshop_tag', policy_name)}")
                                        policies_to_delete.append((policy_arn, policy_name))
                                    else:
                                        print(f"      ⚠️  {get_message('policy_no_workshop_tag', policy_name)}")
                                        debug_print(f"Policy {policy_name} does not have workshop tag, skipping deletion")
                                except ClientError as tag_error:
                                    print(f"      ⚠️  {get_message('cannot_check_policy_tags', policy_name)}")
                                    debug_print(f"Error checking tags: {str(tag_error)}")
                            
                            # Detach the policy from the role
                            print(f"      {get_message('detaching_policy', policy_name)}")
                            iam_client.detach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
                            debug_print(f"Detached managed policy: {policy_arn}")
                            
                    except ClientError as e:
                        print(f"      {get_message('error_detaching_policies', str(e))}")
                        if DEBUG_MODE:
                            print(f"{get_message('debug_full_error')}")
                            print(json.dumps(e.response, indent=2, default=str))
                    
                    # List and delete inline policies
                    try:
                        inline_policies = iam_client.list_role_policies(RoleName=role_name)
                        for policy_name_inline in inline_policies.get('PolicyNames', []):
                            print(f"      {get_message('deleting_inline_policy', policy_name_inline)}")
                            iam_client.delete_role_policy(RoleName=role_name, PolicyName=policy_name_inline)
                            debug_print(f"Deleted inline policy: {policy_name_inline}")
                    except ClientError as e:
                        print(f"      {get_message('error_deleting_inline_policies', str(e))}")
                        if DEBUG_MODE:
                            print(f"{get_message('debug_full_error')}")
                            print(json.dumps(e.response, indent=2, default=str))
                    
                    # Delete the role
                    print(f"    {get_message('deleting_iam_role', role_name)}")
                    iam_client.delete_role(RoleName=role_name)
                    print(f"    ✅ {get_message('deleted_resource', 'IAM Role', role_name)}")
                    
                    # Now delete the tagged policies that were attached to the role
                    if policies_to_delete:
                        for policy_arn, policy_name_to_delete in policies_to_delete:
                            try:
                                print(f"      {get_message('deleting_iam_policy', policy_name_to_delete)}")
                                iam_client.delete_policy(PolicyArn=policy_arn)
                                print(f"      ✅ {get_message('deleted_resource', 'IAM Policy', policy_name_to_delete)}")
                            except ClientError as e:
                                print(f"      ❌ {get_message('error_deleting_iam_policy', policy_name_to_delete, str(e))}")
                                if DEBUG_MODE:
                                    print(f"{get_message('debug_full_error')}")
                                    print(json.dumps(e.response, indent=2, default=str))
                    
                except ClientError as e:
                    if e.response["Error"]["Code"] == "NoSuchEntity":
                        print(f"    {get_message('iam_role_not_found', role_name)}")
                    else:
                        print(f"    {get_message('error_checking_iam_role', role_name, str(e))}")
                        if DEBUG_MODE:
                            print(f"{get_message('debug_full_error')}")
                            print(json.dumps(e.response, indent=2, default=str))
                            
            except Exception as e:
                print(f"  {get_message('error_parsing_role_arn', role_arn, str(e))}")
                if DEBUG_MODE:
                    traceback.print_exc()
    
    except Exception as e:
        print(f"{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()
    
    print(f"\n{get_message('iam_cleanup_completed')}")


def cleanup_local_files():
    """Clean up local certificate files"""
    print(f"\n{get_message('step9_title')}")
    print(get_message("step_separator"))

    # Clean up certificates directory
    cert_dir = os.path.join(os.path.dirname(__file__), "..", "certificates")
    cert_dir = os.path.abspath(cert_dir)

    print(get_message("checking_cert_directory", cert_dir))

    if os.path.exists(cert_dir):
        print(get_message("cert_directory_contents"))
        try:
            for item in os.listdir(cert_dir):
                print(f"  • {item}")

            shutil.rmtree(cert_dir)
            print(get_message("removed_cert_directory", cert_dir))
            debug_print(get_message("directory_deleted_success", cert_dir))

        except Exception as e:
            print(get_message("error_removing_cert_dir", str(e)))
            if DEBUG_MODE:
                print(f"{get_message('debug_full_traceback')}")
                traceback.print_exc()
    else:
        print(get_message("no_cert_directory"))
        debug_print(get_message("directory_not_exist", cert_dir))

    # Clean up sample-certs directory
    sample_cert_dir = os.path.join(os.path.dirname(__file__), "..", "sample-certs")
    sample_cert_dir = os.path.abspath(sample_cert_dir)

    print(f"\n{get_message('checking_sample_cert_dir', sample_cert_dir)}")

    if os.path.exists(sample_cert_dir):
        print(get_message("sample_cert_contents"))
        try:
            for item in os.listdir(sample_cert_dir):
                print(f"  • {item}")

            shutil.rmtree(sample_cert_dir)
            print(get_message("removed_sample_cert_dir", sample_cert_dir))
            debug_print(get_message("directory_deleted_success", sample_cert_dir))

        except Exception as e:
            print(get_message("error_removing_sample_dir", str(e)))
            if DEBUG_MODE:
                print(f"{get_message('debug_full_traceback')}")
                traceback.print_exc()
    else:
        print(get_message("no_sample_cert_dir"))
        debug_print(get_message("directory_not_exist", sample_cert_dir))

    # Clean up device state files
    script_dir = os.path.dirname(__file__)
    for filename in os.listdir(script_dir):
        if filename.startswith("device_state") and filename.endswith(".json"):
            file_path = os.path.join(script_dir, filename)
            try:
                os.remove(file_path)
                debug_print(f"Removed device state file: {filename}")
            except Exception as e:
                debug_print(f"Error removing {filename}: {e}")


def list_all_rules(iot_client):
    """List all IoT rules"""
    try:
        response = iot_client.list_topic_rules()
        return response.get('rules', [])
    except Exception as e:
        if DEBUG_MODE:
            print(f"Error listing rules: {e}")
        return []


def main():
    global USER_LANG, messages, DEBUG_MODE

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Clean up AWS IoT Core sample resources created by workshop setup scripts"
    )
    parser.add_argument(
        '--things-prefix',
        default='Vehicle-VIN-',
        help='Prefix for thing names (default: Vehicle-VIN-)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Identify resources without deleting them'
    )
    parser.add_argument(
        '--debug',
        '-d',
        action='store_true',
        help='Enable debug mode with detailed API call logging'
    )
    
    args = parser.parse_args()
    
    # Set debug mode
    DEBUG_MODE = args.debug
    
    # Validate things prefix
    if not validate_thing_prefix(args.things_prefix):
        print(f"Error: Invalid things prefix '{args.things_prefix}'")
        print("Prefix must start with a letter and contain only alphanumeric characters, hyphens, and underscores")
        sys.exit(1)

    # Get language preference
    USER_LANG = get_language()

    # Load messages
    messages = load_messages("cleanup_sample_data", USER_LANG)

    print(get_message("title"))
    print(get_message("separator"))
    
    if args.dry_run:
        print(f"\n{'='*60}")
        print("DRY RUN MODE - No resources will be deleted")
        print(f"{'='*60}")

    # AWS context information
    print(f"\n{get_message('aws_context_info')}")
    try:
        sts_client = boto3.client("sts")
        identity = sts_client.get_caller_identity()
        print(f"  {get_message('account_id')}: {identity.get('Account', 'Unknown')}")
        print(f"  {get_message('region')}: {boto3.Session().region_name or 'us-east-1'}")
    except Exception as e:
        print(get_message("aws_context_error", str(e)))
        print(get_message("aws_credentials_reminder"))

    # Description
    print(f"\n{get_message('description_intro')}")
    for script in get_message("setup_scripts"):
        print(script)
    print(f"\n{get_message('no_affect_other')}")

    if DEBUG_MODE:
        print(f"\n{get_message('debug_enabled')}")
        for feature in get_message("debug_features"):
            print(feature)
    else:
        print(f"\n{get_message('tip')}")

    # Resources to cleanup
    print(f"\n{get_message('resources_to_cleanup')}")
    print(get_message("things_prefix", args.things_prefix))
    print(get_message("thing_types", ", ".join(SAMPLE_THING_TYPES)))
    print(get_message("thing_groups", ", ".join(SAMPLE_THING_GROUPS)))
    print(get_message("certificates_attached"))
    print(get_message("local_cert_files"))
    print(get_message("policies_manual_review"))

    # Confirmation
    if not args.dry_run:
        response = input(f"\n{get_message('continue_cleanup')}").strip().lower()
        if not is_yes(response, USER_LANG):
            print(get_message("cleanup_cancelled"))
            return

    try:
        # Initialize IoT client
        iot_client = boto3.client("iot")
        print(f"\n{get_message('client_initialized')}")

        if DEBUG_MODE:
            print(get_message("debug_client_config"))
            print(f"  {get_message('service_label')}: {iot_client._service_model.service_name}")
            print(f"  {get_message('api_version_label')}: {iot_client._service_model.api_version}")

        # Initialize iot_helpers modules
        try:
            s3_client = boto3.client('s3')
            iam_client = boto3.client('iam')
            identifier = ResourceIdentifier(iot_client, s3_client, iam_client, USER_LANG, DEBUG_MODE)
            dependency_handler = DependencyHandler(iot_client, s3_client, iam_client, USER_LANG, DEBUG_MODE)
            engine = DeletionEngine({'iot_client': iot_client, 's3_client': s3_client, 'iam_client': iam_client}, DEBUG_MODE, args.dry_run, USER_LANG)
            reporter = CleanupReporter(USER_LANG)
            
            if DEBUG_MODE:
                print("\niot_helpers modules initialized successfully:")
                print("  - ResourceIdentifier")
                print("  - DependencyHandler")
                print("  - DeletionEngine")
                print("  - CleanupReporter")
        except Exception as e:
            print(f"\nError initializing iot_helpers modules: {e}")
            if DEBUG_MODE:
                traceback.print_exc()
            print("\nFalling back to legacy cleanup methods...")
            identifier = None
            dependency_handler = None
            engine = None
            reporter = None

        # Learning moment
        if not args.dry_run:
            print(f"\n{get_message('learning_moment_title')}")
            print(get_message("learning_moment_content"))
            print(f"\n{get_message('next_cleanup')}")
            input(get_message("press_enter_continue"))

        # Execute cleanup steps using new modules if available
        if engine and identifier and dependency_handler:
            print(f"\n{'='*60}")
            print("Using iot_helpers cleanup engine")
            print(f"{'='*60}")
            
            # Get deletion order (1 = all resources)
            deletion_order = dependency_handler.get_deletion_order(1)
            
            # Collect all statistics
            all_stats = {}
            
            # Process each resource type in order
            for resource_type in deletion_order:
                if resource_type == 'iot_rules':
                    # List all rules
                    rules = list_all_rules(iot_client)
                    if rules:
                        stats = engine.delete_resources(
                            resources=rules,
                            resource_type='iot-rule',
                            identifier=identifier,
                            dependency_handler=dependency_handler,
                            custom_prefix=args.things_prefix
                        )
                        all_stats['iot_rules'] = stats
                elif resource_type == 'things':
                    # List all things
                    response = iot_client.list_things()
                    things = response.get('things', [])
                    if things:
                        stats = engine.delete_resources(
                            resources=things,
                            resource_type='thing',
                            identifier=identifier,
                            dependency_handler=dependency_handler,
                            custom_prefix=args.things_prefix
                        )
                        all_stats['things'] = stats
                elif resource_type == 'certificates':
                    # List all certificates
                    response = iot_client.list_certificates()
                    certificates = response.get('certificates', [])
                    if certificates:
                        stats = engine.delete_resources(
                            resources=certificates,
                            resource_type='certificate',
                            identifier=identifier,
                            dependency_handler=dependency_handler,
                            custom_prefix=args.things_prefix
                        )
                        all_stats['certificates'] = stats
                elif resource_type == 'thing_groups':
                    # List all thing groups
                    response = iot_client.list_thing_groups()
                    groups = response.get('thingGroups', [])
                    if groups:
                        stats = engine.delete_resources(
                            resources=groups,
                            resource_type='thing-group',
                            identifier=identifier,
                            dependency_handler=dependency_handler,
                            custom_prefix=args.things_prefix
                        )
                        all_stats['thing_groups'] = stats
                elif resource_type == 'policies':
                    # List all policies
                    response = iot_client.list_policies()
                    policies = response.get('policies', [])
                    if policies:
                        stats = engine.delete_resources(
                            resources=policies,
                            resource_type='policy',
                            identifier=identifier,
                            dependency_handler=dependency_handler,
                            custom_prefix=args.things_prefix
                        )
                        all_stats['policies'] = stats
            
            # Report summary
            if reporter:
                reporter.report_summary(all_stats, args.dry_run)
            
            # Clean up local files
            cleanup_local_files()
            
        else:
            # Fall back to legacy cleanup methods
            certificates_cleaned = cleanup_sample_things(iot_client)
            skipped_certificates = cleanup_orphaned_certificates(iot_client)
            deleted_policies, skipped_policies = cleanup_sample_policies(iot_client)
            cleanup_sample_thing_groups(iot_client)
            cleanup_sample_thing_types(iot_client)
            cleanup_device_shadows()
            cleanup_sample_rules(iot_client)
            
            # Clean up IAM resources created for IoT Rules
            iam_client = boto3.client('iam')
            cleanup_iam_resources(iot_client, iam_client)
            
            cleanup_local_files()

            # Final summary
            print(f"\n{get_message('cleanup_summary_title')}")
            print(get_message("summary_separator"))
            print(get_message("things_cleaned"))
            print(get_message("certificates_cleaned"))
            print(get_message("groups_cleaned"))
            print(get_message("types_cleaned"))
            print(get_message("local_files_cleaned"))
            print(get_message("device_state_cleaned"))
            print(f"\n{get_message('account_clean')}")

            # Certificate and policy summary
            if skipped_certificates > 0:
                print(f"\n{get_message('certificate_cleanup_summary')}")
                print(get_message("cleaned_certificates", certificates_cleaned))
                print(get_message("skipped_certificates", skipped_certificates))
                print(f"\n{get_message('skipped_certs_production')}")
                print(get_message("manual_cert_deletion"))

            if skipped_policies > 0:
                print(f"\n{get_message('skipped_policies_note')}")
                print(get_message("policies_cleanup_auto"))
                print(get_message("policies_manual_cleanup"))

        if DEBUG_MODE:
            print(f"\n{get_message('debug_cleanup_completed')}")

        print(f"\n{get_message('goodbye')}")

    except KeyboardInterrupt:
        print(f"\n{get_message('cleanup_interrupted')}")

    except Exception as e:
        print(f"\n{get_message('error_generic', str(e))}")
        if DEBUG_MODE:
            print(f"{get_message('debug_full_traceback')}")
            traceback.print_exc()


if __name__ == "__main__":
    main()
