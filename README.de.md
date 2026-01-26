# AWS IoT Core - Lernpfad - Grundlagen

> 🌍 **Verfügbare Sprachen** | **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言** | **사용 가능한 언어**
> 
> - [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | [한국어](README.ko.md) | **Deutsch** (Aktuell)
> - **Dokumentation**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/) | [Deutsch](docs/de/)

Ein umfassendes Python-Toolkit zum Erlernen der grundlegenden Konzepte von Amazon Web Services (AWS) AWS IoT Core durch praktische Erkundung. Interaktive Skripte demonstrieren Geräteverwaltung, Sicherheit, API-Operationen und MQTT-Kommunikation mit detaillierten Erklärungen.

## 🚀 Schnellstart - Kompletter Lernpfad

```bash
# 1. Klonen und einrichten
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Umgebung einrichten
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. AWS-Zugangsdaten konfigurieren
export AWS_ACCESS_KEY_ID=<dein-key>
export AWS_SECRET_ACCESS_KEY=<dein-secret>
export AWS_DEFAULT_REGION=<deine-region (z.B. us-east-1)>

# 4. Optional: Spracheinstellung festlegen
export AWS_IOT_LANG=de  # 'en' für Englisch, 'es' für Spanisch, 'ja' für Japanisch, 'zh-CN' für Chinesisch, 'pt-BR' für Portugiesisch, 'ko' für Koreanisch

# 5. Komplette Lernsequenz durchführen
python scripts/setup_sample_data.py          # Beispiel-IoT-Ressourcen erstellen
python scripts/iot_registry_explorer.py      # AWS IoT APIs erkunden
python scripts/certificate_manager.py        # IoT-Sicherheit lernen
python scripts/mqtt_client_explorer.py       # Echtzeit-MQTT-Kommunikation
python scripts/device_shadow_explorer.py     # Gerätezustandssynchronisation
python scripts/iot_rules_explorer.py         # Nachrichtenrouting und -verarbeitung
python scripts/cleanup_sample_data.py        # Ressourcen aufräumen (WICHTIG!)
```

**⚠️ Kostenwarnung**: Dies erstellt echte AWS-Ressourcen (~0,17 $ insgesamt). Führe das Aufräumen durch, wenn du fertig bist!

## Zielgruppe

**Hauptzielgruppe:** Cloud-Entwickler, Solution Architects, DevOps-Engineers, die neu bei AWS IoT Core sind

**Voraussetzungen:** Grundlegende AWS-Kenntnisse, Python-Grundlagen, Kommandozeilennutzung

**Lernniveau:** Associate-Level mit praktischem Ansatz

## 🔧 Erstellt mit AWS SDKs

Dieses Projekt nutzt die offiziellen AWS SDKs, um authentische AWS IoT Core-Erfahrungen zu bieten:

### **Boto3 - AWS SDK für Python**
- **Zweck**: Ermöglicht alle AWS IoT Registry-Operationen, Zertifikatsverwaltung und Rules Engine-Interaktionen
- **Version**: `>=1.26.0`
- **Dokumentation**: [Boto3 Dokumentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **AWS IoT Core APIs**: [Boto3 IoT Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK für Python**
- **Zweck**: Ermöglicht authentische MQTT-Kommunikation mit AWS IoT Core unter Verwendung von X.509-Zertifikaten
- **Version**: `>=1.11.0`
- **Dokumentation**: [AWS IoT Device SDK für Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Warum diese SDKs wichtig sind:**
- **Produktionsreif**: Dieselben SDKs, die in echten IoT-Anwendungen verwendet werden
- **Sicherheit**: Integrierte Unterstützung für AWS IoT-Sicherheits-Best-Practices
- **Zuverlässigkeit**: Offiziell von AWS gewartete Bibliotheken mit umfassender Fehlerbehandlung
- **Lernwert**: Erlebe authentische AWS IoT-Entwicklungsmuster

## Inhaltsverzeichnis

- 🚀 [Schnellstart](#-schnellstart---kompletter-lernpfad)
- ⚙️ [Installation & Einrichtung](#️-installation--einrichtung)
- 📚 [Lernskripte](#-lernskripte)
- 🧹 [Ressourcen aufräumen](#-ressourcen-aufräumen)
- 🛠️ [Fehlerbehebung](#-fehlerbehebung)
- 📖 [Erweiterte Dokumentation](#-erweiterte-dokumentation)

## ⚙️ Installation & Einrichtung

### Voraussetzungen
- Python 3.10+
- AWS-Konto mit IoT-Berechtigungen
- Terminal/Kommandozeilenzugriff
- OpenSSL (für Zertifikatsfunktionen)

**⚠️ WICHTIGER SICHERHEITSHINWEIS**: Verwende ein dediziertes Entwicklungs-/Lern-AWS-Konto. Führe diese Skripte nicht in Konten aus, die Produktions-IoT-Ressourcen enthalten. Obwohl das Aufräumskript mehrere Sicherheitsmechanismen hat, ist es Best Practice, isolierte Umgebungen für Lernaktivitäten zu verwenden.

### Kosteninformationen

**Dieses Projekt erstellt echte AWS-Ressourcen, die Kosten verursachen (~0,17 $ insgesamt).**

| Service | Nutzung | Geschätzte Kosten (USD) |
|---------|---------|------------------------|
| **AWS IoT Core** | ~100 Nachrichten, 20 Geräte | $0.10 |
| **AWS IoT Device Shadow service** | ~30 Shadow-Operationen | $0.04 |
| **IoT Rules Engine** | ~50 Regelausführungen | $0.01 |
| **Zertifikatspeicherung** | 20 Zertifikate für 1 Tag | $0.01 |
| **Amazon CloudWatch Logs** | Basis-Logging | $0.01 |
| **Geschätzte Gesamtkosten** | **Komplette Lernsession** | **~$0.17** |

**⚠️ Wichtig**: Führe immer das Aufräumskript aus, wenn du fertig bist, um laufende Kosten zu vermeiden.


### Detaillierte Installation

**1. Repository klonen:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. OpenSSL installieren:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Download von der [OpenSSL-Website](https://www.openssl.org/)

**3. Virtuelle Umgebung (Empfohlen):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Sprachkonfiguration (Optional):**
```bash
# Spracheinstellung für alle Skripte festlegen
export AWS_IOT_LANG=de     # Deutsch
export AWS_IOT_LANG=en     # Englisch (Standard)
export AWS_IOT_LANG=es     # Spanisch
export AWS_IOT_LANG=ja     # Japanisch
export AWS_IOT_LANG=zh-CN  # Chinesisch
export AWS_IOT_LANG=pt-BR  # Portugiesisch
export AWS_IOT_LANG=ko     # Koreanisch

# Alternative: Skripte fragen nach der Sprache, wenn nicht gesetzt
```

**Unterstützte Sprachen:**
- **Englisch** (`en`, `english`) - Standard
- **Spanisch** (`es`, `spanish`, `español`) - Vollständige Übersetzung verfügbar
- **Japanisch** (`ja`, `japanese`, `日本語`, `jp`) - Vollständige Übersetzung verfügbar
- **Chinesisch** (`zh-CN`, `chinese`, `中文`, `zh`) - Vollständige Übersetzung verfügbar
- **Portugiesisch** (`pt-BR`, `portuguese`, `português`, `pt`) - Vollständige Übersetzung verfügbar
- **Koreanisch** (`ko`, `korean`, `한국어`, `kr`) - Vollständige Übersetzung verfügbar
- **Deutsch** (`de`, `german`, `deutsch`) - Vollständige Übersetzung verfügbar

## 🌍 Mehrsprachige Unterstützung

Alle Lernskripte unterstützen Englisch, Spanisch, Japanisch, Chinesisch, Portugiesisch, Koreanisch und Deutsch. Die Sprache beeinflusst:

**✅ Was übersetzt wird:**
- Willkommensnachrichten und Bildungsinhalte
- Menüoptionen und Benutzereingaben
- Lernmomente und Erklärungen
- Fehlermeldungen und Bestätigungen
- Fortschrittsindikatoren und Statusmeldungen

**❌ Was in der Originalsprache bleibt:**
- AWS API-Antworten (JSON-Daten)
- Technische Parameternamen und -werte
- HTTP-Methoden und Endpunkte
- Debug-Informationen und Logs
- AWS-Ressourcennamen und -Identifikatoren

**Nutzungsoptionen:**

**Option 1: Umgebungsvariable (Empfohlen)**
```bash
# Spracheinstellung für alle Skripte festlegen
export AWS_IOT_LANG=de     # Deutsch
export AWS_IOT_LANG=en     # Englisch
export AWS_IOT_LANG=es     # Spanisch
export AWS_IOT_LANG=ja     # Japanisch
export AWS_IOT_LANG=zh-CN  # Chinesisch
export AWS_IOT_LANG=pt-BR  # Portugiesisch
export AWS_IOT_LANG=ko     # Koreanisch

# Beliebiges Skript ausführen - Sprache wird automatisch angewendet
python scripts/iot_registry_explorer.py
```

**Option 2: Interaktive Auswahl**
```bash
# Ohne Umgebungsvariable ausführen - Skript fragt nach der Sprache
python scripts/setup_sample_data.py

# Beispielausgabe:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma / 언어 선택 / Sprachauswahl
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# 6. 한국어 (Korean)
# 7. Deutsch (German)
# Select language (1-7): 7
```

**Unterstützte Skripte:**
- ✅ `setup_sample_data.py` - Beispieldatenerstellung
- ✅ `iot_registry_explorer.py` - API-Erkundung
- ✅ `certificate_manager.py` - Zertifikatsverwaltung
- ✅ `mqtt_client_explorer.py` - MQTT-Kommunikation
- ✅ `mqtt_websocket_explorer.py` - WebSocket MQTT
- ✅ `device_shadow_explorer.py` - AWS IoT Device Shadow service-Operationen
- ✅ `iot_rules_explorer.py` - Rules Engine-Erkundung
- ✅ `cleanup_sample_data.py` - Ressourcenaufräumung


## 📚 Lernskripte

**Empfohlener Lernpfad:**

### 1. 📊 Beispieldaten-Setup
**Datei**: `scripts/setup_sample_data.py`
**Zweck**: Erstellt realistische IoT-Ressourcen für praktisches Lernen mit automatischem Tagging
**Erstellt**: 20 Things, 3 Thing Types, 4 Thing Groups, IoT Rules (mit Workshop-Tags)

**Hauptfunktionen:**
- **Automatisches Tagging**: Alle Ressourcen werden für sichere Aufräumidentifikation getaggt
- **Benutzerdefinierte Präfixe**: Unterstützung für benutzerdefinierte Thing-Namen-Präfixe
- **Mehrsprachig**: Vollständige Internationalisierungsunterstützung

**Nutzungsbeispiele:**
```bash
# Basis-Setup mit Standard-Präfix (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Setup mit benutzerdefiniertem Präfix
python scripts/setup_sample_data.py --things-prefix "MeinGerät-"

# Setup mit Sprachauswahl
export AWS_IOT_LANG=de
python scripts/setup_sample_data.py
```

**Ressourcen-Tagging:**
Alle erstellten Ressourcen erhalten diese Tags zur sicheren Identifikation:
- `workshop-resource: true` - Markiert als Workshop-erstellt
- `created-by: setup-script` - Identifiziert das erstellende Skript
- `workshop-name: iot-core-basics` - Gruppiert nach Workshop-Name

Diese Tags ermöglichen es dem Aufräumskript, nur Workshop-Ressourcen sicher zu identifizieren und zu entfernen, wodurch deine Produktions-IoT-Infrastruktur geschützt wird.

### 2. 🔍 IoT Registry API Explorer
**Datei**: `scripts/iot_registry_explorer.py`
**Zweck**: Interaktives Tool zum Erlernen der AWS IoT Registry APIs
**Funktionen**: 8 Kern-APIs mit detaillierten Erklärungen und echten API-Aufrufen

### 3. 🔐 Zertifikats- & Policy-Manager
**Datei**: `scripts/certificate_manager.py`
**Zweck**: Lerne AWS IoT-Sicherheit durch Zertifikats- und Policy-Verwaltung
**Funktionen**: Zertifikatserstellung, Policy-Anhängen, externe Zertifikatsregistrierung

### 4. 📡 MQTT-Kommunikation
**Dateien**: 
- `scripts/mqtt_client_explorer.py` (Zertifikatsbasiert, empfohlen)
- `scripts/mqtt_websocket_explorer.py` (WebSocket-basierte Alternative)

**Zweck**: Erlebe Echtzeit-IoT-Kommunikation mit dem MQTT-Protokoll
**Funktionen**: Interaktive Kommandozeilenschnittstelle, Topic-Abonnement, Nachrichtenveröffentlichung

### 5. 🌟 AWS IoT Device Shadow service Explorer
**Datei**: `scripts/device_shadow_explorer.py`
**Zweck**: Lerne Gerätezustandssynchronisation mit AWS IoT Device Shadow
**Funktionen**: Interaktive Shadow-Verwaltung, Zustandsaktualisierungen, Delta-Verarbeitung

### 6. ⚙️ IoT Rules Engine Explorer
**Datei**: `scripts/iot_rules_explorer.py`
**Zweck**: Lerne Nachrichtenrouting und -verarbeitung mit der IoT Rules Engine
**Funktionen**: Regelerstellung, SQL-Filterung, automatisches AWS IAM-Setup

### 7. 🧹 Beispieldaten-Aufräumung
**Datei**: `scripts/cleanup_sample_data.py`
**Zweck**: Räume alle Lernressourcen auf, um Kosten zu vermeiden
**Funktionen**: Sichere Aufräumung mit Abhängigkeitsbehandlung


## 🧹 Ressourcen aufräumen

**⚠️ WICHTIG**: Führe immer das Aufräumen durch, wenn du mit dem Lernen fertig bist, um laufende AWS-Kosten zu vermeiden.

### Grundlegende Nutzung

```bash
# Standard-Aufräumung - entfernt alle Workshop-Ressourcen
python scripts/cleanup_sample_data.py

# Vorschau, was gelöscht wird (empfohlener erster Schritt)
python scripts/cleanup_sample_data.py --dry-run

# Aufräumung mit benutzerdefiniertem Präfix
python scripts/cleanup_sample_data.py --things-prefix "MeinGerät-"

# Debug-Modus für detailliertes API-Logging aktivieren
python scripts/cleanup_sample_data.py --debug
```

### Kommandozeilenparameter

| Parameter | Beschreibung | Standard | Beispiel |
|-----------|--------------|----------|----------|
| `--things-prefix` | Benutzerdefiniertes Präfix für Thing-Namen | `Vehicle-VIN-` | `--things-prefix "TestGerät-"` |
| `--dry-run` | Vorschau der Aufräumung ohne Löschen | `False` | `--dry-run` |
| `--debug` | Detailliertes API-Logging aktivieren | `False` | `--debug` |

### Wie die Ressourcenidentifikation funktioniert

Das Aufräumskript verwendet ein **duales Identifikationssystem**, um Workshop-Ressourcen sicher zu identifizieren:

**1. Tag-basierte Identifikation (Primäre Methode)**
- Von Setup-Skripten erstellte Ressourcen werden automatisch getaggt mit:
  - `workshop-resource: true` - Identifiziert Workshop-erstellte Ressourcen
  - `created-by: setup-script` - Verfolgt, welches Skript die Ressource erstellt hat
  - `workshop-name: iot-core-basics` - Gruppiert Ressourcen nach Workshop
- **Vorteil**: Zuverlässigste Methode, funktioniert unabhängig von der Benennung

**2. Namenskonventions-Fallback (Sekundäre Methode)**
- Wenn Tags nicht vorhanden sind, identifiziert das Skript Ressourcen anhand von Namensmustern:
  - Things: Entsprechen dem `--things-prefix`-Muster (Standard: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - IoT Rules: Entsprechen `*Rule`, `rule_*` oder `*_workshop_*` Mustern
- **Vorteil**: Funktioniert mit Ressourcen, die vor der Implementierung des Taggings erstellt wurden

### Dry-Run-Modus (Empfohlener erster Schritt)

**Zeige immer eine Vorschau der Aufräumoperationen, bevor du sie ausführst:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Der Dry-Run-Modus wird:**
- ✅ Alle Workshop-Ressourcen identifizieren, die gelöscht würden
- ✅ Eine detaillierte Liste der Ressourcen nach Typ anzeigen
- ✅ Die Löschreihenfolge anzeigen (respektiert Abhängigkeiten)
- ✅ Einen Zusammenfassungsbericht generieren
- ❌ **KEINE Ressourcen löschen**

**Beispiel Dry-Run-Ausgabe:**
```
🔍 DRY RUN MODUS - Keine Ressourcen werden gelöscht

Identifizierte Ressourcen:
  Things: 20 Ressourcen
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Zertifikate: 20 Ressourcen
  Thing Groups: 4 Ressourcen
  Thing Types: 3 Ressourcen
  IoT Rules: 1 Ressource

Gesamt: 48 Ressourcen würden gelöscht
```

### Verwendung benutzerdefinierter Präfixe

Wenn du Ressourcen mit einem benutzerdefinierten Präfix während des Setups erstellt hast, verwende dasselbe Präfix für die Aufräumung:

```bash
# Setup mit benutzerdefiniertem Präfix
python scripts/setup_sample_data.py --things-prefix "MeinGerät-"

# Aufräumung mit passendem Präfix
python scripts/cleanup_sample_data.py --things-prefix "MeinGerät-"
```

**Wichtig**: Das Präfix muss zwischen Setup und Aufräumung genau übereinstimmen, damit die namensbasierte Identifikation korrekt funktioniert.

### Was wird aufgeräumt

**Gelöschte Ressourcen (in Abhängigkeitsreihenfolge):**
1. ✅ Thing Shadows (Gerätezustandsdaten)
2. ✅ Zertifikate (zuerst von Things getrennt)
3. ✅ Things (IoT-Geräte)
4. ✅ IoT Rules (Nachrichtenrouting-Regeln)
5. ✅ Thing Groups (Gerätesammlungen)
6. ✅ Thing Types (Gerätevorlagen)
7. ✅ Policies (Sicherheitsrichtlinien)
8. ✅ Lokale Zertifikatsdateien (aus dem `certs/`-Verzeichnis)

**Geschützte Ressourcen:**
- ❌ Produktions-IoT-Ressourcen (ohne Workshop-Tags)
- ❌ Ressourcen mit unterschiedlichen Namensmustern
- ❌ Zertifikate und Policies, die nicht mit Workshop-Things verbunden sind
- ❌ Ressourcen, die außerhalb der Workshop-Skripte erstellt wurden

### Abhängigkeitsbewusste Löschung

Das Aufräumskript behandelt automatisch AWS IoT-Ressourcenabhängigkeiten:

**Löschreihenfolge:**
```
Thing Shadows → Zertifikate → Things → IoT Rules → Thing Groups → Thing Types → Policies
```

**Warum diese Reihenfolge wichtig ist:**
- Thing Shadows müssen vor Zertifikaten gelöscht werden
- Zertifikate müssen getrennt werden, bevor Things gelöscht werden können
- Things müssen aus Gruppen entfernt werden, bevor Gruppen gelöscht werden können
- Policies müssen getrennt werden, bevor sie gelöscht werden

**Das Skript behandelt dies automatisch** - du musst dir keine Sorgen um Abhängigkeitskonflikte machen.


### Den Zusammenfassungsbericht verstehen

Nach Abschluss der Aufräumung siehst du einen Zusammenfassungsbericht:

```
📊 Aufräumungs-Zusammenfassung

Ressourcentyp    | Identifiziert | Gelöscht | Fehlgeschlagen
-----------------|---------------|----------|----------------
Things           |            20 |       20 |              0
Zertifikate      |            20 |       20 |              0
Thing Groups     |             4 |        4 |              0
Thing Types      |             3 |        3 |              0
IoT Rules        |             1 |        1 |              0
Policies         |            20 |       20 |              0
-----------------|---------------|----------|----------------
Gesamt           |            68 |       68 |              0

✅ Aufräumung erfolgreich abgeschlossen!
```

**Berichtsfelder:**
- **Identifiziert**: Gefundene Ressourcen, die den Workshop-Kriterien entsprechen
- **Gelöscht**: Erfolgreich entfernte Ressourcen
- **Fehlgeschlagen**: Ressourcen, die nicht gelöscht werden konnten (mit Fehlerdetails)

### Fehlerbehebung bei der Aufräumung

**Problem: "Keine Ressourcen gefunden"**
- **Ursache**: Ressourcen haben möglicherweise keine Workshop-Tags oder entsprechen nicht dem Präfix
- **Lösung**: 
  - Überprüfe, ob du während des Setups ein benutzerdefiniertes Präfix verwendet hast
  - Verwende `--things-prefix` mit dem korrekten Präfix
  - Überprüfe, ob Ressourcen in der AWS-Konsole existieren

**Problem: "Berechtigung verweigert"-Fehler**
- **Ursache**: AWS-Zugangsdaten fehlen die notwendigen IoT-Berechtigungen
- **Lösung**: Stelle sicher, dass dein IAM-Benutzer/Rolle IoT-Vollzugriffsberechtigungen hat

**Problem: "Abhängigkeitskonflikt"-Fehler**
- **Ursache**: Ressourcen haben Abhängigkeiten, die nicht behandelt wurden
- **Lösung**: Das Skript sollte dies automatisch behandeln. Wenn es weiterhin besteht, führe es mit `--debug` aus, um Details zu sehen

**Problem: Einige Ressourcen nicht gelöscht**
- **Ursache**: Ressourcen werden möglicherweise verwendet oder haben externe Abhängigkeiten
- **Lösung**: 
  - Überprüfe den Zusammenfassungsbericht auf fehlgeschlagene Ressourcen
  - Verwende die AWS-Konsole, um verbleibende Ressourcen manuell zu inspizieren und zu löschen
  - Führe die Aufräumung erneut aus, nachdem Abhängigkeiten aufgelöst wurden

### Best Practices

1. **Verwende immer zuerst Dry-Run**: Zeige eine Vorschau, was gelöscht wird, bevor du ausführst
2. **Präfixe abgleichen**: Verwende dasselbe `--things-prefix` für Setup und Aufräumung
3. **Überprüfe die Zusammenfassung**: Prüfe den Bericht, um sicherzustellen, dass alle Ressourcen gelöscht wurden
4. **Führe die Aufräumung zeitnah durch**: Lasse Workshop-Ressourcen nicht laufen, um Kosten zu vermeiden
5. **Halte Zugangsdaten sicher**: Committe niemals AWS-Zugangsdaten in die Versionskontrolle

## 🛠️ Fehlerbehebung

### Häufige Probleme

**AWS-Zugangsdaten:**
```bash
# Zugangsdaten setzen
export AWS_ACCESS_KEY_ID=<dein-key>
export AWS_SECRET_ACCESS_KEY=<dein-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Python-Abhängigkeiten:**
```bash
pip install -r requirements.txt
```

**OpenSSL-Probleme:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### Debug-Modus

Alle Skripte unterstützen den Debug-Modus für detailliertes API-Logging:
```bash
python scripts/<skript_name>.py --debug
```


## ❓ Häufig gestellte Fragen (FAQ)

### Allgemeine Fragen

**F: Welche Ressourcen werden vom Aufräumskript gelöscht?**
A: Das Aufräumskript identifiziert und löscht Ressourcen, die von den Workshop-Setup-Skripten erstellt wurden. Dazu gehören Things, Zertifikate, Thing Groups, Thing Types, IoT Rules und Policies, die Workshop-Tags haben oder den Namensmustern entsprechen. Produktionsressourcen sind geschützt.

**F: Wie kann ich eine Vorschau der Aufräumung anzeigen, ohne etwas zu löschen?**
A: Verwende das `--dry-run`-Flag:
```bash
python scripts/cleanup_sample_data.py --dry-run
```
Dies zeigt genau, was gelöscht würde, ohne Änderungen vorzunehmen.

**F: Kann ich ein benutzerdefiniertes Präfix für Thing-Namen verwenden?**
A: Ja! Verwende den `--things-prefix`-Parameter sowohl beim Setup als auch bei der Aufräumung:
```bash
# Setup
python scripts/setup_sample_data.py --things-prefix "MeinGerät-"

# Aufräumung
python scripts/cleanup_sample_data.py --things-prefix "MeinGerät-"
```

**F: Was ist, wenn ich keine Tags auf meinen Ressourcen habe?**
A: Das Aufräumskript hat einen Fallback-Mechanismus. Wenn Tags nicht vorhanden sind, verwendet es Namenskonventionen zur Identifizierung von Workshop-Ressourcen. Ressourcen, die dem Thing-Präfix-Muster entsprechen (Standard: `Vehicle-VIN-`) oder Standard-Workshop-Namen, werden identifiziert.

**F: Wie ändere ich die Sprache?**
A: Setze die `AWS_IOT_LANG`-Umgebungsvariable:
```bash
export AWS_IOT_LANG=de  # Deutsch
export AWS_IOT_LANG=es  # Spanisch
export AWS_IOT_LANG=ja  # Japanisch
export AWS_IOT_LANG=zh-CN  # Chinesisch
export AWS_IOT_LANG=pt-BR  # Portugiesisch
export AWS_IOT_LANG=ko  # Koreanisch
```
Oder führe das Skript ohne Setzen aus - du wirst aufgefordert, interaktiv eine Sprache auszuwählen.

**F: Was ist, wenn die Aufräumung mittendrin fehlschlägt?**
A: Das Aufräumskript ist idempotent konzipiert - du kannst es mehrmals sicher ausführen. Wenn die Aufräumung fehlschlägt:
1. Überprüfe den Zusammenfassungsbericht, um zu sehen, welche Ressourcen fehlgeschlagen sind
2. Führe das Skript erneut aus - es überspringt bereits gelöschte Ressourcen
3. Verwende den `--debug`-Modus, um detaillierte Fehlermeldungen zu sehen
4. Lösche verbleibende Ressourcen bei Bedarf manuell über die AWS-Konsole

**F: Wie überprüfe ich, ob Ressourcen gelöscht wurden?**
A: Überprüfe den Zusammenfassungsbericht am Ende der Aufräumung. Du kannst auch in der AWS IoT-Konsole überprüfen:
- Navigiere zu AWS IoT Core → Verwalten → Things
- Überprüfe, dass Workshop-Things (Vehicle-VIN-*) weg sind
- Überprüfe, dass Thing Groups, Thing Types und Zertifikate entfernt wurden

### Technische Fragen

**F: Warum löscht das Aufräumskript Ressourcen in einer bestimmten Reihenfolge?**
A: AWS IoT-Ressourcen haben Abhängigkeiten. Zum Beispiel kannst du ein Thing nicht löschen, das noch Zertifikate angehängt hat. Das Skript folgt dieser Reihenfolge:
1. Thing Shadows (keine Abhängigkeiten)
2. Zertifikate (müssen von Things getrennt werden)
3. Things (müssen aus Gruppen entfernt werden)
4. IoT Rules (keine Abhängigkeiten von Things)
5. Thing Groups (müssen leer sein)
6. Thing Types (dürfen nicht verwendet werden)
7. Policies (müssen getrennt werden)

**F: Was ist der Unterschied zwischen tag-basierter und namensbasierter Identifikation?**
A: 
- **Tag-basiert** (primär): Verwendet AWS-Ressourcen-Tags (`workshop-resource: true`). Am zuverlässigsten, funktioniert unabhängig von der Benennung.
- **Namensbasiert** (Fallback): Verwendet Namensmuster (z.B. `Vehicle-VIN-*`). Funktioniert mit älteren Ressourcen, die vor der Implementierung des Taggings erstellt wurden.

Das Skript versucht zuerst tag-basiert, dann fällt es auf Namensmuster zurück, wenn Tags nicht vorhanden sind.

**F: Kann ich dies in einem Produktions-AWS-Konto verwenden?**
A: Obwohl das Aufräumskript mehrere Sicherheitsmechanismen hat (Tags, Namensmuster, Dry-Run-Modus), **empfehlen wir dringend, ein dediziertes Entwicklungs-/Lern-AWS-Konto zu verwenden**. Dies folgt AWS-Best-Practices für Umgebungsisolierung.

**F: Was passiert, wenn ich die Aufräumung mit Strg+C unterbreche?**
A: Das Skript behandelt Unterbrechungen elegant. Vor der Unterbrechung gelöschte Ressourcen bleiben gelöscht. Führe einfach das Aufräumskript erneut aus, um fortzufahren - es überspringt bereits gelöschte Ressourcen und vervollständigt die verbleibenden Löschungen.

**F: Wie viel kostet es, diese Lernskripte auszuführen?**
A: Ungefähr 0,17 $ USD für eine komplette Lernsession. Siehe den Abschnitt [Kosteninformationen](#kosteninformationen) für eine detaillierte Aufschlüsselung. Führe immer die Aufräumung durch, wenn du fertig bist, um laufende Kosten zu vermeiden.


## 📖 Erweiterte Dokumentation

### Detaillierte Dokumentation
- **[Detaillierte Skript-Anleitung](docs/de/DETAILED_SCRIPTS.md)** - Ausführliche Skript-Dokumentation
- **[Vollständige Beispiele](docs/de/EXAMPLES.md)** - Komplette Workflows und Beispielausgaben
- **[Fehlerbehebungsanleitung](docs/de/TROUBLESHOOTING.md)** - Häufige Probleme und Lösungen

### Documentation in English
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

### Lernressourcen

#### AWS IoT Core-Dokumentation
- **[AWS IoT Core Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[AWS IoT Core API Reference](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### In diesem Projekt verwendete AWS SDKs
- **[Boto3 Dokumentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Vollständige Python SDK-Dokumentation
- **[Boto3 IoT Client Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - IoT-spezifische API-Methoden
- **[AWS IoT Device SDK für Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - MQTT-Client-Dokumentation
- **[AWS IoT Device SDK GitHub](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Quellcode und Beispiele

#### Protokoll und Standards
- **[MQTT-Protokollspezifikation](https://mqtt.org/)** - Offizielle MQTT-Dokumentation
- **[X.509-Zertifikatsstandard](https://tools.ietf.org/html/rfc5280)** - Zertifikatsformat-Spezifikation

## 🤝 Mitwirken

Dies ist ein Bildungsprojekt. Beiträge, die die Lernerfahrung verbessern, sind willkommen:

- **Fehlerbehebungen** für Skriptprobleme
- **Übersetzungsverbesserungen** für bessere Lokalisierung
- **Dokumentationsverbesserungen** für mehr Klarheit
- **Zusätzliche Lernszenarien**, die zum Grundniveau passen

## 📄 Lizenz

Dieses Projekt ist unter der MIT-0-Lizenz lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.

## 🏷️ Tags

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`
