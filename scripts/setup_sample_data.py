#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import random
import sys
import time
import traceback
import uuid
from datetime import datetime, timedelta

# Add i18n to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "i18n"))

# Add iot_helpers to path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import boto3
from botocore.exceptions import ClientError, NoCredentialsError, NoRegionError

from language_selector import get_language
from loader import load_messages
from confirm_input import is_yes
from iot_helpers.utils.resource_tagger import apply_workshop_tags
from iot_helpers.utils.naming_conventions import (
    generate_thing_name,
    validate_thing_prefix
)

# Configuration
THING_COUNT = 20
THING_TYPES = ["SedanVehicle", "SUVVehicle", "TruckVehicle"]
THING_GROUPS = ["CustomerFleet", "TestFleet", "MaintenanceFleet", "DealerFleet"]
COUNTRIES = ["US", "DE", "JP", "CA", "BR", "GB", "FR", "AU", "IN", "MX"]

# Global variables
USER_LANG = "en"
messages = {}


def get_message(key, *args):
    """Get localized message with optional formatting"""
    msg = messages.get(key, key)
    if args:
        return msg.format(*args)
    return msg


def get_learning_moment(moment_key):
    """Get localized learning moment"""
    return messages.get("learning_moments", {}).get(moment_key, {})


def print_learning_moment(moment_key):
    """Print a formatted learning moment"""
    moment = get_learning_moment(moment_key)
    if moment:
        print(f"\n{moment.get('title', '')}")
        print(moment.get("content", ""))
        print(f"\n🔄 NEXT: {moment.get('next', '')}")


def check_credentials():
    """Validate AWS credentials are available"""
    required_vars = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print(get_message("credentials_check_failed"))
        for var in missing_vars:
            print(f"   - {var}")
        print()
        for instruction in get_message("credentials_instructions"):
            print(instruction)
        print()
        sys.exit(1)


def print_step(step, description):
    """Print setup step with formatting"""
    print(f"\n🔧 Step {step}: {description}")
    print("-" * 50)


def safe_create(func, resource_type, name, debug=False, **kwargs):
    """Safely create resource with error handling and optional debug info"""
    try:
        if debug:
            print(f"\n{get_message('debug_creating')} {resource_type}: {name}")
            print(f"{get_message('debug_api_call')} {func.__name__}")
            print(get_message("debug_input_params"))
            print(json.dumps(kwargs, indent=2, default=str))
        else:
            print(f"{get_message('creating')} {resource_type}: {name}")

        response = func(**kwargs)

        if debug:
            print(get_message("debug_api_response"))
            print(json.dumps(response, indent=2, default=str))

        print(f"✅ {get_message('created')} {resource_type}: {name}")
        time.sleep(0.5 if not debug else 1.0)
        return response
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceAlreadyExistsException":
            print(f"⚠️  {resource_type} {name} {get_message('already_exists')}")
        else:
            print(f"❌ {get_message('error_creating')} {resource_type} {name}: {e.response['Error']['Message']}")
            if debug:
                print(get_message("debug_full_error"))
                print(json.dumps(e.response, indent=2, default=str))
        time.sleep(0.5)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        if debug:
            print(get_message("debug_full_traceback"))
            traceback.print_exc()
        time.sleep(0.5)


def create_thing_types(iot, debug=False, tag_failures=None):
    """Create predefined Thing Types"""
    if tag_failures is None:
        tag_failures = []
        
    print_step(1, get_message("step_1_title"))

    for thing_type in THING_TYPES:
        # Check if Thing Type already exists
        try:
            response = iot.describe_thing_type(thingTypeName=thing_type)
            if response.get("thingTypeMetadata", {}).get("deprecated"):
                print(f"   ⚠️ Thing Type {thing_type} {get_message('deprecated_undeprecating')}")
                iot.deprecate_thing_type(thingTypeName=thing_type, undoDeprecate=True)
                print(f"   ✅ Thing Type {thing_type} {get_message('undeprecated')}")
            else:
                print(f"   ℹ️ Thing Type {thing_type} {get_message('already_active')}")
            continue
        except iot.exceptions.ResourceNotFoundException:
            # Thing Type doesn't exist, create it
            pass
        except Exception as e:
            print(f"   ❌ {get_message('error_checking')} Thing Type {thing_type}: {str(e)}")
            continue

        description = f"Template for {thing_type.replace('Vehicle', ' Vehicle')} category"
        response = safe_create(
            iot.create_thing_type,
            "Thing Type",
            thing_type,
            debug=debug,
            thingTypeName=thing_type,
            thingTypeProperties={
                "thingTypeDescription": description,
                "searchableAttributes": ["customerId", "country", "manufacturingDate"],
            },
        )
        
        # Add tagging after thing type creation
        if response:
            thing_type_arn = response.get('thingTypeArn')
            if thing_type_arn:
                try:
                    apply_workshop_tags(
                        client=iot,
                        resource_arn=thing_type_arn,
                        resource_type='thing-type',
                        script_name='setup-script'
                    )
                    if debug:
                        print(get_message("tag_applied", thing_type))
                except Exception as e:
                    tag_failures.append({
                        'resource': thing_type,
                        'type': 'thing-type',
                        'error': str(e)
                    })
                    if debug:
                        print(get_message("tag_failed", thing_type, str(e)))


