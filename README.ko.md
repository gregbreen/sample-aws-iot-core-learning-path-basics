# AWS IoT Core - 학습 경로 - 기초

> 🌍 **사용 가능한 언어** | **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言**
> 
> - [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | **한국어** (현재)
> - **문서**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/)

실습을 통해 Amazon Web Services (AWS) AWS IoT Core 기본 개념을 학습할 수 있는 포괄적인 Python 툴킷입니다. 대화형 스크립트는 디바이스 관리, 보안, API 작업 및 MQTT 통신을 자세한 설명과 함께 시연합니다.

## 🚀 빠른 시작 - 완전한 학습 경로

```bash
# 1. 클론 및 설정
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. 환경 설정
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. AWS 자격 증명 구성
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=<your-region (예: us-east-1)>

# 4. 선택사항: 언어 설정
export AWS_IOT_LANG=ko  # 'en' 영어, 'es' 스페인어, 'ja' 일본어, 'zh-CN' 중국어, 'pt-BR' 포르투갈어

# 5. 완전한 학습 순서
python scripts/setup_sample_data.py          # 샘플 IoT 리소스 생성
python scripts/iot_registry_explorer.py      # AWS IoT API 탐색
python scripts/certificate_manager.py        # IoT 보안 학습
python scripts/mqtt_client_explorer.py       # 실시간 MQTT 통신
python scripts/device_shadow_explorer.py     # 디바이스 상태 동기화
python scripts/iot_rules_explorer.py         # 메시지 라우팅 및 처리
python scripts/cleanup_sample_data.py        # 리소스 정리 (중요!)
```

**⚠️ 비용 경고**: 실제 AWS 리소스를 생성합니다 (총 ~$0.17). 완료 후 정리를 실행하세요!

## 대상 사용자

**주요 대상**: AWS IoT Core를 처음 접하는 클라우드 개발자, 솔루션 아키텍트, DevOps 엔지니어

**전제 조건**: 기본 AWS 지식, Python 기초, 명령줄 사용법

**학습 수준**: 실습 접근 방식의 어소시에이트 레벨

## 🔧 AWS SDK로 구축

이 프로젝트는 공식 AWS SDK를 활용하여 진정한 AWS IoT Core 경험을 제공합니다:

