# AWS IoT Core - Percorso di Apprendimento - Fondamenti

> 🌍 **Lingue Disponibili** | **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言** | **사용 가능한 언어**
> 
> - **Italiano** (Corrente) | [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | [한국어](README.ko.md) | [Deutsch](README.de.md)
> - **Documentazione**: [Italiano](docs/it/) | [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/) | [Deutsch](docs/de/)

Un toolkit Python completo per imparare i concetti base di Amazon Web Services (AWS) AWS IoT Core attraverso l'esplorazione pratica. Gli script interattivi dimostrano la gestione dei dispositivi, la sicurezza, le operazioni API e la comunicazione MQTT con spiegazioni dettagliate.

## 🚀 Avvio Rapido - Percorso di Apprendimento Completo

```bash
# 1. Clona e configura
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Configura l'ambiente
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Configura le credenziali AWS
export AWS_ACCESS_KEY_ID=<tua-chiave>
export AWS_SECRET_ACCESS_KEY=<tuo-segreto>
export AWS_DEFAULT_REGION=<tua-regione (es. us-east-1)>

# 4. Opzionale: Imposta la preferenza della lingua
export AWS_IOT_LANG=it  # 'en' per Inglese, 'es' per Spagnolo, 'ja' per Giapponese, 'zh-CN' per Cinese, 'pt-BR' per Portoghese, 'ko' per Coreano, 'de' per Tedesco

# 5. Sequenza di apprendimento completa
python scripts/setup_sample_data.py          # Crea risorse IoT di esempio
python scripts/iot_registry_explorer.py      # Esplora le API AWS IoT
python scripts/certificate_manager.py        # Impara la sicurezza IoT
python scripts/mqtt_client_explorer.py       # Comunicazione MQTT in tempo reale
python scripts/device_shadow_explorer.py     # Sincronizzazione dello stato del dispositivo
python scripts/iot_rules_explorer.py         # Routing e elaborazione dei messaggi
python scripts/cleanup_sample_data.py        # Pulisci le risorse (IMPORTANTE!)
```

**⚠️ Avviso sui Costi**: Questo crea risorse AWS reali (~$0.17 totale). Esegui la pulizia quando hai finito!

## Pubblico di Riferimento

**Pubblico Principale:** Sviluppatori cloud, architetti di soluzioni, ingegneri DevOps nuovi ad AWS IoT Core

**Prerequisiti:** Conoscenza base di AWS, fondamenti di Python, utilizzo della riga di comando

**Livello di Apprendimento:** Livello associato con approccio pratico


## 🔧 Costruito con gli SDK AWS

Questo progetto sfrutta gli SDK ufficiali AWS per fornire esperienze autentiche di AWS IoT Core:

### **Boto3 - AWS SDK per Python**
- **Scopo**: Alimenta tutte le operazioni del Registro AWS IoT, la gestione dei certificati e le interazioni con il Rules Engine
- **Versione**: `>=1.26.0`
- **Documentazione**: [Documentazione Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **API AWS IoT Core**: [Client IoT Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **AWS IoT Device SDK per Python**
- **Scopo**: Abilita la comunicazione MQTT autentica con AWS IoT Core utilizzando certificati X.509
- **Versione**: `>=1.11.0`
- **Documentazione**: [AWS IoT Device SDK per Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Perché Questi SDK Sono Importanti:**
- **Pronti per la Produzione**: Gli stessi SDK utilizzati nelle applicazioni IoT reali
- **Sicurezza**: Supporto integrato per le best practice di sicurezza AWS IoT
- **Affidabilità**: Librerie ufficiali mantenute da AWS con gestione completa degli errori
- **Valore Didattico**: Sperimenta i pattern di sviluppo autentici di AWS IoT

## Indice

- 🚀 [Avvio Rapido](#-avvio-rapido---percorso-di-apprendimento-completo)
- ⚙️ [Installazione e Configurazione](#️-installazione-e-configurazione)
- 📚 [Script di Apprendimento](#-script-di-apprendimento)
- 🧹 [Pulizia delle Risorse](#-pulizia-delle-risorse)
- 🛠️ [Risoluzione dei Problemi](#-risoluzione-dei-problemi)
- 📖 [Documentazione Avanzata](#-documentazione-avanzata)

## ⚙️ Installazione e Configurazione

### Prerequisiti
- Python 3.10+
- Account AWS con permessi IoT
- Accesso al terminale/riga di comando
- OpenSSL (per le funzionalità dei certificati)

**⚠️ NOTA IMPORTANTE SULLA SICUREZZA**: Usa un account AWS dedicato allo sviluppo/apprendimento. Non eseguire questi script in account contenenti risorse IoT di produzione. Sebbene lo script di pulizia abbia molteplici meccanismi di sicurezza, la best practice è utilizzare ambienti isolati per le attività di apprendimento.

### Informazioni sui Costi

**Questo progetto crea risorse AWS reali che comporteranno addebiti (~$0.17 totale).**

| Servizio | Utilizzo | Costo Stimato (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100 messaggi, 20 dispositivi | $0.10 |
| **Servizio AWS IoT Device Shadow** | ~30 operazioni shadow | $0.04 |
| **IoT Rules Engine** | ~50 esecuzioni di regole | $0.01 |
| **Archiviazione Certificati** | 20 certificati per 1 giorno | $0.01 |
| **Amazon CloudWatch Logs** | Logging di base | $0.01 |
| **Totale Stimato** | **Sessione di apprendimento completa** | **~$0.17** |

**⚠️ Importante**: Esegui sempre lo script di pulizia quando hai finito per evitare addebiti continui.



### Installazione Dettagliata

**1. Clona il Repository:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Installa OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Scarica dal [sito web OpenSSL](https://www.openssl.org/)

**3. Ambiente Virtuale (Consigliato):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Configurazione della Lingua (Opzionale):**
```bash
# Imposta la preferenza della lingua per tutti gli script
export AWS_IOT_LANG=it     # Italiano
export AWS_IOT_LANG=en     # Inglese (predefinito)
export AWS_IOT_LANG=es     # Spagnolo
export AWS_IOT_LANG=ja     # Giapponese
export AWS_IOT_LANG=zh-CN  # Cinese
export AWS_IOT_LANG=pt-BR  # Portoghese
export AWS_IOT_LANG=ko     # Coreano
export AWS_IOT_LANG=de     # Tedesco

# Alternativa: Gli script chiederanno la lingua se non impostata
```

**Lingue Supportate:**
- **Inglese** (`en`, `english`) - Predefinito
- **Spagnolo** (`es`, `spanish`, `español`) - Traduzione completa disponibile
- **Giapponese** (`ja`, `japanese`, `日本語`, `jp`) - Traduzione completa disponibile
- **Cinese** (`zh-CN`, `chinese`, `中文`, `zh`) - Traduzione completa disponibile
- **Portoghese** (`pt-BR`, `portuguese`, `português`, `pt`) - Traduzione completa disponibile
- **Coreano** (`ko`, `korean`, `한국어`, `kr`) - Traduzione completa disponibile
- **Tedesco** (`de`, `german`, `deutsch`) - Traduzione completa disponibile
- **Italiano** (`it`, `italian`, `italiano`) - Traduzione completa disponibile

## 🌍 Supporto Multilingue

Tutti gli script di apprendimento supportano interfacce in Inglese, Spagnolo, Giapponese, Cinese, Portoghese, Coreano, Tedesco e Italiano. La lingua influisce su:

**✅ Cosa Viene Tradotto:**
- Messaggi di benvenuto e contenuti educativi
- Opzioni del menu e prompt utente
- Momenti di apprendimento e spiegazioni
- Messaggi di errore e conferme
- Indicatori di progresso e messaggi di stato

**❌ Cosa Rimane nella Lingua Originale:**
- Risposte delle API AWS (dati JSON)
- Nomi e valori dei parametri tecnici
- Metodi HTTP ed endpoint
- Informazioni di debug e log
- Nomi e identificatori delle risorse AWS

**Opzioni di Utilizzo:**

**Opzione 1: Variabile d'Ambiente (Consigliata)**
```bash
# Imposta la preferenza della lingua per tutti gli script
export AWS_IOT_LANG=it     # Italiano
export AWS_IOT_LANG=en     # Inglese
export AWS_IOT_LANG=es     # Spagnolo
export AWS_IOT_LANG=ja     # Giapponese
export AWS_IOT_LANG=zh-CN  # Cinese
export AWS_IOT_LANG=pt-BR  # Portoghese
export AWS_IOT_LANG=ko     # Coreano
export AWS_IOT_LANG=de     # Tedesco

# Esegui qualsiasi script - la lingua verrà applicata automaticamente
python scripts/iot_registry_explorer.py
```

**Opzione 2: Selezione Interattiva**
```bash
# Esegui senza variabile d'ambiente - lo script chiederà la lingua
python scripts/setup_sample_data.py

# Esempio di output:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma / 언어 선택 / Sprachauswahl / Selezione della Lingua
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# 6. 한국어 (Korean)
# 7. Deutsch (German)
# 8. Italiano (Italian)
# Select language (1-8): 8
```

**Script Supportati:**
- ✅ `setup_sample_data.py` - Creazione dati di esempio
- ✅ `iot_registry_explorer.py` - Esplorazione API
- ✅ `certificate_manager.py` - Gestione certificati
- ✅ `mqtt_client_explorer.py` - Comunicazione MQTT
- ✅ `mqtt_websocket_explorer.py` - MQTT WebSocket
- ✅ `device_shadow_explorer.py` - Operazioni del servizio AWS IoT Device Shadow
- ✅ `iot_rules_explorer.py` - Esplorazione Rules Engine
- ✅ `cleanup_sample_data.py` - Pulizia risorse



## 📚 Script di Apprendimento

**Percorso di Apprendimento Consigliato:**

### 1. 📊 Configurazione Dati di Esempio
**File**: `scripts/setup_sample_data.py`
**Scopo**: Crea risorse IoT realistiche per l'apprendimento pratico con tagging automatico
**Crea**: 20 Thing, 3 Thing Type, 4 Thing Group, Regole IoT (con tag workshop)

**Caratteristiche Principali:**
- **Tagging Automatico**: Tutte le risorse sono taggate per un'identificazione sicura durante la pulizia
- **Prefissi Personalizzati**: Supporto per prefissi personalizzati dei nomi thing
- **Multilingue**: Supporto completo per l'internazionalizzazione

**Esempi di Utilizzo:**
```bash
# Configurazione base con prefisso predefinito (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Configurazione con prefisso personalizzato
python scripts/setup_sample_data.py --things-prefix "MioDispositivo-"

# Configurazione con selezione della lingua
export AWS_IOT_LANG=it
python scripts/setup_sample_data.py
```

**Tagging delle Risorse:**
Tutte le risorse create ricevono questi tag per un'identificazione sicura:
- `workshop-resource: true` - Contrassegna come creato dal workshop
- `created-by: setup-script` - Identifica lo script che ha creato la risorsa
- `workshop-name: iot-core-basics` - Raggruppa per nome workshop

Questi tag consentono allo script di pulizia di identificare e rimuovere in modo sicuro solo le risorse del workshop, proteggendo la tua infrastruttura IoT di produzione.

### 2. 🔍 Esploratore API del Registro IoT
**File**: `scripts/iot_registry_explorer.py`
**Scopo**: Strumento interattivo per imparare le API del Registro AWS IoT
**Caratteristiche**: 8 API principali con spiegazioni dettagliate e chiamate API reali

### 3. 🔐 Gestore Certificati e Policy
**File**: `scripts/certificate_manager.py`
**Scopo**: Impara la sicurezza AWS IoT attraverso la gestione di certificati e policy
**Caratteristiche**: Creazione certificati, collegamento policy, registrazione certificati esterni

### 4. 📡 Comunicazione MQTT
**File**: 
- `scripts/mqtt_client_explorer.py` (Basato su certificati, consigliato)
- `scripts/mqtt_websocket_explorer.py` (Alternativa basata su WebSocket)

**Scopo**: Sperimenta la comunicazione IoT in tempo reale utilizzando il protocollo MQTT
**Caratteristiche**: Interfaccia a riga di comando interattiva, sottoscrizione topic, pubblicazione messaggi

### 5. 🌟 Esploratore del Servizio AWS IoT Device Shadow
**File**: `scripts/device_shadow_explorer.py`
**Scopo**: Impara la sincronizzazione dello stato del dispositivo con AWS IoT Device Shadow
**Caratteristiche**: Gestione interattiva shadow, aggiornamenti di stato, elaborazione delta

### 6. ⚙️ Esploratore IoT Rules Engine
**File**: `scripts/iot_rules_explorer.py`
**Scopo**: Impara il routing e l'elaborazione dei messaggi con IoT Rules Engine
**Caratteristiche**: Creazione regole, filtraggio SQL, configurazione automatica AWS IAM

### 7. 🧹 Pulizia Dati di Esempio
**File**: `scripts/cleanup_sample_data.py`
**Scopo**: Pulisci tutte le risorse di apprendimento per evitare addebiti
**Caratteristiche**: Pulizia sicura con gestione delle dipendenze

## 🧹 Pulizia delle Risorse

**⚠️ IMPORTANTE**: Esegui sempre la pulizia quando hai finito di imparare per evitare addebiti AWS continui.

### Utilizzo Base

```bash
# Pulizia standard - rimuove tutte le risorse del workshop
python scripts/cleanup_sample_data.py

# Anteprima di cosa verrà eliminato (primo passo consigliato)
python scripts/cleanup_sample_data.py --dry-run

# Pulizia con prefisso personalizzato
python scripts/cleanup_sample_data.py --things-prefix "MioDispositivo-"

# Abilita la modalità debug per il logging dettagliato delle API
python scripts/cleanup_sample_data.py --debug
```

### Parametri da Riga di Comando

| Parametro | Descrizione | Predefinito | Esempio |
|-----------|-------------|---------|---------|
| `--things-prefix` | Prefisso personalizzato per i nomi thing | `Vehicle-VIN-` | `--things-prefix "DispositivoTest-"` |
| `--dry-run` | Anteprima pulizia senza eliminare | `False` | `--dry-run` |
| `--debug` | Abilita logging dettagliato API | `False` | `--debug` |

### Come Funziona l'Identificazione delle Risorse

Lo script di pulizia utilizza un **sistema di identificazione duale** per identificare in modo sicuro le risorse del workshop:

**1. Identificazione Basata su Tag (Metodo Primario)**
- Le risorse create dagli script di configurazione sono automaticamente taggate con:
  - `workshop-resource: true` - Identifica le risorse create dal workshop
  - `created-by: setup-script` - Traccia quale script ha creato la risorsa
  - `workshop-name: iot-core-basics` - Raggruppa le risorse per workshop
- **Vantaggio**: Metodo più affidabile, funziona indipendentemente dalla denominazione

**2. Fallback Convenzione di Denominazione (Metodo Secondario)**
- Se i tag non sono presenti, lo script identifica le risorse tramite pattern di denominazione:
  - Thing: Corrispondono al pattern `--things-prefix` (predefinito: `Vehicle-VIN-`)
  - Thing Type: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Group: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - Regole IoT: Corrispondono ai pattern `*Rule`, `rule_*`, o `*_workshop_*`
- **Vantaggio**: Funziona con risorse create prima dell'implementazione del tagging



### Modalità Dry-Run (Primo Passo Consigliato)

**Visualizza sempre in anteprima le operazioni di pulizia prima di eseguirle:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**La modalità dry-run:**
- ✅ Identifica tutte le risorse del workshop che verrebbero eliminate
- ✅ Visualizza un elenco dettagliato delle risorse per tipo
- ✅ Mostra l'ordine di eliminazione (rispetta le dipendenze)
- ✅ Genera un report di riepilogo
- ❌ **NON elimina alcuna risorsa**

**Esempio di output dry-run:**
```
🔍 MODALITÀ DRY RUN - Nessuna risorsa verrà eliminata

Risorse Identificate:
  Thing: 20 risorse
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Certificati: 20 risorse
  Thing Group: 4 risorse
  Thing Type: 3 risorse
  Regole IoT: 1 risorsa

Totale: 48 risorse verrebbero eliminate
```

### Utilizzo Prefisso Personalizzato

Se hai creato risorse con un prefisso personalizzato durante la configurazione, usa lo stesso prefisso per la pulizia:

```bash
# Configurazione con prefisso personalizzato
python scripts/setup_sample_data.py --things-prefix "MioDispositivo-"

# Pulizia con prefisso corrispondente
python scripts/cleanup_sample_data.py --things-prefix "MioDispositivo-"
```

**Importante**: Il prefisso deve corrispondere esattamente tra configurazione e pulizia affinché l'identificazione basata sulla denominazione funzioni correttamente.

### Cosa Viene Pulito

**Risorse Eliminate (in ordine di dipendenza):**
1. ✅ Thing Shadow (dati di stato del dispositivo)
2. ✅ Certificati (prima scollegati dai thing)
3. ✅ Thing (dispositivi IoT)
4. ✅ Regole IoT (regole di routing messaggi)
5. ✅ Thing Group (collezioni di dispositivi)
6. ✅ Thing Type (template di dispositivi)
7. ✅ Policy (policy di sicurezza)
8. ✅ File certificati locali (dalla directory `certs/`)

**Risorse Protette:**
- ❌ Risorse IoT di produzione (senza tag workshop)
- ❌ Risorse con pattern di denominazione diversi
- ❌ Certificati e policy non associati ai thing del workshop
- ❌ Risorse create al di fuori degli script del workshop

### Eliminazione Consapevole delle Dipendenze

Lo script di pulizia gestisce automaticamente le dipendenze delle risorse AWS IoT:

**Ordine di Eliminazione:**
```
Thing Shadow → Certificati → Thing → Regole IoT → Thing Group → Thing Type → Policy
```

**Perché questo ordine è importante:**
- I Thing Shadow devono essere eliminati prima dei certificati
- I certificati devono essere scollegati prima che i thing possano essere eliminati
- I thing devono essere rimossi dai gruppi prima che i gruppi possano essere eliminati
- Le policy devono essere scollegate prima dell'eliminazione

**Lo script gestisce questo automaticamente** - non devi preoccuparti dei conflitti di dipendenza.

### Comprendere il Report di Riepilogo

Dopo il completamento della pulizia, vedrai un report di riepilogo:

```
📊 Riepilogo Pulizia

Tipo Risorsa    | Identificate | Eliminate | Fallite
----------------|--------------|-----------|--------
Thing           |           20 |        20 |       0
Certificati     |           20 |        20 |       0
Thing Group     |            4 |         4 |       0
Thing Type      |            3 |         3 |       0
Regole IoT      |            1 |         1 |       0
Policy          |           20 |        20 |       0
----------------|--------------|-----------|--------
Totale          |           68 |        68 |       0

✅ Pulizia completata con successo!
```

**Campi del Report:**
- **Identificate**: Risorse trovate che corrispondono ai criteri del workshop
- **Eliminate**: Risorse rimosse con successo
- **Fallite**: Risorse che non è stato possibile eliminare (con dettagli dell'errore)

### Risoluzione dei Problemi di Pulizia

**Problema: "Nessuna risorsa trovata"**
- **Causa**: Le risorse potrebbero non avere tag workshop o non corrispondono al prefisso
- **Soluzione**: 
  - Verifica se hai usato un prefisso personalizzato durante la configurazione
  - Usa `--things-prefix` con il prefisso corretto
  - Verifica che le risorse esistano nella Console AWS

**Problema: Errori "Permesso negato"**
- **Causa**: Le credenziali AWS mancano dei permessi IoT necessari
- **Soluzione**: Assicurati che il tuo utente/ruolo IAM abbia permessi di accesso completo IoT

**Problema: Errori "Conflitto di dipendenza"**
- **Causa**: Le risorse hanno dipendenze che non sono state gestite
- **Soluzione**: Lo script dovrebbe gestire questo automaticamente. Se persiste, esegui con `--debug` per vedere i dettagli

**Problema: Alcune risorse non eliminate**
- **Causa**: Le risorse potrebbero essere in uso o avere dipendenze esterne
- **Soluzione**: 
  - Controlla il report di riepilogo per le risorse fallite
  - Usa la Console AWS per ispezionare ed eliminare manualmente le risorse rimanenti
  - Esegui nuovamente la pulizia dopo aver risolto le dipendenze

### Best Practice

1. **Usa sempre dry-run prima**: Visualizza in anteprima cosa verrà eliminato prima di eseguire
2. **Abbina i prefissi**: Usa lo stesso `--things-prefix` per configurazione e pulizia
3. **Rivedi il riepilogo**: Controlla il report per assicurarti che tutte le risorse siano state eliminate
4. **Esegui la pulizia tempestivamente**: Non lasciare le risorse del workshop in esecuzione per evitare addebiti
5. **Mantieni le credenziali sicure**: Non committare mai le credenziali AWS nel controllo versione



## 🛠️ Risoluzione dei Problemi

### Problemi Comuni

**Credenziali AWS:**
```bash
# Imposta le credenziali
export AWS_ACCESS_KEY_ID=<tua-chiave>
export AWS_SECRET_ACCESS_KEY=<tuo-segreto>
export AWS_DEFAULT_REGION=us-east-1
```

**Dipendenze Python:**
```bash
pip install -r requirements.txt
```

**Problemi OpenSSL:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### Modalità Debug

Tutti gli script supportano la modalità debug per il logging dettagliato delle API:
```bash
python scripts/<nome_script>.py --debug
```

## ❓ Domande Frequenti (FAQ)

### Domande Generali

**D: Quali risorse verranno eliminate dallo script di pulizia?**
R: Lo script di pulizia identifica ed elimina le risorse create dagli script di configurazione del workshop. Questo include Thing, Certificati, Thing Group, Thing Type, Regole IoT e Policy che hanno tag workshop o corrispondono ai pattern di denominazione. Le risorse di produzione sono protette.

**D: Come posso visualizzare in anteprima la pulizia senza eliminare nulla?**
R: Usa il flag `--dry-run`:
```bash
python scripts/cleanup_sample_data.py --dry-run
```
Questo mostra esattamente cosa verrebbe eliminato senza apportare modifiche.

**D: Posso usare un prefisso personalizzato per i nomi thing?**
R: Sì! Usa il parametro `--things-prefix` sia nella configurazione che nella pulizia:
```bash
# Configurazione
python scripts/setup_sample_data.py --things-prefix "MioDispositivo-"

# Pulizia
python scripts/cleanup_sample_data.py --things-prefix "MioDispositivo-"
```

**D: Cosa succede se non ho tag sulle mie risorse?**
R: Lo script di pulizia ha un meccanismo di fallback. Se i tag non sono presenti, utilizza le convenzioni di denominazione per identificare le risorse del workshop. Le risorse che corrispondono al pattern del prefisso thing (predefinito: `Vehicle-VIN-`) o ai nomi standard del workshop verranno identificate.

**D: Come cambio la lingua?**
R: Imposta la variabile d'ambiente `AWS_IOT_LANG`:
```bash
export AWS_IOT_LANG=it  # Italiano
export AWS_IOT_LANG=es  # Spagnolo
export AWS_IOT_LANG=ja  # Giapponese
export AWS_IOT_LANG=zh-CN  # Cinese
export AWS_IOT_LANG=pt-BR  # Portoghese
export AWS_IOT_LANG=ko  # Coreano
export AWS_IOT_LANG=de  # Tedesco
```
Oppure esegui lo script senza impostarla - ti verrà chiesto di selezionare una lingua in modo interattivo.

**D: Cosa succede se la pulizia fallisce a metà?**
R: Lo script di pulizia è progettato per essere idempotente - puoi eseguirlo più volte in sicurezza. Se la pulizia fallisce:
1. Controlla il report di riepilogo per vedere quali risorse sono fallite
2. Esegui nuovamente lo script - salterà le risorse già eliminate
3. Usa la modalità `--debug` per vedere messaggi di errore dettagliati
4. Elimina manualmente le risorse rimanenti tramite la Console AWS se necessario

**D: Come verifico che le risorse siano state eliminate?**
R: Controlla il report di riepilogo alla fine della pulizia. Puoi anche verificare nella Console AWS IoT:
- Vai a AWS IoT Core → Gestisci → Thing
- Verifica che i thing del workshop (Vehicle-VIN-*) siano spariti
- Verifica che Thing Group, Thing Type e Certificati siano rimossi

### Domande Tecniche

**D: Perché lo script di pulizia elimina le risorse in un ordine specifico?**
R: Le risorse AWS IoT hanno dipendenze. Ad esempio, non puoi eliminare un Thing che ha ancora certificati collegati. Lo script segue questo ordine:
1. Thing Shadow (nessuna dipendenza)
2. Certificati (devono essere scollegati dai thing)
3. Thing (devono essere rimossi dai gruppi)
4. Regole IoT (nessuna dipendenza dai thing)
5. Thing Group (devono essere vuoti)
6. Thing Type (non devono essere in uso)
7. Policy (devono essere scollegate)

**D: Qual è la differenza tra identificazione basata su tag e basata su denominazione?**
R: 
- **Basata su tag** (primaria): Utilizza i tag delle risorse AWS (`workshop-resource: true`). Più affidabile, funziona indipendentemente dalla denominazione.
- **Basata su denominazione** (fallback): Utilizza pattern di denominazione (es. `Vehicle-VIN-*`). Funziona con risorse più vecchie create prima dell'implementazione del tagging.

Lo script prova prima quella basata su tag, poi ricorre ai pattern di denominazione se i tag non sono presenti.

**D: Posso usare questo in un account AWS di produzione?**
R: Sebbene lo script di pulizia abbia molteplici meccanismi di sicurezza (tag, pattern di denominazione, modalità dry-run), **consigliamo vivamente di utilizzare un account AWS dedicato allo sviluppo/apprendimento**. Questo segue le best practice AWS per l'isolamento degli ambienti.

**D: Cosa succede se interrompo la pulizia con Ctrl+C?**
R: Lo script gestisce le interruzioni in modo elegante. Le risorse eliminate prima dell'interruzione rimangono eliminate. Esegui semplicemente lo script di pulizia di nuovo per continuare - salterà le risorse già eliminate e completerà le eliminazioni rimanenti.

**D: Quanto costa eseguire questi script di apprendimento?**
R: Circa $0.17 USD per una sessione di apprendimento completa. Vedi la sezione [Informazioni sui Costi](#informazioni-sui-costi) per una ripartizione dettagliata. Esegui sempre la pulizia quando hai finito per evitare addebiti continui.



## 📖 Documentazione Avanzata

### Documentazione Dettagliata
- **[Guida Dettagliata degli Script](docs/it/DETAILED_SCRIPTS.md)** - Documentazione approfondita degli script
- **[Esempi Completi](docs/it/EXAMPLES.md)** - Flussi di lavoro completi e output di esempio
- **[Guida alla Risoluzione dei Problemi](docs/it/TROUBLESHOOTING.md)** - Problemi comuni e soluzioni

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

### Deutsche Dokumentation
- **[Detaillierte Skript-Anleitung](docs/de/DETAILED_SCRIPTS.md)** - Ausführliche Skript-Dokumentation
- **[Vollständige Beispiele](docs/de/EXAMPLES.md)** - Vollständige Workflows und Beispielausgaben
- **[Fehlerbehebungsanleitung](docs/de/TROUBLESHOOTING.md)** - Häufige Probleme und Lösungen

### Risorse di Apprendimento

#### Documentazione AWS IoT Core
- **[Guida per Sviluppatori AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[Riferimento API AWS IoT Core](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### SDK AWS Utilizzati in Questo Progetto
- **[Documentazione Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Documentazione completa dell'SDK Python
- **[Riferimento Client IoT Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - Metodi API specifici per IoT
- **[AWS IoT Device SDK per Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - Documentazione client MQTT
- **[GitHub AWS IoT Device SDK](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Codice sorgente ed esempi

#### Protocolli e Standard
- **[Specifica Protocollo MQTT](https://mqtt.org/)** - Documentazione ufficiale MQTT
- **[Standard Certificato X.509](https://tools.ietf.org/html/rfc5280)** - Specifica formato certificato

## 🤝 Contribuire

Questo è un progetto educativo. I contributi che migliorano l'esperienza di apprendimento sono benvenuti:

- **Correzioni di bug** per problemi degli script
- **Miglioramenti delle traduzioni** per una migliore localizzazione
- **Miglioramenti della documentazione** per maggiore chiarezza
- **Scenari di apprendimento aggiuntivi** che si adattano al livello base

## 📄 Licenza

Questo progetto è concesso in licenza con la Licenza MIT-0 - vedi il file [LICENSE](LICENSE) per i dettagli.

## 🏷️ Tag

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`
