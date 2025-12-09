# AWS IoT Core - 学习路径 - 基础

> 🌍 **可用语言** | **Available Languages** | **Idiomas Disponibles** | **利用可能な言語**
> 
> - [English](README.md) | [Español](README.es.md) | **中文** (当前) | [日本語](README.ja.md) | [Português](README.pt-BR.md)
> - **文档**: [English](docs/en/) | [Español](docs/es/) | **中文** (docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/)

通过动手探索学习 Amazon Web Services (AWS) AWS IoT Core 基本概念的综合 Python 工具包。交互式脚本演示设备管理、安全性、API 操作和 MQTT 通信，并提供详细说明。

## 🚀 快速开始 - 完整学习路径

```bash
# 1. 克隆和设置
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. 环境设置
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. 配置 AWS 凭证
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=<your-region (例如: us-east-1)>

# 4. 可选：设置语言偏好
export AWS_IOT_LANG=zh-CN  # 'en' 英语, 'es' 西班牙语, 'ja' 日语

# 5. 完整学习序列
python scripts/setup_sample_data.py          # 创建示例 IoT 资源
python scripts/iot_registry_explorer.py      # 探索 AWS IoT API
python scripts/certificate_manager.py        # 学习 IoT 安全
python scripts/mqtt_client_explorer.py       # 实时 MQTT 通信
python scripts/device_shadow_explorer.py     # 设备状态同步
python scripts/iot_rules_explorer.py         # 消息路由和处理
python scripts/cleanup_sample_data.py        # 清理资源（重要！）
```

**⚠️ 费用警告**: 这将创建真实的 AWS 资源（总计约 $0.17）。完成后请运行清理脚本！

## 目标受众

**主要受众**: 初次接触 AWS IoT Core 的云开发者、解决方案架构师、DevOps 工程师

**先决条件**: 基本的 AWS 知识、Python 基础、命令行使用经验

**学习级别**: 通过动手实践的助理级别方法

## 🔧 使用 AWS SDK 构建

此项目利用官方 AWS SDK 提供真实的 AWS IoT Core 体验：