### **Boto3 - Python용 AWS SDK**
- **목적**: 모든 AWS IoT 레지스트리 작업, 인증서 관리 및 규칙 엔진 상호작용을 지원
- **버전**: `>=1.26.0`
- **문서**: [Boto3 문서](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core API**: [Boto3 IoT 클라이언트](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **Python용 AWS IoT 디바이스 SDK**
- **목적**: X.509 인증서를 사용하여 AWS IoT Core와 진정한 MQTT 통신 가능
- **버전**: `>=1.11.0`
- **문서**: [Python용 AWS IoT 디바이스 SDK v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**이러한 SDK가 중요한 이유:**
- **프로덕션 준비**: 실제 IoT 애플리케이션에서 사용되는 동일한 SDK
- **보안**: AWS IoT 보안 모범 사례에 대한 내장 지원
- **신뢰성**: 포괄적인 오류 처리를 갖춘 AWS 공식 유지 관리 라이브러리
- **학습 가치**: 진정한 AWS IoT 개발 패턴 경험

## 목차

- 🚀 [빠른 시작](#-빠른-시작---완전한-학습-경로)
- ⚙️ [설치 및 설정](#️-설치-및-설정)
- 📚 [학습 스크립트](#-학습-스크립트)
- 🧹 [리소스 정리](#-리소스-정리)
- 🛠️ [문제 해결](#-문제-해결)
- 📖 [고급 문서](#-고급-문서)

## ⚙️ 설치 및 설정

### 전제 조건
- Python 3.10+
- IoT 권한이 있는 AWS 계정
- 터미널/명령줄 액세스
- OpenSSL (인증서 기능용)

**⚠️ 중요한 안전 참고사항**: 전용 개발/학습 AWS 계정을 사용하세요. 프로덕션 IoT 리소스가 포함된 계정에서는 이러한 스크립트를 실행하지 마세요. 정리 스크립트에 여러 안전 메커니즘이 있지만, 학습 활동에는 격리된 환경을 사용하는 것이 모범 사례입니다.

### 비용 정보

**이 프로젝트는 요금이 발생하는 실제 AWS 리소스를 생성합니다 (총 ~$0.17).**

| 서비스 | 사용량 | 예상 비용 (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100개 메시지, 20개 디바이스 | $0.10 |
| **AWS IoT Device Shadow service** | ~30개 섀도우 작업 | $0.04 |
| **IoT Rules Engine** | ~50개 규칙 실행 | $0.01 |
| **인증서 저장소** | 1일간 20개 인증서 | $0.01 |
| **Amazon CloudWatch Logs** | 기본 로깅 | $0.01 |
| **총 예상** | **완전한 학습 세션** | **~$0.17** |

**⚠️ 중요**: 지속적인 요금을 피하기 위해 완료 후 항상 정리 스크립트를 실행하세요.

### 자세한 설치

**1. 저장소 클론:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. OpenSSL 설치:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** [OpenSSL 웹사이트](https://www.openssl.org/)에서 다운로드

**3. 가상 환경 (권장):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. 언어 구성 (선택사항):**
```bash
# 모든 스크립트에 대한 언어 설정
export AWS_IOT_LANG=ko     # 한국어
export AWS_IOT_LANG=en     # 영어 (기본값)
export AWS_IOT_LANG=es     # 스페인어
export AWS_IOT_LANG=ja     # 일본어
export AWS_IOT_LANG=zh-CN  # 중국어
export AWS_IOT_LANG=pt-BR  # 포르투갈어

# 대안: 설정되지 않은 경우 스크립트가 언어를 묻습니다
```

**지원되는 언어:**
- **한국어** (`ko`, `korean`, `한국어`, `kr`) - 완전한 번역 제공
- **영어** (`en`, `english`) - 기본값
- **스페인어** (`es`, `spanish`, `español`) - 완전한 번역 제공
- **일본어** (`ja`, `japanese`, `日本語`, `jp`) - 완전한 번역 제공
- **중국어** (`zh-CN`, `chinese`, `中文`, `zh`) - 완전한 번역 제공
- **포르투갈어** (`pt-BR`, `portuguese`, `português`, `pt`) - 완전한 번역 제공

## 🌍 다국어 지원

모든 학습 스크립트는 영어, 스페인어, 일본어, 중국어, 포르투갈어, 한국어 인터페이스를 지원합니다. 언어는 다음에 영향을 줍니다:

**✅ 번역되는 것:**
- 환영 메시지 및 교육 콘텐츠
- 메뉴 옵션 및 사용자 프롬프트
- 학습 순간 및 설명
- 오류 메시지 및 확인
- 진행 표시기 및 상태 메시지

**❌ 원래 언어로 유지되는 것:**
- AWS API 응답 (JSON 데이터)
- 기술적 매개변수 이름 및 값
- HTTP 메서드 및 엔드포인트
- 디버그 정보 및 로그
- AWS 리소스 이름 및 식별자

**사용 옵션:**

**옵션 1: 환경 변수 (권장)**
```bash
# 모든 스크립트에 대한 언어 설정
export AWS_IOT_LANG=ko     # 한국어
export AWS_IOT_LANG=en     # 영어
export AWS_IOT_LANG=es     # 스페인어
export AWS_IOT_LANG=ja     # 일본어
export AWS_IOT_LANG=zh-CN  # 중국어
export AWS_IOT_LANG=pt-BR  # 포르투갈어

# 스크립트 실행 - 언어가 자동으로 적용됩니다
python scripts/iot_registry_explorer.py
```

**옵션 2: 대화형 선택**
```bash
# 환경 변수 없이 실행 - 스크립트가 언어를 묻습니다
python scripts/setup_sample_data.py

# 출력 예시:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma / 언어 선택
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# 6. 한국어 (Korean)
# Select language (1-6): 6
```

**지원되는 스크립트:**
- ✅ `setup_sample_data.py` - 샘플 데이터 생성
- ✅ `iot_registry_explorer.py` - API 탐색
- ✅ `certificate_manager.py` - 인증서 관리
- ✅ `mqtt_client_explorer.py` - MQTT 통신
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - AWS IoT Device Shadow service 작업
- ✅ `iot_rules_explorer.py` - Rules Engine 탐색
- ✅ `cleanup_sample_data.py` - 리소스 정리

## 📚 학습 스크립트

**권장 학습 경로:**

### 1. 📊 샘플 데이터 설정
**파일**: `scripts/setup_sample_data.py`
**목적**: 실습 학습을 위한 현실적인 IoT 리소스 생성
**생성**: 20개 Things, 3개 Thing Types, 4개 Thing Groups

### 2. 🔍 IoT 레지스트리 API 탐색기
**파일**: `scripts/iot_registry_explorer.py`
**목적**: AWS IoT 레지스트리 API 학습을 위한 대화형 도구
**기능**: 자세한 설명과 실제 API 호출이 포함된 8개 핵심 API

### 3. 🔐 인증서 및 정책 관리자
**파일**: `scripts/certificate_manager.py`
**목적**: 인증서 및 정책 관리를 통한 AWS IoT 보안 학습
**기능**: 인증서 생성, 정책 연결, 외부 인증서 등록

### 4. 📡 MQTT 통신
**파일**: 
- `scripts/mqtt_client_explorer.py` (인증서 기반, 권장)
- `scripts/mqtt_websocket_explorer.py` (WebSocket 기반 대안)

**목적**: MQTT 프로토콜을 사용한 실시간 IoT 통신 경험
**기능**: 대화형 명령줄 인터페이스, 주제 구독, 메시지 게시

### 5. 🌟 AWS IoT Device Shadow service 탐색기
**파일**: `scripts/device_shadow_explorer.py`
**목적**: AWS IoT Device Shadow를 사용한 디바이스 상태 동기화 학습
**기능**: 대화형 섀도우 관리, 상태 업데이트, 델타 처리

### 6. ⚙️ IoT Rules Engine 탐색기
**파일**: `scripts/iot_rules_explorer.py`
**목적**: IoT Rules Engine을 사용한 메시지 라우팅 및 처리 학습
**기능**: 규칙 생성, SQL 필터링, 자동 AWS IAM 설정

### 7. 🧹 샘플 데이터 정리
**파일**: `scripts/cleanup_sample_data.py`
**목적**: 요금을 피하기 위해 모든 학습 리소스 정리
**기능**: 종속성 처리를 통한 안전한 정리

## 🧹 리소스 정리

**⚠️ 중요**: 지속적인 AWS 요금을 피하기 위해 학습 완료 후 항상 정리를 실행하세요.

### 기본 사용법

```bash
# 표준 정리 - 모든 워크샵 리소스 제거
python scripts/cleanup_sample_data.py

# 삭제될 항목 미리보기 (첫 번째 단계로 권장)
python scripts/cleanup_sample_data.py --dry-run

# 사용자 지정 접두사로 정리
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# 상세한 API 로깅을 위한 디버그 모드 활성화
python scripts/cleanup_sample_data.py --debug
```

### 명령줄 매개변수

| 매개변수 | 설명 | 기본값 | 예시 |
|-----------|-------------|---------|---------|
| `--things-prefix` | Thing 이름의 사용자 지정 접두사 | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | 삭제하지 않고 정리 미리보기 | `False` | `--dry-run` |
| `--debug` | 상세한 API 로깅 활성화 | `False` | `--debug` |

### 리소스 식별 작동 방식

정리 스크립트는 **이중 식별 시스템**을 사용하여 워크샵 리소스를 안전하게 식별합니다:

**1. 태그 기반 식별 (주요 방법)**
- 설정 스크립트로 생성된 리소스는 자동으로 태그가 지정됩니다:
  - `workshop-resource: true` - 워크샵에서 생성된 리소스 식별
  - `created-by: setup-script` - 리소스를 생성한 스크립트 추적
  - `workshop-name: iot-core-basics` - 워크샵별로 리소스 그룹화
- **장점**: 가장 신뢰할 수 있는 방법, 이름 지정과 관계없이 작동

**2. 명명 규칙 대체 (보조 방법)**
- 태그가 없는 경우 스크립트는 명명 패턴으로 리소스를 식별:
  - Things: `--things-prefix` 패턴과 일치 (기본값: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - IoT 규칙: `*Rule`, `rule_*`, 또는 `*_workshop_*` 패턴과 일치
- **장점**: 태그 지정이 구현되기 전에 생성된 리소스에서 작동

### Dry-Run 모드 (첫 번째 단계로 권장)

**정리 작업을 실행하기 전에 항상 미리보기하세요:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-run 모드는:**
- ✅ 삭제될 모든 워크샵 리소스 식별
- ✅ 유형별 리소스의 상세 목록 표시
- ✅ 삭제 순서 표시 (종속성 존중)
- ✅ 요약 보고서 생성
- ❌ **리소스를 삭제하지 않음**

**Dry-run 출력 예시:**
```
🔍 DRY RUN MODE - 리소스가 삭제되지 않습니다

식별된 리소스:
  Things: 20개 리소스
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  인증서: 20개 리소스
  Thing Groups: 4개 리소스
  Thing Types: 3개 리소스
  IoT 규칙: 1개 리소스

총계: 48개 리소스가 삭제됩니다
```

### 사용자 지정 접두사 사용

설정 중에 사용자 지정 접두사로 리소스를 생성한 경우 정리에 동일한 접두사를 사용하세요:

```bash
# 사용자 지정 접두사로 설정
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# 일치하는 접두사로 정리
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**중요**: 이름 기반 식별이 올바르게 작동하려면 설정과 정리 간에 접두사가 정확히 일치해야 합니다.

### 정리되는 항목

**삭제되는 리소스 (종속성 순서):**
1. ✅ Thing Shadows (디바이스 상태 데이터)
2. ✅ 인증서 (먼저 Things에서 분리)
3. ✅ Things (IoT 디바이스)
4. ✅ IoT 규칙 (메시지 라우팅 규칙)
5. ✅ Thing Groups (디바이스 컬렉션)
6. ✅ Thing Types (디바이스 템플릿)
7. ✅ 정책 (보안 정책)
8. ✅ 로컬 인증서 파일 (`certs/` 디렉토리에서)

**보호되는 리소스:**
- ❌ 프로덕션 IoT 리소스 (워크샵 태그 없음)
- ❌ 다른 명명 패턴의 리소스
- ❌ 워크샵 Things와 연결되지 않은 인증서 및 정책
- ❌ 워크샵 스크립트 외부에서 생성된 리소스

### 종속성 인식 삭제

정리 스크립트는 AWS IoT 리소스 종속성을 자동으로 처리합니다:

**삭제 순서:**
```
Thing Shadows → 인증서 → Things → IoT 규칙 → Thing Groups → Thing Types → 정책
```

**이 순서가 중요한 이유:**
- Thing Shadows는 인증서 전에 삭제해야 합니다
- 인증서는 Things를 삭제하기 전에 분리해야 합니다
- Things는 그룹을 삭제하기 전에 그룹에서 제거해야 합니다
- 정책은 삭제 전에 분리해야 합니다

**스크립트가 이를 자동으로 처리합니다** - 종속성 충돌에 대해 걱정할 필요가 없습니다.

### 요약 보고서 이해

정리가 완료되면 요약 보고서가 표시됩니다:

```
📊 정리 요약

리소스 유형    | 식별됨 | 삭제됨 | 실패
---------------|--------|--------|------
Things         |     20 |     20 |    0
인증서         |     20 |     20 |    0
Thing Groups   |      4 |      4 |    0
Thing Types    |      3 |      3 |    0
IoT 규칙       |      1 |      1 |    0
정책           |     20 |     20 |    0
---------------|--------|--------|------
총계           |     68 |     68 |    0

✅ 정리가 성공적으로 완료되었습니다!
```

**보고서 필드:**
- **식별됨**: 워크샵 기준과 일치하는 리소스 발견
- **삭제됨**: 성공적으로 제거된 리소스
- **실패**: 삭제할 수 없었던 리소스 (오류 세부 정보 포함)

### 정리 문제 해결

**문제: "리소스를 찾을 수 없음"**
- **원인**: 리소스에 워크샵 태그가 없거나 접두사와 일치하지 않을 수 있습니다
- **해결책**: 
  - 설정 중에 사용자 지정 접두사를 사용했는지 확인
  - 올바른 접두사로 `--things-prefix` 사용
  - AWS 콘솔에서 리소스가 존재하는지 확인

**문제: "권한 거부" 오류**
- **원인**: AWS 자격 증명에 필요한 IoT 권한이 없습니다
- **해결책**: IAM 사용자/역할에 IoT 전체 액세스 권한이 있는지 확인

**문제: "종속성 충돌" 오류**
- **원인**: 리소스에 처리되지 않은 종속성이 있습니다
- **해결책**: 스크립트가 이를 자동으로 처리해야 합니다. 문제가 지속되면 `--debug`로 실행하여 세부 정보 확인

**문제: 일부 리소스가 삭제되지 않음**
- **원인**: 리소스가 사용 중이거나 외부 종속성이 있을 수 있습니다
- **해결책**: 
  - 요약 보고서에서 실패한 리소스 확인
  - AWS 콘솔을 사용하여 남은 리소스를 수동으로 검사 및 삭제
  - 종속성을 해결한 후 정리를 다시 실행

### 모범 사례

1. **항상 먼저 dry-run 사용**: 실행하기 전에 삭제될 항목 미리보기
2. **접두사 일치**: 설정 및 정리에 동일한 `--things-prefix` 사용
3. **요약 검토**: 보고서를 확인하여 모든 리소스가 삭제되었는지 확인
4. **신속하게 정리 실행**: 요금을 피하기 위해 워크샵 리소스를 실행 상태로 두지 마세요
5. **자격 증명 보안 유지**: AWS 자격 증명을 버전 관리에 커밋하지 마세요

## 🛠️ 문제 해결

### 일반적인 문제

**AWS 자격 증명:**
```bash
# 자격 증명 설정
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Python 종속성:**
```bash
pip install -r requirements.txt
```

**OpenSSL 문제:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### 디버그 모드

모든 스크립트는 자세한 API 로깅을 위한 디버그 모드를 지원합니다:
```bash
python scripts/<script_name>.py --debug
```

## 📖 고급 문서

### 자세한 문서
- **[자세한 스크립트 가이드](docs/ko/DETAILED_SCRIPTS.md)** - 심층 스크립트 문서
- **[완전한 예제](docs/ko/EXAMPLES.md)** - 전체 워크플로우 및 샘플 출력
- **[문제 해결 가이드](docs/ko/TROUBLESHOOTING.md)** - 일반적인 문제 및 해결책

### 학습 리소스

#### AWS IoT Core 문서
- **[AWS IoT Core 개발자 가이드](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[AWS IoT Core API 참조](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### 이 프로젝트에서 사용된 AWS SDK
- **[Boto3 문서](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - 완전한 Python SDK 문서
- **[Boto3 IoT 클라이언트 참조](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT 특정 API 메서드
- **[Python용 AWS IoT 디바이스 SDK v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTT 클라이언트 문서
- **[AWS IoT 디바이스 SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - 소스 코드 및 예제

#### 프로토콜 및 표준
- **[MQTT 프로토콜 사양](https://mqtt.org/)** - 공식 MQTT 문서
- **[X.509 인증서 표준](https://tools.ietf.org/html/rfc5280)** - 인증서 형식 사양

## 🤝 기여

이것은 교육 프로젝트입니다. 학습 경험을 개선하는 기여를 환영합니다:

- 스크립트 문제에 대한 **버그 수정**
- 더 나은 현지화를 위한 **번역 개선**
- 명확성을 위한 **문서 개선**
- 기본 수준에 맞는 **추가 학습 시나리오**

## 📄 라이선스

이 프로젝트는 MIT-0 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🏷️ 태그

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`