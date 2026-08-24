# AWS IoT Core - Parcours d'Apprentissage - Bases

> 🌍 **Langues Disponibles** | **Available Languages** | **Idiomas Disponibles** | **利用可能な言語** | **可用语言** | **사용 가능한 언어** | **Verfügbare Sprachen** | **Lingue Disponibili**
> 
> - **Français** (Actuel) | [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) 🇩🇪 | [Italiano](README.it.md) 🇮🇹
> - **Documentation** : [Français](docs/fr/) 🇫🇷 | [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/) | [한국어](docs/ko/) | [Deutsch](docs/de/) 🇩🇪 | [Italiano](docs/it/) 🇮🇹

Une boîte à outils Python complète pour apprendre les concepts de base d'AWS IoT Core à travers une exploration pratique. Des scripts interactifs démontrent la gestion des appareils, la sécurité, les opérations API et la communication MQTT avec des explications détaillées.

Ces mêmes scripts servent de base à l'[atelier AWS IoT Core - Bases](https://catalog.workshops.aws/workshops/a007780e-1086-421b-a7e3-b7ac63e37089), accessible au public. Au-delà de la boîte à outils elle-même, l'atelier est un excellent moyen de mieux comprendre les différents cas d'usage d'AWS IoT Core grâce à une expérience pratique et guidée.

## 🚀 Démarrage Rapide - Parcours d'Apprentissage Complet

```bash
# 1. Cloner et configurer
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Configurer l'environnement
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Configurer les identifiants AWS
export AWS_ACCESS_KEY_ID=<votre-clé>
export AWS_SECRET_ACCESS_KEY=<votre-secret>
export AWS_DEFAULT_REGION=<votre-région (ex. us-east-1)>

# 4. Optionnel : Définir la préférence de langue
export AWS_IOT_LANG=fr  # 'en' pour anglais, 'es' pour espagnol, 'ja' pour japonais, 'zh-CN' pour chinois, 'pt-BR' pour portugais, 'ko' pour coréen, 'de' pour allemand, 'it' pour italien

# 5. Séquence d'apprentissage complète
python scripts/setup_sample_data.py          # Créer des ressources IoT d'exemple
python scripts/iot_registry_explorer.py      # Explorer les API AWS IoT
python scripts/certificate_manager.py        # Apprendre la sécurité IoT
python scripts/mqtt_client_explorer.py       # Communication MQTT en temps réel
python scripts/device_shadow_explorer.py     # Synchronisation de l'état des appareils
python scripts/iot_rules_explorer.py         # Routage et traitement des messages
python scripts/cleanup_sample_data.py        # Nettoyer les ressources (IMPORTANT !)
```

**⚠️ Avertissement de Coût** : Cela crée de vraies ressources AWS (~0,17 $ au total). Lancez le nettoyage quand vous avez terminé !

## Public Cible

**Public Principal :** Développeurs cloud, architectes de solutions, ingénieurs DevOps débutants avec AWS IoT Core

**Prérequis :** Connaissances de base d'AWS, fondamentaux Python, utilisation de la ligne de commande

**Niveau d'Apprentissage :** Niveau associé avec approche pratique

## 🔧 Construit avec les SDK AWS

Ce projet utilise les SDK AWS officiels pour offrir des expériences authentiques avec AWS IoT Core :

