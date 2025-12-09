# AWS IoT Core - 学習パス - 基礎

> 🌍 **利用可能な言語** | **Available Languages** | **Idiomas Disponibles** | **可用语言**
> 
> - [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | **日本語** (現在) | [Português](README.pt-BR.md)
> - **ドキュメント**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | **日本語** (docs/ja/) | [Português](docs/pt-BR/)

Amazon Web Services (AWS) AWS IoT Core の基本概念をハンズオン探索で学習するための包括的なPythonツールキット。インタラクティブなスクリプトで、デバイス管理、セキュリティ、API操作、MQTT通信を詳細な説明付きで実演します。

## 🚀 クイックスタート - 完全学習パス

```bash
# 1. クローンとセットアップ
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. 環境セットアップ
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. AWS認証情報を設定
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=<your-region (例: us-east-1)>

# 4. オプション: 言語設定
export AWS_IOT_LANG=ja  # 'en' 英語, 'es' スペイン語, 'zh-CN' 中国語

# 5. 完全学習シーケンス
python scripts/setup_sample_data.py          # サンプルIoTリソースを作成
python scripts/iot_registry_explorer.py      # AWS IoT APIを探索
python scripts/certificate_manager.py        # IoTセキュリティを学習
python scripts/mqtt_client_explorer.py       # リアルタイムMQTT通信
python scripts/device_shadow_explorer.py     # デバイス状態同期
python scripts/iot_rules_explorer.py         # メッセージルーティングと処理
python scripts/cleanup_sample_data.py        # リソースクリーンアップ（重要！）
```

**⚠️ コスト警告**: これは実際のAWSリソースを作成します（合計約$0.17）。完了後はクリーンアップを実行してください！

## 対象読者

**主要対象**: AWS IoT Coreが初めてのクラウド開発者、ソリューションアーキテクト、DevOpsエンジニア

**前提条件**: 基本的なAWS知識、Python基礎、コマンドライン使用経験

**学習レベル**: アソシエイトレベルのハンズオンアプローチ

## 🔧 AWS SDKで構築

このプロジェクトは、本格的なAWS IoT Core体験を提供するために公式AWS SDKを活用しています：

### **Boto3 - AWS SDK for Python**
- **目的**: すべてのAWS IoT Registry操作、証明書管理、Rules Engineインタラクションを強化
- **バージョン**: `>=1.26.0`
- **ドキュメント**: [Boto3ドキュメント](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core API**: [Boto3 IoTクライアント](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK for Python**
- **目的**: X.509証明書を使用してAWS IoT Coreとの本格的なMQTT通信を可能にする
- **バージョン**: `>=1.11.0`
- **ドキュメント**: [AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**これらのSDKが重要な理由:**
- **本番対応**: 実際のIoTアプリケーションで使用されているのと同じSDK
- **セキュリティ**: AWS IoTセキュリティベストプラクティスの組み込みサポート
- **信頼性**: 包括的なエラーハンドリングを備えたAWS公式メンテナンスライブラリ
- **学習価値**: 本格的なAWS IoT開発パターンを体験

## 目次

- 🚀 [クイックスタート](#-クイックスタート---完全学習パス)
- ⚙️ [インストール・セットアップ](#️-インストールセットアップ)
- 📚 [学習スクリプト](#-学習スクリプト)
- 🧹 [リソースクリーンアップ](#-リソースクリーンアップ)
- 🛠️ [トラブルシューティング](#-トラブルシューティング)
- 📖 [高度なドキュメント](#-高度なドキュメント)

## ⚙️ インストール・セットアップ

### 前提条件
- Python 3.10+
- IoT権限を持つAWSアカウント
- ターミナル/コマンドラインアクセス
- OpenSSL（証明書機能用）

**⚠️ 重要な安全注意事項**: 専用の開発/学習用AWSアカウントを使用してください。本番IoTリソースを含むアカウントでこれらのスクリプトを実行しないでください。クリーンアップスクリプトには複数の安全メカニズムがありますが、学習活動には分離された環境を使用することがベストプラクティスです。

### コスト情報

**このプロジェクトは実際のAWSリソースを作成し、料金が発生します（合計約$0.17）。**

| サービス | 使用量 | 推定コスト (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | 約100メッセージ、20デバイス | $0.10 |
| **AWS IoT Device Shadow service** | 約30シャドウ操作 | $0.04 |
| **IoT Rules Engine** | 約50ルール実行 | $0.01 |
| **証明書ストレージ** | 20証明書を1日間 | $0.01 |
| **Amazon CloudWatch Logs** | 基本ログ記録 | $0.01 |
| **合計推定** | **完全学習セッション** | **約$0.17** |

**⚠️ 重要**: 継続的な料金を避けるため、完了後は必ずクリーンアップスクリプトを実行してください。



### 詳細インストール

**1. リポジトリをクローン:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. OpenSSLをインストール:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** [OpenSSL website](https://www.openssl.org/)からダウンロード

**3. 仮想環境（推奨）:**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. 言語設定（オプション）:**
```bash
# すべてのスクリプトの言語設定
export AWS_IOT_LANG=ja     # 日本語
export AWS_IOT_LANG=en     # 英語（デフォルト）
export AWS_IOT_LANG=es     # スペイン語
export AWS_IOT_LANG=zh-CN  # 中国語

# 代替: 設定されていない場合、スクリプトが言語を尋ねます
```

**サポート言語:**
- **英語** (`en`, `english`) - デフォルト
- **スペイン語** (`es`, `spanish`, `español`) - 完全翻訳利用可能
- **日本語** (`ja`, `japanese`, `日本語`, `jp`) - 完全翻訳利用可能
- **中国語** (`zh-CN`, `chinese`, `中文`, `zh`) - 完全翻訳利用可能

## 🌍 多言語サポート

すべての学習スクリプトは英語、スペイン語、日本語、中国語のインターフェースをサポートしています。言語は以下に影響します:

**✅ 翻訳される内容:**
- ウェルカムメッセージと教育コンテンツ
- メニューオプションとユーザープロンプト
- 学習ポイントと説明
- エラーメッセージと確認
- 進行状況インジケーターとステータスメッセージ

**❌ 元の言語のまま:**
- AWS APIレスポンス（JSONデータ）
- 技術パラメータ名と値
- HTTPメソッドとエンドポイント
- デバッグ情報とログ
- AWSリソース名と識別子

**使用オプション:**

**オプション1: 環境変数（推奨）**
```bash
# すべてのスクリプトの言語設定
export AWS_IOT_LANG=ja     # 日本語
export AWS_IOT_LANG=en     # 英語
export AWS_IOT_LANG=es     # スペイン語
export AWS_IOT_LANG=zh-CN  # 中国語

# 任意のスクリプトを実行 - 言語が自動適用されます
python scripts/iot_registry_explorer.py
```

**オプション2: インタラクティブ選択**
```bash
# 環境変数なしで実行 - スクリプトが言語を尋ねます
python scripts/setup_sample_data.py

# 出力例:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# Select language (1-4): 3
```

**サポートスクリプト:**
- ✅ `setup_sample_data.py` - サンプルデータ作成
- ✅ `iot_registry_explorer.py` - API探索
- ✅ `certificate_manager.py` - 証明書管理
- ✅ `mqtt_client_explorer.py` - MQTT通信
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - Device Shadow操作
- ✅ `iot_rules_explorer.py` - Rules Engine探索
- ✅ `cleanup_sample_data.py` - リソースクリーンアップ

## 📚 学習スクリプト

**推奨学習パス:**

### 1. 📊 サンプルデータセットアップ
**ファイル**: `scripts/setup_sample_data.py`
**目的**: ハンズオン学習のための現実的なIoTリソースを作成
**作成内容**: 20個のThings、3個のThing Types、4個のThing Groups

### 2. 🔍 IoT Registry API エクスプローラー
**ファイル**: `scripts/iot_registry_explorer.py`
**目的**: AWS IoT Registry APIを学習するためのインタラクティブツール
**機能**: 詳細な説明と実際のAPI呼び出しを含む8つのコアAPI

### 3. 🔐 証明書・ポリシーマネージャー
**ファイル**: `scripts/certificate_manager.py`
**目的**: 証明書とポリシー管理を通じてAWS IoTセキュリティを学習
**機能**: 証明書作成、ポリシーアタッチ、外部証明書登録

### 4. 📡 MQTT通信
**ファイル**: 
- `scripts/mqtt_client_explorer.py` (証明書ベース、推奨)
- `scripts/mqtt_websocket_explorer.py` (WebSocketベース代替)

**目的**: MQTTプロトコルを使用したリアルタイムIoT通信を体験
**機能**: インタラクティブコマンドラインインターフェース、トピック購読、メッセージ公開

### 5. 🌟 AWS IoT Device Shadow service エクスプローラー
**ファイル**: `scripts/device_shadow_explorer.py`
**目的**: AWS IoT Device Shadowを使用したデバイス状態同期を学習
**機能**: インタラクティブシャドウ管理、状態更新、差分処理

### 6. ⚙️ IoT Rules Engine エクスプローラー
**ファイル**: `scripts/iot_rules_explorer.py`
**目的**: IoT Rules Engineを使用したメッセージルーティングと処理を学習
**機能**: ルール作成、SQLフィルタリング、自動IAMセットアップ

### 7. 🧹 サンプルデータクリーンアップ
**ファイル**: `scripts/cleanup_sample_data.py`
**目的**: 料金を避けるためにすべての学習リソースをクリーンアップ
**機能**: 依存関係処理による安全なクリーンアップ

## 🧹 リソースクリーンアップ

**⚠️ 重要**: 継続的なAWS料金を避けるため、学習完了後は必ずクリーンアップを実行してください。

### 基本的な使用方法

```bash
# 標準クリーンアップ - すべてのワークショップリソースを削除
python scripts/cleanup_sample_data.py

# 削除されるものをプレビュー（最初のステップとして推奨）
python scripts/cleanup_sample_data.py --dry-run

# カスタムプレフィックスでクリーンアップ
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# 詳細なAPIログ記録のためのデバッグモードを有効化
python scripts/cleanup_sample_data.py --debug
```

### コマンドラインパラメータ

| パラメータ | 説明 | デフォルト | 例 |
|-----------|-------------|---------|---------|
| `--things-prefix` | Thing名のカスタムプレフィックス | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | 削除せずにクリーンアップをプレビュー | `False` | `--dry-run` |
| `--debug` | 詳細なAPIログ記録を有効化 | `False` | `--debug` |

### リソース識別の仕組み

クリーンアップスクリプトは**二重識別システム**を使用してワークショップリソースを安全に識別します：

**1. タグベースの識別（主要方法）**
- セットアップスクリプトで作成されたリソースは自動的にタグ付けされます：
  - `workshop-resource: true` - ワークショップで作成されたリソースを識別
  - `created-by: setup-script` - リソースを作成したスクリプトを追跡
  - `workshop-name: iot-core-basics` - ワークショップ別にリソースをグループ化
- **利点**: 最も信頼性の高い方法、命名に関係なく機能

**2. 命名規則フォールバック（二次方法）**
- タグが存在しない場合、スクリプトは命名パターンでリソースを識別：
  - Things: `--things-prefix`パターンに一致（デフォルト: `Vehicle-VIN-`）
  - Thing Types: `SedanVehicle`、`SUVVehicle`、`TruckVehicle`
  - Thing Groups: `CustomerFleet`、`TestFleet`、`MaintenanceFleet`、`DealerFleet`
  - IoTルール: `*Rule`、`rule_*`、または`*_workshop_*`パターンに一致
- **利点**: タグ付けが実装される前に作成されたリソースで機能

### Dry-Runモード（最初のステップとして推奨）

**クリーンアップ操作を実行する前に必ずプレビューしてください：**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-runモードは：**
- ✅ 削除されるすべてのワークショップリソースを識別
- ✅ タイプ別のリソースの詳細リストを表示
- ✅ 削除順序を表示（依存関係を尊重）
- ✅ サマリーレポートを生成
- ❌ **リソースを削除しない**

**Dry-run出力例：**
```
🔍 DRY RUN MODE - リソースは削除されません

識別されたリソース:
  Things: 20リソース
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  証明書: 20リソース
  Thing Groups: 4リソース
  Thing Types: 3リソース
  IoTルール: 1リソース

合計: 48リソースが削除されます
```

### カスタムプレフィックスの使用

セットアップ中にカスタムプレフィックスでリソースを作成した場合、クリーンアップに同じプレフィックスを使用してください：

```bash
# カスタムプレフィックスでセットアップ
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# 一致するプレフィックスでクリーンアップ
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**重要**: 命名ベースの識別が正しく機能するには、セットアップとクリーンアップの間でプレフィックスが正確に一致する必要があります。

### クリーンアップされる内容

**削除されるリソース（依存関係順）：**
1. ✅ Thing Shadows（デバイス状態データ）
2. ✅ 証明書（最初にThingsから切り離し）
3. ✅ Things（IoTデバイス）
4. ✅ IoTルール（メッセージルーティングルール）
5. ✅ Thing Groups（デバイスコレクション）
6. ✅ Thing Types（デバイステンプレート）
7. ✅ ポリシー（セキュリティポリシー）
8. ✅ ローカル証明書ファイル（`certs/`ディレクトリから）

**保護されるリソース：**
- ❌ 本番IoTリソース（ワークショップタグなし）
- ❌ 異なる命名パターンのリソース
- ❌ ワークショップThingsに関連付けられていない証明書とポリシー
- ❌ ワークショップスクリプト外で作成されたリソース

### 依存関係を考慮した削除

クリーンアップスクリプトはAWS IoTリソースの依存関係を自動的に処理します：

**削除順序：**
```
Thing Shadows → 証明書 → Things → IoTルール → Thing Groups → Thing Types → ポリシー
```

**この順序が重要な理由：**
- Thing Shadowsは証明書の前に削除する必要があります
- 証明書はThingsを削除する前に切り離す必要があります
- Thingsはグループを削除する前にグループから削除する必要があります
- ポリシーは削除前に切り離す必要があります

**スクリプトはこれを自動的に処理します** - 依存関係の競合を心配する必要はありません。

### サマリーレポートの理解

クリーンアップが完了すると、サマリーレポートが表示されます：

```
📊 クリーンアップサマリー

リソースタイプ  | 識別済み | 削除済み | 失敗
----------------|----------|----------|------
Things          |       20 |       20 |    0
証明書          |       20 |       20 |    0
Thing Groups    |        4 |        4 |    0
Thing Types     |        3 |        3 |    0
IoTルール       |        1 |        1 |    0
ポリシー        |       20 |       20 |    0
----------------|----------|----------|------
合計            |       68 |       68 |    0

✅ クリーンアップが正常に完了しました！
```

**レポートフィールド：**
- **識別済み**: ワークショップ基準に一致するリソースが見つかりました
- **削除済み**: 正常に削除されたリソース
- **失敗**: 削除できなかったリソース（エラー詳細付き）

### クリーンアップのトラブルシューティング

**問題: 「リソースが見つかりません」**
- **原因**: リソースにワークショップタグがないか、プレフィックスと一致しない可能性があります
- **解決策**: 
  - セットアップ中にカスタムプレフィックスを使用したかどうかを確認
  - 正しいプレフィックスで`--things-prefix`を使用
  - AWSコンソールでリソースが存在することを確認

**問題: 「アクセス拒否」エラー**
- **原因**: AWS認証情報に必要なIoT権限がありません
- **解決策**: IAMユーザー/ロールにIoTフルアクセス権限があることを確認

**問題: 「依存関係の競合」エラー**
- **原因**: リソースに処理されなかった依存関係があります
- **解決策**: スクリプトはこれを自動的に処理するはずです。問題が続く場合は、`--debug`で実行して詳細を確認

**問題: 一部のリソースが削除されない**
- **原因**: リソースが使用中または外部依存関係がある可能性があります
- **解決策**: 
  - サマリーレポートで失敗したリソースを確認
  - AWSコンソールを使用して残りのリソースを手動で検査および削除
  - 依存関係を解決した後、クリーンアップを再実行

### ベストプラクティス

1. **常に最初にdry-runを使用**: 実行前に削除されるものをプレビュー
2. **プレフィックスを一致させる**: セットアップとクリーンアップに同じ`--things-prefix`を使用
3. **サマリーを確認**: レポートを確認してすべてのリソースが削除されたことを確認
4. **速やかにクリーンアップを実行**: 料金を避けるためにワークショップリソースを実行したままにしない
5. **認証情報を安全に保つ**: AWS認証情報をバージョン管理にコミットしない

## 🛠️ トラブルシューティング

### よくある問題

**AWS認証情報:**
```bash
# 認証情報を設定
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Python依存関係:**
```bash
pip install -r requirements.txt
```

**OpenSSLの問題:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### デバッグモード

すべてのスクリプトは詳細なAPIログ記録のためのデバッグモードをサポートしています:
```bash
python scripts/<script_name>.py --debug
```

## 📖 高度なドキュメント

### 詳細ドキュメント
- **[詳細スクリプトガイド](docs/ja/DETAILED_SCRIPTS.md)** - 詳細なスクリプトドキュメント
- **[完全な例](docs/ja/EXAMPLES.md)** - 完全なワークフローとサンプル出力
- **[トラブルシューティングガイド](docs/ja/TROUBLESHOOTING.md)** - よくある問題と解決策

### 学習リソース
- **[AWS IoT Core ドキュメント](https://docs.aws.amazon.com/iot/)**
- **[AWS IoT Device SDK](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)**
- **[MQTT プロトコル仕様](https://mqtt.org/)**

## 🤝 貢献

これは教育プロジェクトです。学習体験を向上させる貢献を歓迎します:

- **バグ修正** スクリプトの問題に対して
- **翻訳改善** より良いローカライゼーションのために
- **ドキュメント強化** 明確性のために
- **追加学習シナリオ** 基礎レベルに適したもの

### 学習リソース

#### AWS IoT Core ドキュメント
- **[AWS IoT Core 開発者ガイド](https://docs.aws.amazon.com/iot/latest/developerguide/)** - 完全な開発者ガイド
- **[AWS IoT Core API リファレンス](https://docs.aws.amazon.com/iot/latest/apireference/)** - API ドキュメント

#### このプロジェクトで使用されているAWS SDK
- **[Boto3 ドキュメント](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - 完全なPython SDK ドキュメント
- **[Boto3 IoT クライアントリファレンス](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT固有のAPIメソッド
- **[AWS IoT Device SDK for Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTTクライアントドキュメント
- **[AWS IoT Device SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - ソースコードと例

#### プロトコルと標準
- **[MQTT プロトコル仕様](https://mqtt.org/)** - 公式MQTTドキュメント
- **[X.509 証明書標準](https://tools.ietf.org/html/rfc5280)** - 証明書フォーマット仕様

## 📄 ライセンス

このプロジェクトはMIT-0ライセンスの下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 🏷️ タグ

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive` `japanese` `日本語`