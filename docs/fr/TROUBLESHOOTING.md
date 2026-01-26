# Guide de Dépannage

Ce document fournit des conseils de dépannage complets pour le projet d'apprentissage AWS IoT Core - Bases.

## Table des Matières

- [Problèmes Courants](#problèmes-courants)
  - [Identifiants AWS](#identifiants-aws)
  - [Problèmes d'Environnement Virtuel](#problèmes-denvironnement-virtuel)
  - [Problèmes de Dépendances](#problèmes-de-dépendances)
  - [Problèmes de Permissions](#problèmes-de-permissions)
  - [Problèmes de Certificats](#problèmes-de-certificats)
- [Problèmes de Connexion MQTT](#problèmes-de-connexion-mqtt)
  - [Problèmes MQTT Basés sur Certificat](#problèmes-mqtt-basés-sur-certificat)
  - [Problèmes MQTT WebSocket](#problèmes-mqtt-websocket)
- [Problèmes du Service AWS IoT Device Shadow](#problèmes-du-service-aws-iot-device-shadow)
  - [Problèmes de Connexion Shadow](#problèmes-de-connexion-shadow)
  - [Problèmes de Fichier d'État Shadow](#problèmes-de-fichier-détat-shadow)
- [Problèmes du Moteur de Règles](#problèmes-du-moteur-de-règles)
  - [Problèmes de Création de Règles](#problèmes-de-création-de-règles)
  - [Problèmes de Test de Règles](#problèmes-de-test-de-règles)
- [Problèmes OpenSSL](#problèmes-openssl)
  - [Problèmes d'Installation](#problèmes-dinstallation)
  - [Problèmes de Génération de Certificats](#problèmes-de-génération-de-certificats)
- [Problèmes de Réseau et de Connectivité](#problèmes-de-réseau-et-de-connectivité)
  - [Problèmes de Pare-feu et Proxy](#problèmes-de-pare-feu-et-proxy)
  - [Problèmes de Résolution DNS](#problèmes-de-résolution-dns)
- [Problèmes de Performance et de Timing](#problèmes-de-performance-et-de-timing)
  - [Limitation de Débit API](#limitation-de-débit-api)
  - [Délais de Connexion](#délais-de-connexion)
- [Obtenir de l'Aide Supplémentaire](#obtenir-de-laide-supplémentaire)
  - [Utilisation du Mode Debug](#utilisation-du-mode-debug)
  - [Vérification dans la Console AWS IoT](#vérification-dans-la-console-aws-iot)
  - [Journaux Amazon CloudWatch](#journaux-amazon-cloudwatch)
  - [Étapes de Résolution Courantes](#étapes-de-résolution-courantes)
  - [Ressources de Support](#ressources-de-support)

## Problèmes Courants

### Identifiants AWS

#### Vérifier que les Identifiants Sont Définis
```bash
# Vérifier si les identifiants sont configurés
aws sts get-caller-identity

# Vérifier la région actuelle
echo $AWS_DEFAULT_REGION

# Lister les variables d'environnement
env | grep AWS
```

#### Problèmes Courants d'Identifiants

**Problème : "Unable to locate credentials"**
```bash
# Solution 1 : Définir les variables d'environnement
export AWS_ACCESS_KEY_ID=<votre-clé-accès>
export AWS_SECRET_ACCESS_KEY=<votre-clé-secrète>
export AWS_DEFAULT_REGION=us-east-1

# Solution 2 : Utiliser la configuration AWS CLI
aws configure

# Solution 3 : Vérifier la configuration existante
aws configure list
```

**Problème : "You must specify a region"**
```bash
# Définir la région par défaut
export AWS_DEFAULT_REGION=us-east-1

# Ou spécifier dans la config AWS CLI
aws configure set region us-east-1
```


**Problème : "The security token included in the request is invalid"**
- **Cause** : Identifiants temporaires expirés ou jeton de session incorrect
- **Solution** : Rafraîchissez vos identifiants ou supprimez le jeton de session expiré
```bash
unset AWS_SESSION_TOKEN
# Puis définir de nouveaux identifiants
```

### Problèmes d'Environnement Virtuel

#### Vérifier l'Environnement Virtuel
```bash
# Vérifier si venv est actif
which python
# Devrait afficher : /chemin/vers/votre/projet/venv/bin/python

# Vérifier la version Python
python --version
# Devrait être 3.7 ou supérieur

# Lister les packages installés
pip list
```

#### Problèmes d'Environnement Virtuel

**Problème : Environnement virtuel non activé**
```bash
# Activer l'environnement virtuel
# Sur macOS/Linux :
source venv/bin/activate

# Sur Windows :
venv\Scripts\activate

# Vérifier l'activation
which python
```

**Problème : Mauvaise version de Python**
```bash
# Créer un nouveau venv avec une version Python spécifique
python3.9 -m venv venv
# ou
python3 -m venv venv

# Activer et vérifier
source venv/bin/activate
python --version
```

**Problème : L'installation de packages échoue**
```bash
# Mettre à jour pip d'abord
python -m pip install --upgrade pip

# Installer les requirements
pip install -r requirements.txt

# Si ça échoue toujours, essayer les packages individuellement
pip install boto3
pip install awsiotsdk
```

### Problèmes de Dépendances

#### Réinstaller les Dépendances
```bash
# Mettre à jour tous les packages
pip install --upgrade -r requirements.txt

# Forcer la réinstallation
pip install --force-reinstall -r requirements.txt

# Vider le cache pip et réinstaller
pip cache purge
pip install -r requirements.txt
```

#### Erreurs de Dépendances Courantes

**Problème : "No module named 'boto3'"**
```bash
# S'assurer que venv est activé et installer
pip install boto3

# Vérifier l'installation
python -c "import boto3; print(boto3.__version__)"
```

**Problème : "No module named 'awsiot'"**
```bash
# Installer le SDK AWS IoT
pip install awsiotsdk

# Vérifier l'installation
python -c "import awsiot; print('SDK AWS IoT installé')"
```

**Problème : Erreurs de certificat SSL/TLS**
```bash
# Sur macOS, mettre à jour les certificats
/Applications/Python\ 3.x/Install\ Certificates.command

# Ou installer le package certificates
pip install --upgrade certifi
```

### Problèmes de Permissions

#### Permissions AWS Identity and Access Management (AWS IAM)

**Permissions Requises pour les Scripts d'Apprentissage :**
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


**Permissions Minimales (si iot:* est trop large) :**
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

**Erreurs de Permission Courantes :**

**Problème : "User is not authorized to perform: iot:CreateThing"**
- **Cause** : Permissions AWS IAM insuffisantes
- **Solution** : Ajouter les permissions IoT à votre utilisateur/rôle AWS IAM

**Problème : "Access Denied" lors de la création de rôles AWS IAM**
- **Cause** : Permissions AWS IAM manquantes pour le moteur de règles
- **Solution** : Ajouter les permissions AWS IAM ou utiliser un rôle existant

### Problèmes de Certificats

#### Problèmes de Fichiers de Certificats

**Problème : Fichiers de certificats introuvables**
```bash
# Vérifier si le répertoire certificates existe
ls -la certificates/

# Vérifier les certificats d'un Thing spécifique
ls -la certificates/Vehicle-VIN-001/

# Vérifier les fichiers de certificats
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -text -noout
```

**Problème : Certificat non attaché au Thing**
```bash
# Exécuter l'explorateur de registre pour vérifier
python iot_registry_explorer.py
# Sélectionner l'option 5 (Describe Thing) et vérifier que les certificats sont listés
```

**Problème : Politique non attachée au certificat**
```bash
# Utiliser le gestionnaire de certificats pour attacher la politique
python certificate_manager.py
# Sélectionner l'option 3 (Attach Policy to Existing Certificate)
```

#### Problèmes de Statut de Certificat

**Problème : Le certificat est INACTIVE**
```bash
# Utiliser le gestionnaire de certificats pour activer
python certificate_manager.py
# Sélectionner l'option 5 (Enable/Disable Certificate)
```

**Problème : La validation du certificat échoue**
```bash
# Vérifier le format du certificat
head -5 certificates/Vehicle-VIN-001/cert-id.crt
# Devrait commencer par : -----BEGIN CERTIFICATE-----

# Valider le certificat
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -noout
# Pas de sortie signifie valide, erreur signifie invalide
```

## Problèmes de Connexion MQTT

### Problèmes MQTT Basés sur Certificat

#### Diagnostics de Connexion
```bash
# Utiliser le mode debug pour des informations d'erreur détaillées
python mqtt_client_explorer.py --debug

# Tester la connectivité de base avec OpenSSL
openssl s_client -connect <votre-endpoint>:8883 \
  -cert certificates/Vehicle-VIN-001/<cert-id>.crt \
  -key certificates/Vehicle-VIN-001/<cert-id>.key
```


#### Erreurs MQTT Courantes

**Problème : "Connection timeout"**
- **Causes** : Connectivité réseau, endpoint incorrect, pare-feu
- **Solutions** :
  ```bash
  # Vérifier l'endpoint
  python iot_registry_explorer.py
  # Sélectionner l'option 8 (Describe Endpoint)
  
  # Tester la connectivité réseau
  ping votre-endpoint-iot.amazonaws.com
  
  # Vérifier le pare-feu (le port 8883 doit être ouvert)
  telnet votre-endpoint-iot.amazonaws.com 8883
  ```

**Problème : "Authentication failed"**
- **Causes** : Problèmes de certificat, problèmes de politique, Thing non attaché
- **Solutions** :
  1. Vérifier que le certificat est ACTIVE
  2. Vérifier que le certificat est attaché au Thing
  3. Vérifier que la politique est attachée au certificat
  4. Vérifier que les permissions de la politique incluent iot:Connect

**Problème : "Subscription/Publish failed"**
- **Causes** : Restrictions de politique, format de topic invalide
- **Solutions** :
  ```bash
  # Vérifier les permissions de la politique
  # La politique doit inclure : iot:Subscribe, iot:Publish, iot:Receive
  
  # Vérifier le format du topic (pas d'espaces, caractères valides)
  # Valide : device/sensor/temperature
  # Invalide : device sensor temperature
  ```

#### Commandes de Dépannage MQTT

**Dans le Client MQTT :**
```bash
📡 MQTT> debug                    # Afficher les diagnostics de connexion
📡 MQTT> status                   # Afficher les infos de connexion
📡 MQTT> messages                 # Afficher l'historique des messages
```

**Exemple de Sortie Debug :**
```
🔍 Diagnostics de Connexion :
   Endpoint : a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   Port : 8883
   ID Client : Vehicle-VIN-001-mqtt-12345678
   Certificat : certificates/Vehicle-VIN-001/abc123.crt
   Clé Privée : certificates/Vehicle-VIN-001/abc123.key
   Statut de Connexion : CONNECTÉ
   Keep Alive : 30 secondes
   Session Propre : True
```

### Problèmes MQTT WebSocket

#### Diagnostics WebSocket
```bash
# Vérifier les identifiants AWS
aws sts get-caller-identity

# Vérifier les permissions AWS IAM
aws iam get-user-policy --user-name <votre-nom-utilisateur> --policy-name <nom-politique>

# Utiliser le mode debug
python mqtt_websocket_explorer.py --debug
```

#### Erreurs WebSocket Courantes

**Problème : "Credential validation failed"**
- **Cause** : Identifiants AWS manquants ou invalides
- **Solution** : Définir les identifiants AWS appropriés
  ```bash
  export AWS_ACCESS_KEY_ID=<votre-clé>
  export AWS_SECRET_ACCESS_KEY=<votre-secret>
  export AWS_DEFAULT_REGION=us-east-1
  ```

**Problème : "WebSocket connection failed"**
- **Causes** : Problèmes réseau, paramètres proxy, pare-feu
- **Solutions** :
  ```bash
  # Tester la connectivité HTTPS
  curl -I https://votre-endpoint.amazonaws.com
  
  # Vérifier les paramètres proxy
  echo $HTTP_PROXY
  echo $HTTPS_PROXY
  ```

**Problème : "SigV4 signing error"**
- **Cause** : Décalage d'horloge, identifiants invalides
- **Solutions** :
  ```bash
  # Synchroniser l'horloge système
  sudo ntpdate -s time.nist.gov  # Linux/macOS
  
  # Vérifier que les identifiants ne sont pas expirés
  aws sts get-caller-identity
  ```

### Problèmes du Service AWS IoT Device Shadow

#### Problèmes de Connexion Shadow

**Problème : Les opérations shadow échouent**
- **Causes** : Permissions shadow manquantes, problèmes de certificat
- **Solutions** :
  1. Vérifier que la politique inclut les permissions shadow :
     ```json
     {
       "Action": [
         "iot:GetThingShadow",
         "iot:UpdateThingShadow"
       ]
     }
     ```
  2. Vérifier que le certificat est attaché au bon Thing
  3. Vérifier que le nom du Thing correspond aux opérations shadow


**Problème : Messages delta non reçus**
- **Causes** : Problèmes d'abonnement, permissions de topic
- **Solutions** :
  ```bash
  # Vérifier les abonnements aux topics shadow
  🌟 Shadow> status
  
  # Vérifier que la politique autorise les abonnements aux topics shadow
  # Topics : $aws/things/{thingName}/shadow/update/delta
  ```

#### Problèmes de Fichier d'État Shadow

**Problème : Fichier d'état local introuvable**
- **Cause** : Permissions de création de fichier, problèmes de chemin
- **Solution** :
  ```bash
  # Vérifier les permissions du répertoire certificates
  ls -la certificates/
  
  # Créer le fichier d'état manuellement si nécessaire
  echo '{"temperature": 20.0, "status": "online"}' > certificates/Vehicle-VIN-001/device_state.json
  ```

**Problème : JSON invalide dans le fichier d'état**
- **Cause** : Erreurs d'édition manuelle
- **Solution** :
  ```bash
  # Valider le format JSON
  python -m json.tool certificates/Vehicle-VIN-001/device_state.json
  
  # Corriger ou recréer le fichier
  ```

### Problèmes du Moteur de Règles

#### Problèmes de Création de Règles

**Problème : La création du rôle AWS IAM échoue**
- **Causes** : Permissions AWS IAM insuffisantes, rôle déjà existant
- **Solutions** :
  ```bash
  # Vérifier si le rôle existe
  aws iam get-role --role-name IoTRulesEngineRole
  
  # Créer le rôle manuellement si nécessaire
  aws iam create-role --role-name IoTRulesEngineRole --assume-role-policy-document file://trust-policy.json
  ```

**Problème : Erreurs de syntaxe SQL**
- **Causes** : Format SQL invalide, fonctions non supportées
- **Solutions** :
  - Utiliser des clauses SELECT, FROM, WHERE simples
  - Éviter les fonctions SQL complexes
  - Tester d'abord avec des règles basiques

#### Problèmes de Test de Règles

**Problème : La règle ne se déclenche pas**
- **Causes** : Incompatibilité de topic, problèmes de clause WHERE, règle désactivée
- **Solutions** :
  1. Vérifier que le modèle de topic correspond au topic publié
  2. Vérifier la logique de la clause WHERE
  3. S'assurer que la règle est ENABLED
  4. Tester d'abord avec une règle simple

**Problème : Aucune sortie de règle reçue**
- **Causes** : Problèmes d'abonnement, configuration d'action
- **Solutions** :
  ```bash
  # Vérifier les actions de la règle
  python iot_rules_explorer.py
  # Sélectionner l'option 2 (Describe Rule)
  
  # Vérifier l'abonnement au topic de sortie
  # S'abonner à : processed/* ou alerts/*
  ```

## Problèmes OpenSSL

### Problèmes d'Installation

**macOS :**
```bash
# Installer via Homebrew
brew install openssl

# Ajouter au PATH si nécessaire
export PATH="/usr/local/opt/openssl/bin:$PATH"
```

**Ubuntu/Debian :**
```bash
# Mettre à jour la liste des packages et installer
sudo apt-get update
sudo apt-get install openssl

# Vérifier l'installation
openssl version
```

**Windows :**
```bash
# Télécharger depuis : https://slproweb.com/products/Win32OpenSSL.html
# Ou utiliser Windows Subsystem for Linux (WSL)

# Dans WSL :
sudo apt-get install openssl
```

### Problèmes de Génération de Certificats

**Problème : Commande OpenSSL introuvable**
- **Solution** : Installer OpenSSL ou ajouter au PATH

**Problème : Permission refusée lors de la création de fichiers de certificats**
- **Solution** : Vérifier les permissions du répertoire ou exécuter avec les privilèges appropriés

**Problème : Format de certificat invalide**
- **Solution** : Vérifier la syntaxe et les paramètres de la commande OpenSSL


## Problèmes de Réseau et de Connectivité

### Problèmes de Pare-feu et Proxy

**Ports Requis :**
- **MQTT sur TLS** : 8883
- **WebSocket MQTT** : 443
- **HTTPS (appels API)** : 443

**Pare-feu d'Entreprise :**
```bash
# Tester la connectivité des ports
telnet votre-endpoint-iot.amazonaws.com 8883
telnet votre-endpoint-iot.amazonaws.com 443

# Vérifier les paramètres proxy
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

**Configuration Proxy :**
```bash
# Définir le proxy pour HTTPS
export HTTPS_PROXY=http://proxy.entreprise.com:8080

# Contourner le proxy pour les endpoints AWS
export NO_PROXY=amazonaws.com,.amazonaws.com
```

### Problèmes de Résolution DNS

**Problème : Impossible de résoudre l'endpoint IoT**
```bash
# Tester la résolution DNS
nslookup votre-endpoint-iot.amazonaws.com

# Utiliser un DNS alternatif
export AWS_IOT_ENDPOINT=$(dig +short votre-endpoint-iot.amazonaws.com)
```

## Problèmes de Performance et de Timing

### Limitation de Débit API

**Problème : ThrottlingException**
- **Cause** : Trop d'appels API trop rapidement
- **Solution** : Ajouter des délais entre les opérations ou réduire la concurrence

**Problème : Délais de cohérence éventuelle**
- **Cause** : Les services AWS ont besoin de temps pour propager les changements
- **Solution** : Ajouter des temps d'attente après la création de ressources

### Délais de Connexion

**Problème : Délais de keep-alive MQTT**
- **Cause** : Instabilité réseau, longues périodes d'inactivité
- **Solutions** :
  - Réduire l'intervalle de keep-alive
  - Implémenter une logique de reconnexion
  - Vérifier la stabilité du réseau

## Obtenir de l'Aide Supplémentaire

### Utilisation du Mode Debug

**Activer le mode debug pour tous les scripts :**
```bash
python nom_du_script.py --debug
```

**Le mode debug fournit :**
- Journalisation détaillée des requêtes/réponses API
- Diagnostics de connexion
- Traces de pile d'erreurs
- Informations de timing

### Vérification dans la Console AWS IoT

**Vérifier les ressources dans la Console AWS :**
1. **Things** : AWS IoT Core → Gérer → Things
2. **Certificats** : AWS IoT Core → Sécuriser → Certificats
3. **Politiques** : AWS IoT Core → Sécuriser → Politiques
4. **Règles** : AWS IoT Core → Agir → Règles

### Journaux Amazon CloudWatch

**Activer la journalisation IoT pour le débogage en production :**
1. Aller dans AWS IoT Core → Paramètres
2. Activer la journalisation avec le niveau de log approprié
3. Vérifier les journaux Amazon CloudWatch pour des informations d'erreur détaillées

### Étapes de Résolution Courantes

**Quand tout le reste échoue :**
1. **Repartir de zéro** : Exécuter le script de nettoyage et recommencer
2. **Vérifier le statut AWS** : Visiter le tableau de bord de santé des services AWS
3. **Vérifier les limites du compte** : Vérifier les quotas de service AWS
4. **Tester avec une configuration minimale** : Utiliser la configuration la plus simple possible
5. **Comparer avec des exemples fonctionnels** : Utiliser les données d'exemple fournies

### Ressources de Support

- **Documentation AWS IoT** : https://docs.aws.amazon.com/iot/
- **Guide du Développeur AWS IoT** : https://docs.aws.amazon.com/iot/latest/developerguide/
- **Support AWS** : https://aws.amazon.com/support/
- **Forums AWS** : https://forums.aws.amazon.com/forum.jspa?forumID=210
