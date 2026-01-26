# Fehlerbehebungsanleitung

Dieses Dokument bietet umfassende Anleitungen zur Fehlerbehebung für das Amazon Web Services (AWS) AWS IoT Core - Basics Lernprojekt.

## Inhaltsverzeichnis

- [Häufige Probleme](#häufige-probleme)
  - [AWS-Zugangsdaten](#aws-zugangsdaten)
  - [Probleme mit virtueller Umgebung](#probleme-mit-virtueller-umgebung)
  - [Abhängigkeitsprobleme](#abhängigkeitsprobleme)
  - [Berechtigungsprobleme](#berechtigungsprobleme)
  - [Zertifikatsprobleme](#zertifikatsprobleme)
- [MQTT-Verbindungsprobleme](#mqtt-verbindungsprobleme)
  - [Zertifikatsbasierte MQTT-Probleme](#zertifikatsbasierte-mqtt-probleme)
  - [WebSocket MQTT-Probleme](#websocket-mqtt-probleme)
- [AWS IoT Device Shadow service-Probleme](#device-shadow-probleme)
  - [Shadow-Verbindungsprobleme](#shadow-verbindungsprobleme)
  - [Shadow-Zustandsdatei-Probleme](#shadow-zustandsdatei-probleme)
- [Rules Engine-Probleme](#rules-engine-probleme)
  - [Regelerstellungsprobleme](#regelerstellungsprobleme)
  - [Regeltestprobleme](#regeltestprobleme)
- [OpenSSL-Probleme](#openssl-probleme)
  - [Installationsprobleme](#installationsprobleme)
  - [Zertifikatsgenerierungsprobleme](#zertifikatsgenerierungsprobleme)
- [Netzwerk- und Konnektivitätsprobleme](#netzwerk--und-konnektivitätsprobleme)
  - [Firewall- und Proxy-Probleme](#firewall--und-proxy-probleme)
  - [DNS-Auflösungsprobleme](#dns-auflösungsprobleme)
- [Leistungs- und Timing-Probleme](#leistungs--und-timing-probleme)
  - [API-Ratenbegrenzung](#api-ratenbegrenzung)
  - [Verbindungs-Timeouts](#verbindungs-timeouts)
- [Zusätzliche Hilfe erhalten](#zusätzliche-hilfe-erhalten)
  - [Debug-Modus-Nutzung](#debug-modus-nutzung)
  - [AWS IoT Console-Überprüfung](#aws-iot-console-überprüfung)
  - [Amazon CloudWatch Logs](#cloudwatch-logs)
  - [Allgemeine Lösungsschritte](#allgemeine-lösungsschritte)
  - [Support-Ressourcen](#support-ressourcen)

## Häufige Probleme

### AWS-Zugangsdaten

#### Zugangsdaten überprüfen
```bash
# Prüfen, ob Zugangsdaten konfiguriert sind
aws sts get-caller-identity

# Aktuelle Region prüfen
echo $AWS_DEFAULT_REGION

# Umgebungsvariablen auflisten
env | grep AWS
```

#### Häufige Zugangsdatenprobleme

**Problem: "Unable to locate credentials"**
```bash
# Lösung 1: Umgebungsvariablen setzen
export AWS_ACCESS_KEY_ID=<dein-access-key>
export AWS_SECRET_ACCESS_KEY=<dein-secret-key>
export AWS_DEFAULT_REGION=us-east-1

# Lösung 2: AWS CLI-Konfiguration verwenden
aws configure

# Lösung 3: Bestehende Konfiguration prüfen
aws configure list
```

**Problem: "You must specify a region"**
```bash
# Standard-Region setzen
export AWS_DEFAULT_REGION=us-east-1

# Oder in AWS CLI-Konfiguration angeben
aws configure set region us-east-1
```

**Problem: "The security token included in the request is invalid"**
- **Ursache**: Abgelaufene temporäre Zugangsdaten oder falsches Session-Token
- **Lösung**: Aktualisiere deine Zugangsdaten oder entferne abgelaufenes Session-Token
```bash
unset AWS_SESSION_TOKEN
# Dann neue Zugangsdaten setzen
```


### Probleme mit virtueller Umgebung

#### Virtuelle Umgebung überprüfen
```bash
# Prüfen, ob venv aktiv ist
which python
# Sollte zeigen: /pfad/zu/deinem/projekt/venv/bin/python

# Python-Version prüfen
python --version
# Sollte 3.7 oder höher sein

# Installierte Pakete auflisten
pip list
```

#### Probleme mit virtueller Umgebung

**Problem: Virtuelle Umgebung nicht aktiviert**
```bash
# Virtuelle Umgebung aktivieren
# Auf macOS/Linux:
source venv/bin/activate

# Auf Windows:
venv\Scripts\activate

# Aktivierung überprüfen
which python
```

**Problem: Falsche Python-Version**
```bash
# Neue venv mit spezifischer Python-Version erstellen
python3.9 -m venv venv
# oder
python3 -m venv venv

# Aktivieren und überprüfen
source venv/bin/activate
python --version
```

**Problem: Paketinstallation schlägt fehl**
```bash
# Pip zuerst aktualisieren
python -m pip install --upgrade pip

# Requirements installieren
pip install -r requirements.txt

# Wenn es immer noch fehlschlägt, einzelne Pakete versuchen
pip install boto3
pip install awsiotsdk
```

### Abhängigkeitsprobleme

#### Abhängigkeiten neu installieren
```bash
# Alle Pakete aktualisieren
pip install --upgrade -r requirements.txt

# Neuinstallation erzwingen
pip install --force-reinstall -r requirements.txt

# Pip-Cache leeren und neu installieren
pip cache purge
pip install -r requirements.txt
```

#### Häufige Abhängigkeitsfehler

**Problem: "No module named 'boto3'"**
```bash
# Sicherstellen, dass venv aktiviert ist und installieren
pip install boto3

# Installation überprüfen
python -c "import boto3; print(boto3.__version__)"
```

**Problem: "No module named 'awsiot'"**
```bash
# AWS IoT SDK installieren
pip install awsiotsdk

# Installation überprüfen
python -c "import awsiot; print('AWS IoT SDK installed')"
```

**Problem: SSL/TLS-Zertifikatsfehler**
```bash
# Auf macOS Zertifikate aktualisieren
/Applications/Python\ 3.x/Install\ Certificates.command

# Oder Zertifikatspaket installieren
pip install --upgrade certifi
```

### Berechtigungsprobleme

#### AWS Identity and Access Management (AWS IAM)-Berechtigungen

**Erforderliche Berechtigungen für Lernskripte:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:*",
        "iam:CreateRole",
        "iam:CreatePolicy",
        "iam:AttachRolePolicy",
        "iam:GetRole",
        "iam:PassRole"
      ],
      "Resource": "*"
    }
  ]
}
```

**Minimale Berechtigungen (wenn iot:* zu weit gefasst ist):**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:CreateThing",
        "iot:ListThings",
        "iot:DescribeThing",
        "iot:DeleteThing",
        "iot:CreateThingType",
        "iot:ListThingTypes",
        "iot:DescribeThingType",
        "iot:DeleteThingType",
        "iot:CreateThingGroup",
        "iot:ListThingGroups",
        "iot:DescribeThingGroup",
        "iot:DeleteThingGroup",
        "iot:CreateKeysAndCertificate",
        "iot:ListCertificates",
        "iot:DescribeCertificate",
        "iot:UpdateCertificate",
        "iot:DeleteCertificate",
        "iot:CreatePolicy",
        "iot:ListPolicies",
        "iot:GetPolicy",
        "iot:AttachPolicy",
        "iot:DetachPolicy",
        "iot:AttachThingPrincipal",
        "iot:DetachThingPrincipal",
        "iot:ListThingPrincipals",
        "iot:ListPrincipalThings",
        "iot:Connect",
        "iot:Publish",
        "iot:Subscribe",
        "iot:Receive",
        "iot:GetThingShadow",
        "iot:UpdateThingShadow",
        "iot:CreateTopicRule",
        "iot:ListTopicRules",
        "iot:GetTopicRule",
        "iot:DeleteTopicRule"
      ],
      "Resource": "*"
    }
  ]
}
```

**Häufige Berechtigungsfehler:**

**Problem: "User is not authorized to perform: iot:CreateThing"**
- **Ursache**: Unzureichende AWS IAM-Berechtigungen
- **Lösung**: IoT-Berechtigungen zu deinem AWS IAM-Benutzer/Rolle hinzufügen

**Problem: "Access Denied" beim Erstellen von AWS IAM-Rollen**
- **Ursache**: Fehlende AWS IAM-Berechtigungen für Rules Engine
- **Lösung**: AWS IAM-Berechtigungen hinzufügen oder bestehende Rolle verwenden


### Zertifikatsprobleme

#### Zertifikatsdatei-Probleme

**Problem: Zertifikatsdateien nicht gefunden**
```bash
# Prüfen, ob Zertifikatsverzeichnis existiert
ls -la certificates/

# Spezifische Thing-Zertifikate prüfen
ls -la certificates/Vehicle-VIN-001/

# Zertifikatsdateien überprüfen
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -text -noout
```

**Problem: Zertifikat nicht an Thing angehängt**
```bash
# Registry Explorer ausführen, um zu prüfen
python iot_registry_explorer.py
# Option 5 (Describe Thing) wählen und überprüfen, ob Zertifikate aufgelistet sind
```

**Problem: Policy nicht an Zertifikat angehängt**
```bash
# Certificate Manager verwenden, um Policy anzuhängen
python certificate_manager.py
# Option 3 (Attach Policy to Existing Certificate) wählen
```

#### Zertifikatsstatus-Probleme

**Problem: Zertifikat ist INACTIVE**
```bash
# Certificate Manager verwenden, um zu aktivieren
python certificate_manager.py
# Option 5 (Enable/Disable Certificate) wählen
```

**Problem: Zertifikatsvalidierung schlägt fehl**
```bash
# Zertifikatsformat prüfen
head -5 certificates/Vehicle-VIN-001/cert-id.crt
# Sollte beginnen mit: -----BEGIN CERTIFICATE-----

# Zertifikat validieren
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -noout
# Keine Ausgabe bedeutet gültig, Fehler bedeutet ungültig
```

## MQTT-Verbindungsprobleme

### Zertifikatsbasierte MQTT-Probleme

#### Verbindungsdiagnose
```bash
# Debug-Modus für detaillierte Fehlerinformationen verwenden
python mqtt_client_explorer.py --debug

# Grundlegende Konnektivität mit OpenSSL testen
openssl s_client -connect <dein-endpoint>:8883 \
  -cert certificates/Vehicle-VIN-001/<cert-id>.crt \
  -key certificates/Vehicle-VIN-001/<cert-id>.key
```

#### Häufige MQTT-Fehler

**Problem: "Connection timeout"**
- **Ursachen**: Netzwerkkonnektivität, falscher Endpoint, Firewall
- **Lösungen**:
  ```bash
  # Endpoint prüfen
  python iot_registry_explorer.py
  # Option 8 (Describe Endpoint) wählen
  
  # Netzwerkkonnektivität testen
  ping dein-iot-endpoint.amazonaws.com
  
  # Firewall prüfen (Port 8883 muss offen sein)
  telnet dein-iot-endpoint.amazonaws.com 8883
  ```

**Problem: "Authentication failed"**
- **Ursachen**: Zertifikatsprobleme, Policy-Probleme, Thing nicht angehängt
- **Lösungen**:
  1. Überprüfen, dass Zertifikat ACTIVE ist
  2. Prüfen, dass Zertifikat an Thing angehängt ist
  3. Überprüfen, dass Policy an Zertifikat angehängt ist
  4. Prüfen, dass Policy-Berechtigungen iot:Connect enthalten

**Problem: "Subscription/Publish failed"**
- **Ursachen**: Policy-Einschränkungen, ungültiges Topic-Format
- **Lösungen**:
  ```bash
  # Policy-Berechtigungen prüfen
  # Policy muss enthalten: iot:Subscribe, iot:Publish, iot:Receive
  
  # Topic-Format überprüfen (keine Leerzeichen, gültige Zeichen)
  # Gültig: device/sensor/temperature
  # Ungültig: device sensor temperature
  ```

#### MQTT-Fehlerbehebungsbefehle

**Innerhalb des MQTT-Clients:**
```bash
📡 MQTT> debug                    # Verbindungsdiagnose anzeigen
📡 MQTT> status                   # Verbindungsinfo anzeigen
📡 MQTT> messages                 # Nachrichtenverlauf anzeigen
```

**Debug-Ausgabe-Beispiel:**
```
🔍 Verbindungsdiagnose:
   Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   Port: 8883
   Client ID: Vehicle-VIN-001-mqtt-12345678
   Zertifikat: certificates/Vehicle-VIN-001/abc123.crt
   Private Key: certificates/Vehicle-VIN-001/abc123.key
   Verbindungsstatus: CONNECTED
   Keep Alive: 30 Sekunden
   Clean Session: True
```

### WebSocket MQTT-Probleme

#### WebSocket-Diagnose
```bash
# AWS-Zugangsdaten überprüfen
aws sts get-caller-identity

# AWS IAM-Berechtigungen prüfen
aws iam get-user-policy --user-name <dein-benutzername> --policy-name <policy-name>

# Debug-Modus verwenden
python mqtt_websocket_explorer.py --debug
```

#### Häufige WebSocket-Fehler

**Problem: "Credential validation failed"**
- **Ursache**: Fehlende oder ungültige AWS-Zugangsdaten
- **Lösung**: Richtige AWS-Zugangsdaten setzen
  ```bash
  export AWS_ACCESS_KEY_ID=<dein-key>
  export AWS_SECRET_ACCESS_KEY=<dein-secret>
  export AWS_DEFAULT_REGION=us-east-1
  ```

**Problem: "WebSocket connection failed"**
- **Ursachen**: Netzwerkprobleme, Proxy-Einstellungen, Firewall
- **Lösungen**:
  ```bash
  # HTTPS-Konnektivität testen
  curl -I https://dein-endpoint.amazonaws.com
  
  # Proxy-Einstellungen prüfen
  echo $HTTP_PROXY
  echo $HTTPS_PROXY
  ```

**Problem: "SigV4 signing error"**
- **Ursache**: Zeitabweichung, ungültige Zugangsdaten
- **Lösungen**:
  ```bash
  # Systemuhr synchronisieren
  sudo ntpdate -s time.nist.gov  # Linux/macOS
  
  # Überprüfen, dass Zugangsdaten nicht abgelaufen sind
  aws sts get-caller-identity
  ```


### AWS IoT Device Shadow service-Probleme

#### Shadow-Verbindungsprobleme

**Problem: Shadow-Operationen schlagen fehl**
- **Ursachen**: Fehlende Shadow-Berechtigungen, Zertifikatsprobleme
- **Lösungen**:
  1. Überprüfen, dass Policy Shadow-Berechtigungen enthält:
     ```json
     {
       "Action": [
         "iot:GetThingShadow",
         "iot:UpdateThingShadow"
       ]
     }
     ```
  2. Prüfen, dass Zertifikat an korrektes Thing angehängt ist
  3. Überprüfen, dass Thing-Name mit Shadow-Operationen übereinstimmt

**Problem: Delta-Nachrichten werden nicht empfangen**
- **Ursachen**: Abonnementprobleme, Topic-Berechtigungen
- **Lösungen**:
  ```bash
  # Shadow-Topic-Abonnements prüfen
  🌟 Shadow> status
  
  # Überprüfen, dass Policy Shadow-Topic-Abonnements erlaubt
  # Topics: $aws/things/{thingName}/shadow/update/delta
  ```

#### Shadow-Zustandsdatei-Probleme

**Problem: Lokale Zustandsdatei nicht gefunden**
- **Ursache**: Dateierstellungsberechtigungen, Pfadprobleme
- **Lösung**:
  ```bash
  # Berechtigungen des Zertifikatsverzeichnisses prüfen
  ls -la certificates/
  
  # Zustandsdatei bei Bedarf manuell erstellen
  echo '{"temperature": 20.0, "status": "online"}' > certificates/Vehicle-VIN-001/device_state.json
  ```

**Problem: Ungültiges JSON in Zustandsdatei**
- **Ursache**: Manuelle Bearbeitungsfehler
- **Lösung**:
  ```bash
  # JSON-Format validieren
  python -m json.tool certificates/Vehicle-VIN-001/device_state.json
  
  # Datei korrigieren oder neu erstellen
  ```

### Rules Engine-Probleme

#### Regelerstellungsprobleme

**Problem: AWS IAM-Rollenerstellung schlägt fehl**
- **Ursachen**: Unzureichende AWS IAM-Berechtigungen, Rolle existiert bereits
- **Lösungen**:
  ```bash
  # Prüfen, ob Rolle existiert
  aws iam get-role --role-name IoTRulesEngineRole
  
  # Rolle bei Bedarf manuell erstellen
  aws iam create-role --role-name IoTRulesEngineRole --assume-role-policy-document file://trust-policy.json
  ```

**Problem: SQL-Syntaxfehler**
- **Ursachen**: Ungültiges SQL-Format, nicht unterstützte Funktionen
- **Lösungen**:
  - Einfache SELECT, FROM, WHERE-Klauseln verwenden
  - Komplexe SQL-Funktionen vermeiden
  - Zuerst mit einfachen Regeln testen

#### Regeltestprobleme

**Problem: Regel wird nicht ausgelöst**
- **Ursachen**: Topic-Nichtübereinstimmung, WHERE-Klausel-Probleme, Regel deaktiviert
- **Lösungen**:
  1. Überprüfen, dass Topic-Muster mit veröffentlichtem Topic übereinstimmt
  2. WHERE-Klausel-Logik prüfen
  3. Sicherstellen, dass Regel ENABLED ist
  4. Zuerst mit einfacher Regel testen

**Problem: Keine Regelausgabe empfangen**
- **Ursachen**: Abonnementprobleme, Aktionskonfiguration
- **Lösungen**:
  ```bash
  # Regelaktionen prüfen
  python iot_rules_explorer.py
  # Option 2 (Describe Rule) wählen
  
  # Abonnement auf Ausgabe-Topic überprüfen
  # Abonnieren auf: processed/* oder alerts/*
  ```

## OpenSSL-Probleme

### Installationsprobleme

**macOS:**
```bash
# Über Homebrew installieren
brew install openssl

# Bei Bedarf zu PATH hinzufügen
export PATH="/usr/local/opt/openssl/bin:$PATH"
```

**Ubuntu/Debian:**
```bash
# Paketliste aktualisieren und installieren
sudo apt-get update
sudo apt-get install openssl

# Installation überprüfen
openssl version
```

**Windows:**
```bash
# Download von: https://slproweb.com/products/Win32OpenSSL.html
# Oder Windows Subsystem for Linux (WSL) verwenden

# In WSL:
sudo apt-get install openssl
```

### Zertifikatsgenerierungsprobleme

**Problem: OpenSSL-Befehl nicht gefunden**
- **Lösung**: OpenSSL installieren oder zu PATH hinzufügen

**Problem: Berechtigung verweigert beim Erstellen von Zertifikatsdateien**
- **Lösung**: Verzeichnisberechtigungen prüfen oder mit entsprechenden Rechten ausführen

**Problem: Ungültiges Zertifikatsformat**
- **Lösung**: OpenSSL-Befehlssyntax und -parameter überprüfen

## Netzwerk- und Konnektivitätsprobleme

### Firewall- und Proxy-Probleme

**Erforderliche Ports:**
- **MQTT über TLS**: 8883
- **WebSocket MQTT**: 443
- **HTTPS (API-Aufrufe)**: 443

**Unternehmens-Firewall:**
```bash
# Port-Konnektivität testen
telnet dein-iot-endpoint.amazonaws.com 8883
telnet dein-iot-endpoint.amazonaws.com 443

# Proxy-Einstellungen prüfen
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

**Proxy-Konfiguration:**
```bash
# Proxy für HTTPS setzen
export HTTPS_PROXY=http://proxy.firma.com:8080

# Proxy für AWS-Endpoints umgehen
export NO_PROXY=amazonaws.com,.amazonaws.com
```

### DNS-Auflösungsprobleme

**Problem: IoT-Endpoint kann nicht aufgelöst werden**
```bash
# DNS-Auflösung testen
nslookup dein-iot-endpoint.amazonaws.com

# Alternatives DNS verwenden
export AWS_IOT_ENDPOINT=$(dig +short dein-iot-endpoint.amazonaws.com)
```

## Leistungs- und Timing-Probleme

### API-Ratenbegrenzung

**Problem: ThrottlingException**
- **Ursache**: Zu viele API-Aufrufe zu schnell
- **Lösung**: Verzögerungen zwischen Operationen hinzufügen oder Parallelität reduzieren

**Problem: Eventual Consistency-Verzögerungen**
- **Ursache**: AWS-Services benötigen Zeit, um Änderungen zu propagieren
- **Lösung**: Wartezeiten nach Ressourcenerstellung hinzufügen

### Verbindungs-Timeouts

**Problem: MQTT Keep-Alive-Timeouts**
- **Ursache**: Netzwerkinstabilität, lange Leerlaufzeiten
- **Lösungen**:
  - Keep-Alive-Intervall reduzieren
  - Verbindungswiederholungslogik implementieren
  - Netzwerkstabilität prüfen


## Zusätzliche Hilfe erhalten

### Debug-Modus-Nutzung

**Debug-Modus für alle Skripte aktivieren:**
```bash
python script_name.py --debug
```

**Debug-Modus bietet:**
- Detailliertes API-Request/Response-Logging
- Verbindungsdiagnose
- Fehler-Stack-Traces
- Timing-Informationen

### AWS IoT Console-Überprüfung

**Ressourcen in der AWS-Konsole prüfen:**
1. **Things**: AWS IoT Core → Verwalten → Things
2. **Zertifikate**: AWS IoT Core → Sichern → Zertifikate
3. **Policies**: AWS IoT Core → Sichern → Policies
4. **Rules**: AWS IoT Core → Handeln → Rules

### Amazon CloudWatch Logs

**IoT-Logging für Produktions-Debugging aktivieren:**
1. Gehe zu AWS IoT Core → Einstellungen
2. Logging mit entsprechendem Log-Level aktivieren
3. Amazon CloudWatch Logs für detaillierte Fehlerinformationen prüfen

### Allgemeine Lösungsschritte

**Wenn alles andere fehlschlägt:**
1. **Neu beginnen**: Aufräumskript ausführen und von vorne beginnen
2. **AWS-Status prüfen**: AWS Service Health Dashboard besuchen
3. **Kontolimits überprüfen**: AWS-Service-Quotas prüfen
4. **Mit minimalem Setup testen**: Einfachstmögliche Konfiguration verwenden
5. **Mit funktionierenden Beispielen vergleichen**: Bereitgestellte Beispieldaten verwenden

### Support-Ressourcen

- **AWS IoT-Dokumentation**: https://docs.aws.amazon.com/iot/
- **AWS IoT Developer Guide**: https://docs.aws.amazon.com/iot/latest/developerguide/
- **AWS Support**: https://aws.amazon.com/support/
- **AWS-Foren**: https://forums.aws.amazon.com/forum.jspa?forumID=210
