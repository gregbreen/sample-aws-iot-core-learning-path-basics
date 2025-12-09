# Usage Examples and Workflows

This document provides detailed examples and complete workflows for the AWS IoT Core - Basics learning project.

## Table of Contents

- [Complete Learning Workflow](#complete-learning-workflow)
  - [Recommended Learning Sequence](#recommended-learning-sequence)
- [Sample Data Setup Examples](#sample-data-setup-examples)
  - [Interactive Experience Walkthrough](#interactive-experience-walkthrough)
  - [Debug Mode Example](#debug-mode-example)
  - [Custom Prefix Examples](#custom-prefix-examples)
  - [Multi-Environment Setup](#multi-environment-setup)
- [IoT Registry API Explorer Examples](#iot-registry-api-explorer-examples)
  - [Interactive Menu Navigation](#interactive-menu-navigation)
  - [List Things Example](#list-things-example)
  - [Describe Thing Example](#describe-thing-example)
- [Certificate Manager Examples](#certificate-manager-examples)
  - [Complete Certificate Workflow](#complete-certificate-workflow)
  - [External Certificate Registration Example](#external-certificate-registration-example)
- [MQTT Communication Examples](#mqtt-communication-examples)
  - [Certificate-Based MQTT Session](#certificate-based-mqtt-session)
  - [WebSocket MQTT Session](#websocket-mqtt-session)
- [AWS IoT Device Shadow service Examples](#device-shadow-examples)
  - [Shadow State Synchronization](#shadow-state-synchronization)
- [Rules Engine Examples](#rules-engine-examples)
  - [Rule Creation Workflow](#rule-creation-workflow)
  - [Rule Testing Example](#rule-testing-example)
- [Cleanup Examples](#cleanup-examples)
  - [Safe Resource Cleanup](#safe-resource-cleanup)
  - [Dry-Run Mode Examples](#dry-run-mode-examples)
  - [Prefix-Based Cleanup](#prefix-based-cleanup)
  - [Multi-Environment Cleanup](#multi-environment-cleanup)
- [Error Handling Examples](#error-handling-examples)
  - [Common Error Scenarios](#common-error-scenarios)

## Complete Learning Workflow

### Recommended Learning Sequence

**Full End-to-End Learning Path:**

```bash
# 1. Environment Setup
source venv/bin/activate
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1

# 2. Create Sample IoT Resources
python setup_sample_data.py

# 3. Explore AWS IoT Registry APIs
python iot_registry_explorer.py

# 4. Learn Security with Certificates and Policies
python certificate_manager.py

# 5. Experience Real-time MQTT Communication
python mqtt_client_explorer.py
# OR
python mqtt_websocket_explorer.py

# 6. Learn Device State Synchronization with Shadows
python device_shadow_explorer.py

# 7. Master Message Routing with Rules Engine
python iot_rules_explorer.py

# 8. Clean Up When Done Learning
python cleanup_sample_data.py
```

**Apart from the initial setup script, all other scripts can be run independently based on your learning interests.**

## Sample Data Setup Examples

### Interactive Experience Walkthrough

**When you run `python setup_sample_data.py`, you'll see:**

```
🚀 AWS IoT Sample Data Setup
============================
This script will create sample IoT resources for learning:
• 3 Thing Types (vehicle categories)
• 4 Thing Groups (fleet categories)  
• 20 Things (simulated vehicles)

⚠️  This will create real AWS resources that incur charges.
Estimated cost: ~$0.05 for Thing storage

Do you want to continue? (y/N): y

🔄 Step 1: Creating Thing Types
✅ Created Thing Type: SedanVehicle
✅ Created Thing Type: SUVVehicle  
✅ Created Thing Type: TruckVehicle

🔄 Step 2: Creating Thing Groups
✅ Created Thing Group: CustomerFleet
✅ Created Thing Group: TestFleet
✅ Created Thing Group: MaintenanceFleet
✅ Created Thing Group: DealerFleet

🔄 Step 3: Creating Things (20 vehicles)
✅ Created Thing: Vehicle-VIN-001 (SedanVehicle → CustomerFleet)
✅ Created Thing: Vehicle-VIN-002 (SUVVehicle → TestFleet)
...
✅ Created Thing: Vehicle-VIN-020 (TruckVehicle → DealerFleet)

📊 Summary:
   Thing Types: 3 created
   Thing Groups: 4 created  
   Things: 20 created
   
🎉 Sample data setup complete!
```

### Debug Mode Example

**With `python setup_sample_data.py --debug`:**

```
🔍 DEBUG: Creating Thing Type 'SedanVehicle'
📥 API Call: create_thing_type
📤 Request: {
  "thingTypeName": "SedanVehicle",
  "thingTypeProperties": {
    "description": "Passenger sedan vehicles",
    "searchableAttributes": ["customerId", "country", "manufacturingDate"]
  }
}
📨 Response: {
  "thingTypeName": "SedanVehicle",
  "thingTypeArn": "arn:aws:iot:us-east-1:123456789012:thingtype/SedanVehicle"
}
⏱️  Duration: 0.45 seconds
```

### Custom Prefix Examples

**Using Custom Prefix for Development Environment:**

```bash
$ python setup_sample_data.py --things-prefix "Dev-Vehicle-"

🚀 AWS IoT Sample Data Setup
============================
This script will create sample IoT resources for learning:
• 3 Thing Types (vehicle categories)
• 4 Thing Groups (fleet categories)  
• 20 Things (simulated vehicles)

📝 Configuration:
   Thing Name Prefix: Dev-Vehicle-
   Thing Names: Dev-Vehicle-001 through Dev-Vehicle-020

⚠️  This will create real AWS resources that incur charges.
Estimated cost: ~$0.05 for Thing storage

Do you want to continue? (y/N): y

🔄 Step 1: Creating Thing Types
✅ Created Thing Type: SedanVehicle
✅ Created Thing Type: SUVVehicle  
✅ Created Thing Type: TruckVehicle

🔄 Step 2: Creating Thing Groups
✅ Created Thing Group: CustomerFleet
✅ Created Thing Group: TestFleet
✅ Created Thing Group: MaintenanceFleet
✅ Created Thing Group: DealerFleet

🔄 Step 3: Creating Things (20 vehicles)
✅ Created Thing: Dev-Vehicle-001 (SedanVehicle → CustomerFleet)
✅ Created Thing: Dev-Vehicle-002 (SUVVehicle → TestFleet)
✅ Created Thing: Dev-Vehicle-003 (TruckVehicle → MaintenanceFleet)
...
✅ Created Thing: Dev-Vehicle-020 (SedanVehicle → DealerFleet)

📊 Summary:
   Thing Types: 3 created
   Thing Groups: 4 created  
   Things: 20 created (prefix: Dev-Vehicle-)
   
🎉 Sample data setup complete!
```

**Invalid Prefix Example:**

```bash
$ python setup_sample_data.py --things-prefix "123-Device-"

❌ Error: Invalid prefix '123-Device-'

💡 Prefix Requirements:
   • Must start with a letter (a-z, A-Z)
   • Can contain letters, numbers, hyphens (-), underscores (_)
   • Cannot start with numbers or contain spaces

✅ Valid examples:
   • Vehicle-VIN-
   • Dev-Device-
   • MyFleet_
   • TestEnv-

❌ Invalid examples:
   • 123-Device- (starts with number)
   • My Device- (contains space)
   • Fleet@Home- (contains special character)
```

### Multi-Environment Setup

**Scenario**: Create separate development and staging environments in the same AWS account.

**Step 1: Create Development Environment**

```bash
$ python setup_sample_data.py --things-prefix "Dev-"

🚀 AWS IoT Sample Data Setup
============================
📝 Configuration:
   Thing Name Prefix: Dev-
   Thing Names: Dev-001 through Dev-020

Do you want to continue? (y/N): y

🔄 Creating resources...
✅ Created 20 Things with prefix 'Dev-'
✅ Created 3 Thing Types
✅ Created 4 Thing Groups

🎉 Development environment setup complete!
```

**Step 2: Create Staging Environment**

```bash
$ python setup_sample_data.py --things-prefix "Staging-"

🚀 AWS IoT Sample Data Setup
============================
📝 Configuration:
   Thing Name Prefix: Staging-
   Thing Names: Staging-001 through Staging-020

Do you want to continue? (y/N): y

🔄 Creating resources...
✅ Created 20 Things with prefix 'Staging-'
✅ Created 3 Thing Types
✅ Created 4 Thing Groups

🎉 Staging environment setup complete!
```

**Step 3: Verify Both Environments Exist**

```bash
$ python iot_registry_explorer.py

📋 Available Operations:
1. List Things
...

Select operation (1-9): 1

🔄 API Call: list_things
📤 Response: Found 40 Things

Development Environment:
1. Dev-001 (Type: SedanVehicle)
2. Dev-002 (Type: SUVVehicle)
...
20. Dev-020 (Type: TruckVehicle)

Staging Environment:
21. Staging-001 (Type: SedanVehicle)
22. Staging-002 (Type: SUVVehicle)
...
40. Staging-020 (Type: TruckVehicle)
```

## IoT Registry API Explorer Examples

### Interactive Menu Navigation

**Main Menu:**
```
📋 Available Operations:
1. List Things
2. List Certificates  
3. List Thing Groups
4. List Thing Types
5. Describe Thing
6. Describe Thing Group
7. Describe Thing Type
8. Describe Endpoint
9. Exit

Select operation (1-9): 1
```

### List Things Example

**Basic Listing:**
```
🔄 API Call: list_things
🌐 HTTP Request: GET https://iot.us-east-1.amazonaws.com/things
ℹ️  Description: Retrieves all IoT Things in your AWS account
📥 Input Parameters: None (basic listing)
💡 Response Explanation: Returns array of Thing objects with names, types, and attributes

📤 Response Payload:
Found 20 Things:
1. Vehicle-VIN-001 (Type: SedanVehicle)
   Attributes: customerId=a1b2c3d4-e5f6-7890, country=US, manufacturingDate=2024-03-15
2. Vehicle-VIN-002 (Type: SUVVehicle)  
   Attributes: customerId=b2c3d4e5-f6g7-8901, country=Germany, manufacturingDate=2024-07-22
...
```

**With Pagination:**
```
📋 Pagination Options:
1. Show all Things
2. Set maximum results per page
3. Go back

Select option (1-3): 2
Enter max results per page (1-250): 5

🔄 API Call: list_things  
📥 Input Parameters: {"maxResults": 5}
📤 Response: 5 Things returned (page 1)

Continue to next page? (y/N): y
```

**Filter by Thing Type:**
```
📋 Filter Options:
1. No filter (show all)
2. Filter by Thing Type
3. Filter by attribute
4. Go back

Select option (1-4): 2

Available Thing Types:
1. SedanVehicle
2. SUVVehicle  
3. TruckVehicle

Select Thing Type (1-3): 1

🔄 API Call: list_things
📥 Input Parameters: {"thingTypeName": "SedanVehicle"}
📤 Response: Found 7 SedanVehicle Things
```

### Describe Thing Example

**Thing Selection:**
```
Enter Thing name: Vehicle-VIN-001

🔄 API Call: describe_thing
🌐 HTTP Request: GET https://iot.us-east-1.amazonaws.com/things/Vehicle-VIN-001
📥 Input Parameters: {"thingName": "Vehicle-VIN-001"}

📤 Response Payload:
{
  "thingName": "Vehicle-VIN-001",
  "thingId": "12345678-1234-1234-1234-123456789012",
  "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/Vehicle-VIN-001",
  "thingTypeName": "SedanVehicle",
  "attributes": {
    "customerId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "country": "US", 
    "manufacturingDate": "2024-03-15"
  },
  "version": 1
}
```

## Certificate Manager Examples

### Complete Certificate Workflow

**Option 1: Create AWS IoT Certificate & Attach to Thing**

```
📋 Main Menu:
1. Create AWS IoT Certificate & Attach to Thing (+ Optional Policy)
2. Register External Certificate & Attach to Thing (+ Optional Policy)  
3. Attach Policy to Existing Certificate
4. Detach Policy from Certificate
5. Enable/Disable Certificate
6. Exit

Select option (1-6): 1

📚 LEARNING MOMENT: Certificate Creation & Thing Attachment
Creating an AWS IoT certificate establishes a unique digital identity for your device...

Press Enter to continue...

📱 Available Things (20 found):
   1. Vehicle-VIN-001 (Type: SedanVehicle)
   2. Vehicle-VIN-002 (Type: SUVVehicle)
   ...
   10. Vehicle-VIN-010 (Type: TruckVehicle)
   ... and 10 more

📋 Options:
   • Enter number (1-20) to select Thing
   • Type 'all' to see all Things  
   • Type 'manual' to enter Thing name manually

Your choice: 1
✅ Selected Thing: Vehicle-VIN-001
```

**Certificate Creation Process:**
```
🔐 Step 1: Creating X.509 Certificate
--------------------------------------------------
ℹ️  X.509 certificates are used for device authentication in AWS IoT
ℹ️  Each certificate contains a public/private key pair

🔍 API Details:
   Operation: create_keys_and_certificate
   HTTP Method: POST
   API Path: /keys-and-certificate
   Description: Creates a new X.509 certificate with public/private key pair
   Input Parameters: setAsActive: true (activates certificate immediately)
   Expected Output: certificateArn, certificateId, certificatePem, keyPair

🔄 Creating certificate and key pair...
📥 Input: {"setAsActive": true}
✅ Creating certificate and key pair completed successfully

📋 Certificate Details:
   Certificate ID: abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890
   Certificate ARN: arn:aws:iot:us-east-1:123456789012:cert/abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890
   Status: ACTIVE

   📄 Certificate: certificates/Vehicle-VIN-001/abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890.crt
   🔐 Private Key: certificates/Vehicle-VIN-001/abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890.key
   🔑 Public Key: certificates/Vehicle-VIN-001/abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890.pub

💾 Certificate files saved to: certificates/Vehicle-VIN-001

🔑 Certificate Components Created:
   • Public Key (for AWS IoT)
   • Private Key (keep secure on device)
   • Certificate PEM (for device authentication)
```

**Certificate-Thing Attachment:**
```
🔐 Step 2: Attaching Certificate to Thing
--------------------------------------------------
ℹ️  Certificates must be attached to Things for device authentication
ℹ️  This creates a secure relationship between the certificate and the IoT device
ℹ️  Certificate will be attached to: Vehicle-VIN-001

🔗 Attaching certificate to Thing: Vehicle-VIN-001

🔍 API Details:
   Operation: attach_thing_principal
   HTTP Method: PUT
   API Path: /things/Vehicle-VIN-001/principals
   Description: Attaches a certificate (principal) to a Thing for authentication
   Input Parameters: thingName: Vehicle-VIN-001, principal: arn:aws:iot:...
   Expected Output: Empty response on success

🔄 Attaching certificate to Vehicle-VIN-001...
✅ Attaching certificate to Vehicle-VIN-001 completed
✅ Certificate successfully attached to Vehicle-VIN-001
   ℹ️  The Thing can now use this certificate for authentication
```

**Policy Creation:**
```
🔐 Step 3: IoT Policy Management
--------------------------------------------------
ℹ️  IoT Policies define what actions a certificate can perform
ℹ️  You can create a new policy or use an existing one

📝 No existing policies found. Creating new policy...

Enter new policy name: BasicDevicePolicy
✅ Policy name 'BasicDevicePolicy' is available

📝 Policy Templates:
1. Basic Device Policy (connect, publish, subscribe)
2. Read-Only Policy (connect, subscribe only)
3. Custom Policy (enter your own JSON)

Select policy template (1-3): 1

⚠️  Production Security Note:
   This policy uses 'Resource': '*' for demonstration purposes.
   In production, use specific resource ARNs and policy variables
   like ${iot:Connection.Thing.ThingName} to restrict device access
   to only their specific resources. Policy variables are beyond
   the scope of this basic learning path.

📄 Policy to be created:
   Name: BasicDevicePolicy
   Document: {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "iot:Connect",
           "iot:Publish", 
           "iot:Subscribe",
           "iot:Receive"
         ],
         "Resource": "*"
       }
     ]
   }

🔄 Creating policy 'BasicDevicePolicy'...
✅ Policy 'BasicDevicePolicy' created successfully
```

**Policy Attachment:**
```
🔐 Step 4: Attaching Policy to Certificate
--------------------------------------------------
ℹ️  Policies must be attached to certificates to grant permissions
ℹ️  Without a policy, the certificate cannot perform any IoT operations

🔗 Attaching policy 'BasicDevicePolicy' to certificate

🔄 Attaching policy to certificate...
✅ Policy 'BasicDevicePolicy' attached to certificate
   ℹ️  Certificate now has the permissions defined in the policy
```

**Final Summary:**
```
🔐 Step 5: Setup Complete! 🎉
--------------------------------------------------
📊 Summary of what was created:
   🔐 Certificate ID: abc123def456789ghi012jkl345mno678pqr901stu234vwx567yz890
   📱 Attached to Thing: Vehicle-VIN-001
   📄 Policy Attached: BasicDevicePolicy

🔍 What you can explore now:
   • Use iot_registry_explorer.py to view the certificate
   • Check the Thing to see its attached certificate
   • Review the policy permissions

💡 Key Learning Points:
   • Certificates provide device identity and authentication
   • Things represent your IoT devices in AWS
   • Policies define what actions certificates can perform
   • All three work together for secure IoT communication
```

### External Certificate Registration Example

**OpenSSL Certificate Generation:**
```
📜 External Certificate Registration Workflow
==================================================

📋 Certificate Options:
1. Use existing certificate file
2. Generate sample certificate with OpenSSL

Select option (1-2): 2

🔐 Step OpenSSL: Generate Sample Certificate with OpenSSL
--------------------------------------------------
ℹ️  This creates a self-signed certificate for learning purposes
ℹ️  In production, use certificates from a trusted Certificate Authority

Enter certificate name [default: sample-device]: my-test-device

🔑 Generating certificate files:
   Private Key: sample-certs/my-test-device.key
   Certificate: sample-certs/my-test-device.crt

🔄 Running OpenSSL command...
📥 Command: openssl req -x509 -newkey rsa:2048 -keyout sample-certs/my-test-device.key -out sample-certs/my-test-device.crt -days 365 -nodes -subj /CN=my-test-device/O=AWS IoT Learning/C=US

✅ Certificate generated successfully

📊 Certificate Details:
   • Type: Self-signed X.509
   • Key Size: 2048-bit RSA
   • Validity: 365 days
   • Subject: CN=my-test-device, O=AWS IoT Learning, C=US
```

## MQTT Communication Examples

### Certificate-Based MQTT Session

**Device Selection:**
```
🔍 Discovering Things with certificates...
📋 Found 3 Things with certificates:
   1. Vehicle-VIN-001 → Certificate: abc123def456...
   2. Vehicle-VIN-002 → Certificate: def456ghi789...
   3. Vehicle-VIN-003 → Certificate: ghi789jkl012...

Select Thing (1-3): 1
✅ Selected: Vehicle-VIN-001

🔍 Certificate validation:
   📄 Certificate file: ✅ Found
   🔐 Private key file: ✅ Found
   📱 Thing attachment: ✅ Verified
```

**Connection Establishment:**
```
🔐 Step 1: Establishing MQTT Connection for Shadow Operations
--------------------------------------------------
🔗 Shadow Connection Parameters:
   Client ID: Vehicle-VIN-001-mqtt-a1b2c3d4
   Thing Name: Vehicle-VIN-001
   Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   Port: 8883
   Protocol: MQTT 3.1.1 over TLS
   Authentication: X.509 Certificate
   Shadow Type: Classic Shadow

🔄 Connecting to AWS IoT Core...
✅ Successfully connected to AWS IoT Core

======================================================================
🔔 SHADOW CONNECTION ESTABLISHED [14:30:10.123]
======================================================================
Status: Successfully connected to AWS IoT Core
Client ID: Vehicle-VIN-001-mqtt-a1b2c3d4
Thing Name: Vehicle-VIN-001
Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
Shadow Type: Classic Shadow
Clean Session: True
Keep Alive: 30 seconds
TLS Version: 1.2
Certificate Authentication: X.509 mutual TLS
======================================================================
```

**Interactive MQTT Commands:**
```
📡 MQTT Client Connected - Type 'help' for commands

📡 MQTT> help
Available commands:
  sub <topic>              - Subscribe to topic (QoS 0)
  sub1 <topic>             - Subscribe to topic (QoS 1)
  unsub <topic>            - Unsubscribe from topic
  pub <topic> <message>    - Publish message (QoS 0)
  pub1 <topic> <message>   - Publish message (QoS 1)
  json <topic> key=val...  - Publish JSON message
  test                     - Send test message
  status                   - Show connection status
  messages                 - Show message history
  debug                    - Connection diagnostics
  quit                     - Exit client

📡 MQTT> sub device/+/temperature
✅ [14:30:15.456] SUBSCRIBED to device/+/temperature (QoS: 0)

📡 MQTT> pub device/sensor/temperature 23.5
✅ [14:30:20.789] PUBLISHED
   📤 Topic: device/sensor/temperature
   🏷️  QoS: 0 | Packet ID: 1
   📊 Size: 4 bytes

======================================================================
🔔 INCOMING MESSAGE #1 [14:30:20.890]
======================================================================
📥 Topic: device/sensor/temperature
🏷️  QoS: 0 (At most once)
📊 Payload Size: 4 bytes
💬 Message: 23.5
======================================================================

📡 MQTT> json device/data temperature=25.0 humidity=60 status=online
✅ [14:30:25.123] PUBLISHED JSON
   📤 Topic: device/data
   🏷️  QoS: 0 | Packet ID: 2
   📊 Size: 52 bytes
   💬 JSON: {"temperature": 25.0, "humidity": 60, "status": "online"}

📡 MQTT> status
🔍 Connection Status:
   📡 Status: CONNECTED
   🏷️  Client ID: Vehicle-VIN-001-mqtt-a1b2c3d4
   🌐 Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   📊 Messages Published: 2
   📥 Messages Received: 1
   📋 Active Subscriptions: 1
      • device/+/temperature (QoS: 0)
```

### WebSocket MQTT Session

**Credential Validation:**
```
🌐 WebSocket MQTT Client
========================
🔍 Validating AWS credentials...
✅ AWS credentials validated
   Account ID: 123456789012
   Region: us-east-1

🔗 WebSocket Connection Parameters:
   Endpoint: wss://a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com/mqtt
   Authentication: AWS SigV4
   Client ID: websocket-client-a1b2c3d4
   Protocol: MQTT over WebSocket

🔄 Establishing WebSocket connection...
✅ WebSocket MQTT connection established

📡 WebSocket MQTT> sub alerts/#
✅ [14:35:10.123] SUBSCRIBED to alerts/# (QoS: 0)

📡 WebSocket MQTT> pub alerts/temperature "High temperature detected"
✅ [14:35:15.456] PUBLISHED
   📤 Topic: alerts/temperature
   💬 Message: High temperature detected
```

## AWS IoT Device Shadow service Examples

### Shadow State Synchronization

**Initial Shadow Setup:**
```
🌟 AWS IoT Device Shadow service Explorer
=========================
🔍 Discovering Things with certificates...
✅ Selected Thing: Vehicle-VIN-001

📱 Local Device State Setup:
   📄 State file: certificates/Vehicle-VIN-001/device_state.json
   📊 Initial state: {
     "temperature": 22.5,
     "humidity": 45.0,
     "status": "online",
     "firmware_version": "1.0.0"
   }

🔄 Connecting to AWS IoT for shadow operations...
✅ Shadow connection established

🌟 Step 2: Subscribing to Shadow Topics
--------------------------------------------------
📋 Classic Shadow Topics:
   ✅ $aws/things/Vehicle-VIN-001/shadow/get/accepted
   ✅ $aws/things/Vehicle-VIN-001/shadow/get/rejected
   ✅ $aws/things/Vehicle-VIN-001/shadow/update/accepted
   ✅ $aws/things/Vehicle-VIN-001/shadow/update/rejected
   ✅ $aws/things/Vehicle-VIN-001/shadow/update/delta

✅ Successfully subscribed to all 5 shadow topics

📖 Shadow Topic Explanations:
   • get/accepted - Shadow document retrieval success
   • get/rejected - Shadow document retrieval failure
   • update/accepted - Shadow update success
   • update/rejected - Shadow update failure
   • update/delta - Desired ≠ Reported (action needed)
```

**Shadow Operations:**
```
🌟 Shadow> get
🔄 Requesting current shadow document...

======================================================================
🌟 SHADOW MESSAGE RECEIVED [14:40:10.123]
======================================================================
✅ SHADOW GET ACCEPTED
   📊 Version: 1
   ⏰ Timestamp: 1642248610
   📡 Current Shadow: {
     "state": {
       "reported": {
         "temperature": 22.5,
         "humidity": 45.0,
         "status": "online"
       }
     },
     "metadata": {
       "reported": {
         "temperature": {"timestamp": 1642248500},
         "humidity": {"timestamp": 1642248500},
         "status": {"timestamp": 1642248500}
       }
     },
     "version": 1,
     "timestamp": 1642248610
   }
======================================================================

🌟 Shadow> desire temperature=25.0 status=active
🔄 Setting desired state (simulating cloud/app request)...

======================================================================
🌟 SHADOW MESSAGE RECEIVED [14:40:15.456]
======================================================================
🔄 SHADOW DELTA RECEIVED
   📝 Description: Desired state differs from reported state
   📊 Version: 2
   🔄 Changes Needed: {
     "temperature": 25.0,
     "status": "active"
   }

🔍 State Comparison:
   📱 Local State: {
     "temperature": 22.5,
     "status": "online"
   }
   🔄 Delta: {
     "temperature": 25.0,
     "status": "active"
   }

⚠️  Differences Found:
   • temperature: 22.5 → 25.0
   • status: online → active

Apply these changes to local device? (y/N): y
✅ Local state updated successfully
📡 Automatically reporting updated state to shadow...

======================================================================
🌟 SHADOW MESSAGE RECEIVED [14:40:18.789]
======================================================================
✅ SHADOW UPDATE ACCEPTED
   📊 New Version: 3
   ⏰ Timestamp: 1642248618
   📡 Updated Reported: {
     "temperature": 25.0,
     "humidity": 45.0,
     "status": "active",
     "firmware_version": "1.0.0"
   }
======================================================================
```

**Interactive State Editing:**
```
🌟 Shadow> edit
📝 Local State Editor
Current state: {
  "temperature": 25.0,
  "humidity": 45.0,
  "status": "active",
  "firmware_version": "1.0.0"
}

Options:
1. Edit individual values
2. Replace entire state with JSON
3. Cancel

Select option (1-3): 1

Current values:
   1. temperature: 25.0
   2. humidity: 45.0
   3. status: active
   4. firmware_version: 1.0.0
   5. Add new key
   6. Done editing

Select item to edit (1-6): 2

Editing 'humidity' (current: 45.0)
New value (or press Enter to keep current): 50.0
✅ Updated humidity = 50.0

Select item to edit (1-6): 6
✅ Editing complete

🌟 Shadow> report
🔄 Reporting local state to shadow...

======================================================================
🌟 SHADOW MESSAGE RECEIVED [14:40:25.123]
======================================================================
✅ SHADOW UPDATE ACCEPTED
   📊 New Version: 4
   📡 Updated Reported: {
     "temperature": 25.0,
     "humidity": 50.0,
     "status": "active",
     "firmware_version": "1.0.0"
   }
======================================================================
```

## Rules Engine Examples

### Rule Creation Workflow

**Rule Creation Menu:**
```
⚙️ IoT Rules Engine Explorer
============================
📋 Main Menu:
1. List all IoT Rules
2. Describe specific IoT Rule
3. Create new IoT Rule
4. Manage IoT Rule (enable/disable/delete)
5. Test IoT Rule with MQTT
6. Exit

Select option (1-6): 3

🔧 Rule Creation Wizard
======================
Enter rule name: TemperatureAlert
✅ Rule name 'TemperatureAlert' is available

📊 Event Type Selection:
1. temperature - Temperature sensor readings
2. humidity - Humidity measurements
3. pressure - Pressure sensor data
4. motion - Motion detection events
5. door - Door sensor status
6. alarm - Alarm system events
7. status - General device status
8. battery - Battery level reports
9. Custom - User-defined event type

Select event type (1-9): 1
✅ Selected event type: temperature
```

**SQL Statement Building:**
```
🔧 SQL Statement Builder
=======================
📥 Topic Pattern: testRulesEngineTopic/+/temperature

📝 SELECT Clause Options:
1. SELECT * (all attributes)
2. SELECT deviceId, timestamp, value (specific attributes)
3. SELECT deviceId, timestamp, temperature, humidity (multiple sensors)
4. Custom SELECT clause

Select option (1-4): 2
✅ SELECT clause: deviceId, timestamp, value

🔍 WHERE Clause (optional):
Enter WHERE condition (or press Enter for no filter): value > 30
✅ WHERE clause: value > 30

📝 Complete SQL Statement:
SELECT deviceId, timestamp, value 
FROM 'testRulesEngineTopic/+/temperature' 
WHERE value > 30

🎯 Action Configuration:
📤 Republish target topic: processed/temperature
🔑 AWS IAM Role: IoTRulesEngineRole (will be created if needed)

Confirm rule creation? (y/N): y
```

**Automatic AWS IAM Setup:**
```
🔧 Setting up AWS IAM role for Rules Engine...
🔍 Checking if role 'IoTRulesEngineRole' exists...
❌ Role not found, creating new role...

🔄 Creating AWS IAM role 'IoTRulesEngineRole'...
✅ AWS IAM role created successfully

🔄 Attaching policy to role...
✅ Policy attached successfully

⏳ Waiting for AWS IAM eventual consistency (5 seconds)...

🔄 Creating IoT Rule 'TemperatureAlert'...
✅ Rule 'TemperatureAlert' created successfully!

📊 Rule Summary:
   Name: TemperatureAlert
   Status: ENABLED
   SQL: SELECT deviceId, timestamp, value FROM 'testRulesEngineTopic/+/temperature' WHERE value > 30
   Actions: 1 (republish to processed/temperature)
```

### Rule Testing Example

**Test Setup:**
```
📋 Main Menu:
5. Test IoT Rule with MQTT

Select option (1-6): 5

🧪 Rule Testing Mode
===================
📋 Available Rules:
1. TemperatureAlert - ENABLED
2. BatteryMonitor - DISABLED

Select rule to test (1-2): 1
✅ Selected rule: TemperatureAlert

📖 Rule Analysis:
   SQL: SELECT deviceId, timestamp, value FROM 'testRulesEngineTopic/+/temperature' WHERE value > 30
   📥 Topic Pattern: testRulesEngineTopic/+/temperature
   🔍 WHERE Condition: value > 30
   📤 Output Topic: processed/temperature

🔗 Establishing MQTT connection for testing...
✅ Connected to AWS IoT with certificate authentication
✅ Subscribed to output topic: processed/temperature
```

**Interactive Message Testing:**
```
🧪 Test Message Generator
========================
🧪 Test Message #1

📥 Topic Pattern: testRulesEngineTopic/+/temperature
Should this message MATCH the topic pattern? (y/n): y

🔍 WHERE Condition: value > 30
Should this message MATCH the WHERE condition? (y/n): y

📝 Generated Test Message:
📡 Topic: testRulesEngineTopic/device123/temperature
💬 Payload: {
  "deviceId": "test-device-123",
  "timestamp": 1642248600000,
  "value": 35.0,
  "unit": "celsius"
}

🔮 Prediction: Rule SHOULD trigger (topic matches AND value > 30)

📤 Publishing test message...
⏳ Waiting 3 seconds for rule processing...

======================================================================
🔔 RULE OUTPUT RECEIVED [14:45:10.123]
======================================================================
📤 Output Topic: processed/temperature
💬 Processed Message: {
  "deviceId": "test-device-123",
  "timestamp": 1642248600000,
  "value": 35.0
}
✅ Rule 'TemperatureAlert' processed and forwarded the message!
======================================================================

🧪 Test Message #2

📥 Topic Pattern: testRulesEngineTopic/+/temperature
Should this message MATCH the topic pattern? (y/n): y

🔍 WHERE Condition: value > 30
Should this message MATCH the WHERE condition? (y/n): n

📝 Generated Test Message:
📡 Topic: testRulesEngineTopic/sensor456/temperature
💬 Payload: {
  "deviceId": "test-sensor-456",
  "timestamp": 1642248605000,
  "value": 25.0,
  "unit": "celsius"
}

🔮 Prediction: Rule should NOT trigger (topic matches BUT value <= 30)

📤 Publishing test message...
⏳ Waiting 3 seconds for rule processing...

❌ No rule output received (as expected - WHERE condition not met)
✅ Rule correctly filtered out the message!
```

## Cleanup Examples

### Safe Resource Cleanup

**Cleanup Confirmation:**
```
🧹 AWS IoT Sample Data Cleanup
==============================
This script will safely remove ONLY the sample resources created by setup_sample_data.py:

✅ Safe to Delete:
   • 20 Things: Vehicle-VIN-001 through Vehicle-VIN-020
   • 3 Thing Types: SedanVehicle, SUVVehicle, TruckVehicle
   • 4 Thing Groups: CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet
   • Associated certificates and local files

❌ Will NOT Delete:
   • Your existing Things, Thing Types, or Thing Groups
   • Certificates attached to non-sample Things
   • IoT Policies (require manual review)

⚠️  This action cannot be undone.
Do you want to continue? (y/N): y
```

**Cleanup Process:**
```
🔍 Step 1: Discovering sample resources...
📋 Found Resources:
   Things: 20 sample Things found
   Thing Types: 3 sample Thing Types found
   Thing Groups: 4 sample Thing Groups found
   Certificates: 15 certificates attached to sample Things

🧹 Step 2: Certificate cleanup...
🔄 Processing Thing: Vehicle-VIN-001
   🔍 Found 1 certificate attached
   🔓 Detaching policies from certificate abc123def456...
   🔗 Detaching certificate from Thing...
   🔴 Deactivating certificate...
   🗑️  Deleting certificate...
   📁 Removing local certificate files...
   ✅ Certificate cleanup complete

🧹 Step 3: Thing cleanup...
🔄 Deleting Thing: Vehicle-VIN-001...
✅ Thing deleted successfully
...
✅ All 20 Things deleted successfully

🧹 Step 4: Thing Group cleanup...
🔄 Deleting Thing Group: CustomerFleet...
✅ Thing Group deleted successfully
...
✅ All 4 Thing Groups deleted successfully

🧹 Step 5: Thing Type cleanup...
⚠️  AWS requires 5-minute wait before deleting Thing Types
📋 Options:
1. Wait 5 minutes and delete automatically
2. Skip deletion (deprecate only)
3. Try immediate deletion (may fail)

Select option (1-3): 1

🔄 Deprecating Thing Type: SedanVehicle...
✅ Thing Type deprecated
⏳ Waiting 5 minutes for AWS propagation...
🔄 Deleting Thing Type: SedanVehicle...
✅ Thing Type deleted successfully
...

📊 Cleanup Summary:
   ✅ Things deleted: 20
   ✅ Certificates deleted: 15
   ✅ Thing Groups deleted: 4
   ✅ Thing Types deleted: 3
   ✅ Local files removed: 45

🎉 Cleanup complete! All sample resources have been removed.
💡 Your AWS account is now clean and no longer incurring charges for these resources.
```

### Dry-Run Mode Examples

**Preview Cleanup Before Deleting:**

```bash
$ python cleanup_sample_data.py --dry-run

🧹 AWS IoT Sample Data Cleanup
==============================

==============================
DRY RUN MODE - No resources will be deleted
==============================

This script will safely remove ONLY the sample resources created by setup_sample_data.py:

✅ Resources to Identify:
   • 20 Things: Vehicle-VIN-001 through Vehicle-VIN-020
   • 3 Thing Types: SedanVehicle, SUVVehicle, TruckVehicle
   • 4 Thing Groups: CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet
   • Associated certificates and local files

🔍 Step 1: Discovering sample resources...
📋 Found Resources:
   Things: 20 sample Things found
      • Vehicle-VIN-001, Vehicle-VIN-002, Vehicle-VIN-003, ...
   Thing Types: 3 sample Thing Types found
      • SedanVehicle, SUVVehicle, TruckVehicle
   Thing Groups: 4 sample Thing Groups found
      • CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet
   Certificates: 15 certificates attached to sample Things
      • abc123def456... → Vehicle-VIN-001
      • def456ghi789... → Vehicle-VIN-002
      • ...
   Policies: 3 IoT policies found
      • BasicDevicePolicy (attached to 10 certificates)
      • ReadOnlyPolicy (attached to 3 certificates)
      • CustomPolicy (attached to 2 certificates)
   IAM Roles: 1 role found
      • IoTRulesEngineRole (used by 2 rules)

🔍 Step 2: Analyzing dependencies...
📋 Dependency Analysis:
   Certificate Dependencies:
      • 15 certificates attached to Things
      • 15 policies attached to certificates
      • All dependencies can be resolved

   Thing Group Dependencies:
      • 20 Things in Thing Groups
      • All Things will be removed from groups before deletion

   Thing Type Dependencies:
      • 20 Things using Thing Types
      • Thing Types will be deprecated before deletion

   IAM Role Dependencies:
      • IoTRulesEngineRole used by 2 rules
      • Rules will be deleted before role deletion

📊 Deletion Summary (DRY RUN):
   Would delete: 20 Things
   Would delete: 15 Certificates
   Would detach and delete: 3 Policies
   Would delete: 4 Thing Groups
   Would deprecate and delete: 3 Thing Types
   Would delete: 1 IAM Role
   Would delete: 2 IoT Rules
   Would remove: 45 local certificate files

⏱️  Estimated cleanup time: 2-3 minutes
💾 Estimated storage freed: ~50 MB (local certificates)

💡 DRY RUN COMPLETE - No resources were modified or deleted

To perform actual cleanup, run:
   python cleanup_sample_data.py
```

**Dry-Run with Custom Prefix:**

```bash
$ python cleanup_sample_data.py --dry-run --things-prefix "Dev-"

🧹 AWS IoT Sample Data Cleanup
==============================
DRY RUN MODE - No resources will be deleted
==============================

📝 Configuration:
   Target Prefix: Dev-
   Searching for Things: Dev-001 through Dev-020

🔍 Step 1: Discovering sample resources...
📋 Found Resources:
   Things: 20 sample Things found with prefix 'Dev-'
      • Dev-001, Dev-002, Dev-003, ... Dev-020
   Thing Types: 3 sample Thing Types found
   Thing Groups: 4 sample Thing Groups found
   Certificates: 12 certificates attached to Dev- Things
   Policies: 2 IoT policies found

📊 Deletion Summary (DRY RUN):
   Would delete: 20 Things (prefix: Dev-)
   Would delete: 12 Certificates
   Would delete: 2 Policies
   Would delete: 4 Thing Groups
   Would delete: 3 Thing Types
   Would remove: 36 local certificate files

💡 DRY RUN COMPLETE - No resources were modified or deleted

💡 Note: Things with prefix 'Staging-' and 'Prod-' will NOT be affected
```

### Prefix-Based Cleanup

**Clean Up Specific Environment:**

```bash
$ python cleanup_sample_data.py --things-prefix "Dev-"

🧹 AWS IoT Sample Data Cleanup
==============================

📝 Configuration:
   Target Prefix: Dev-
   Searching for Things: Dev-001 through Dev-020

This script will safely remove ONLY the sample resources with prefix 'Dev-':

✅ Safe to Delete:
   • 20 Things: Dev-001 through Dev-020
   • 3 Thing Types: SedanVehicle, SUVVehicle, TruckVehicle
   • 4 Thing Groups: CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet
   • Associated certificates and local files

❌ Will NOT Delete:
   • Things with other prefixes (Staging-, Prod-, etc.)
   • Your existing Things, Thing Types, or Thing Groups
   • Certificates attached to non-Dev Things

⚠️  This action cannot be undone.
Do you want to continue? (y/N): y

🔍 Step 1: Discovering sample resources...
✅ Found 20 Things with prefix 'Dev-'

🧹 Step 2: Certificate cleanup...
🔄 Processing Thing: Dev-001
   ✅ Certificate cleanup complete
...

🧹 Step 3: Thing cleanup...
✅ Deleted Thing: Dev-001
✅ Deleted Thing: Dev-002
...
✅ All 20 Things deleted successfully

🧹 Step 4: Thing Group cleanup...
✅ All 4 Thing Groups deleted successfully

🧹 Step 5: Thing Type cleanup...
✅ All 3 Thing Types deleted successfully

📊 Cleanup Summary:
   ✅ Things deleted: 20 (prefix: Dev-)
   ✅ Certificates deleted: 12
   ✅ Policies deleted: 2
   ✅ Thing Groups deleted: 4
   ✅ Thing Types deleted: 3
   ✅ Local files removed: 36

🎉 Cleanup complete! All Dev- resources have been removed.
💡 Resources with other prefixes remain untouched.
```

**Verify Other Environments Remain:**

```bash
$ python iot_registry_explorer.py

Select operation (1-9): 1

🔄 API Call: list_things
📤 Response: Found 20 Things

Staging Environment (Still Exists):
1. Staging-001 (Type: SedanVehicle)
2. Staging-002 (Type: SUVVehicle)
...
20. Staging-020 (Type: TruckVehicle)

✅ Dev- resources deleted
✅ Staging- resources preserved
```

### Multi-Environment Cleanup

**Scenario**: Clean up multiple environments selectively.

**Step 1: Preview All Environments**

```bash
# Preview dev cleanup
$ python cleanup_sample_data.py --dry-run --things-prefix "Dev-"
📊 Would delete: 20 Things (prefix: Dev-)

# Preview staging cleanup
$ python cleanup_sample_data.py --dry-run --things-prefix "Staging-"
📊 Would delete: 20 Things (prefix: Staging-)

# Preview prod cleanup
$ python cleanup_sample_data.py --dry-run --things-prefix "Prod-"
📊 Would delete: 20 Things (prefix: Prod-)
```

**Step 2: Clean Up Development Only**

```bash
$ python cleanup_sample_data.py --things-prefix "Dev-"

Do you want to continue? (y/N): y

✅ Deleted 20 Things with prefix 'Dev-'
🎉 Dev environment cleaned up!
```

**Step 3: Verify Staging and Prod Remain**

```bash
$ python iot_registry_explorer.py

Select operation (1-9): 1

📤 Response: Found 40 Things

Staging Environment (Preserved):
1. Staging-001 through Staging-020

Production Environment (Preserved):
21. Prod-001 through Prod-020

✅ Only Dev- resources were deleted
✅ Staging and Prod environments remain intact
```

**Step 4: Clean Up Staging When Ready**

```bash
$ python cleanup_sample_data.py --things-prefix "Staging-"

Do you want to continue? (y/N): y

✅ Deleted 20 Things with prefix 'Staging-'
🎉 Staging environment cleaned up!
```

**Complete Workflow Example:**

```bash
# Day 1: Create multiple environments
python setup_sample_data.py --things-prefix "Dev-"
python setup_sample_data.py --things-prefix "Staging-"
python setup_sample_data.py --things-prefix "Prod-"

# Day 2: Work with dev environment
python certificate_manager.py  # Select Dev- Things
python mqtt_client_explorer.py  # Test with Dev- devices

# Day 3: Preview dev cleanup
python cleanup_sample_data.py --dry-run --things-prefix "Dev-"

# Day 4: Clean up dev, keep staging and prod
python cleanup_sample_data.py --things-prefix "Dev-"

# Day 5: Clean up staging when testing complete
python cleanup_sample_data.py --things-prefix "Staging-"

# Day 6: Keep prod for demos, or clean up when done
python cleanup_sample_data.py --things-prefix "Prod-"
```

## Error Handling Examples

### Common Error Scenarios

**Certificate Not Found Error:**
```
❌ Error in MQTT connection setup
Certificate files not found for Thing: Vehicle-VIN-001

💡 Solution:
1. Run certificate_manager.py first
2. Create and attach a certificate to this Thing
3. Ensure certificate files exist in certificates/Vehicle-VIN-001/

🔍 Debug steps:
   ls -la certificates/Vehicle-VIN-001/
   python certificate_manager.py
```

**Permission Denied Error:**
```
❌ Error: AccessDeniedException - User is not authorized to perform: iot:CreateThing

💡 Solution:
Your AWS credentials need IoT permissions. Add this policy to your AWS IAM user:
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": "iot:*",
    "Resource": "*"
  }]
}

🔍 Check current permissions:
   aws sts get-caller-identity
   aws iam list-attached-user-policies --user-name <your-username>
```

**MQTT Connection Timeout:**
```
❌ MQTT Connection failed: Connection timeout

💡 Troubleshooting steps:
1. Check network connectivity:
   ping a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com

2. Verify certificate is active:
   python iot_registry_explorer.py
   # Select option 2 (List Certificates)

3. Check firewall (port 8883 must be open):
   telnet a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com 8883

4. Verify certificate-Thing attachment:
   python iot_registry_explorer.py
   # Select option 5 (Describe Thing)
```

These examples demonstrate the complete learning journey from setup through cleanup, showing real interactions and outputs you'll see when using the scripts.