### **Boto3 - AWS SDK for Python**
- **目的**: 支持所有 AWS IoT Registry 操作、证书管理和 Rules Engine 交互
- **版本**: `>=1.26.0`
- **文档**: [Boto3 文档](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core API**: [Boto3 IoT 客户端](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK for Python**
- **目的**: 使用 X.509 证书实现与 AWS IoT Core 的真实 MQTT 通信
- **版本**: `>=1.11.0`
- **文档**: [AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**为什么这些 SDK 很重要:**
- **生产就绪**: 与真实 IoT 应用程序中使用的相同 SDK
- **安全性**: 内置支持 AWS IoT 安全最佳实践
- **可靠性**: AWS 官方维护的库，具有全面的错误处理
- **学习价值**: 体验真实的 AWS IoT 开发模式

## 目录

- 🚀 [快速开始](#-快速开始---完整学习路径)
- ⚙️ [安装和设置](#️-安装和设置)
- 📚 [学习脚本](#-学习脚本)
- 🧹 [资源清理](#-资源清理)
- 🛠️ [故障排除](#-故障排除)
- 📖 [高级文档](#-高级文档)

## ⚙️ 安装和设置

### 先决条件
- Python 3.10+
- 具有 IoT 权限的 AWS 账户
- 终端/命令行访问
- OpenSSL（用于证书功能）

**⚠️ 重要安全注意事项**: 使用专用的开发/学习 AWS 账户。不要在包含生产 IoT 资源的账户中运行这些脚本。虽然清理脚本具有多重安全机制，但最佳实践是为学习活动使用隔离的环境。

### 费用信息

**此项目创建真实的 AWS 资源，将产生费用（总计约 $0.17）。**

| 服务 | 使用量 | 预估费用 (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | 约100条消息，20个设备 | $0.10 |
| **AWS IoT Device Shadow service** | 约30次影子操作 | $0.04 |
| **IoT Rules Engine** | 约50次规则执行 | $0.01 |
| **证书存储** | 20个证书存储1天 | $0.01 |
| **Amazon CloudWatch Logs** | 基本日志记录 | $0.01 |
| **总计预估** | **完整学习会话** | **约 $0.17** |

**⚠️ 重要**: 完成后务必运行清理脚本以避免持续费用。



### 详细安装

**1. 克隆仓库:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. 安装 OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** 从 [OpenSSL 网站](https://www.openssl.org/) 下载

**3. 虚拟环境（推荐）:**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. 语言配置（可选）:**
```bash
# 为所有脚本设置语言偏好
export AWS_IOT_LANG=zh-CN  # 中文
export AWS_IOT_LANG=en     # 英语（默认）
export AWS_IOT_LANG=es     # 西班牙语
export AWS_IOT_LANG=ja     # 日语

# 替代方案：如果未设置，脚本将提示选择语言
```

**支持的语言:**
- **英语** (`en`, `english`) - 默认
- **西班牙语** (`es`, `spanish`, `español`) - 完整翻译可用
- **日语** (`ja`, `japanese`, `日本語`, `jp`) - 完整翻译可用
- **中文** (`zh-CN`, `chinese`, `中文`, `zh`) - 完整翻译可用

## 🌍 多语言支持

所有学习脚本都支持英语、西班牙语、日语和中文界面。语言影响：

**✅ 翻译的内容:**
- 欢迎消息和教育内容
- 菜单选项和用户提示
- 学习要点和解释
- 错误消息和确认
- 进度指示器和状态消息

**❌ 保持原语言:**
- AWS API 响应（JSON 数据）
- 技术参数名称和值
- HTTP 方法和端点
- 调试信息和日志
- AWS 资源名称和标识符

**使用选项:**

**选项1: 环境变量（推荐）**
```bash
# 为所有脚本设置语言偏好
export AWS_IOT_LANG=zh-CN  # 中文
export AWS_IOT_LANG=en     # 英语
export AWS_IOT_LANG=es     # 西班牙语
export AWS_IOT_LANG=ja     # 日语

# 运行任何脚本 - 语言将自动应用
python scripts/iot_registry_explorer.py
```

**选项2: 交互式选择**
```bash
# 不使用环境变量运行 - 脚本将提示选择语言
python scripts/setup_sample_data.py

# 输出示例:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# Select language (1-4): 4
```

**支持的脚本:**
- ✅ `setup_sample_data.py` - 示例数据创建
- ✅ `iot_registry_explorer.py` - API 探索
- ✅ `certificate_manager.py` - 证书管理
- ✅ `mqtt_client_explorer.py` - MQTT 通信
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - AWS IoT Device Shadow service 操作
- ✅ `iot_rules_explorer.py` - Rules Engine 探索
- ✅ `cleanup_sample_data.py` - 资源清理

## 📚 学习脚本

**推荐学习路径:**

### 1. 📊 示例数据设置
**文件**: `scripts/setup_sample_data.py`
**目的**: 为动手学习创建真实的 IoT 资源
**创建**: 20个 Things、3个 Thing Types、4个 Thing Groups

### 2. 🔍 IoT Registry API 探索器
**文件**: `scripts/iot_registry_explorer.py`
**目的**: 学习 AWS IoT Registry API 的交互式工具
**功能**: 8个核心 API，包含详细说明和真实 API 调用

### 3. 🔐 证书和策略管理器
**文件**: `scripts/certificate_manager.py`
**目的**: 通过证书和策略管理学习 AWS IoT 安全
**功能**: 证书创建、策略附加、外部证书注册

### 4. 📡 MQTT 通信
**文件**: 
- `scripts/mqtt_client_explorer.py` (基于证书，推荐)
- `scripts/mqtt_websocket_explorer.py` (基于 WebSocket 的替代方案)

**目的**: 使用 MQTT 协议体验实时 IoT 通信
**功能**: 交互式命令行界面、主题订阅、消息发布

### 5. 🌟 AWS IoT Device Shadow service 探索器
**文件**: `scripts/device_shadow_explorer.py`
**目的**: 使用 AWS IoT Device Shadow 学习设备状态同步
**功能**: 交互式影子管理、状态更新、增量处理

### 6. ⚙️ IoT Rules Engine 探索器
**文件**: `scripts/iot_rules_explorer.py`
**目的**: 使用 IoT Rules Engine 学习消息路由和处理
**功能**: 规则创建、SQL 过滤、自动 AWS IAM 设置

### 7. 🧹 示例数据清理
**文件**: `scripts/cleanup_sample_data.py`
**目的**: 清理所有学习资源以避免费用
**功能**: 具有依赖关系处理的安全清理

## 🧹 资源清理

**⚠️ 重要**: 学习完成后务必运行清理以避免持续的 AWS 费用。

### 基本用法

```bash
# 标准清理 - 删除所有研讨会资源
python scripts/cleanup_sample_data.py

# 预览将被删除的内容（建议首先执行此步骤）
python scripts/cleanup_sample_data.py --dry-run

# 使用自定义前缀清理
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# 启用调试模式以获取详细的 API 日志
python scripts/cleanup_sample_data.py --debug
```

### 命令行参数

| 参数 | 描述 | 默认值 | 示例 |
|-----------|-------------|---------|---------|
| `--things-prefix` | Thing 名称的自定义前缀 | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | 预览清理而不删除 | `False` | `--dry-run` |
| `--debug` | 启用详细的 API 日志记录 | `False` | `--debug` |

### 资源识别工作原理

清理脚本使用**双重识别系统**来安全识别研讨会资源：

**1. 基于标签的识别（主要方法）**
- 由设置脚本创建的资源会自动标记：
  - `workshop-resource: true` - 标识研讨会创建的资源
  - `created-by: setup-script` - 跟踪创建资源的脚本
  - `workshop-name: iot-core-basics` - 按研讨会对资源分组
- **优势**: 最可靠的方法，无论命名如何都能工作

**2. 命名约定回退（次要方法）**
- 如果标签不存在，脚本通过命名模式识别资源：
  - Things: 匹配 `--things-prefix` 模式（默认：`Vehicle-VIN-`）
  - Thing Types: `SedanVehicle`、`SUVVehicle`、`TruckVehicle`
  - Thing Groups: `CustomerFleet`、`TestFleet`、`MaintenanceFleet`、`DealerFleet`
  - IoT 规则: 匹配 `*Rule`、`rule_*` 或 `*_workshop_*` 模式
- **优势**: 适用于在实施标记之前创建的资源

### Dry-Run 模式（建议首先执行此步骤）

**在执行清理操作之前始终预览：**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-run 模式将：**
- ✅ 识别将被删除的所有研讨会资源
- ✅ 按类型显示资源的详细列表
- ✅ 显示删除顺序（尊重依赖关系）
- ✅ 生成摘要报告
- ❌ **不删除任何资源**

**Dry-run 输出示例：**
```
🔍 DRY RUN MODE - 不会删除任何资源

已识别的资源:
  Things: 20个资源
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  证书: 20个资源
  Thing Groups: 4个资源
  Thing Types: 3个资源
  IoT 规则: 1个资源

总计: 将删除48个资源
```

### 自定义前缀使用

如果您在设置期间使用自定义前缀创建了资源，请在清理时使用相同的前缀：

```bash
# 使用自定义前缀设置
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# 使用匹配的前缀清理
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**重要**: 前缀必须在设置和清理之间完全匹配，基于命名的识别才能正常工作。

### 清理的内容

**删除的资源（按依赖顺序）：**
1. ✅ Thing Shadows（设备状态数据）
2. ✅ 证书（首先从 things 分离）
3. ✅ Things（IoT 设备）
4. ✅ IoT 规则（消息路由规则）
5. ✅ Thing Groups（设备集合）
6. ✅ Thing Types（设备模板）
7. ✅ 策略（安全策略）
8. ✅ 本地证书文件（来自 `certs/` 目录）

**受保护的资源：**
- ❌ 生产 IoT 资源（没有研讨会标签）
- ❌ 具有不同命名模式的资源
- ❌ 未与研讨会 things 关联的证书和策略
- ❌ 在研讨会脚本之外创建的资源

### 依赖关系感知删除

清理脚本自动处理 AWS IoT 资源依赖关系：

**删除顺序：**
```
Thing Shadows → 证书 → Things → IoT 规则 → Thing Groups → Thing Types → 策略
```

**为什么这个顺序很重要：**
- Thing Shadows 必须在证书之前删除
- 证书必须在删除 things 之前分离
- Things 必须在删除组之前从组中删除
- 策略必须在删除之前分离

**脚本会自动处理这些** - 您无需担心依赖冲突。

### 理解摘要报告

清理完成后，您将看到摘要报告：

```
📊 清理摘要

资源类型      | 已识别 | 已删除 | 失败
--------------|--------|--------|------
Things        |     20 |     20 |    0
证书          |     20 |     20 |    0
Thing Groups  |      4 |      4 |    0
Thing Types   |      3 |      3 |    0
IoT 规则      |      1 |      1 |    0
策略          |     20 |     20 |    0
--------------|--------|--------|------
总计          |     68 |     68 |    0

✅ 清理成功完成！
```

**报告字段：**
- **已识别**: 找到符合研讨会标准的资源
- **已删除**: 成功删除的资源
- **失败**: 无法删除的资源（带有错误详细信息）

### 清理故障排除

**问题："未找到资源"**
- **原因**: 资源可能没有研讨会标签或与前缀不匹配
- **解决方案**: 
  - 检查您在设置期间是否使用了自定义前缀
  - 使用正确的前缀使用 `--things-prefix`
  - 在 AWS 控制台中验证资源是否存在

**问题："权限被拒绝"错误**
- **原因**: AWS 凭证缺少必要的 IoT 权限
- **解决方案**: 确保您的 IAM 用户/角色具有 IoT 完全访问权限

**问题："依赖冲突"错误**
- **原因**: 资源具有未处理的依赖关系
- **解决方案**: 脚本应该自动处理这个问题。如果持续存在，使用 `--debug` 运行以查看详细信息

**问题：某些资源未被删除**
- **原因**: 资源可能正在使用或具有外部依赖关系
- **解决方案**: 
  - 检查摘要报告中的失败资源
  - 使用 AWS 控制台手动检查和删除剩余资源
  - 解决依赖关系后再次运行清理

### 最佳实践

1. **始终首先使用 dry-run**: 在执行之前预览将被删除的内容
2. **匹配前缀**: 对设置和清理使用相同的 `--things-prefix`
3. **查看摘要**: 检查报告以确保所有资源都已删除
4. **及时运行清理**: 不要让研讨会资源继续运行以避免费用
5. **保持凭证安全**: 永远不要将 AWS 凭证提交到版本控制

## 🛠️ 故障排除

### 常见问题

**AWS 凭证:**
```bash
# 设置凭证
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Python 依赖项:**
```bash
pip install -r requirements.txt
```

**OpenSSL 问题:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### 调试模式

所有脚本都支持详细 API 日志记录的调试模式:
```bash
python scripts/<script_name>.py --debug
```

## 📖 高级文档

### 详细文档
- **[详细脚本指南](docs/zh-CN/DETAILED_SCRIPTS.md)** - 深入的脚本文档
- **[完整示例](docs/zh-CN/EXAMPLES.md)** - 完整的工作流程和示例输出
- **[故障排除指南](docs/zh-CN/TROUBLESHOOTING.md)** - 常见问题和解决方案

### 学习资源
- **[AWS IoT Core 文档](https://docs.aws.amazon.com/iot/)**
- **[AWS IoT Device SDK](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)**
- **[MQTT 协议规范](https://mqtt.org/)**

## 🤝 贡献

这是一个教育项目。欢迎改善学习体验的贡献：

- **错误修复** 针对脚本问题
- **翻译改进** 为了更好的本地化
- **文档增强** 为了清晰度
- **额外学习场景** 适合基础级别的

### 学习资源

#### AWS IoT Core 文档
- **[AWS IoT Core 开发者指南](https://docs.aws.amazon.com/iot/latest/developerguide/)** - 完整的开发者指南
- **[AWS IoT Core API 参考](https://docs.aws.amazon.com/iot/latest/apireference/)** - API 文档

#### 此项目中使用的 AWS SDK
- **[Boto3 文档](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - 完整的 Python SDK 文档
- **[Boto3 IoT 客户端参考](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT 特定的 API 方法
- **[AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTT 客户端文档
- **[AWS IoT Device SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - 源代码和示例

#### 协议和标准
- **[MQTT 协议规范](https://mqtt.org/)** - 官方 MQTT 文档
- **[X.509 证书标准](https://tools.ietf.org/html/rfc5280)** - 证书格式规范

## 📄 许可证

此项目在 MIT-0 许可证下授权 - 详情请参阅 [LICENSE](LICENSE) 文件。

## 🏷️ 标签

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive` `chinese` `中文`