# Guia de Solução de Problemas

Opa! Encontrou algum problema? Relaxa - todo mundo passa por isso. Este guia vai te ajudar a resolver os problemas mais comuns que você pode encontrar enquanto aprende AWS IoT Core.

## Índice

- [Problemas Comuns](#problemas-comuns)
  - [Credenciais AWS](#credenciais-aws)
  - [Problemas de Ambiente Virtual](#problemas-de-ambiente-virtual)
  - [Problemas de Dependências](#problemas-de-dependências)
  - [Problemas de Permissão](#problemas-de-permissão)
  - [Problemas de Certificado](#problemas-de-certificado)
- [Problemas de Conexão MQTT](#problemas-de-conexão-mqtt)
  - [Problemas MQTT Baseado em Certificado](#problemas-mqtt-baseado-em-certificado)
  - [Problemas MQTT WebSocket](#problemas-mqtt-websocket)
- [Problemas de AWS IoT Device Shadow service](#problemas-de-device-shadow)
  - [Problemas de Conexão Shadow](#problemas-de-conexão-shadow)
  - [Problemas de Arquivo de Estado Shadow](#problemas-de-arquivo-de-estado-shadow)
- [Problemas do Rules Engine](#problemas-do-rules-engine)
  - [Problemas de Criação de Regra](#problemas-de-criação-de-regra)
  - [Problemas de Teste de Regra](#problemas-de-teste-de-regra)
- [Problemas do OpenSSL](#problemas-do-openssl)
  - [Problemas de Instalação](#problemas-de-instalação)
  - [Problemas de Geração de Certificado](#problemas-de-geração-de-certificado)
- [Problemas de Rede e Conectividade](#problemas-de-rede-e-conectividade)
  - [Problemas de Firewall e Proxy](#problemas-de-firewall-e-proxy)
  - [Problemas de Resolução DNS](#problemas-de-resolução-dns)
- [Problemas de Performance e Timing](#problemas-de-performance-e-timing)
  - [Limitação de Taxa de API](#limitação-de-taxa-de-api)
  - [Timeouts de Conexão](#timeouts-de-conexão)
- [Obtendo Ajuda Adicional](#obtendo-ajuda-adicional)
  - [Uso do Modo Debug](#uso-do-modo-debug)
  - [Verificação do Console AWS IoT](#verificação-do-console-aws-iot)
  - [Amazon CloudWatch Logs](#cloudwatch-logs)
  - [Passos Comuns de Resolução](#passos-comuns-de-resolução)
  - [Recursos de Suporte](#recursos-de-suporte)

## Problemas Comuns

### Credenciais AWS

#### Vamos Verificar Suas Credenciais
```bash
# Verificar se as credenciais estão configuradas
aws sts get-caller-identity

# Verificar região atual
echo $AWS_DEFAULT_REGION

# Listar variáveis de ambiente
env | grep AWS
```

#### Problemas Comuns de Credenciais

**Problema: "Unable to locate credentials"**
```bash
# Solução 1: Definir variáveis de ambiente
export AWS_ACCESS_KEY_ID=<sua-chave-de-acesso>
export AWS_SECRET_ACCESS_KEY=<sua-chave-secreta>
export AWS_DEFAULT_REGION=us-east-1

# Solução 2: Usar configuração AWS CLI
aws configure

# Solução 3: Verificar configuração existente
aws configure list
```

**Problema: "You must specify a region"**
```bash
# Definir região padrão
export AWS_DEFAULT_REGION=us-east-1

# Ou especificar na configuração AWS CLI
aws configure set region us-east-1
```

**Problema: "The security token included in the request is invalid"**
- **O que está acontecendo**: Suas credenciais temporárias expiraram ou o token de sessão não está correto
- **Como resolver**: Atualize suas credenciais ou remova o token de sessão expirado
```bash
unset AWS_SESSION_TOKEN
# Depois defina novas credenciais
```

### Problemas de Ambiente Virtual

#### Vamos Verificar Seu Ambiente Virtual
```bash
# Verificar se venv está ativo
which python
# Deve mostrar: /caminho/para/seu/projeto/venv/bin/python

# Verificar versão do Python
python --version
# Deve ser 3.7 ou superior

# Listar pacotes instalados
pip list
```

#### Problemas de Ambiente Virtual

**Problema: Ambiente virtual não ativado**
```bash
# Ativar ambiente virtual
# No macOS/Linux:
source venv/bin/activate

# No Windows:
venv\Scripts\activate

# Verificar ativação
which python
```

**Problema: Versão errada do Python**
```bash
# Criar novo venv com versão específica do Python
python3.9 -m venv venv
# ou
python3 -m venv venv

# Ativar e verificar
source venv/bin/activate
python --version
```

**Problema: Falha na instalação de pacotes**
```bash
# Vamos atualizar o pip primeiro
python -m pip install --upgrade pip

# Agora instalar os requirements
pip install -r requirements.txt

# Se ainda não funcionar, tente instalar os pacotes um por um
pip install boto3
pip install awsiotsdk
```

### Problemas de Dependências

#### Vamos Reinstalar Suas Dependências
```bash
# Atualizar todos os pacotes
pip install --upgrade -r requirements.txt

# Forçar reinstalação
pip install --force-reinstall -r requirements.txt

# Limpar cache do pip e reinstalar
pip cache purge
pip install -r requirements.txt
```

#### Erros Comuns de Dependências

**Problema: "No module named 'boto3'"**
```bash
# Garantir que venv está ativado e instalar
pip install boto3

# Verificar instalação
python -c "import boto3; print(boto3.__version__)"
```

**Problema: "No module named 'awsiot'"**
```bash
# Instalar AWS IoT SDK
pip install awsiotsdk

# Verificar instalação
python -c "import awsiot; print('AWS IoT SDK instalado')"
```

**Problema: Erros de certificado SSL/TLS**
```bash
# No macOS, vamos atualizar os certificados
/Applications/Python\ 3.x/Install\ Certificates.command

# Ou você pode instalar o pacote de certificados
pip install --upgrade certifi
```

### Problemas de Permissão

#### Permissões AWS IAM Que Você Vai Precisar

**Aqui está o que os scripts de aprendizagem precisam:**
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

**Permissões Mínimas (se iot:* for muito amplo):**
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

**Erros Comuns de Permissão:**

**Problema: "User is not authorized to perform: iot:CreateThing"**
- **O que está acontecendo**: Você precisa de mais permissões AWS IAM
- **Como resolver**: Adicione permissões IoT ao seu usuário ou função AWS IAM

**Problema: "Access Denied" ao criar funções AWS IAM**
- **O que está acontecendo**: Faltam permissões AWS IAM para o Rules Engine
- **Como resolver**: Adicione permissões AWS IAM ou use uma função existente

### Problemas de Certificado

#### Problemas de Arquivo de Certificado

**Problema: Arquivos de certificado não encontrados**
```bash
# Verificar se o diretório certificates existe
ls -la certificates/

# Verificar certificados de Thing específico
ls -la certificates/Vehicle-VIN-001/

# Verificar arquivos de certificado
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -text -noout
```

**Problema: Certificado não anexado ao Thing**
```bash
# Vamos executar o explorador de registro para verificar
python iot_registry_explorer.py
# Selecione a opção 5 (Descrever Thing) e verifique se os certificados estão listados
```

**Problema: Política não anexada ao certificado**
```bash
# Use o gerenciador de certificados para anexar a política
python certificate_manager.py
# Selecione a opção 3 (Anexar Política ao Certificado Existente)
```

#### Problemas de Status de Certificado

**Problema: Certificado está INATIVO**
```bash
# Use o gerenciador de certificados para ativar
python certificate_manager.py
# Selecione a opção 5 (Habilitar/Desabilitar Certificado)
```

**Problema: Validação de certificado falha**
```bash
# Verificar formato do certificado
head -5 certificates/Vehicle-VIN-001/cert-id.crt
# Deve começar com: -----BEGIN CERTIFICATE-----

# Validar certificado
openssl x509 -in certificates/Vehicle-VIN-001/cert-id.crt -noout
# Nenhuma saída significa válido, erro significa inválido
```

## Problemas de Conexão MQTT

### Problemas MQTT Baseado em Certificado

#### Diagnósticos de Conexão
```bash
# Usar modo debug para informações detalhadas de erro
python mqtt_client_explorer.py --debug

# Testar conectividade básica com OpenSSL
openssl s_client -connect <seu-endpoint>:8883 \
  -cert certificates/Vehicle-VIN-001/<cert-id>.crt \
  -key certificates/Vehicle-VIN-001/<cert-id>.key
```

#### Erros Comuns de MQTT

**Problema: "Connection timeout"**
- **O que pode estar acontecendo**: Problemas de conectividade de rede, endpoint incorreto ou firewall bloqueando
- **Vamos tentar estas soluções**:
  ```bash
  # Verifique seu endpoint
  python iot_registry_explorer.py
  # Selecione a opção 8 (Descrever Endpoint)
  
  # Teste a conectividade de rede
  ping seu-iot-endpoint.amazonaws.com
  
  # Verifique o firewall (a porta 8883 precisa estar aberta)
  telnet seu-iot-endpoint.amazonaws.com 8883
  ```

**Problema: "Authentication failed"**
- **O que pode estar acontecendo**: Problemas de certificado, problemas de política ou Thing não anexado
- **Vamos tentar estas soluções**:
  1. Verifique se seu certificado está ATIVO
  2. Confirme que o certificado está anexado ao seu Thing
  3. Verifique se a política está anexada ao certificado
  4. Confirme que as permissões da política incluem iot:Connect

**Problema: "Subscription/Publish failed"**
- **O que pode estar acontecendo**: Restrições de política ou formato de tópico inválido
- **Vamos tentar estas soluções**:
  ```bash
  # Verifique as permissões da sua política
  # A política precisa incluir: iot:Subscribe, iot:Publish, iot:Receive
  
  # Verifique o formato do tópico (sem espaços, apenas caracteres válidos)
  # Válido: device/sensor/temperature
  # Inválido: device sensor temperature
  ```

#### Comandos de Solução de Problemas MQTT

**Dentro do Cliente MQTT:**
```bash
📡 MQTT> debug                    # Mostrar diagnósticos de conexão
📡 MQTT> status                   # Exibir informações de conexão
📡 MQTT> messages                 # Mostrar histórico de mensagens
```

**Exemplo de Saída de Debug:**
```
🔍 Diagnósticos de Conexão:
   Endpoint: a1b2c3d4e5f6g7-ats.iot.us-east-1.amazonaws.com
   Porta: 8883
   ID do Cliente: Vehicle-VIN-001-mqtt-12345678
   Certificado: certificates/Vehicle-VIN-001/abc123.crt
   Chave Privada: certificates/Vehicle-VIN-001/abc123.key
   Status da Conexão: CONECTADO
   Keep Alive: 30 segundos
   Sessão Limpa: True
```

### Problemas MQTT WebSocket

#### Diagnósticos WebSocket
```bash
# Verificar credenciais AWS
aws sts get-caller-identity

# Verificar permissões IAM
aws iam get-user-policy --user-name <seu-nome-de-usuario> --policy-name <nome-da-politica>

# Usar modo debug
python mqtt_websocket_explorer.py --debug
```

#### Erros Comuns de WebSocket

**Problema: "Credential validation failed"**
- **O que está acontecendo**: Credenciais AWS ausentes ou inválidas
- **Como resolver**: Vamos configurar as credenciais AWS adequadas
  ```bash
  export AWS_ACCESS_KEY_ID=<sua-chave>
  export AWS_SECRET_ACCESS_KEY=<sua-chave-secreta>
  export AWS_DEFAULT_REGION=us-east-1
  ```

**Problema: "WebSocket connection failed"**
- **O que pode estar acontecendo**: Problemas de rede, configurações de proxy ou firewall bloqueando
- **Vamos tentar estas soluções**:
  ```bash
  # Teste a conectividade HTTPS
  curl -I https://seu-endpoint.amazonaws.com
  
  # Verifique as configurações de proxy
  echo $HTTP_PROXY
  echo $HTTPS_PROXY
  ```

**Problema: "SigV4 signing error"**
- **O que está acontecendo**: Desvio de relógio ou credenciais inválidas
- **Vamos tentar estas soluções**:
  ```bash
  # Sincronize o relógio do sistema
  sudo ntpdate -s time.nist.gov  # Linux/macOS
  
  # Verifique se as credenciais não expiraram
  aws sts get-caller-identity
  ```

### Problemas de AWS IoT Device Shadow service

#### Problemas de Conexão Shadow

**Problema: Operações shadow falham**
- **O que pode estar acontecendo**: Permissões shadow ausentes ou problemas de certificado
- **Vamos tentar estas soluções**:
  1. Verifique se a política inclui permissões shadow:
     ```json
     {
       "Action": [
         "iot:GetThingShadow",
         "iot:UpdateThingShadow"
       ]
     }
     ```
  2. Confirme que o certificado está anexado ao Thing correto
  3. Verifique se o nome do Thing corresponde às operações shadow

**Problema: Mensagens delta não recebidas**
- **O que pode estar acontecendo**: Problemas de assinatura ou permissões de tópico
- **Vamos tentar estas soluções**:
  ```bash
  # Verifique suas assinaturas de tópico shadow
  🌟 Shadow> status
  
  # Verifique se a política permite assinaturas de tópico shadow
  # Tópicos: $aws/things/{thingName}/shadow/update/delta
  ```

#### Problemas de Arquivo de Estado Shadow

**Problema: Arquivo de estado local não encontrado**
- **O que está acontecendo**: Permissões de criação de arquivo ou problemas de caminho
- **Como resolver**:
  ```bash
  # Verifique as permissões do diretório certificates
  ls -la certificates/
  
  # Crie o arquivo de estado manualmente se precisar
  echo '{"temperature": 20.0, "status": "online"}' > certificates/Vehicle-VIN-001/device_state.json
  ```

**Problema: JSON inválido no arquivo de estado**
- **O que está acontecendo**: Erros de edição manual
- **Como resolver**:
  ```bash
  # Valide o formato JSON
  python -m json.tool certificates/Vehicle-VIN-001/device_state.json
  
  # Corrija ou recrie o arquivo
  ```

### Problemas do Rules Engine

#### Problemas de Criação de Regra

**Problema: Falha na criação de função AWS IAM**
- **O que pode estar acontecendo**: Permissões AWS IAM insuficientes ou a função já existe
- **Vamos tentar estas soluções**:
  ```bash
  # Verifique se a função existe
  aws iam get-role --role-name IoTRulesEngineRole
  
  # Crie a função manualmente se precisar
  aws iam create-role --role-name IoTRulesEngineRole --assume-role-policy-document file://trust-policy.json
  ```

**Problema: Erros de sintaxe SQL**
- **O que pode estar acontecendo**: Formato SQL inválido ou funções não suportadas
- **Vamos tentar estas soluções**:
  - Use cláusulas SELECT, FROM, WHERE simples
  - Evite funções SQL complexas
  - Teste com regras básicas primeiro

#### Problemas de Teste de Regra

**Problema: Regra não dispara**
- **O que pode estar acontecendo**: Incompatibilidade de tópico, problemas de cláusula WHERE ou regra desabilitada
- **Vamos tentar estas soluções**:
  1. Verifique se o padrão de tópico corresponde ao tópico publicado
  2. Confira a lógica da cláusula WHERE
  3. Garanta que a regra está HABILITADA
  4. Teste com uma regra simples primeiro

**Problema: Nenhuma saída de regra recebida**
- **O que pode estar acontecendo**: Problemas de assinatura ou configuração de ação
- **Vamos tentar estas soluções**:
  ```bash
  # Verifique as ações da regra
  python iot_rules_explorer.py
  # Selecione a opção 2 (Descrever Regra)
  
  # Verifique se você está inscrito no tópico de saída
  # Assine em: processed/* ou alerts/*
  ```

## Problemas do OpenSSL

### Problemas de Instalação

**macOS:**
```bash
# Instalar via Homebrew
brew install openssl

# Adicionar ao PATH se necessário
export PATH="/usr/local/opt/openssl/bin:$PATH"
```

**Ubuntu/Debian:**
```bash
# Atualizar lista de pacotes e instalar
sudo apt-get update
sudo apt-get install openssl

# Verificar instalação
openssl version
```

**Windows:**
```bash
# Baixar de: https://slproweb.com/products/Win32OpenSSL.html
# Ou usar Windows Subsystem for Linux (WSL)

# No WSL:
sudo apt-get install openssl
```

### Problemas de Geração de Certificado

**Problema: Comando OpenSSL não encontrado**
- **Como resolver**: Instale o OpenSSL ou adicione-o ao seu PATH

**Problema: Permissão negada ao criar arquivos de certificado**
- **Como resolver**: Verifique as permissões de diretório ou execute com privilégios apropriados

**Problema: Formato de certificado inválido**
- **Como resolver**: Verifique a sintaxe e os parâmetros do comando OpenSSL

## Problemas de Rede e Conectividade

### Problemas de Firewall e Proxy

**Portas Necessárias:**
- **MQTT sobre TLS**: 8883
- **WebSocket MQTT**: 443
- **HTTPS (chamadas de API)**: 443

**Firewall Corporativo:**
```bash
# Testar conectividade de porta
telnet seu-iot-endpoint.amazonaws.com 8883
telnet seu-iot-endpoint.amazonaws.com 443

# Verificar configurações de proxy
echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
```

**Configuração de Proxy:**
```bash
# Definir proxy para HTTPS
export HTTPS_PROXY=http://proxy.empresa.com:8080

# Ignorar proxy para endpoints AWS
export NO_PROXY=amazonaws.com,.amazonaws.com
```

### Problemas de Resolução DNS

**Problema: Não é possível resolver endpoint IoT**
```bash
# Testar resolução DNS
nslookup seu-iot-endpoint.amazonaws.com

# Usar DNS alternativo
export AWS_IOT_ENDPOINT=$(dig +short seu-iot-endpoint.amazonaws.com)
```

## Problemas de Performance e Timing

### Limitação de Taxa de API

**Problema: ThrottlingException**
- **O que está acontecendo**: Muitas chamadas de API acontecendo muito rapidamente
- **Como resolver**: Adicione alguns atrasos entre as operações ou reduza a concorrência

**Problema: Atrasos de consistência eventual**
- **O que está acontecendo**: Os serviços AWS precisam de um tempo para propagar as mudanças
- **Como resolver**: Adicione tempos de espera após criar recursos

### Timeouts de Conexão

**Problema: Timeouts de keep-alive MQTT**
- **O que está acontecendo**: Instabilidade de rede ou períodos longos de inatividade
- **Vamos tentar estas soluções**:
  - Reduza o intervalo de keep-alive
  - Implemente lógica de retry de conexão
  - Verifique a estabilidade da rede

## Obtendo Ajuda Adicional

### Uso do Modo Debug

**Habilitar modo debug para todos os scripts:**
```bash
python nome_do_script.py --debug
```

**Modo debug fornece:**
- Logging detalhado de requisição/resposta de API
- Diagnósticos de conexão
- Stack traces de erro
- Informações de timing

### Verificação do Console AWS IoT

**Verifique os recursos no Console AWS:**
1. **Things**: AWS IoT Core → Gerenciar → Things
2. **Certificados**: AWS IoT Core → Proteger → Certificados
3. **Políticas**: AWS IoT Core → Proteger → Políticas
4. **Regras**: AWS IoT Core → Agir → Regras

### Amazon CloudWatch Logs

**Habilite o logging IoT para debug de produção:**
1. Vá para AWS IoT Core → Configurações
2. Habilite o logging com o nível de log apropriado
3. Verifique o Amazon CloudWatch Logs para informações detalhadas de erro

### Passos Comuns de Resolução

**Quando tudo mais falhar, aqui está o que tentar:**
1. **Começar do zero**: Execute o script de limpeza e comece novamente
2. **Verificar status da AWS**: Visite o AWS Service Health Dashboard
3. **Verificar limites da conta**: Confira suas cotas de serviço AWS
4. **Testar com configuração mínima**: Use a configuração mais simples possível
5. **Comparar com exemplos funcionais**: Use os dados de exemplo fornecidos

### Recursos de Suporte

- **Documentação AWS IoT**: https://docs.aws.amazon.com/iot/
- **Guia do Desenvolvedor AWS IoT**: https://docs.aws.amazon.com/iot/latest/developerguide/
- **Suporte AWS**: https://aws.amazon.com/support/
- **Fóruns AWS**: https://forums.aws.amazon.com/forum.jspa?forumID=210