# AWS IoT Core - Learning Path - Basics

> 🌍 **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言** | **사용 가능한 언어** | **Verfügbare Sprachen** | **Lingue Disponibili** | **Langues Disponibles**
> 
> - **English** (Current) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) 🇩🇪 | [Italiano](README.it.md) 🇮🇹 | [Français](README.fr.md) 🇫🇷
> - **Documentation**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/) | [Deutsch](docs/de/) 🇩🇪 | [Italiano](docs/it/) 🇮🇹 | [Français](docs/fr/) 🇫🇷

A friendly Python toolkit to help you learn Amazon Web Services (AWS) AWS IoT Core basics through hands-on exploration. Interactive scripts walk you through device management, security, API operations, and MQTT communication with clear explanations along the way.

These same scripts serve as the baseline for the publicly available [AWS IoT Core Basics Workshop](https://catalog.workshops.aws/workshops/a007780e-1086-421b-a7e3-b7ac63e37089). Beyond the toolkit itself, the workshop is a great way to better understand the different AWS IoT Core use cases through a guided, hands-on experience.

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
export AWS_IOT_LANG=en  # 'es' for Spanish, 'ja' for Japanese, 'zh-CN' for Chinese, 'pt-BR' for Portuguese, 'ko' for Korean, 'de' for German, 'it' for Italian, 'fr' for French

# 5. Complete learning sequence
python scripts/setup_sample_data.py          # Create sample IoT resources
python scripts/iot_registry_explorer.py      # Explore AWS IoT APIs
python scripts/certificate_manager.py        # Learn IoT security
python scripts/mqtt_client_explorer.py       # Real-time MQTT communication
python scripts/device_shadow_explorer.py     # Device state synchronization
python scripts/iot_rules_explorer.py         # Message routing and processing
python scripts/cleanup_sample_data.py        # Clean up resources (IMPORTANT!)
```

**⚠️ Heads up**: This creates real AWS resources (about $0.17 total). Make sure to run cleanup when you're done!

## Who This Is For

**Perfect for:** Cloud developers, solution architects, and DevOps engineers who are new to AWS IoT Core

**You'll need:** Basic AWS knowledge, some Python fundamentals, and comfort with the command line

**Learning Level:** Associate level with a hands-on approach

## 🔧 Built with AWS SDKs

This project uses the official AWS SDKs to give you an authentic AWS IoT Core experience:

### **Boto3 - AWS SDK for Python**
- **What it does**: Powers all AWS IoT Registry operations, certificate management, and Rules Engine interactions
- **Version**: `>=1.26.0`
- **Documentation**: [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core APIs**: [Boto3 IoT Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK for Python**
- **What it does**: Enables authentic MQTT communication with AWS IoT Core using X.509 certificates
- **Version**: `>=1.11.0`
- **Documentation**: [AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Why These SDKs Matter:**
- **Production-Ready**: Same SDKs used in real IoT applications
- **Security**: Built-in support for AWS IoT security best practices
- **Reliability**: Official AWS-maintained libraries with solid error handling
- **Learning Value**: You'll experience authentic AWS IoT development patterns

## Table of Contents

- 🚀 [Quick Start](#-quick-start---complete-learning-path)
- ⚙️ [Installation & Setup](#️-installation--setup)
- 📚 [Learning Scripts](#-learning-scripts)
- 🧹 [Resource Cleanup](#-resource-cleanup)
- 🛠️ [Troubleshooting](#-troubleshooting)
- 📖 [Advanced Documentation](#-advanced-documentation)

## ⚙️ Installation & Setup

### What You'll Need
- Python 3.10 or higher
- An AWS account with IoT permissions
- Terminal or command line access
- OpenSSL (for certificate features)

**⚠️ IMPORTANT SAFETY NOTE**: Please use a dedicated development or learning AWS account. Don't run these scripts in accounts with production IoT resources. While the cleanup script has multiple safety features, it's always best practice to use isolated environments for learning.

### What It Costs

**This project creates real AWS resources that will cost about $0.17 total.**

| Service | Usage | Estimated Cost (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100 messages, 20 devices | $0.10 |
| **AWS IoT Device Shadow service** | ~30 shadow operations | $0.04 |
| **IoT Rules Engine** | ~50 rule executions | $0.01 |
| **Certificate Storage** | 20 certificates for 1 day | $0.01 |
| **Amazon CloudWatch Logs** | Basic logging | $0.01 |
| **Total Estimated** | **Complete learning session** | **~$0.17** |

**⚠️ Important**: Always run the cleanup script when you're done to avoid ongoing charges.



### Getting Set Up

**1. Clone the Repository:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Install OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Download from [OpenSSL website](https://www.openssl.org/)

**3. Set Up a Virtual Environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Choose Your Language (Optional):**
```bash
# Set language preference for all scripts
export AWS_IOT_LANG=en     # English (default)
export AWS_IOT_LANG=es     # Spanish
export AWS_IOT_LANG=ja     # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko     # Korean
export AWS_IOT_LANG=de     # German
export AWS_IOT_LANG=it     # Italian
export AWS_IOT_LANG=fr     # French

# Alternative: Scripts will ask you to pick a language if you don't set one
```

**Supported Languages:**
- **English** (`en`, `english`) - Default
- **Spanish** (`es`, `spanish`, `español`) - Full translation available
- **Japanese** (`ja`, `japanese`, `日本語`, `jp`) - Full translation available
- **Chinese** (`zh-CN`, `chinese`, `中文`, `zh`) - Full translation available
- **Portuguese** (`pt-BR`, `portuguese`, `português`, `pt`) - Full translation available
- **Korean** (`ko`, `korean`, `한국어`, `kr`) - Full translation available
- **German** (`de`, `german`, `deutsch`) - Full translation available
- **Italian** (`it`, `italian`, `italiano`) - Full translation available
- **French** (`fr`, `french`, `français`) - Full translation available

## 🌍 Multi-Language Support

All learning scripts support English, Spanish, Japanese, Chinese, Portuguese, Korean, German, Italian, and French. The language you choose affects:

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

**How to Use It:**

**Option 1: Set an Environment Variable (Recommended)**
```bash
# Set language preference for all scripts
export AWS_IOT_LANG=en     # English
export AWS_IOT_LANG=es     # Spanish
export AWS_IOT_LANG=ja     # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko     # Korean
export AWS_IOT_LANG=de     # German
export AWS_IOT_LANG=it     # Italian
export AWS_IOT_LANG=fr     # French

# Run any script - language will be applied automatically
python scripts/iot_registry_explorer.py
```

**Option 2: Pick Interactively**
```bash
# Run without setting the environment variable - the script will ask you to pick a language
python scripts/setup_sample_data.py

# Here's what you'll see:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma / 언어 선택 / Sprachauswahl / Selezione della Lingua / Sélection de la Langue
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# 6. 한국어 (Korean)
# 7. Deutsch (German)
# 8. Italiano (Italian)
# 9. Français (French)
# Select language (1-9): 9
```

**Scripts That Support Multiple Languages:**
- ✅ `setup_sample_data.py` - Sample data creation
- ✅ `iot_registry_explorer.py` - API exploration
- ✅ `certificate_manager.py` - Certificate management
- ✅ `mqtt_client_explorer.py` - MQTT communication
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - AWS IoT Device Shadow service operations
- ✅ `iot_rules_explorer.py` - Rules Engine exploration
- ✅ `cleanup_sample_data.py` - Resource cleanup



## 📚 Learning Scripts

**Here's Your Learning Path:**

### 1. 📊 Set Up Sample Data
**File**: `scripts/setup_sample_data.py`
**What it does**: Creates realistic IoT resources for hands-on learning with automatic tagging
**Creates**: 20 Things, 3 Thing Types, 4 Thing Groups, IoT Rules (all tagged for easy cleanup)

**Cool Features:**
- **Automatic Tagging**: All resources get tagged so cleanup can find them easily
- **Custom Prefixes**: You can use your own thing name prefixes
- **Multi-Language**: Works in all supported languages

**How to Use It:**
```bash
# Basic setup with default prefix (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Setup with custom prefix
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Setup with language selection
export AWS_IOT_LANG=es
python scripts/setup_sample_data.py
```

**How Resources Get Tagged:**
All created resources get these tags so cleanup can find them safely:
- `workshop-resource: true` - Marks as workshop-created
- `created-by: setup-script` - Identifies the creating script
- `workshop-name: iot-core-basics` - Groups by workshop name

These tags help the cleanup script safely find and remove only workshop resources, keeping your production IoT stuff protected.

### 2. 🔍 Explore IoT Registry APIs
**File**: `scripts/iot_registry_explorer.py`
**What it does**: Interactive tool for learning AWS IoT Registry APIs
**Features**: 8 core APIs with clear explanations and real API calls

### 3. 🔐 Manage Certificates & Policies
**File**: `scripts/certificate_manager.py`
**What it does**: Learn AWS IoT security through certificate and policy management
**Features**: Certificate creation, policy attachment, external certificate registration

### 4. 📡 Try MQTT Communication
**Files**: 
- `scripts/mqtt_client_explorer.py` (Certificate-based, recommended)
- `scripts/mqtt_websocket_explorer.py` (WebSocket-based alternative)

**What it does**: Experience real-time IoT communication using MQTT protocol
**Features**: Interactive command-line interface, topic subscription, message publishing

### 5. 🌟 Explore AWS IoT Device Shadow
**File**: `scripts/device_shadow_explorer.py`
**What it does**: Learn device state synchronization with AWS IoT Device Shadow
**Features**: Interactive shadow management, state updates, delta processing

### 6. ⚙️ Explore IoT Rules Engine
**File**: `scripts/iot_rules_explorer.py`
**What it does**: Learn message routing and processing with IoT Rules Engine
**Features**: Rule creation, SQL filtering, automatic AWS IAM setup

### 7. 🧹 Clean Up Sample Data
**File**: `scripts/cleanup_sample_data.py`
**What it does**: Clean up all learning resources to avoid charges
**Features**: Safe cleanup with dependency handling

## 🧹 Resource Cleanup

**⚠️ IMPORTANT**: Always run cleanup when you're done learning to avoid ongoing AWS charges.

### How to Use It

```bash
# Standard cleanup - removes all workshop resources
python scripts/cleanup_sample_data.py

# Preview what will be deleted (we recommend doing this first)
python scripts/cleanup_sample_data.py --dry-run

# Cleanup with a custom prefix
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# Turn on debug mode for detailed API logging
python scripts/cleanup_sample_data.py --debug
```

### What the Parameters Do

| Parameter | Description | Default | Example |
|-----------|-------------|---------|---------|
| `--things-prefix` | Custom prefix for thing names | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | Preview cleanup without deleting | `False` | `--dry-run` |
| `--debug` | Enable detailed API logging | `False` | `--debug` |

### How Resource Identification Works

The cleanup script uses a **dual identification system** to safely find workshop resources:

**1. Tag-Based Identification (Main Method)**
- Resources created by setup scripts automatically get tagged with:
  - `workshop-resource: true` - Marks it as workshop-created
  - `created-by: setup-script` - Shows which script created it
  - `workshop-name: iot-core-basics` - Groups resources by workshop
- **Why it's great**: Most reliable method, works no matter what you named things

**2. Naming Convention Fallback (Backup Method)**
- If tags aren't there, the script looks for resources by their names:
  - Things: Match the `--things-prefix` pattern (default: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - IoT Rules: Match `*Rule`, `rule_*`, or `*_workshop_*` patterns
- **Why it's useful**: Works with resources created before we added tagging

### Try Dry-Run First (We Recommend This!)

**Always preview cleanup operations before running them:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-run mode will:**
- ✅ Find all workshop resources that would be deleted
- ✅ Show you a detailed list of resources by type
- ✅ Show the deletion order (respects dependencies)
- ✅ Give you a summary report
- ❌ **NOT delete anything**

**Here's what you'll see:**
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

### Using Custom Prefixes

If you created resources with a custom prefix during setup, use the same prefix for cleanup:

```bash
# Setup with custom prefix
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Cleanup with matching prefix
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**Important**: The prefix needs to match exactly between setup and cleanup for name-based identification to work.

### What Gets Cleaned Up

**Resources We'll Delete (in the right order):**
1. ✅ Thing Shadows (device state data)
2. ✅ Certificates (detached from things first)
3. ✅ Things (IoT devices)
4. ✅ IoT Rules (message routing rules)
5. ✅ Thing Groups (device collections)
6. ✅ Thing Types (device templates)
7. ✅ Policies (security policies)
8. ✅ Local certificate files (from `certs/` directory)

**Resources We'll Keep Safe:**
- ❌ Production IoT resources (without workshop tags)
- ❌ Resources with different naming patterns
- ❌ Certificates and policies not associated with workshop things
- ❌ Resources created outside the workshop scripts

### How We Handle Dependencies

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

**The script handles this automatically** - you don't need to worry about it.

### Understanding Your Summary Report

After cleanup finishes, you'll see a summary report:

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

**What the columns mean:**
- **Identified**: Resources we found matching workshop criteria
- **Deleted**: Resources we successfully removed
- **Failed**: Resources that couldn't be deleted (with error details)

### If Something Goes Wrong

**Issue: "No resources found"**
- **Why**: Resources might not have workshop tags or don't match the prefix
- **Fix**: 
  - Check if you used a custom prefix during setup
  - Use `--things-prefix` with the right prefix
  - Check if resources exist in AWS Console

**Issue: "Permission denied" errors**
- **Why**: Your AWS credentials don't have the necessary IoT permissions
- **Fix**: Make sure your IAM user or role has IoT full access permissions

**Issue: "Dependency conflict" errors**
- **Why**: Resources have dependencies that weren't handled
- **Fix**: The script should handle this automatically. If it keeps happening, run with `--debug` to see details

**Issue: Some resources didn't get deleted**
- **Why**: Resources might be in use or have external dependencies
- **Fix**: 
  - Check the summary report for failed resources
  - Use AWS Console to manually look at and delete remaining resources
  - Run cleanup again after fixing dependencies

### Tips for Success

1. **Always try dry-run first**: Preview what will be deleted before running it
2. **Match your prefixes**: Use the same `--things-prefix` for setup and cleanup
3. **Check the summary**: Look at the report to make sure all resources were deleted
4. **Run cleanup soon**: Don't leave workshop resources running to avoid charges
5. **Keep credentials safe**: Never commit AWS credentials to version control

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

### Turn On Debug Mode

All scripts support debug mode for detailed API logging:
```bash
python scripts/<script_name>.py --debug
```

## ❓ Questions You Might Have

### General Questions

**Q: What resources will be deleted by the cleanup script?**
A: The cleanup script finds and deletes resources created by the workshop setup scripts. This includes Things, Certificates, Thing Groups, Thing Types, IoT Rules, and Policies that have workshop tags or match the naming patterns. Your production resources stay safe.

**Q: How do I preview cleanup without deleting anything?**
A: Use the `--dry-run` flag:
```bash
python scripts/cleanup_sample_data.py --dry-run
```
This shows exactly what would be deleted without actually changing anything.

**Q: Can I use a custom prefix for thing names?**
A: Yes! Use the `--things-prefix` parameter in both setup and cleanup:
```bash
# Setup
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Cleanup
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**Q: What if I don't have tags on my resources?**
A: No worries! The cleanup script has a backup plan. If tags aren't there, it uses naming conventions to find workshop resources. Resources matching the thing prefix pattern (default: `Vehicle-VIN-`) or standard workshop names will be found.

**Q: How do I change the language?**
A: Set the `AWS_IOT_LANG` environment variable:
```bash
export AWS_IOT_LANG=es  # Spanish
export AWS_IOT_LANG=ja  # Japanese
export AWS_IOT_LANG=zh-CN  # Chinese
export AWS_IOT_LANG=pt-BR  # Portuguese
export AWS_IOT_LANG=ko  # Korean
```
Or run the script without setting it - you'll get asked to pick a language.

**Q: What if cleanup fails partway through?**
A: The cleanup script is designed to be run multiple times safely. If cleanup fails:
1. Check the summary report to see which resources failed
2. Run the script again - it will skip already-deleted resources
3. Use `--debug` mode to see detailed error messages
4. Manually delete remaining resources via AWS Console if needed

**Q: How do I verify resources were deleted?**
A: Check the summary report at the end of cleanup. You can also check in the AWS IoT Console:
- Go to AWS IoT Core → Manage → Things
- Make sure workshop things (Vehicle-VIN-*) are gone
- Check that Thing Groups, Thing Types, and Certificates are removed

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
- **Tag-based** (main method): Uses AWS resource tags (`workshop-resource: true`). Most reliable, works no matter what you named things.
- **Naming-based** (backup): Uses naming patterns (like `Vehicle-VIN-*`). Works with older resources created before we added tagging.

The script tries tags first, then falls back to naming patterns if tags aren't there.

**Q: Can I use this in a production AWS account?**
A: While the cleanup script has multiple safety features (tags, naming patterns, dry-run mode), **we strongly recommend using a dedicated development or learning AWS account**. This follows AWS best practices for keeping environments separate.

**Q: What happens if I interrupt cleanup with Ctrl+C?**
A: The script handles interruptions gracefully. Resources deleted before you stopped stay deleted. Just run the cleanup script again to continue - it will skip already-deleted resources and finish the rest.

**Q: How much does it cost to run these learning scripts?**
A: About $0.17 USD for a complete learning session. Check out the [What It Costs](#what-it-costs) section for a detailed breakdown. Always run cleanup when you're done to avoid ongoing charges.

## 📖 More Documentation

### Detailed Guides
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

### Deutsche Dokumentation
- **[Detaillierte Skript-Anleitung](docs/de/DETAILED_SCRIPTS.md)** - Ausführliche Dokumentation der Skripte
- **[Vollständige Beispiele](docs/de/EXAMPLES.md)** - Vollständige Workflows und Beispielausgaben
- **[Fehlerbehebungsanleitung](docs/de/TROUBLESHOOTING.md)** - Häufige Probleme und Lösungen

### Documentazione Italiana
- **[Guida Dettagliata agli Script](docs/it/DETAILED_SCRIPTS.md)** - Documentazione approfondita degli script
- **[Esempi Completi](docs/it/EXAMPLES.md)** - Flussi di lavoro completi ed esempi di output
- **[Guida alla Risoluzione dei Problemi](docs/it/TROUBLESHOOTING.md)** - Problemi comuni e soluzioni

### Documentation Française
- **[Guide Détaillé des Scripts](docs/fr/DETAILED_SCRIPTS.md)** - Documentation approfondie des scripts
- **[Exemples Complets](docs/fr/EXAMPLES.md)** - Flux de travail complets et exemples de sortie
- **[Guide de Dépannage](docs/fr/TROUBLESHOOTING.md)** - Problèmes courants et solutions


### Where to Learn More

#### AWS IoT Core Documentation
- **[AWS IoT Core Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[AWS IoT Core API Reference](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### AWS SDKs We Use in This Project
- **[Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Complete Python SDK documentation
- **[Boto3 IoT Client Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT-specific API methods
- **[AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTT client documentation
- **[AWS IoT Device SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Source code and examples

#### Protocols and Standards
- **[MQTT Protocol Specification](https://mqtt.org/)** - Official MQTT documentation
- **[X.509 Certificate Standard](https://tools.ietf.org/html/rfc5280)** - Certificate format specification

## 🤝 Want to Contribute?

This is an educational project. We welcome contributions that make the learning experience better:

- **Bug fixes** for script issues
- **Translation improvements** for better localization
- **Documentation improvements** for clarity
- **Additional learning scenarios** that fit the basic level

## 📄 License

This project is licensed under the MIT-0 License - see the [LICENSE](LICENSE) file for details.

## 🏷️ Tags

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`