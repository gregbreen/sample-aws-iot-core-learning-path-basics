# Guida alla Risoluzione dei Problemi

Questo documento fornisce una guida completa alla risoluzione dei problemi per il progetto di apprendimento Amazon Web Services (AWS) AWS IoT Core - Fondamenti.

## Indice

- [Problemi Comuni](#problemi-comuni)
  - [Credenziali AWS](#credenziali-aws)
  - [Problemi con l'Ambiente Virtuale](#problemi-con-lambiente-virtuale)
  - [Problemi con le Dipendenze](#problemi-con-le-dipendenze)
  - [Problemi di Permessi](#problemi-di-permessi)
  - [Problemi con i Certificati](#problemi-con-i-certificati)
- [Problemi di Connessione MQTT](#problemi-di-connessione-mqtt)
  - [Problemi MQTT Basati su Certificati](#problemi-mqtt-basati-su-certificati)
  - [Problemi MQTT WebSocket](#problemi-mqtt-websocket)
- [Problemi del Servizio AWS IoT Device Shadow](#problemi-del-servizio-aws-iot-device-shadow)
  - [Problemi di Connessione Shadow](#problemi-di-connessione-shadow)
  - [Problemi con i File di Stato Shadow](#problemi-con-i-file-di-stato-shadow)
- [Problemi del Rules Engine](#problemi-del-rules-engine)
  - [Problemi di Creazione Regole](#problemi-di-creazione-regole)
  - [Problemi di Test delle Regole](#problemi-di-test-delle-regole)
- [Problemi OpenSSL](#problemi-openssl)
  - [Problemi di Installazione](#problemi-di-installazione)
  - [Problemi di Generazione Certificati](#problemi-di-generazione-certificati)
- [Problemi di Rete e Connettività](#problemi-di-rete-e-connettività)
  - [Problemi di Firewall e Proxy](#problemi-di-firewall-e-proxy)
  - [Problemi di Risoluzione DNS](#problemi-di-risoluzione-dns)
- [Problemi di Prestazioni e Temporizzazione](#problemi-di-prestazioni-e-temporizzazione)
  - [Limitazione della Frequenza API](#limitazione-della-frequenza-api)
  - [Timeout di Connessione](#timeout-di-connessione)
- [Ottenere Aiuto Aggiuntivo](#ottenere-aiuto-aggiuntivo)
  - [Utilizzo della Modalità Debug](#utilizzo-della-modalità-debug)
  - [Verifica nella Console AWS IoT](#verifica-nella-console-aws-iot)
  - [Log Amazon CloudWatch](#log-amazon-cloudwatch)
  - [Passaggi di Risoluzione Comuni](#passaggi-di-risoluzione-comuni)
  - [Risorse di Supporto](#risorse-di-supporto)

## Problemi Comuni

### Credenziali AWS

#### Verifica che le Credenziali Siano Impostate
```bash
# Controlla se le credenziali sono configurate
aws sts get-caller-identity

# Controlla la regione corrente
echo $AWS_DEFAULT_REGION

# Elenca le variabili d'ambiente
env | grep AWS
```


#### Problemi Comuni con le Credenziali

**Problema: "Unable to locate credentials"**
```bash
# Soluzione 1: Imposta le variabili d'ambiente
export AWS_ACCESS_KEY_ID=<tua-chiave-accesso>
export AWS_SECRET_ACCESS_KEY=<tua-chiave-segreta>
export AWS_DEFAULT_REGION=us-east-1

# Soluzione 2: Usa la configurazione AWS CLI
aws configure

# Soluzione 3: Controlla la configurazione esistente
aws configure list
```

**Problema: "You must specify a region"**
```bash
# Imposta la regione predefinita
export AWS_DEFAULT_REGION=us-east-1

# Oppure specifica nella configurazione AWS CLI
aws configure set region us-east-1
```

**Problema: "The security token included in the request is invalid"**
- **Causa**: Credenziali temporanee scadute o token di sessione non corretto
- **Soluzione**: Aggiorna le tue credenziali o rimuovi il token di sessione scaduto
```bash
unset AWS_SESSION_TOKEN
# Poi imposta nuove credenziali
```

### Problemi con l'Ambiente Virtuale

#### Verifica l'Ambiente Virtuale
```bash
# Controlla se venv è attivo
which python
# Dovrebbe mostrare: /percorso/al/tuo/progetto/venv/bin/python

# Controlla la versione di Python
python --version
# Dovrebbe essere 3.7 o superiore

# Elenca i pacchetti installati
pip list
```

#### Problemi con l'Ambiente Virtuale

**Problema: Ambiente virtuale non attivato**
```bash
# Attiva l'ambiente virtuale
# Su macOS/Linux:
source venv/bin/activate

# Su Windows:
venv\Scripts\activate

# Verifica l'attivazione
which python
```

**Problema: Versione Python errata**
```bash
# Crea un nuovo venv con una versione specifica di Python
python3.9 -m venv venv
# oppure
python3 -m venv venv

# Attiva e verifica
source venv/bin/activate
python --version
```

**Problema: Installazione pacchetto fallisce**
```bash
# Aggiorna pip prima
python -m pip install --upgrade pip

# Installa i requisiti
pip install -r requirements.txt

# Se ancora fallisce, prova i pacchetti individuali
pip install boto3
pip install awsiotsdk
```

### Problemi con le Dipendenze

#### Reinstalla le Dipendenze
```bash
# Aggiorna tutti i pacchetti
pip install --upgrade -r requirements.txt

# Forza la reinstallazione
pip install --force-reinstall -r requirements.txt

# Pulisci la cache pip e reinstalla
pip cache purge
pip install -r requirements.txt
```

#### Errori Comuni con le Dipendenze

**Problema: "No module named 'boto3'"**
```bash
# Assicurati che venv sia attivato e installa
pip install boto3

# Verifica l'installazione
python -c "import boto3; print(boto3.__version__)"
```

**Problema: "No module named 'awsiot'"**
```bash
# Installa AWS IoT SDK
pip install awsiotsdk

# Verifica l'installazione
python -c "import awsiot; print('AWS IoT SDK installato')"
```

**Problema: Errori certificato SSL/TLS**
```bash
# Su macOS, aggiorna i certificati
/Applications/Python\ 3.x/Install\ Certificates.command

# Oppure installa il pacchetto certificati
pip install --upgrade certifi
```

### Problemi di Permessi

#### Permessi AWS Identity and Access Management (AWS IAM)

**Permessi Richiesti per gli Script di Apprendimento:**
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

**Permessi Minimi (se iot:* è troppo ampio):**
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

**Errori Comuni di Permessi:**

**Problema: "User is not authorized to perform: iot:CreateThing"**
- **Causa**: Permessi AWS IAM insufficienti
- **Soluzione**: Aggiungi permessi IoT al tuo utente/ruolo AWS IAM

**Problema: "Access Denied" durante la creazione di ruoli AWS IAM**
- **Causa**: Permessi AWS IAM mancanti per Rules Engine
- **Soluzione**: Aggiungi permessi AWS IAM o usa un ruolo esistente



### Problemi con i Certificati

#### Problemi con i File Certificato

**Problema: File certificato non trovati**
```bash
# Controlla se la directory certificati esiste
ls -la certificates/

# Controlla i certificati di un Thing specifico
ls -la certificates/Vehicle-VIN-001/

# Verifica i file certificato
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -text -noout
```

**Problema: Certificato non collegato al Thing**
```bash
# Esegui l'esploratore del registro per controllare
python iot_registry_explorer.py
# Seleziona l'opzione 5 (Describe Thing) e verifica che i certificati siano elencati
```

**Problema: Policy non collegata al certificato**
```bash
# Usa il gestore certificati per collegare la policy
python certificate_manager.py
# Seleziona l'opzione 3 (Attach Policy to Existing Certificate)
```

#### Problemi di Stato del Certificato

**Problema: Il certificato è INACTIVE**
```bash
# Usa il gestore certificati per attivare
python certificate_manager.py
# Seleziona l'opzione 5 (Enable/Disable Certificate)
```

**Problema: La validazione del certificato fallisce**
```bash
# Controlla il formato del certificato
head -5 certificates/Vehicle-VIN-001/cert-id.crt
# Dovrebbe iniziare con: -----BEGIN CERTIFICATE-----

# Valida il certificato
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -noout
# Nessun output significa valido, errore significa non valido
```

## Problemi di Connessione MQTT

### Problemi MQTT Basati su Certificati

#### Diagnostica della Connessione
```bash
# Usa la modalità debug per informazioni dettagliate sugli errori
python mqtt_client_explorer.py --debug

# Testa la connettività di base con OpenSSL
openssl s_client -connect <tuo-endpoint>:8883 \
  -cert certificates/Vehicle-VIN-001/<cert-id>.crt \
  -key certificates/Vehicle-VIN-001/<cert-id>.key
```

#### Errori MQTT Comuni

**Problema: "Connection timeout"**
- **Cause**: Connettività di rete, endpoint non corretto, firewall
- **Soluzioni**:
  ```bash
  # Controlla l'endpoint
  python iot_registry_explorer.py
  # Seleziona l'opzione 8 (Describe Endpoint)
  
  # Testa la connettività di rete
  ping tuo-iot-endpoint.amazonaws.com
  
  # Controlla il firewall (la porta 8883 deve essere aperta)
  telnet tuo-iot-endpoint.amazonaws.com 8883
  ```

**Problema: "Authentication failed"**
- **Cause**: Problemi con i certificati, problemi con le policy, Thing non collegato
- **Soluzioni**:
  1. Verifica che il certificato sia ACTIVE
  2. Controlla che il certificato sia collegato al Thing
  3. Verifica che la policy sia collegata al certificato
  4. Controlla che i permessi della policy includano iot:Connect

**Problema: "Subscription/Publish failed"**
- **Cause**: Restrizioni della policy, formato topic non valido
- **Soluzioni**:
  ```bash
  # Controlla i permessi della policy
  # La policy deve includere: iot:Subscribe, iot:Publish, iot:Receive
  
  # Verifica il formato del topic (nessuno spazio, caratteri validi)
  # Valido: device/sensor/temperature
  # Non valido: device sensor temperature
  ```

#### Comandi di Risoluzione Problemi MQTT

**All'interno del Client MQTT:**
```bash
📡 MQTT> debug                    # Mostra diagnostica della connessione
📡 MQTT> status                   # Visualizza info connessione
📡 MQTT> messages                 # Mostra cronologia messaggi
```

**Esempio di Output Debug:**
```
🔍 Diagnostica Connessione:
   Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   Porta: 8883
   ID Client: Vehicle-VIN-001-mqtt-12345678
   Certificato: certificates/Vehicle-VIN-001/abc123.crt
   Chiave Privata: certificates/Vehicle-VIN-001/abc123.key
   Stato Connessione: CONNECTED
   Keep Alive: 30 secondi
   Sessione Pulita: True
```

### Problemi MQTT WebSocket

#### Diagnostica WebSocket
```bash
# Verifica le credenziali AWS
aws sts get-caller-identity

# Controlla i permessi AWS IAM
aws iam get-user-policy --user-name <tuo-nome-utente> --policy-name <nome-policy>

# Usa la modalità debug
python mqtt_websocket_explorer.py --debug
```

#### Errori WebSocket Comuni

**Problema: "Credential validation failed"**
- **Causa**: Credenziali AWS mancanti o non valide
- **Soluzione**: Imposta credenziali AWS corrette
  ```bash
  export AWS_ACCESS_KEY_ID=<tua-chiave>
  export AWS_SECRET_ACCESS_KEY=<tuo-segreto>
  export AWS_DEFAULT_REGION=us-east-1
  ```

**Problema: "WebSocket connection failed"**
- **Cause**: Problemi di rete, impostazioni proxy, firewall
- **Soluzioni**:
  ```bash
  # Testa la connettività HTTPS
  curl -I https://tuo-endpoint.amazonaws.com
  
  # Controlla le impostazioni proxy
  echo $HTTP_PROXY
  echo $HTTPS_PROXY
  ```

**Problema: "SigV4 signing error"**
- **Causa**: Disallineamento dell'orologio, credenziali non valide
- **Soluzioni**:
  ```bash
  # Sincronizza l'orologio di sistema
  sudo ntpdate -s time.nist.gov  # Linux/macOS
  
  # Verifica che le credenziali non siano scadute
  aws sts get-caller-identity
  ```



### Problemi del Servizio AWS IoT Device Shadow

#### Problemi di Connessione Shadow

**Problema: Le operazioni shadow falliscono**
- **Cause**: Permessi shadow mancanti, problemi con i certificati
- **Soluzioni**:
  1. Verifica che la policy includa i permessi shadow:
     ```json
     {
       "Action": [
         "iot:GetThingShadow",
         "iot:UpdateThingShadow"
       ]
     }
     ```
  2. Controlla che il certificato sia collegato al Thing corretto
  3. Verifica che il nome del Thing corrisponda alle operazioni shadow

**Problema: Messaggi delta non ricevuti**
- **Cause**: Problemi di sottoscrizione, permessi topic
- **Soluzioni**:
  ```bash
  # Controlla le sottoscrizioni ai topic shadow
  🌟 Shadow> status
  
  # Verifica che la policy consenta le sottoscrizioni ai topic shadow
  # Topic: $aws/things/{thingName}/shadow/update/delta
  ```

#### Problemi con i File di Stato Shadow

**Problema: File di stato locale non trovato**
- **Causa**: Permessi di creazione file, problemi di percorso
- **Soluzione**:
  ```bash
  # Controlla i permessi della directory certificati
  ls -la certificates/
  
  # Crea il file di stato manualmente se necessario
  echo '{"temperature": 20.0, "status": "online"}' > certificates/Vehicle-VIN-001/device_state.json
  ```

**Problema: JSON non valido nel file di stato**
- **Causa**: Errori di modifica manuale
- **Soluzione**:
  ```bash
  # Valida il formato JSON
  python -m json.tool certificates/Vehicle-VIN-001/device_state.json
  
  # Correggi o ricrea il file
  ```

### Problemi del Rules Engine

#### Problemi di Creazione Regole

**Problema: La creazione del ruolo AWS IAM fallisce**
- **Cause**: Permessi AWS IAM insufficienti, ruolo già esistente
- **Soluzioni**:
  ```bash
  # Controlla se il ruolo esiste
  aws iam get-role --role-name IoTRulesEngineRole
  
  # Crea il ruolo manualmente se necessario
  aws iam create-role --role-name IoTRulesEngineRole --assume-role-policy-document file://trust-policy.json
  ```

**Problema: Errori di sintassi SQL**
- **Cause**: Formato SQL non valido, funzioni non supportate
- **Soluzioni**:
  - Usa clausole semplici SELECT, FROM, WHERE
  - Evita funzioni SQL complesse
  - Testa prima con regole di base

#### Problemi di Test delle Regole

**Problema: La regola non si attiva**
- **Cause**: Mancata corrispondenza topic, problemi clausola WHERE, regola disabilitata
- **Soluzioni**:
  1. Verifica che il pattern del topic corrisponda al topic pubblicato
  2. Controlla la logica della clausola WHERE
  3. Assicurati che la regola sia ENABLED
  4. Testa prima con una regola semplice

**Problema: Nessun output della regola ricevuto**
- **Cause**: Problemi di sottoscrizione, configurazione azione
- **Soluzioni**:
  ```bash
  # Controlla le azioni della regola
  python iot_rules_explorer.py
  # Seleziona l'opzione 2 (Describe Rule)
  
  # Verifica la sottoscrizione al topic di output
  # Sottoscrivi a: processed/* o alerts/*
  ```

## Problemi OpenSSL

### Problemi di Installazione

**macOS:**
```bash
# Installa tramite Homebrew
brew install openssl

# Aggiungi al PATH se necessario
export PATH="/usr/local/opt/openssl/bin:$PATH"
```

**Ubuntu/Debian:**
```bash
# Aggiorna l'elenco dei pacchetti e installa
sudo apt-get update
sudo apt-get install openssl

# Verifica l'installazione
openssl version
```

**Windows:**
```bash
# Scarica da: https://slproweb.com/products/Win32OpenSSL.html
# Oppure usa Windows Subsystem for Linux (WSL)

# In WSL:
sudo apt-get install openssl
```

### Problemi di Generazione Certificati

**Problema: Comando OpenSSL non trovato**
- **Soluzione**: Installa OpenSSL o aggiungi al PATH

**Problema: Permesso negato durante la creazione dei file certificato**
- **Soluzione**: Controlla i permessi della directory o esegui con privilegi appropriati

**Problema: Formato certificato non valido**
- **Soluzione**: Verifica la sintassi e i parametri del comando OpenSSL

## Problemi di Rete e Connettività

### Problemi di Firewall e Proxy

**Porte Richieste:**
- **MQTT su TLS**: 8883
- **WebSocket MQTT**: 443
- **HTTPS (chiamate API)**: 443

**Firewall Aziendale:**
```bash
# Testa la connettività delle porte
telnet tuo-iot-endpoint.amazonaws.com 8883
telnet tuo-iot-endpoint.amazonaws.com 443

# Controlla le impostazioni proxy
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

**Configurazione Proxy:**
```bash
# Imposta proxy per HTTPS
export HTTPS_PROXY=http://proxy.azienda.com:8080

# Bypassa proxy per endpoint AWS
export NO_PROXY=amazonaws.com,.amazonaws.com
```

### Problemi di Risoluzione DNS

**Problema: Impossibile risolvere l'endpoint IoT**
```bash
# Testa la risoluzione DNS
nslookup tuo-iot-endpoint.amazonaws.com

# Usa DNS alternativo
export AWS_IOT_ENDPOINT=$(dig +short tuo-iot-endpoint.amazonaws.com)
```

## Problemi di Prestazioni e Temporizzazione

### Limitazione della Frequenza API

**Problema: ThrottlingException**
- **Causa**: Troppe chiamate API troppo velocemente
- **Soluzione**: Aggiungi ritardi tra le operazioni o riduci la concorrenza

**Problema: Ritardi di coerenza eventuale**
- **Causa**: I servizi AWS necessitano di tempo per propagare le modifiche
- **Soluzione**: Aggiungi tempi di attesa dopo la creazione delle risorse

### Timeout di Connessione

**Problema: Timeout keep-alive MQTT**
- **Causa**: Instabilità di rete, lunghi periodi di inattività
- **Soluzioni**:
  - Riduci l'intervallo keep-alive
  - Implementa logica di riconnessione
  - Controlla la stabilità della rete



## Ottenere Aiuto Aggiuntivo

### Utilizzo della Modalità Debug

**Abilita la modalità debug per tutti gli script:**
```bash
python nome_script.py --debug
```

**La modalità debug fornisce:**
- Logging dettagliato delle richieste/risposte API
- Diagnostica della connessione
- Tracce dello stack degli errori
- Informazioni sui tempi

### Verifica nella Console AWS IoT

**Controlla le risorse nella Console AWS:**
1. **Thing**: AWS IoT Core → Gestisci → Thing
2. **Certificati**: AWS IoT Core → Proteggi → Certificati
3. **Policy**: AWS IoT Core → Proteggi → Policy
4. **Regole**: AWS IoT Core → Agisci → Regole

### Log Amazon CloudWatch

**Abilita il logging IoT per il debug in produzione:**
1. Vai a AWS IoT Core → Impostazioni
2. Abilita il logging con il livello di log appropriato
3. Controlla i Log Amazon CloudWatch per informazioni dettagliate sugli errori

### Passaggi di Risoluzione Comuni

**Quando tutto il resto fallisce:**
1. **Ricomincia da capo**: Esegui lo script di pulizia e ricomincia
2. **Controlla lo stato AWS**: Visita il Dashboard dello Stato dei Servizi AWS
3. **Verifica i limiti dell'account**: Controlla le quote dei servizi AWS
4. **Testa con configurazione minima**: Usa la configurazione più semplice possibile
5. **Confronta con esempi funzionanti**: Usa i dati di esempio forniti

### Risorse di Supporto

- **Documentazione AWS IoT**: https://docs.aws.amazon.com/iot/
- **Guida per Sviluppatori AWS IoT**: https://docs.aws.amazon.com/iot/latest/developerguide/
- **Supporto AWS**: https://aws.amazon.com/support/
- **Forum AWS**: https://forums.aws.amazon.com/forum.jspa?forumID=210
