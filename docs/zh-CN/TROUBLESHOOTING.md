# 故障排除指南

这份指南会帮你解决在使用 AWS IoT Core 学习项目时可能遇到的各种问题。别担心，大多数问题都很容易解决！

## 目录

- [常见问题](#常见问题)
  - [AWS 凭证](#aws-凭证)
  - [虚拟环境问题](#虚拟环境问题)
  - [依赖项问题](#依赖项问题)
  - [权限问题](#权限问题)
  - [证书问题](#证书问题)
- [MQTT 连接问题](#mqtt-连接问题)
  - [基于证书的 MQTT 问题](#基于证书的-mqtt-问题)
  - [WebSocket MQTT 问题](#websocket-mqtt-问题)
- [AWS IoT Device Shadow service 问题](#device-shadow-问题)
  - [Shadow 连接问题](#shadow-连接问题)
  - [Shadow 状态文件问题](#shadow-状态文件问题)
- [Rules Engine 问题](#rules-engine-问题)
  - [规则创建问题](#规则创建问题)
  - [规则测试问题](#规则测试问题)
- [OpenSSL 问题](#openssl-问题)
  - [安装问题](#安装问题)
  - [证书生成问题](#证书生成问题)
- [网络和连接问题](#网络和连接问题)
  - [防火墙和代理问题](#防火墙和代理问题)
  - [DNS 解析问题](#dns-解析问题)
- [性能和时序问题](#性能和时序问题)
  - [API 速率限制](#api-速率限制)
  - [连接超时](#连接超时)
- [获取额外帮助](#获取额外帮助)
  - [使用调试模式](#使用调试模式)
  - [AWS IoT 控制台检查](#aws-iot-控制台检查)
  - [Amazon CloudWatch 日志](#cloudwatch-日志)
  - [通用解决步骤](#通用解决步骤)
  - [支持资源](#支持资源)

## 常见问题

### AWS 凭证

#### 检查凭证是否已设置
```bash
# 看看凭证是不是已经设置好了
aws sts get-caller-identity

# 检查一下当前区域
echo $AWS_DEFAULT_REGION

# 列出环境变量
env | grep AWS
```

#### 常见凭证问题

**问题: "Unable to locate credentials"**
```bash
# 解决方案1: 设置环境变量
export AWS_ACCESS_KEY_ID=<your-access-key>
export AWS_SECRET_ACCESS_KEY=<your-secret-key>
export AWS_DEFAULT_REGION=us-east-1

# 解决方案2: 用 AWS CLI 配置
aws configure

# 解决方案3: 看看现有配置
aws configure list
```

**问题: "You must specify a region"**
```bash
# 设置默认区域
export AWS_DEFAULT_REGION=us-east-1

# 或者在 AWS CLI 配置中指定
aws configure set region us-east-1
```

**问题: "The security token included in the request is invalid"**
- **原因**: 临时凭证过期了或会话令牌无效
- **解决方案**: 刷新一下凭证或删除过期的会话令牌
```bash
unset AWS_SESSION_TOKEN
# 然后设置新的凭证
```

### 虚拟环境问题

#### 检查虚拟环境
```bash
# 看看 venv 是不是已经激活了
which python
# 应该显示: /path/to/your/project/venv/bin/python

# 检查 Python 版本
python --version
# 应该是 3.7 或更高版本

# 列出已安装的包
pip list
```

#### 虚拟环境故障排除

**问题: 使用系统 Python 而不是 venv**
```bash
# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 验证一下是否激活了
which python
pip list
```

**问题: venv 不存在**
```bash
# 创建一个新的虚拟环境
python -m venv venv

# 激活并安装依赖项
source venv/bin/activate
pip install -r requirements.txt
```

**问题: Python 版本不兼容**
```bash
# 检查系统 Python 版本
python3 --version

# 用特定的 Python 版本创建 venv
python3.8 -m venv venv  # 如果你有 Python 3.8
```

### 依赖项问题

#### 安装依赖项
```bash
# 确保 venv 已经激活了
source venv/bin/activate

# 升级 pip
pip install --upgrade pip

# 安装项目依赖项
pip install -r requirements.txt

# 验证安装
pip list | grep boto3
pip list | grep awsiotsdk
```

#### 常见依赖项问题

**问题: "No module named 'boto3'"**
```bash
# 确保在正确的环境中
which python
which pip

# 安装 boto3
pip install boto3>=1.26.0
```

**问题: "No module named 'awsiotsdk'"**
```bash
# 安装 AWS IoT SDK
pip install awsiotsdk>=1.11.0
```

**问题: 版本冲突**
```bash
# 看看当前版本
pip show boto3
pip show awsiotsdk

# 升级到需要的版本
pip install --upgrade boto3>=1.26.0
pip install --upgrade awsiotsdk>=1.11.0
```

### 权限问题

#### 检查 AWS IAM 权限
你的 AWS 用户或角色需要以下权限：

**基本 IoT 权限:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:*",
        "iam:ListRoles",
        "iam:CreateRole",
        "iam:AttachRolePolicy",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}
```

#### 常见权限错误

**问题: "User is not authorized to perform: iot:CreateThing"**
- **原因**: 缺少 IoT 权限
- **解决方案**: 给你的 IAM 用户/角色添加 IoT 权限

**问题: "User is not authorized to perform: iam:CreateRole"**
- **原因**: Rules Engine 脚本需要 AWS IAM 权限
- **解决方案**: 添加 AWS IAM 权限或跳过 Rules Engine 脚本

### 证书问题

#### 证书文件问题

**问题: "Certificate file not found"**
```bash
# 检查证书目录
ls -la certificates/

# 检查特定设备的证书
ls -la certificates/Vehicle-VIN-001/

# 如果缺少证书，运行证书管理器
python scripts/certificate_manager.py
```

**问题: "Invalid certificate format"**
- **原因**: 证书文件损坏了或格式不对
- **解决方案**: 重新生成证书
```bash
# 删除损坏的证书
rm -rf certificates/Vehicle-VIN-001/

# 重新运行证书管理器
python scripts/certificate_manager.py
```

**问题: "Certificate is not active"**
```bash
# 用证书管理器激活证书
python scripts/certificate_manager.py
# 选择选项 5: 管理证书状态
```

## MQTT 连接问题

### 基于证书的 MQTT 问题

#### 连接故障排除

**问题: "Connection failed with error code 5"**
- **原因**: 认证失败了
- **检查**:
  1. 证书文件是否存在且有效
  2. 证书是否处于活动状态
  3. 策略是否已附加到证书

```bash
# 检查证书文件
ls -la certificates/Vehicle-VIN-001/

# 用调试模式运行
python scripts/mqtt_client_explorer.py --debug
```

**问题: "Connection timeout"**
- **原因**: 网络问题或端点不对
- **解决方案**:
```bash
# 检查 IoT 端点
python scripts/iot_registry_explorer.py
# 选择选项 8: 描述端点

# 测试网络连接
ping your-iot-endpoint.iot.us-east-1.amazonaws.com
```

**问题: "SSL handshake failed"**
- **原因**: 证书或 SSL 配置有问题
- **解决方案**:
  1. 验证证书文件完整性
  2. 检查系统时间是否正确
  3. 验证 CA 证书

### WebSocket MQTT 问题

#### WebSocket 连接故障排除

**问题: "WebSocket connection failed"**
- **原因**: 凭证或网络有问题
- **解决方案**:
```bash
# 检查 AWS 凭证
aws sts get-caller-identity

# 检查 IAM 权限
aws iam get-user
```

**问题: "Signature mismatch"**
- **原因**: 时钟偏差或凭证有问题
- **解决方案**:
  1. 同步系统时间
  2. 刷新 AWS 凭证
  3. 检查区域设置

## AWS IoT Device Shadow service 问题

### Shadow 连接问题

**问题: "Thing not found"**
- **原因**: Thing 不存在或名称不对
- **解决方案**:
```bash
# 列出可用的 Things
python scripts/iot_registry_explorer.py
# 选择选项 1: 列出 Things

# 如果没有 Things，创建示例数据
python scripts/setup_sample_data.py
```

**问题: "Access denied to shadow"**
- **原因**: 缺少 AWS IoT Device Shadow service 权限
- **解决方案**: 给你的 AWS IAM 策略添加 Shadow 权限
```json
{
  "Effect": "Allow",
  "Action": [
    "iot:GetThingShadow",
    "iot:UpdateThingShadow",
    "iot:DeleteThingShadow"
  ],
  "Resource": "arn:aws:iot:*:*:thing/*"
}
```

### Shadow 状态文件问题

**问题: "Invalid JSON in shadow update"**
- **原因**: JSON 格式有问题
- **解决方案**: 验证 JSON 语法
```bash
# 用调试模式查看完整的有效负载
python scripts/device_shadow_explorer.py --debug
```

**问题: "Version conflict"**
- **原因**: 并发 shadow 更新
- **解决方案**: 重试操作或使用最新版本

## Rules Engine 问题

### 规则创建问题

**问题: "Invalid SQL statement"**
- **原因**: SQL 语法错误
- **解决方案**: 验证 SQL 语法
```sql
-- 正确的语法示例
SELECT * FROM 'topic/+/data' WHERE temperature > 25

-- 常见错误: 缺少引号
SELECT * FROM topic/+/data WHERE temperature > 25  -- 错误
```

**问题: "AWS IAM role creation failed"**
- **原因**: 缺少 AWS IAM 权限
- **解决方案**: 添加 AWS IAM 权限或手动创建角色

### 规则测试问题

**问题: "Rule not triggering"**
- **原因**: 主题模式不匹配或 SQL 过滤器有问题
- **解决方案**:
  1. 验证主题模式
  2. 测试 SQL 语句
  3. 检查消息格式

## OpenSSL 问题

### 安装问题

**macOS:**
```bash
# 用 Homebrew 安装
brew install openssl

# 如果有路径问题
export PATH="/usr/local/opt/openssl/bin:$PATH"
```

**Ubuntu/Debian:**
```bash
# 安装 OpenSSL
sudo apt-get update
sudo apt-get install openssl

# 验证安装
openssl version
```

**Windows:**
- 从 [OpenSSL 网站](https://www.openssl.org/) 下载
- 或使用 Windows Subsystem for Linux (WSL)

### 证书生成问题

**问题: "OpenSSL command not found"**
- **解决方案**: 安装 OpenSSL 或将其添加到 PATH

**问题: "Certificate generation failed"**
```bash
# 检查 OpenSSL 版本
openssl version

# 手动测试证书生成
openssl req -x509 -newkey rsa:2048 -keyout test.key -out test.crt -days 365 -nodes
```

## 网络和连接问题

### 防火墙和代理问题

**问题: 连接被防火墙阻止**
- **端口**: 确保端口 443 (HTTPS) 和 8883 (MQTT) 是开放的
- **域**: 允许访问 `*.amazonaws.com`

**问题: 代理配置**
```bash
# 设置代理环境变量
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# 对于 AWS CLI
aws configure set proxy.http http://proxy.company.com:8080
aws configure set proxy.https http://proxy.company.com:8080
```

### DNS 解析问题

**问题: "Could not resolve hostname"**
```bash
# 测试 DNS 解析
nslookup your-endpoint.iot.us-east-1.amazonaws.com

# 使用不同的 DNS 服务器
nslookup your-endpoint.iot.us-east-1.amazonaws.com 8.8.8.8
```

## 性能和时序问题

### API 速率限制

**问题: "ThrottlingException"**
- **原因**: 超过 API 速率限制了
- **解决方案**: 在 API 调用之间添加延迟
```python
import time
time.sleep(1)  # 在调用之间等待 1 秒
```

### 连接超时

**问题: 连接超时**
- **原因**: 网络延迟或服务器负载
- **解决方案**: 增加超时值或重试逻辑

## 获取额外帮助

### 使用调试模式

所有脚本都支持调试模式，可以获得详细输出：
```bash
python scripts/<script_name>.py --debug
```

调试模式会提供：
- 详细的 API 请求/响应
- 完整的错误堆栈跟踪
- 连接详细信息
- 时序信息

### AWS IoT 控制台检查

用 AWS IoT 控制台验证：
1. **Things**: 检查设备是否已创建
2. **证书**: 验证证书状态和策略
3. **策略**: 检查策略文档和附加
4. **规则**: 验证规则配置和状态

### Amazon CloudWatch 日志

检查 Amazon CloudWatch 日志可以获得更多信息：
```bash
# 用 AWS CLI 检查日志
aws logs describe-log-groups --log-group-name-prefix "/aws/iot"
aws logs get-log-events --log-group-name "/aws/iot/rules" --log-stream-name "your-rule-name"
```

### 通用解决步骤

1. **检查基础知识**:
   - AWS 凭证已经设置好了
   - 区域是正确的
   - 虚拟环境已经激活了
   - 依赖项已经安装好了

2. **用调试模式**:
   ```bash
   python scripts/<script_name>.py --debug
   ```

3. **检查 AWS 控制台**:
   - 验证资源存在
   - 检查权限和策略
   - 查看 Amazon CloudWatch 日志

4. **网络故障排除**:
   - 测试连接性
   - 检查防火墙/代理设置
   - 验证 DNS 解析

5. **重新创建资源**:
   ```bash
   # 清理并重新开始
   python scripts/cleanup_sample_data.py
   python scripts/setup_sample_data.py
   ```

### 支持资源

- **AWS IoT 文档**: https://docs.aws.amazon.com/iot/
- **AWS IoT 开发者指南**: https://docs.aws.amazon.com/iot/latest/developerguide/
- **AWS IoT API 参考**: https://docs.aws.amazon.com/iot/latest/apireference/
- **AWS 支持**: https://aws.amazon.com/support/
- **AWS 论坛**: https://forums.aws.amazon.com/forum.jspa?forumID=210

### 报告问题

如果你遇到了这份指南没有涵盖的问题，请提供：
1. 完整的错误消息
2. 调试模式输出
3. 你的环境详细信息（OS、Python 版本）
4. 重现问题的步骤

---

**记住**: 大多数问题都跟 AWS 凭证、权限或网络配置有关。先从基础知识开始检查，然后再深入到更具体的问题。