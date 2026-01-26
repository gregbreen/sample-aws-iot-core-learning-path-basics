# AWS IoT Core - 学習パス - 基礎

> 🌍 **利用可能な言語** | **Available Languages** | **Idiomas Disponibles** | **可用语言**
> 
> - [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | **日本語** (現在) | [Português](README.pt-BR.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Italiano](README.it.md) | [Français](README.fr.md)
> - **ドキュメント**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | **日本語** (docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/) | [Deutsch](docs/de/) | [Italiano](docs/it/) | [Français](docs/fr/)

AWS IoT Coreの基本を楽しく学べるPythonツールキットです！インタラクティブなスクリプトを使って、デバイス管理やセキュリティ、API操作、MQTT通信などを実際に体験しながら学んでいきましょう。

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

**⚠️ コスト注意**: 実際のAWSリソースを作成するので、少し料金がかかります（合計約$0.17）。完了したら必ずクリーンアップしてくださいね！

## こんな方におすすめ

**主な対象者**: AWS IoT Coreを初めて使うクラウド開発者、ソリューションアーキテクト、DevOpsエンジニアの方

**前提知識**: AWSの基本、Pythonの基礎、コマンドラインの使い方がわかればOKです

**学習レベル**: アソシエイトレベルの実践的な内容です

## 🔧 使っているAWS SDK

このプロジェクトでは、本格的なAWS IoT Core体験を提供するために公式AWS SDKを使っています：

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

**これらのSDKを使う理由:**
- **本番対応**: 実際のIoTアプリケーションで使われているのと同じSDKです
- **セキュリティ**: AWS IoTのセキュリティベストプラクティスが組み込まれています
- **信頼性**: AWSが公式にメンテナンスしているライブラリで、エラーハンドリングも充実
- **学習価値**: 本格的なAWS IoT開発パターンを体験できます

## 目次

- 🚀 [クイックスタート](#-クイックスタート---完全学習パス)
- ⚙️ [インストール・セットアップ](#️-インストールセットアップ)
- 📚 [学習スクリプト](#-学習スクリプト)
- 🧹 [リソースクリーンアップ](#-リソースクリーンアップ)
- 🛠️ [トラブルシューティング](#-トラブルシューティング)
- 📖 [高度なドキュメント](#-高度なドキュメント)

## ⚙️ インストールとセットアップ

### 必要なもの
- Python 3.10以上
- IoT権限があるAWSアカウント
- ターミナル/コマンドラインが使える環境
- OpenSSL（証明書機能で使います）

**⚠️ 安全のために**: 専用の開発・学習用AWSアカウントを使うことをおすすめします。本番のIoTリソースがあるアカウントでは実行しないでくださいね。クリーンアップスクリプトには安全機能がありますが、学習用には別の環境を使うのがベストです。

### かかる費用について

**このプロジェクトでは実際のAWSリソースを作成するので、少し料金がかかります（合計約$0.17）。**

| サービス | 使用量 | 推定コスト (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | 約100メッセージ、20デバイス | $0.10 |
| **AWS IoT Device Shadow service** | 約30シャドウ操作 | $0.04 |
| **IoT Rules Engine** | 約50ルール実行 | $0.01 |
| **証明書ストレージ** | 20証明書を1日間 | $0.01 |
| **Amazon CloudWatch Logs** | 基本ログ記録 | $0.01 |
| **合計推定** | **完全学習セッション** | **約$0.17** |

**⚠️ 大切なこと**: 継続的な料金を避けるため、完了したら必ずクリーンアップスクリプトを実行してくださいね。



### インストール手順

**1. リポジトリをクローンします:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. OpenSSLをインストールします:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** [OpenSSL website](https://www.openssl.org/)からダウンロード

**3. 仮想環境を作ります（推奨）:**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. 言語を設定します（お好みで）:**
```bash
# すべてのスクリプトで使う言語を設定できます
export AWS_IOT_LANG=ja     # 日本語
export AWS_IOT_LANG=en     # 英語（デフォルト）
export AWS_IOT_LANG=es     # スペイン語
export AWS_IOT_LANG=zh-CN  # 中国語

# 設定しない場合は、スクリプトが言語を聞いてくれます
```

**使える言語:**
- **英語** (`en`, `english`) - デフォルト
- **スペイン語** (`es`, `spanish`, `español`) - 完全対応
- **日本語** (`ja`, `japanese`, `日本語`, `jp`) - 完全対応
- **中国語** (`zh-CN`, `chinese`, `中文`, `zh`) - 完全対応

## 🌍 多言語サポート

すべての学習スクリプトは英語、スペイン語、日本語、中国語に対応しています。言語設定で変わるのは：

**✅ 翻訳されるもの:**
- ウェルカムメッセージと学習コンテンツ
- メニューとユーザーへの質問
- 学習ポイントと説明
- エラーメッセージと確認メッセージ
- 進行状況とステータス表示

**❌ そのまま英語で表示されるもの:**
- AWS APIのレスポンス（JSONデータ）
- 技術的なパラメータ名と値
- HTTPメソッドとエンドポイント
- デバッグ情報とログ
- AWSリソース名とID

**使い方:**

**方法1: 環境変数で設定（おすすめ）**
```bash
# すべてのスクリプトで使う言語を設定
export AWS_IOT_LANG=ja     # 日本語
export AWS_IOT_LANG=en     # 英語
export AWS_IOT_LANG=es     # スペイン語
export AWS_IOT_LANG=zh-CN  # 中国語

# どのスクリプトを実行しても、設定した言語が使われます
python scripts/iot_registry_explorer.py
```

**方法2: 対話的に選択**
```bash
# 環境変数を設定せずに実行すると、スクリプトが言語を聞いてくれます
python scripts/setup_sample_data.py

# こんな感じで表示されます:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# Select language (1-4): 3
```

**対応しているスクリプト:**
- ✅ `setup_sample_data.py` - サンプルデータ作成
- ✅ `iot_registry_explorer.py` - API探索
- ✅ `certificate_manager.py` - 証明書管理
- ✅ `mqtt_client_explorer.py` - MQTT通信
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - Device Shadow操作
- ✅ `iot_rules_explorer.py` - Rules Engine探索
- ✅ `cleanup_sample_data.py` - リソースクリーンアップ

## 📚 学習スクリプト

**おすすめの学習順序:**

### 1. 📊 サンプルデータのセットアップ
**ファイル**: `scripts/setup_sample_data.py`
**何をするの**: 実際に触って学べるIoTリソースを作ります
**作られるもの**: 20個のThings、3個のThing Types、4個のThing Groups

### 2. 🔍 IoT Registry API を探索
**ファイル**: `scripts/iot_registry_explorer.py`
**何をするの**: AWS IoT Registry APIを対話的に学べます
**機能**: 8つの主要APIを詳しい説明付きで体験できます

### 3. 🔐 証明書とポリシーの管理
**ファイル**: `scripts/certificate_manager.py`
**何をするの**: AWS IoTのセキュリティを証明書とポリシーで学びます
**機能**: 証明書の作成、ポリシーの紐付け、外部証明書の登録など

### 4. 📡 MQTT通信を体験
**ファイル**: 
- `scripts/mqtt_client_explorer.py` (証明書ベース、おすすめ)
- `scripts/mqtt_websocket_explorer.py` (WebSocketベースの代替)

**何をするの**: MQTTプロトコルでリアルタイムIoT通信を体験
**機能**: 対話的なコマンドライン、トピックの購読、メッセージの送信

### 5. 🌟 AWS IoT Device Shadow を探索
**ファイル**: `scripts/device_shadow_explorer.py`
**何をするの**: AWS IoT Device Shadowでデバイスの状態同期を学びます
**機能**: 対話的なシャドウ管理、状態の更新、差分の処理

### 6. ⚙️ IoT Rules Engine を探索
**ファイル**: `scripts/iot_rules_explorer.py`
**何をするの**: IoT Rules Engineでメッセージのルーティングと処理を学びます
**機能**: ルールの作成、SQLフィルタリング、IAMの自動セットアップ

### 7. 🧹 サンプルデータのクリーンアップ
**ファイル**: `scripts/cleanup_sample_data.py`
**何をするの**: 料金がかからないように、すべての学習リソースを削除します
**機能**: 依存関係を考慮した安全なクリーンアップ

## 🧹 リソースのクリーンアップ

**⚠️ 大切**: 学習が終わったら、継続的な料金を避けるために必ずクリーンアップを実行してくださいね。

### 基本的な使い方

```bash
# 標準クリーンアップ - すべてのワークショップリソースを削除
python scripts/cleanup_sample_data.py

# 何が削除されるか確認（最初にこれをやるのがおすすめ）
python scripts/cleanup_sample_data.py --dry-run

# カスタムプレフィックスでクリーンアップ
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# 詳しいログを見たい時はデバッグモード
python scripts/cleanup_sample_data.py --debug
```

### コマンドラインオプション

| オプション | 説明 | デフォルト | 例 |
|-----------|-------------|---------|---------|
| `--things-prefix` | Thing名のカスタムプレフィックス | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | 削除せずに確認だけする | `False` | `--dry-run` |
| `--debug` | 詳しいログを表示 | `False` | `--debug` |

### リソースの見つけ方

クリーンアップスクリプトは**2つの方法**でワークショップリソースを安全に見つけます：

**1. タグで見つける（メインの方法）**
- セットアップスクリプトで作ったリソースには自動的にタグが付きます：
  - `workshop-resource: true` - ワークショップで作ったリソース
  - `created-by: setup-script` - どのスクリプトで作ったか
  - `workshop-name: iot-core-basics` - どのワークショップか
- **いいところ**: 一番確実で、名前に関係なく動きます

**2. 名前で見つける（サブの方法）**
- タグがない場合は、名前のパターンで見つけます：
  - Things: `--things-prefix`のパターン（デフォルト: `Vehicle-VIN-`）
  - Thing Types: `SedanVehicle`、`SUVVehicle`、`TruckVehicle`
  - Thing Groups: `CustomerFleet`、`TestFleet`、`MaintenanceFleet`、`DealerFleet`
  - IoTルール: `*Rule`、`rule_*`、`*_workshop_*`のパターン
- **いいところ**: タグが付く前に作ったリソースでも動きます

### Dry-Runモード（最初にこれをやろう）

**クリーンアップする前に、必ず確認しましょう：**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Dry-runモードでできること：**
- ✅ 削除されるワークショップリソースをすべて確認
- ✅ タイプ別の詳しいリストを表示
- ✅ 削除される順番を表示（依存関係を考慮）
- ✅ サマリーレポートを生成
- ❌ **リソースは削除しません**

**Dry-runの出力例：**
```
🔍 DRY RUN MODE - リソースは削除されません

見つかったリソース:
  Things: 20個
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  証明書: 20個
  Thing Groups: 4個
  Thing Types: 3個
  IoTルール: 1個

合計: 48個のリソースが削除されます
```

### カスタムプレフィックスを使う場合

セットアップの時にカスタムプレフィックスを使った場合は、クリーンアップでも同じものを使ってください：

```bash
# カスタムプレフィックスでセットアップ
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# 同じプレフィックスでクリーンアップ
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**大切**: 名前で見つける方法を使う場合、セットアップとクリーンアップで同じプレフィックスを使う必要があります。

### 削除されるもの

**削除されるリソース（依存関係の順番で）：**
1. ✅ Thing Shadows（デバイスの状態データ）
2. ✅ 証明書（最初にThingsから外します）
3. ✅ Things（IoTデバイス）
4. ✅ IoTルール（メッセージルーティングルール）
5. ✅ Thing Groups（デバイスのグループ）
6. ✅ Thing Types（デバイスのテンプレート）
7. ✅ ポリシー（セキュリティポリシー）
8. ✅ ローカルの証明書ファイル（`certs/`フォルダから）

**削除されないもの：**
- ❌ 本番のIoTリソース（ワークショップタグなし）
- ❌ 違う名前パターンのリソース
- ❌ ワークショップのThingsに紐付いていない証明書とポリシー
- ❌ ワークショップスクリプト以外で作ったリソース

### 依存関係を考えた削除

クリーンアップスクリプトは、AWS IoTリソースの依存関係を自動で処理します：

**削除の順番：**
```
Thing Shadows → 証明書 → Things → IoTルール → Thing Groups → Thing Types → ポリシー
```

**なぜこの順番？**
- Thing Shadowsは証明書より先に削除する必要があります
- 証明書はThingsを削除する前に外す必要があります
- Thingsはグループを削除する前にグループから外す必要があります
- ポリシーは削除する前に外す必要があります

**スクリプトが自動でやってくれます** - 依存関係の心配は不要です。

### サマリーレポートの見方

クリーンアップが終わると、こんなレポートが表示されます：

```
📊 クリーンアップサマリー

リソースタイプ  | 見つかった | 削除した | 失敗
----------------|----------|----------|------
Things          |       20 |       20 |    0
証明書          |       20 |       20 |    0
Thing Groups    |        4 |        4 |    0
Thing Types     |        3 |        3 |    0
IoTルール       |        1 |        1 |    0
ポリシー        |       20 |       20 |    0
----------------|----------|----------|------
合計            |       68 |       68 |    0

✅ クリーンアップが無事完了しました！
```

**レポートの項目：**
- **見つかった**: ワークショップの条件に合うリソースが見つかりました
- **削除した**: 無事削除できたリソース
- **失敗**: 削除できなかったリソース（エラーの詳細付き）

### トラブルシューティング

**問題: 「リソースが見つかりません」**
- **原因**: リソースにワークショップタグがないか、プレフィックスが合わない可能性
- **解決方法**: 
  - セットアップの時にカスタムプレフィックスを使ったか確認
  - 正しいプレフィックスで`--things-prefix`を使う
  - AWSコンソールでリソースが存在するか確認

**問題: 「アクセス拒否」エラー**
- **原因**: AWS認証情報に必要なIoT権限がありません
- **解決方法**: IAMユーザー/ロールにIoTフルアクセス権限があるか確認

**問題: 「依存関係の競合」エラー**
- **原因**: リソースに処理されていない依存関係があります
- **解決方法**: スクリプトが自動で処理するはずです。問題が続く場合は`--debug`で実行して詳細を確認

**問題: 一部のリソースが削除されない**
- **原因**: リソースが使用中か、外部依存関係がある可能性
- **解決方法**: 
  - サマリーレポートで失敗したリソースを確認
  - AWSコンソールで残ったリソースを手動で確認・削除
  - 依存関係を解決してから、もう一度クリーンアップを実行

### おすすめの使い方

1. **最初は必ずdry-runで**: 実行前に何が削除されるか確認しましょう
2. **プレフィックスを合わせる**: セットアップとクリーンアップで同じ`--things-prefix`を使いましょう
3. **サマリーを確認**: レポートを見て、すべてのリソースが削除されたか確認しましょう
4. **早めにクリーンアップ**: 料金を避けるため、ワークショップリソースを放置しないようにしましょう
5. **認証情報は安全に**: AWS認証情報をバージョン管理にコミットしないようにしましょう

## 🛠️ トラブルシューティング

### よくある問題

**AWS認証情報の設定:**
```bash
# 認証情報を設定します
export AWS_ACCESS_KEY_ID=<your-key>
export AWS_SECRET_ACCESS_KEY=<your-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Pythonの依存関係:**
```bash
pip install -r requirements.txt
```

**OpenSSLの問題:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### デバッグモード

すべてのスクリプトで、詳しいAPIログを見るためのデバッグモードが使えます:
```bash
python scripts/<script_name>.py --debug
```

## 📖 もっと詳しく知りたい方へ

### 詳しいドキュメント
- **[詳細スクリプトガイド](docs/ja/DETAILED_SCRIPTS.md)** - 各スクリプトの詳しい説明
- **[完全な例](docs/ja/EXAMPLES.md)** - 完全なワークフローとサンプル出力
- **[トラブルシューティングガイド](docs/ja/TROUBLESHOOTING.md)** - よくある問題と解決方法

### 学習リソース
- **[AWS IoT Core ドキュメント](https://docs.aws.amazon.com/iot/)**
- **[AWS IoT Device SDK](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)**
- **[MQTT プロトコル仕様](https://mqtt.org/)**

## 🤝 貢献について

これは教育プロジェクトです。学習体験をより良くする貢献を歓迎します:

- **バグ修正** スクリプトの問題を見つけたら
- **翻訳の改善** より良いローカライゼーションのために
- **ドキュメントの強化** わかりやすくするために
- **学習シナリオの追加** 基礎レベルに合ったもの

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

このプロジェクトはMIT-0ライセンスです - 詳しくは[LICENSE](LICENSE)ファイルをご覧ください。

## 🏷️ タグ

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive` `japanese` `日本語`