def create_thing_groups(iot, debug=False, tag_failures=None):
    """Create predefined Thing Groups"""
    if tag_failures is None:
        tag_failures = []
        
    print_step(2, get_message("step_2_title"))

    for group in THING_GROUPS:
        description = f"Group for devices in {group.replace('Floor', ' Floor')}"
        response = safe_create(
            iot.create_thing_group,
            "Thing Group",
            group,
            debug=debug,
            thingGroupName=group,
            thingGroupProperties={
                "thingGroupDescription": description,
                "attributePayload": {"attributes": {"location": group, "managed": "true"}},
            },
        )
        
        # Add tagging after thing group creation
        if response:
            group_arn = response.get('thingGroupArn')
            if group_arn:
                try:
                    apply_workshop_tags(
                        client=iot,
                        resource_arn=group_arn,
                        resource_type='thing-group',
                        script_name='setup-script'
                    )
                    if debug:
                        print(get_message("tag_applied", group))
                except Exception as e:
                    tag_failures.append({
                        'resource': group,
                        'type': 'thing-group',
                        'error': str(e)
                    })
                    if debug:
                        print(get_message("tag_failed", group, str(e)))


def generate_random_date():
    """Generate random date within last year"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime("%Y-%m-%d")


def create_things(iot, debug=False, things_prefix='Vehicle-VIN-', tag_failures=None):
    """Create sample Things with attributes"""
    if tag_failures is None:
        tag_failures = []
        
    print_step(3, get_message("step_3_title", THING_COUNT))

    for i in range(1, THING_COUNT + 1):
        thing_name = generate_thing_name(things_prefix, i)
        customer_id = str(uuid.uuid4())
        country = random.choice(COUNTRIES)
        manufacturing_date = generate_random_date()
        thing_type = random.choice(THING_TYPES)

        if not debug:
            print(f"\n{get_message('creating_thing')} {thing_name}")
            print(f"   {get_message('customer_id')} {customer_id}")
            print(f"   {get_message('country')} {country}")
            print(f"   {get_message('manufacturing_date')} {manufacturing_date}")
            print(f"   {get_message('thing_type')} {thing_type}")
            time.sleep(0.8)

        response = safe_create(
            iot.create_thing,
            "Thing",
            thing_name,
            debug=debug,
            thingName=thing_name,
            thingTypeName=thing_type,
            attributePayload={
                "attributes": {
                    "customerId": customer_id,
                    "country": country,
                    "manufacturingDate": manufacturing_date,
                }
            },
        )
        
        # Note: Things do not support tagging via AWS IoT API
        # They will be identified by naming conventions during cleanup


def add_things_to_groups(iot, debug=False, things_prefix='Vehicle-VIN-'):
    """Add Things to random Thing Groups"""
    print_step(4, get_message("step_4_title"))

    for i in range(1, THING_COUNT + 1):
        thing_name = generate_thing_name(things_prefix, i)
        group_name = random.choice(THING_GROUPS)

        try:
            if debug:
                print(f"\n🔍 DEBUG: {get_message('adding_to_group', thing_name, group_name)}")
                print(f"{get_message('debug_api_call')} add_thing_to_thing_group")
                print(get_message("debug_input_params"))
                print(
                    json.dumps(
                        {"thingGroupName": group_name, "thingName": thing_name},
                        indent=2,
                    )
                )
            else:
                print(get_message("adding_to_group", thing_name, group_name))

            response = iot.add_thing_to_thing_group(thingGroupName=group_name, thingName=thing_name)

            if debug:
                print(get_message("debug_api_response"))
                print(json.dumps(response, indent=2, default=str))

            print(f"✅ {get_message('added_to_group', thing_name, group_name)}")
            time.sleep(0.3 if not debug else 1.0)
        except ClientError as e:
            print(f"❌ {get_message('error_adding', thing_name, group_name)} {e.response['Error']['Message']}")
            if debug:
                print(get_message("debug_full_error"))
                print(json.dumps(e.response, indent=2, default=str))
            time.sleep(0.3)


def print_summary(iot):
    """Print summary of created resources"""
    print_step(5, get_message("step_5_title"))

    try:
        things = iot.list_things()
        thing_types = iot.list_thing_types()
        thing_groups = iot.list_thing_groups()

        print(get_message("resources_created"))
        print(f"   {get_message('things')} {len(things.get('things', []))}")
        print(f"   {get_message('thing_types')} {len(thing_types.get('thingTypes', []))}")
        print(f"   {get_message('thing_groups')} {len(thing_groups.get('thingGroups', []))}")

        print(f"\n{get_message('sample_thing_names')}")
        for thing in things.get("things", [])[:5]:
            print(f"   - {thing['thingName']}")
        if len(things.get("things", [])) > 5:
            print(f"   {get_message('and_more', len(things.get('things', [])) - 5)}")

    except Exception as e:
        print(f"{get_message('error_summary')} {str(e)}")


def main():
    global USER_LANG, messages

    try:
        # Get user's preferred language
        USER_LANG = get_language()

        # Load messages for this script and language
        messages = load_messages("setup_sample_data", USER_LANG)

        # Parse command-line arguments
        import argparse
        parser = argparse.ArgumentParser(description='Setup sample IoT Core data')
        parser.add_argument('--debug', '-d', action='store_true', help='Enable debug mode')
        parser.add_argument(
            '--things-prefix',
            default='Vehicle-VIN-',
            help='Prefix for thing names (default: Vehicle-VIN-)'
        )
        args = parser.parse_args()
        
        debug_mode = args.debug
        
        # Validate things prefix
        if not validate_thing_prefix(args.things_prefix):
            print(get_message("invalid_prefix", args.things_prefix))
            sys.exit(1)

        print(get_message("title"))
        print(get_message("separator"))

        # Check credentials first - exit immediately if missing
        check_credentials()

        # Display AWS context first
        try:
            sts = boto3.client("sts")
            iot = boto3.client("iot")
            identity = sts.get_caller_identity()

            print(get_message("aws_config"))
            print(f"   {get_message('account_id')}: {identity['Account']}")
            print(f"   {get_message('region')}: {iot.meta.region_name}")
            print()

        except Exception as e:
            print(f"{get_message('aws_context_error', str(e))}")
            print(get_message("aws_credentials_reminder"))
            print()

        print(get_message("description_intro"))
        print(f"• {len(THING_TYPES)} {get_message('thing_types_desc')} {', '.join(THING_TYPES)}")
        print(f"• {len(THING_GROUPS)} {get_message('thing_groups_desc')} {', '.join(THING_GROUPS)}")
        print(f"• {THING_COUNT} {get_message('things_desc')}")

        if debug_mode:
            print(f"\n{get_message('debug_mode_enabled')}")
            for feature in get_message("debug_features"):
                print(feature)
        else:
            print(f"\n{get_message('debug_tip')}")

        print(get_message("separator"))

        confirm = input(get_message("continue_prompt")).strip().lower()
        if not is_yes(confirm, USER_LANG):
            print(get_message("setup_cancelled"))
            return

        try:
            iot = boto3.client("iot")
            print(get_message("client_initialized"))

            if debug_mode:
                print("🔍 DEBUG: Client configuration:")
                print(f"   Service: {iot.meta.service_model.service_name}")
                print(f"   API Version: {iot.meta.service_model.api_version}")
        except NoCredentialsError:
            print(get_message("invalid_credentials"))
            sys.exit(1)
        except NoRegionError:
            print(get_message("no_region_error"))
            for instruction in get_message("region_setup_instructions"):
                print(f"   {instruction}")
            sys.exit(1)
        except Exception as e:
            print(f"{get_message('client_error')} {str(e)}")
            print(get_message("credentials_reminder"))
            return

        print_learning_moment("hierarchy")
        input(get_message("press_enter"))

        # Track tagging failures
        tag_failures = []

        # Execute setup steps with debug flag and tagging
        create_thing_types(iot, debug=debug_mode, tag_failures=tag_failures)

        print_learning_moment("thing_groups")
        input(get_message("press_enter"))

        create_thing_groups(iot, debug=debug_mode, tag_failures=tag_failures)

        print_learning_moment("things")
        input(get_message("press_enter"))

        create_things(iot, debug=debug_mode, things_prefix=args.things_prefix, tag_failures=tag_failures)

        print_learning_moment("relationships")
        input(get_message("press_enter"))

        add_things_to_groups(iot, debug=debug_mode, things_prefix=args.things_prefix)
        print_summary(iot)

        # Report tag failures if any (excluding Things which don't support tagging via API)
        reportable_failures = [f for f in tag_failures if f['type'] != 'thing']
        if reportable_failures:
            print(f"\n⚠️  {get_message('tag_failures_summary', len(reportable_failures))}")
            for failure in reportable_failures[:5]:  # Show first 5
                print(f"   - {failure['type']}: {failure['resource']}")
            if len(reportable_failures) > 5:
                print(f"   ... and {len(reportable_failures) - 5} more")
            print(get_message("tag_failures_note"))

        print(f"\n{get_message('setup_complete')}")

        if debug_mode:
            print(f"\n{get_message('debug_session_complete')}")

    except KeyboardInterrupt:
        print(f"\n\n{get_message('setup_cancelled_user')}")


if __name__ == "__main__":
    main()
