# AWS IoT Core - Learning Path - Basics

> 🌍 **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言** | **사용 가능한 언어**
> 
> - **English** (Current) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | [한국어](README.ko.md)
> - **Documentation**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/)

A comprehensive Python toolkit for learning Amazon Web Services (AWS) AWS IoT Core basic concepts through hands-on exploration. Interactive scripts demonstrate device management, security, API operations, and MQTT communication with detailed explanations.

## 🚀 Quick Start - Complete Learning Path

```bash
# 1. Clone and setup
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Setup environment
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Configure AWS credentials
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=<your-region (e.g. us-east-1)>

# 4. Optional: Set language preference
export AWS_IOT_LANG=en  # 'es' for Spanish, 'ja' for Japanese, 'zh-CN' for Chinese, 'pt-BR' for Portuguese, 'ko' for Korean

# 5. Complete learning sequence
python scripts/setup_sample_data.py          # Create sample IoT resources
python scripts/iot_registry_explorer.py      # Explore AWS IoT APIs
python scripts/certificate_manager.py        # Learn IoT security
python scripts/mqtt_client_explorer.py       # Real-time MQTT communication
python scripts/device_shadow_explorer.py     # Device state synchronization
python scripts/iot_rules_explorer.py         # Message routing and processing
python scripts/cleanup_sample_data.py        # Clean up resources (IMPORTANT!)
```

**⚠️ Cost Warning**: This creates real AWS resources (~$0.17 total). Run cleanup when finished!

## Target Audience

**Primary Audience:** Cloud developers, solution architects, DevOps engineers new to AWS IoT Core

**Prerequisites:** Basic AWS knowledge, Python fundamentals, command line usage

**Learning Level:** Associate level with hands-on approach

## 🔧 Built with AWS SDKs

This project leverages the official AWS SDKs to provide authentic AWS IoT Core experiences:

### **Boto3 - AWS SDK for Python**
- **Purpose**: Powers all AWS IoT Registry operations, certificate management, and Rules Engine interactions
- **Version**: `>=1.26.0`
- **Documentation**: [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core APIs**: [Boto3 IoT Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK for Python**
- **Purpose**: Enables authentic MQTT communication with AWS IoT Core using X.509 certificates
- **Version**: `>=1.11.0`
- **Documentation**: [AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Why These SDKs Matter:**
- **Production-Ready**: Same SDKs used in real IoT applications
- **Security**: Built-in support for AWS IoT security best practices
- **Reliability**: Official AWS-maintained libraries with comprehensive error handling
- **Learning Value**: Experience authentic AWS IoT development patterns

## Table of Contents

- 🚀 [Quick Start](#-quick-start---complete-learning-path)
- ⚙️ [Installation & Setup](#️-installation--setup)
- 📚 [Learning Scripts](#-learning-scripts)
- 🧹 [Resource Cleanup](#-resource-cleanup)
- 🛠️ [Troubleshooting](#-troubleshooting)
- 📖 [Advanced Documentation](#-advanced-documentation)

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- AWS account with IoT permissions
- Terminal/command line access
- OpenSSL (for certificate features)

**⚠️ IMPORTANT SAFETY NOTE**: Use a dedicated development/learning AWS account. Do not run these scripts in accounts containing production IoT resources. While the cleanup script has multiple safety mechanisms, best practice is to use isolated environments for learning activities.

### Cost Information

**This project creates real AWS resources that will incur charges (~$0.17 total).**

| Service | Usage | Estimated Cost (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100 messages, 20 devices | $0.10 |
| **AWS IoT Device Shadow service** | ~30 shadow operations | $0.04 |
| **IoT Rules Engine** | ~50 rule executions | $0.01 |
| **Certificate Storage** | 20 certificates for 1 day | $0.01 |
| **Amazon CloudWatch Logs** | Basic logging | $0.01 |
| **Total Estimated** | **Complete learning session** | **~$0.17** |

**⚠️ Important**: Always run the cleanup script when finished to avoid ongoing charges.



### Detailed Installation

**1. Clone Repository:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Install OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Download from [OpenSSL website](https://www.openssl.org/)

**3. Virtual Environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Language Configuration (Optional):**
```bash
# Set language preference for all scripts
export AWS_IOT_LANG=en     # English (default)
export AWS_IOT_LANG=es     # Spanish
export AWS_IOT_LANG=ja     # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko     # Korean

# Alternative: Scripts will prompt for language if not set
```

**Supported Languages:**
- **English** (`en`, `english`) - Default
- **Spanish** (`es`, `spanish`, `español`) - Full translation available
- **Japanese** (`ja`, `japanese`, `日本語`, `jp`) - Full translation available
- **Chinese** (`zh-CN`, `chinese`, `中文`, `zh`) - Full translation available
- **Portuguese** (`pt-BR`, `portuguese`, `português`, `pt`) - Full translation available
- **Korean** (`ko`, `korean`, `한국어`, `kr`) - Full translation available

## 🌍 Multi-Language Support

All learning scripts support English, Spanish, Japanese, Chinese, Portuguese, and Korean interfaces. The language affects:

**✅ What Gets Translated:**
- Welcome messages and educational content
- Menu options and user prompts
- Learning moments and explanations
- Error messages and confirmations
- Progress indicators and status messages

**❌ What Stays in Original Language:**
- AWS API responses (JSON data)
- Technical parameter names and values
- HTTP methods and endpoints
- Debug information and logs
- AWS resource names and identifiers

**Usage Options:**

**Option 1: Environment Variable (Recommended)**
```bash
# Set language preference for all scripts
export AWS_IOT_LANG=en     # English
export AWS_IOT_LANG=es     # Spanish
export AWS_IOT_LANG=ja     # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko     # Korean

# Run any script - language will be applied automatically
python scripts/iot_registry_explorer.py
```

**Option 2: Interactive Selection**
```bash
# Run without environment variable - script will prompt for language
python scripts/setup_sample_data.py

# Output example:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma / 언어 선택
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# 6. 한국어 (Korean)
# Select language (1-6): 6
```

**Supported Scripts:**
- ✅ `setup_sample_data.py` - Sample data creation
- ✅ `iot_registry_explorer.py` - API exploration
- ✅ `certificate_manager.py` - Certificate management
- ✅ `mqtt_client_explorer.py` - MQTT communication
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - AWS IoT Device Shadow service operations
- ✅ `iot_rules_explorer.py` - Rules Engine exploration
- ✅ `cleanup_sample_data.py` - Resource cleanup



## 📚 Learning Scripts

**Recommended Learning Path:**

### 1. 📊 Sample Data Setup
**File**: `scripts/setup_sample_data.py`
**Purpose**: Creates realistic IoT resources for hands-on learning with automatic tagging
**Creates**: 20 Things, 3 Thing Types, 4 Thing Groups, IoT Rules (with workshop tags)

**Key Features:**
- **Automatic Tagging**: All resources are tagged for safe cleanup identification
- **Custom Prefixes**: Support for custom thing name prefixes
- **Multi-Language**: Full internationalization support

**Usage Examples:**
```bash
# Basic setup with default prefix (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Setup with custom prefix
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Setup with language selection
export AWS_IOT_LANG=es
python scripts/setup_sample_data.py
```

**Resource Tagging:**
All created resources receive these tags for safe identification:
- `workshop-resource: true` - Marks as workshop-created
- `created-by: setup-script` - Identifies the creating script
- `workshop-name: iot-core-basics` - Groups by workshop name

These tags enable the cleanup script to safely identify and remove only workshop resources, protecting your production IoT infrastructure.

### 2. 🔍 IoT Registry API Explorer
**File**: `scripts/iot_registry_explorer.py`
**Purpose**: Interactive tool for learning AWS IoT Registry APIs
**Features**: 8 core APIs with detailed explanations and real API calls

### 3. 🔐 Certificate & Policy Manager
**File**: `scripts/certificate_manager.py`
**Purpose**: Learn AWS IoT security through certificate and policy management
**Features**: Certificate creation, policy attachment, external certificate registration

### 4. 📡 MQTT Communication
**Files**: 
- `scripts/mqtt_client_explorer.py` (Certificate-based, recommended)
- `scripts/mqtt_websocket_explorer.py` (WebSocket-based alternative)

**Purpose**: Experience real-time IoT communication using MQTT protocol
**Features**: Interactive command-line interface, topic subscription, message publishing

### 5. 🌟 AWS IoT Device Shadow service Explorer
**File**: `scripts/device_shadow_explorer.py`
**Purpose**: Learn device state synchronization with AWS IoT Device Shadow
**Features**: Interactive shadow management, state updates, delta processing

### 6. ⚙️ IoT Rules Engine Explorer
**File**: `scripts/iot_rules_explorer.py`
**Purpose**: Learn message routing and processing with IoT Rules Engine
**Features**: Rule creation, SQL filtering, automatic AWS IAM setup

### 7. 🧹 Sample Data Cleanup
**File**: `scripts/cleanup_sample_data.py`
**Purpose**: Clean up all learning resources to avoid charges
**Features**: Safe cleanup with dependency handling

## 🧹 Resource Cleanup

**⚠️ IMPORTANT**: Always run cleanup when finished learning to avoid ongoing AWS charges.

### Basic Usage

```bash
# Standard cleanup - removes all workshop resources
python scripts/cleanup_sample_data.py

# Preview what will be deleted (recommended first step)
python scripts/cleanup_sample_data.py --dry-run

# Cleanup with custom prefix
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# Enable debug mode for detailed API logging
python scripts/cleanup_sample_data.py --debug
```

### Command-Line Parameters

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `--things-prefix` | Custom prefix for thing names | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | Preview cleanup without deleting | `False` | `--dry-run` |
| `--debug` | Enable detailed API logging | `False` | `--debug` |

### How Resource Identification Works

The cleanup script uses a **dual identification system** to safely identify workshop resources:

**1. Tag-Based Identification (Primary Method)**
- Resources created by setup scripts are automatically tagged with:
  - `workshop-resource: true` - Identifies workshop-created resources
  - `created-by: setup-script` - Tracks which script created the resource
  - `workshop-name: iot-core-basics` - Groups resources by workshop
- **Advantage**: Most reliable method, works regardless of naming

**2. Naming Convention Fallback (Secondary Method)**
- If tags are not present, the script identifies resources by naming patterns:
  - Things: Match the `--things-prefix` pattern (default: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - IoT Rules: Match `*Rule`, `rule_*`, or `*_workshop_*` patterns
- **Advantage**: Works with resources created before tagging was implemented

### Dry-Run Mode (Recommended First Step)

**Always preview cleanup operations before executing them:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-run mode will:**
- ✅ Identify all workshop resources that would be deleted
- ✅ Display a detailed list of resources by type
- ✅ Show the deletion order (respects dependencies)
- ✅ Generate a summary report
- ❌ **NOT delete any resources**

**Example dry-run output:**
```
🔍 DRY RUN MODE - No resources will be deleted

Identified Resources:
  Things: 20 resources
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Certificates: 20 resources
  Thing Groups: 4 resources
  Thing Types: 3 resources
  IoT Rules: 1 resource

Total: 48 resources would be deleted
```

### Custom Prefix Usage

If you created resources with a custom prefix during setup, use the same prefix for cleanup:

```bash
# Setup with custom prefix
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Cleanup with matching prefix
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**Important**: The prefix must match exactly between setup and cleanup for naming-based identification to work correctly.

### What Gets Cleaned Up

**Resources Deleted (in dependency order):**
1. ✅ Thing Shadows (device state data)
2. ✅ Certificates (detached from things first)
3. ✅ Things (IoT devices)
4. ✅ IoT Rules (message routing rules)
5. ✅ Thing Groups (device collections)
6. ✅ Thing Types (device templates)
7. ✅ Policies (security policies)
8. ✅ Local certificate files (from `certs/` directory)

**Resources Protected:**
- ❌ Production IoT resources (without workshop tags)
- ❌ Resources with different naming patterns
- ❌ Certificates and policies not associated with workshop things
- ❌ Resources created outside the workshop scripts

### Dependency-Aware Deletion

The cleanup script automatically handles AWS IoT resource dependencies:

**Deletion Order:**
```
Thing Shadows → Certificates → Things → IoT Rules → Thing Groups → Thing Types → Policies
```

**Why this order matters:**
- Thing Shadows must be deleted before certificates
- Certificates must be detached before things can be deleted
- Things must be removed from groups before groups can be deleted
- Policies must be detached before deletion

**The script handles this automatically** - you don't need to worry about dependency conflicts.

### Understanding the Summary Report

After cleanup completes, you'll see a summary report:

```
📊 Cleanup Summary

Resource Type    | Identified | Deleted | Failed
-----------------|------------|---------|--------
Things           |         20 |      20 |      0
Certificates     |         20 |      20 |      0
Thing Groups     |          4 |       4 |      0
Thing Types      |          3 |       3 |      0
IoT Rules        |          1 |       1 |      0
Policies         |         20 |      20 |      0
-----------------|------------|---------|--------
Total            |         68 |      68 |      0

✅ Cleanup completed successfully!
```

**Report Fields:**
- **Identified**: Resources found matching workshop criteria
- **Deleted**: Resources successfully removed
- **Failed**: Resources that couldn't be deleted (with error details)

### Troubleshooting Cleanup

**Issue: "No resources found"**
- **Cause**: Resources may not have workshop tags or don't match the prefix
- **Solution**: 
  - Check if you used a custom prefix during setup
  - Use `--things-prefix` with the correct prefix
  - Verify resources exist in AWS Console

**Issue: "Permission denied" errors**
- **Cause**: AWS credentials lack necessary IoT permissions
- **Solution**: Ensure your IAM user/role has IoT full access permissions

**Issue: "Dependency conflict" errors**
- **Cause**: Resources have dependencies that weren't handled
- **Solution**: The script should handle this automatically. If it persists, run with `--debug` to see details

**Issue: Some resources not deleted**
- **Cause**: Resources may be in use or have external dependencies
- **Solution**: 
  - Check the summary report for failed resources
  - Use AWS Console to manually inspect and delete remaining resources
  - Run cleanup again after resolving dependencies

### Best Practices

1. **Always use dry-run first**: Preview what will be deleted before executing
2. **Match prefixes**: Use the same `--things-prefix` for setup and cleanup
3. **Review the summary**: Check the report to ensure all resources were deleted
4. **Run cleanup promptly**: Don't leave workshop resources running to avoid charges
5. **Keep credentials secure**: Never commit AWS credentials to version control

## 🛠️ Troubleshooting

### Common Issues

**AWS Credentials:**
```bash
# Set credentials
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Python Dependencies:**
```bash
pip install -r requirements.txt
```

**OpenSSL Issues:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### Debug Mode

All scripts support debug mode for detailed API logging:
```bash
python scripts/<script_name>.py --debug
```

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: What resources will be deleted by the cleanup script?**
A: The cleanup script identifies and deletes resources created by the workshop setup scripts. This includes Things, Certificates, Thing Groups, Thing Types, IoT Rules, and Policies that have workshop tags or match the naming patterns. Production resources are protected.

**Q: How do I preview cleanup without deleting anything?**
A: Use the `--dry-run` flag:
```bash
python scripts/cleanup_sample_data.py --dry-run
```
This shows exactly what would be deleted without making any changes.

**Q: Can I use a custom prefix for thing names?**
A: Yes! Use the `--things-prefix` parameter in both setup and cleanup:
```bash
# Setup
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Cleanup
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**Q: What if I don't have tags on my resources?**
A: The cleanup script has a fallback mechanism. If tags aren't present, it uses naming conventions to identify workshop resources. Resources matching the thing prefix pattern (default: `Vehicle-VIN-`) or standard workshop names will be identified.

**Q: How do I change the language?**
A: Set the `AWS_IOT_LANG` environment variable:
```bash
export AWS_IOT_LANG=es  # Spanish
export AWS_IOT_LANG=ja  # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko  # Korean
```
Or run the script without setting it - you'll be prompted to select a language interactively.

**Q: What if cleanup fails partway through?**
A: The cleanup script is designed to be idempotent - you can run it multiple times safely. If cleanup fails:
1. Check the summary report to see which resources failed
2. Run the script again - it will skip already-deleted resources
3. Use `--debug` mode to see detailed error messages
4. Manually delete remaining resources via AWS Console if needed

**Q: How do I verify resources were deleted?**
A: Check the summary report at the end of cleanup. You can also verify in the AWS IoT Console:
- Navigate to AWS IoT Core → Manage → Things
- Check that workshop things (Vehicle-VIN-*) are gone
- Verify Thing Groups, Thing Types, and Certificates are removed

### Technical Questions

**Q: Why does the cleanup script delete resources in a specific order?**
A: AWS IoT resources have dependencies. For example, you can't delete a Thing that still has certificates attached. The script follows this order:
1. Thing Shadows (no dependencies)
2. Certificates (must be detached from things)
3. Things (must be removed from groups)
4. IoT Rules (no dependencies on things)
5. Thing Groups (must be empty)
6. Thing Types (must not be in use)
7. Policies (must be detached)

**Q: What's the difference between tag-based and naming-based identification?**
A: 
- **Tag-based** (primary): Uses AWS resource tags (`workshop-resource: true`). Most reliable, works regardless of naming.
- **Naming-based** (fallback): Uses naming patterns (e.g., `Vehicle-VIN-*`). Works with older resources created before tagging was implemented.

The script tries tag-based first, then falls back to naming patterns if tags aren't present.

**Q: Can I use this in a production AWS account?**
A: While the cleanup script has multiple safety mechanisms (tags, naming patterns, dry-run mode), **we strongly recommend using a dedicated development/learning AWS account**. This follows AWS best practices for environment isolation.

**Q: What happens if I interrupt cleanup with Ctrl+C?**
A: The script handles interruptions gracefully. Resources deleted before the interruption remain deleted. Simply run the cleanup script again to continue - it will skip already-deleted resources and complete the remaining deletions.

**Q: How much does it cost to run these learning scripts?**
A: Approximately $0.17 USD for a complete learning session. See the [Cost Information](#cost-information) section for detailed breakdown. Always run cleanup when finished to avoid ongoing charges.

## 📖 Advanced Documentation

### Detailed Documentation
- **[Detailed Scripts Guide](docs/en/DETAILED_SCRIPTS.md)** - In-depth script documentation
- **[Complete Examples](docs/en/EXAMPLES.md)** - Full workflows and sample outputs
- **[Troubleshooting Guide](docs/en/TROUBLESHOOTING.md)** - Common issues and solutions

### Documentación en Español
- **[Guía Detallada de Scripts](docs/es/DETAILED_SCRIPTS.md)** - Documentación en profundidad de scripts
- **[Ejemplos Completos](docs/es/EXAMPLES.md)** - Flujos de trabajo completos y salidas de muestra
- **[Guía de Solución de Problemas](docs/es/TROUBLESHOOTING.md)** - Problemas comunes y soluciones

### Documentação em Português
- **[Guia Detalhado de Scripts](docs/pt-BR/DETAILED_SCRIPTS.md)** - Documentação aprofundada dos scripts
- **[Exemplos Completos](docs/pt-BR/EXAMPLES.md)** - Fluxos de trabalho completos e saídas de exemplo
- **[Guia de Solução de Problemas](docs/pt-BR/TROUBLESHOOTING.md)** - Problemas comuns e soluções

### 日本語ドキュメント
- **[詳細スクリプトガイド](docs/ja/DETAILED_SCRIPTS.md)** - 詳細なスクリプトドキュメント
- **[完全な例](docs/ja/EXAMPLES.md)** - 完全なワークフローとサンプル出力
- **[トラブルシューティングガイド](docs/ja/TROUBLESHOOTING.md)** - よくある問題と解決策

### 中文文档
- **[详细脚本指南](docs/zh-CN/DETAILED_SCRIPTS.md)** - 每个学习脚本的深入文档
- **[完整示例](docs/zh-CN/EXAMPLES.md)** - 完整的工作流程和实际场景
- **[故障排除指南](docs/zh-CN/TROUBLESHOOTING.md)** - 常见问题和错误的解决方案

### 한국어 문서
- **[자세한 스크립트 가이드](docs/ko/DETAILED_SCRIPTS.md)** - 각 학습 스크립트에 대한 심층 문서
- **[완전한 예제](docs/ko/EXAMPLES.md)** - 완전한 워크플로우 및 샘플 출력
- **[문제 해결 가이드](docs/ko/TROUBLESHOOTING.md)** - 일반적인 문제 및 해결책


### Learning Resources

#### AWS IoT Core Documentation
- **[AWS IoT Core Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[AWS IoT Core API Reference](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### AWS SDKs Used in This Project
- **[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Complete Python SDK documentation
- **[Boto3 IoT Client Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT-specific API methods
- **[AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTT client documentation
- **[AWS IoT Device SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Source code and examples

#### Protocol and Standards
- **[MQTT Protocol Specification](https://mqtt.org/)** - Official MQTT documentation
- **[X.509 Certificate Standard](https://tools.ietf.org/html/rfc5280)** - Certificate format specification

## 🤝 Contributing

This is an educational project. Contributions that improve the learning experience are welcome:

- **Bug fixes** for script issues
- **Translation improvements** for better localization
- **Documentation enhancements** for clarity
- **Additional learning scenarios** that fit the basic level

## 📄 License

This project is licensed under the MIT-0 License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`