### **Boto3 - SDK AWS pour Python**
- **Objectif** : Alimente toutes les opérations du registre AWS IoT, la gestion des certificats et les interactions avec le moteur de règles
- **Version** : `>=1.26.0`
- **Documentation** : [Documentation Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **API AWS IoT Core** : [Client IoT Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **SDK AWS IoT Device pour Python**
- **Objectif** : Permet une communication MQTT authentique avec AWS IoT Core en utilisant des certificats X.509
- **Version** : `>=1.11.0`
- **Documentation** : [SDK AWS IoT Device pour Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub** : [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Pourquoi Ces SDK Sont Importants :**
- **Prêts pour la Production** : Mêmes SDK utilisés dans les vraies applications IoT
- **Sécurité** : Support intégré des meilleures pratiques de sécurité AWS IoT
- **Fiabilité** : Bibliothèques officielles maintenues par AWS avec gestion complète des erreurs
- **Valeur d'Apprentissage** : Expérience des modèles de développement AWS IoT authentiques


## Table des Matières

- 🚀 [Démarrage Rapide](#-démarrage-rapide---parcours-dapprentissage-complet)
- ⚙️ [Installation et Configuration](#️-installation-et-configuration)
- 📚 [Scripts d'Apprentissage](#-scripts-dapprentissage)
- 🧹 [Nettoyage des Ressources](#-nettoyage-des-ressources)
- 🛠️ [Dépannage](#-dépannage)
- 📖 [Documentation Avancée](#-documentation-avancée)

## ⚙️ Installation et Configuration

### Prérequis
- Python 3.10+
- Compte AWS avec permissions IoT
- Accès terminal/ligne de commande
- OpenSSL (pour les fonctionnalités de certificat)

**⚠️ NOTE DE SÉCURITÉ IMPORTANTE** : Utilisez un compte AWS dédié au développement/apprentissage. N'exécutez pas ces scripts dans des comptes contenant des ressources IoT de production. Bien que le script de nettoyage dispose de plusieurs mécanismes de sécurité, la meilleure pratique consiste à utiliser des environnements isolés pour les activités d'apprentissage.

### Informations sur les Coûts

**Ce projet crée de vraies ressources AWS qui entraîneront des frais (~0,17 $ au total).**

| Service | Utilisation | Coût Estimé (USD) |
|---------|-------------|-------------------|
| **AWS IoT Core** | ~100 messages, 20 appareils | 0,10 $ |
| **Service AWS IoT Device Shadow** | ~30 opérations shadow | 0,04 $ |
| **Moteur de Règles IoT** | ~50 exécutions de règles | 0,01 $ |
| **Stockage de Certificats** | 20 certificats pendant 1 jour | 0,01 $ |
| **Amazon CloudWatch Logs** | Journalisation de base | 0,01 $ |
| **Total Estimé** | **Session d'apprentissage complète** | **~0,17 $** |

**⚠️ Important** : Lancez toujours le script de nettoyage quand vous avez terminé pour éviter des frais continus.

### Installation Détaillée

**1. Cloner le Dépôt :**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Installer OpenSSL :**
- **macOS :** `brew install openssl`
- **Ubuntu/Debian :** `sudo apt-get install openssl`
- **Windows :** Télécharger depuis le [site web OpenSSL](https://www.openssl.org/)

**3. Environnement Virtuel (Recommandé) :**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Configuration de la Langue (Optionnel) :**
```bash
# Définir la préférence de langue pour tous les scripts
export AWS_IOT_LANG=fr     # Français
export AWS_IOT_LANG=en     # Anglais
export AWS_IOT_LANG=es     # Espagnol
export AWS_IOT_LANG=ja     # Japonais
export AWS_IOT_LANG=zh-CN  # Chinois
export AWS_IOT_LANG=pt-BR  # Portugais
export AWS_IOT_LANG=ko     # Coréen
export AWS_IOT_LANG=de     # Allemand
export AWS_IOT_LANG=it     # Italien

# Alternative : Les scripts vous demanderont la langue si elle n'est pas définie
```

**Langues Supportées :**
- **Anglais** (`en`, `english`) - Par défaut
- **Espagnol** (`es`, `spanish`, `español`) - Traduction complète disponible
- **Japonais** (`ja`, `japanese`, `日本語`, `jp`) - Traduction complète disponible
- **Chinois** (`zh-CN`, `chinese`, `中文`, `zh`) - Traduction complète disponible
- **Portugais** (`pt-BR`, `portuguese`, `português`, `pt`) - Traduction complète disponible
- **Coréen** (`ko`, `korean`, `한국어`, `kr`) - Traduction complète disponible
- **Allemand** (`de`, `german`, `deutsch`) - Traduction complète disponible
- **Italien** (`it`, `italian`, `italiano`) - Traduction complète disponible
- **Français** (`fr`, `french`, `français`) - Traduction complète disponible


## 🌍 Support Multi-Langues

Tous les scripts d'apprentissage supportent les interfaces en anglais, espagnol, japonais, chinois, portugais, coréen, allemand, italien et français. La langue affecte :

**✅ Ce Qui Est Traduit :**
- Messages de bienvenue et contenu éducatif
- Options de menu et invites utilisateur
- Moments d'apprentissage et explications
- Messages d'erreur et confirmations
- Indicateurs de progression et messages de statut

**❌ Ce Qui Reste dans la Langue Originale :**
- Réponses de l'API AWS (données JSON)
- Noms de paramètres techniques et valeurs
- Méthodes HTTP et points de terminaison
- Informations de débogage et journaux
- Noms et identifiants de ressources AWS

**Options d'Utilisation :**

**Option 1 : Variable d'Environnement (Recommandé)**
```bash
# Définir la préférence de langue pour tous les scripts
export AWS_IOT_LANG=fr     # Français
export AWS_IOT_LANG=en     # Anglais
export AWS_IOT_LANG=es     # Espagnol
export AWS_IOT_LANG=ja     # Japonais
export AWS_IOT_LANG=zh-CN  # Chinois
export AWS_IOT_LANG=pt-BR  # Portugais
export AWS_IOT_LANG=ko     # Coréen
export AWS_IOT_LANG=de     # Allemand
export AWS_IOT_LANG=it     # Italien

# Exécuter n'importe quel script - la langue sera appliquée automatiquement
python scripts/iot_registry_explorer.py
```

**Option 2 : Sélection Interactive**
```bash
# Exécuter sans variable d'environnement - le script vous demandera la langue
python scripts/setup_sample_data.py

# Exemple de sortie :
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

**Scripts Supportés :**
- ✅ `setup_sample_data.py` - Création de données d'exemple
- ✅ `iot_registry_explorer.py` - Exploration des API
- ✅ `certificate_manager.py` - Gestion des certificats
- ✅ `mqtt_client_explorer.py` - Communication MQTT
- ✅ `mqtt_websocket_explorer.py` - MQTT WebSocket
- ✅ `device_shadow_explorer.py` - Opérations du service AWS IoT Device Shadow
- ✅ `iot_rules_explorer.py` - Exploration du moteur de règles
- ✅ `cleanup_sample_data.py` - Nettoyage des ressources

## 📚 Scripts d'Apprentissage

**Parcours d'Apprentissage Recommandé :**

### 1. 📊 Configuration des Données d'Exemple
**Fichier** : `scripts/setup_sample_data.py`
**Objectif** : Crée des ressources IoT réalistes pour l'apprentissage pratique avec marquage automatique
**Crée** : 20 Things, 3 Thing Types, 4 Thing Groups, Règles IoT (avec tags d'atelier)

**Fonctionnalités Clés :**
- **Marquage Automatique** : Toutes les ressources sont marquées pour une identification sûre lors du nettoyage
- **Préfixes Personnalisés** : Support des préfixes de noms de things personnalisés
- **Multi-Langue** : Support complet de l'internationalisation

**Exemples d'Utilisation :**
```bash
# Configuration de base avec préfixe par défaut (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Configuration avec préfixe personnalisé
python scripts/setup_sample_data.py --things-prefix "MonAppareil-"

# Configuration avec sélection de langue
export AWS_IOT_LANG=fr
python scripts/setup_sample_data.py
```

**Marquage des Ressources :**
Toutes les ressources créées reçoivent ces tags pour une identification sûre :
- `workshop-resource: true` - Marque comme créé par l'atelier
- `created-by: setup-script` - Identifie le script créateur
- `workshop-name: iot-core-basics` - Groupe par nom d'atelier

Ces tags permettent au script de nettoyage d'identifier et de supprimer en toute sécurité uniquement les ressources de l'atelier, protégeant votre infrastructure IoT de production.


### 2. 🔍 Explorateur d'API du Registre IoT
**Fichier** : `scripts/iot_registry_explorer.py`
**Objectif** : Outil interactif pour apprendre les API du registre AWS IoT
**Fonctionnalités** : 8 API principales avec explications détaillées et appels API réels

### 3. 🔐 Gestionnaire de Certificats et Politiques
**Fichier** : `scripts/certificate_manager.py`
**Objectif** : Apprendre la sécurité AWS IoT à travers la gestion des certificats et des politiques
**Fonctionnalités** : Création de certificats, attachement de politiques, enregistrement de certificats externes

### 4. 📡 Communication MQTT
**Fichiers** : 
- `scripts/mqtt_client_explorer.py` (Basé sur certificat, recommandé)
- `scripts/mqtt_websocket_explorer.py` (Alternative basée sur WebSocket)

**Objectif** : Expérimenter la communication IoT en temps réel en utilisant le protocole MQTT
**Fonctionnalités** : Interface en ligne de commande interactive, abonnement aux topics, publication de messages

### 5. 🌟 Explorateur du Service AWS IoT Device Shadow
**Fichier** : `scripts/device_shadow_explorer.py`
**Objectif** : Apprendre la synchronisation de l'état des appareils avec AWS IoT Device Shadow
**Fonctionnalités** : Gestion interactive des shadows, mises à jour d'état, traitement des deltas

### 6. ⚙️ Explorateur du Moteur de Règles IoT
**Fichier** : `scripts/iot_rules_explorer.py`
**Objectif** : Apprendre le routage et le traitement des messages avec le moteur de règles IoT
**Fonctionnalités** : Création de règles, filtrage SQL, configuration automatique AWS IAM

### 7. 🧹 Nettoyage des Données d'Exemple
**Fichier** : `scripts/cleanup_sample_data.py`
**Objectif** : Nettoyer toutes les ressources d'apprentissage pour éviter les frais
**Fonctionnalités** : Nettoyage sûr avec gestion des dépendances

## 🧹 Nettoyage des Ressources

**⚠️ IMPORTANT** : Lancez toujours le nettoyage quand vous avez terminé l'apprentissage pour éviter des frais AWS continus.

### Utilisation de Base

```bash
# Nettoyage standard - supprime toutes les ressources de l'atelier
python scripts/cleanup_sample_data.py

# Prévisualiser ce qui sera supprimé (première étape recommandée)
python scripts/cleanup_sample_data.py --dry-run

# Nettoyage avec préfixe personnalisé
python scripts/cleanup_sample_data.py --things-prefix "MonAppareil-"

# Activer le mode debug pour la journalisation détaillée des API
python scripts/cleanup_sample_data.py --debug
```

### Paramètres de Ligne de Commande

| Paramètre | Description | Par Défaut | Exemple |
|-----------|-------------|------------|---------|
| `--things-prefix` | Préfixe personnalisé pour les noms de things | `Vehicle-VIN-` | `--things-prefix "AppareilTest-"` |
| `--dry-run` | Prévisualiser le nettoyage sans supprimer | `False` | `--dry-run` |
| `--debug` | Activer la journalisation détaillée des API | `False` | `--debug` |

### Comment Fonctionne l'Identification des Ressources

Le script de nettoyage utilise un **système d'identification double** pour identifier en toute sécurité les ressources de l'atelier :

**1. Identification Basée sur les Tags (Méthode Principale)**
- Les ressources créées par les scripts de configuration sont automatiquement marquées avec :
  - `workshop-resource: true` - Identifie les ressources créées par l'atelier
  - `created-by: setup-script` - Suit quel script a créé la ressource
  - `workshop-name: iot-core-basics` - Groupe les ressources par atelier
- **Avantage** : Méthode la plus fiable, fonctionne indépendamment du nommage

**2. Repli sur la Convention de Nommage (Méthode Secondaire)**
- Si les tags ne sont pas présents, le script identifie les ressources par modèles de nommage :
  - Things : Correspondent au modèle `--things-prefix` (par défaut : `Vehicle-VIN-`)
  - Thing Types : `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups : `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - Règles IoT : Correspondent aux modèles `*Rule`, `rule_*`, ou `*_workshop_*`
- **Avantage** : Fonctionne avec les ressources créées avant l'implémentation du marquage


### Mode Dry-Run (Première Étape Recommandée)

**Prévisualisez toujours les opérations de nettoyage avant de les exécuter :**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Le mode dry-run va :**
- ✅ Identifier toutes les ressources de l'atelier qui seraient supprimées
- ✅ Afficher une liste détaillée des ressources par type
- ✅ Montrer l'ordre de suppression (respecte les dépendances)
- ✅ Générer un rapport récapitulatif
- ❌ **NE PAS supprimer de ressources**

**Exemple de sortie en mode dry-run :**
```
🔍 MODE DRY RUN - Aucune ressource ne sera supprimée

Ressources Identifiées :
  Things : 20 ressources
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Certificats : 20 ressources
  Thing Groups : 4 ressources
  Thing Types : 3 ressources
  Règles IoT : 1 ressource

Total : 48 ressources seraient supprimées
```

### Utilisation de Préfixe Personnalisé

Si vous avez créé des ressources avec un préfixe personnalisé lors de la configuration, utilisez le même préfixe pour le nettoyage :

```bash
# Configuration avec préfixe personnalisé
python scripts/setup_sample_data.py --things-prefix "MonAppareil-"

# Nettoyage avec préfixe correspondant
python scripts/cleanup_sample_data.py --things-prefix "MonAppareil-"
```

**Important** : Le préfixe doit correspondre exactement entre la configuration et le nettoyage pour que l'identification basée sur le nommage fonctionne correctement.

### Ce Qui Est Nettoyé

**Ressources Supprimées (dans l'ordre des dépendances) :**
1. ✅ Thing Shadows (données d'état des appareils)
2. ✅ Certificats (détachés des things d'abord)
3. ✅ Things (appareils IoT)
4. ✅ Règles IoT (règles de routage des messages)
5. ✅ Thing Groups (collections d'appareils)
6. ✅ Thing Types (modèles d'appareils)
7. ✅ Politiques (politiques de sécurité)
8. ✅ Fichiers de certificats locaux (du répertoire `certs/`)

**Ressources Protégées :**
- ❌ Ressources IoT de production (sans tags d'atelier)
- ❌ Ressources avec des modèles de nommage différents
- ❌ Certificats et politiques non associés aux things de l'atelier
- ❌ Ressources créées en dehors des scripts de l'atelier

### Suppression Consciente des Dépendances

Le script de nettoyage gère automatiquement les dépendances des ressources AWS IoT :

**Ordre de Suppression :**
```
Thing Shadows → Certificats → Things → Règles IoT → Thing Groups → Thing Types → Politiques
```

**Pourquoi cet ordre est important :**
- Les Thing Shadows doivent être supprimés avant les certificats
- Les certificats doivent être détachés avant que les things puissent être supprimés
- Les things doivent être retirés des groupes avant que les groupes puissent être supprimés
- Les politiques doivent être détachées avant la suppression

**Le script gère cela automatiquement** - vous n'avez pas à vous soucier des conflits de dépendances.

### Comprendre le Rapport Récapitulatif

Après la fin du nettoyage, vous verrez un rapport récapitulatif :

```
📊 Récapitulatif du Nettoyage

Type de Ressource | Identifiées | Supprimées | Échecs
------------------|-------------|------------|--------
Things            |          20 |         20 |      0
Certificats       |          20 |         20 |      0
Thing Groups      |           4 |          4 |      0
Thing Types       |           3 |          3 |      0
Règles IoT        |           1 |          1 |      0
Politiques        |          20 |         20 |      0
------------------|-------------|------------|--------
Total             |          68 |         68 |      0

✅ Nettoyage terminé avec succès !
```

**Champs du Rapport :**
- **Identifiées** : Ressources trouvées correspondant aux critères de l'atelier
- **Supprimées** : Ressources supprimées avec succès
- **Échecs** : Ressources qui n'ont pas pu être supprimées (avec détails d'erreur)


### Dépannage du Nettoyage

**Problème : "Aucune ressource trouvée"**
- **Cause** : Les ressources peuvent ne pas avoir de tags d'atelier ou ne correspondent pas au préfixe
- **Solution** : 
  - Vérifiez si vous avez utilisé un préfixe personnalisé lors de la configuration
  - Utilisez `--things-prefix` avec le préfixe correct
  - Vérifiez que les ressources existent dans la Console AWS

**Problème : Erreurs "Permission refusée"**
- **Cause** : Les identifiants AWS manquent des permissions IoT nécessaires
- **Solution** : Assurez-vous que votre utilisateur/rôle IAM a les permissions d'accès complet IoT

**Problème : Erreurs "Conflit de dépendance"**
- **Cause** : Les ressources ont des dépendances qui n'ont pas été gérées
- **Solution** : Le script devrait gérer cela automatiquement. Si cela persiste, exécutez avec `--debug` pour voir les détails

**Problème : Certaines ressources non supprimées**
- **Cause** : Les ressources peuvent être en cours d'utilisation ou avoir des dépendances externes
- **Solution** : 
  - Vérifiez le rapport récapitulatif pour les ressources échouées
  - Utilisez la Console AWS pour inspecter et supprimer manuellement les ressources restantes
  - Relancez le nettoyage après avoir résolu les dépendances

### Meilleures Pratiques

1. **Utilisez toujours dry-run d'abord** : Prévisualisez ce qui sera supprimé avant d'exécuter
2. **Faites correspondre les préfixes** : Utilisez le même `--things-prefix` pour la configuration et le nettoyage
3. **Examinez le récapitulatif** : Vérifiez le rapport pour vous assurer que toutes les ressources ont été supprimées
4. **Lancez le nettoyage rapidement** : Ne laissez pas les ressources de l'atelier en cours d'exécution pour éviter les frais
5. **Gardez les identifiants sécurisés** : Ne commitez jamais les identifiants AWS dans le contrôle de version

## 🛠️ Dépannage

### Problèmes Courants

**Identifiants AWS :**
```bash
# Définir les identifiants
export AWS_ACCESS_KEY_ID=<votre-clé>
export AWS_SECRET_ACCESS_KEY=<votre-secret>
export AWS_DEFAULT_REGION=us-east-1
```

**Dépendances Python :**
```bash
pip install -r requirements.txt
```

**Problèmes OpenSSL :**
- **macOS** : `brew install openssl`
- **Ubuntu** : `sudo apt-get install openssl`

### Mode Debug

Tous les scripts supportent le mode debug pour la journalisation détaillée des API :
```bash
python scripts/<nom_du_script>.py --debug
```

## ❓ Foire Aux Questions (FAQ)

### Questions Générales

**Q : Quelles ressources seront supprimées par le script de nettoyage ?**
R : Le script de nettoyage identifie et supprime les ressources créées par les scripts de configuration de l'atelier. Cela inclut les Things, Certificats, Thing Groups, Thing Types, Règles IoT et Politiques qui ont des tags d'atelier ou correspondent aux modèles de nommage. Les ressources de production sont protégées.

**Q : Comment puis-je prévisualiser le nettoyage sans rien supprimer ?**
R : Utilisez le flag `--dry-run` :
```bash
python scripts/cleanup_sample_data.py --dry-run
```
Cela montre exactement ce qui serait supprimé sans faire de changements.

**Q : Puis-je utiliser un préfixe personnalisé pour les noms de things ?**
R : Oui ! Utilisez le paramètre `--things-prefix` dans la configuration et le nettoyage :
```bash
# Configuration
python scripts/setup_sample_data.py --things-prefix "MonAppareil-"

# Nettoyage
python scripts/cleanup_sample_data.py --things-prefix "MonAppareil-"
```

**Q : Que faire si je n'ai pas de tags sur mes ressources ?**
R : Le script de nettoyage a un mécanisme de repli. Si les tags ne sont pas présents, il utilise les conventions de nommage pour identifier les ressources de l'atelier. Les ressources correspondant au modèle de préfixe de thing (par défaut : `Vehicle-VIN-`) ou aux noms d'atelier standard seront identifiées.


**Q : Comment changer la langue ?**
R : Définissez la variable d'environnement `AWS_IOT_LANG` :
```bash
export AWS_IOT_LANG=fr  # Français
export AWS_IOT_LANG=es  # Espagnol
export AWS_IOT_LANG=ja  # Japonais
export AWS_IOT_LANG=zh-CN  # Chinois
export AWS_IOT_LANG=pt-BR  # Portugais
export AWS_IOT_LANG=ko  # Coréen
```
Ou exécutez le script sans la définir - vous serez invité à sélectionner une langue de manière interactive.

**Q : Que faire si le nettoyage échoue à mi-chemin ?**
R : Le script de nettoyage est conçu pour être idempotent - vous pouvez l'exécuter plusieurs fois en toute sécurité. Si le nettoyage échoue :
1. Vérifiez le rapport récapitulatif pour voir quelles ressources ont échoué
2. Relancez le script - il ignorera les ressources déjà supprimées
3. Utilisez le mode `--debug` pour voir les messages d'erreur détaillés
4. Supprimez manuellement les ressources restantes via la Console AWS si nécessaire

**Q : Comment vérifier que les ressources ont été supprimées ?**
R : Vérifiez le rapport récapitulatif à la fin du nettoyage. Vous pouvez également vérifier dans la Console AWS IoT :
- Naviguez vers AWS IoT Core → Gérer → Things
- Vérifiez que les things de l'atelier (Vehicle-VIN-*) ont disparu
- Vérifiez que les Thing Groups, Thing Types et Certificats sont supprimés

### Questions Techniques

**Q : Pourquoi le script de nettoyage supprime-t-il les ressources dans un ordre spécifique ?**
R : Les ressources AWS IoT ont des dépendances. Par exemple, vous ne pouvez pas supprimer un Thing qui a encore des certificats attachés. Le script suit cet ordre :
1. Thing Shadows (pas de dépendances)
2. Certificats (doivent être détachés des things)
3. Things (doivent être retirés des groupes)
4. Règles IoT (pas de dépendances sur les things)
5. Thing Groups (doivent être vides)
6. Thing Types (ne doivent pas être utilisés)
7. Politiques (doivent être détachées)

**Q : Quelle est la différence entre l'identification basée sur les tags et celle basée sur le nommage ?**
R : 
- **Basée sur les tags** (principale) : Utilise les tags de ressources AWS (`workshop-resource: true`). Plus fiable, fonctionne indépendamment du nommage.
- **Basée sur le nommage** (repli) : Utilise les modèles de nommage (ex. `Vehicle-VIN-*`). Fonctionne avec les anciennes ressources créées avant l'implémentation du marquage.

Le script essaie d'abord l'identification basée sur les tags, puis se replie sur les modèles de nommage si les tags ne sont pas présents.

**Q : Puis-je utiliser cela dans un compte AWS de production ?**
R : Bien que le script de nettoyage dispose de plusieurs mécanismes de sécurité (tags, modèles de nommage, mode dry-run), **nous recommandons fortement d'utiliser un compte AWS dédié au développement/apprentissage**. Cela suit les meilleures pratiques AWS pour l'isolation des environnements.

**Q : Que se passe-t-il si j'interromps le nettoyage avec Ctrl+C ?**
R : Le script gère les interruptions avec élégance. Les ressources supprimées avant l'interruption restent supprimées. Relancez simplement le script de nettoyage pour continuer - il ignorera les ressources déjà supprimées et terminera les suppressions restantes.

**Q : Combien coûte l'exécution de ces scripts d'apprentissage ?**
R : Environ 0,17 $ USD pour une session d'apprentissage complète. Consultez la section [Informations sur les Coûts](#informations-sur-les-coûts) pour une répartition détaillée. Lancez toujours le nettoyage quand vous avez terminé pour éviter des frais continus.

## 📖 Documentation Avancée

### Documentation Détaillée
- **[Guide Détaillé des Scripts](docs/en/DETAILED_SCRIPTS.md)** - Documentation approfondie des scripts
- **[Exemples Complets](docs/en/EXAMPLES.md)** - Flux de travail complets et exemples de sortie
- **[Guide de Dépannage](docs/en/TROUBLESHOOTING.md)** - Problèmes courants et solutions

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

### Ressources d'Apprentissage

#### Documentation AWS IoT Core
- **[Guide du Développeur AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[Référence API AWS IoT Core](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### SDK AWS Utilisés dans Ce Projet
- **[Documentation Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Documentation complète du SDK Python
- **[Référence Client IoT Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - Méthodes API spécifiques à IoT
- **[SDK AWS IoT Device pour Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - Documentation du client MQTT
- **[GitHub SDK AWS IoT Device](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Code source et exemples

#### Protocole et Standards
- **[Spécification du Protocole MQTT](https://mqtt.org/)** - Documentation officielle MQTT
- **[Standard de Certificat X.509](https://tools.ietf.org/html/rfc5280)** - Spécification du format de certificat

## 🤝 Contribution

Ceci est un projet éducatif. Les contributions qui améliorent l'expérience d'apprentissage sont les bienvenues :

- **Corrections de bugs** pour les problèmes de scripts
- **Améliorations de traduction** pour une meilleure localisation
- **Améliorations de documentation** pour plus de clarté
- **Scénarios d'apprentissage supplémentaires** qui correspondent au niveau de base

## 📄 Licence

Ce projet est sous licence MIT-0 - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🏷️ Tags

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`
