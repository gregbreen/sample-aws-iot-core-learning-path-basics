# AWS IoT Core - Caminho de Aprendizagem - Conceitos Básicos

> 🌍 **Idiomas Disponíveis** | **Available Languages** | **利用可能な言語** | **可用语言**
> 
> - [English](README.md) | [Español](README.es.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | **Português** (Atual)
> - **Documentação**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/)

Um conjunto abrangente de ferramentas em Python para aprender os conceitos básicos do Amazon Web Services (AWS) AWS IoT Core através de exploração prática. Scripts interativos demonstram gerenciamento de dispositivos, segurança, operações de API e comunicação MQTT com explicações detalhadas.

## 🚀 Início Rápido - Caminho de Aprendizagem Completo

```bash
# 1. Clonar e configurar
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Configurar ambiente
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Configurar credenciais AWS
export AWS_ACCESS_KEY_ID=<sua-chave>
export AWS_SECRET_ACCESS_KEY=<sua-chave-secreta>
export AWS_DEFAULT_REGION=<sua-regiao (ex. us-east-1)>

# 4. Opcional: Definir preferência de idioma
export AWS_IOT_LANG=pt-BR  # 'en' para inglês, 'es' para espanhol, 'ja' para japonês

# 5. Sequência completa de aprendizagem
python scripts/setup_sample_data.py          # Criar recursos IoT de exemplo
python scripts/iot_registry_explorer.py      # Explorar APIs do AWS IoT
python scripts/certificate_manager.py        # Aprender segurança IoT
python scripts/mqtt_client_explorer.py       # Comunicação MQTT em tempo real
python scripts/device_shadow_explorer.py     # Sincronização de estado de dispositivos
python scripts/iot_rules_explorer.py         # Roteamento e processamento de mensagens
python scripts/cleanup_sample_data.py        # Limpar recursos (IMPORTANTE!)
```

**⚠️ Aviso de Custos**: Isso cria recursos reais da AWS (~$0.17 total). Execute a limpeza quando terminar!

## Público-Alvo

**Público Principal:** Desenvolvedores cloud, arquitetos de soluções, engenheiros DevOps novos no AWS IoT Core

**Pré-requisitos:** Conhecimento básico de AWS, fundamentos de Python, uso de linha de comando

**Nível de Aprendizagem:** Nível associado com abordagem prática

## 🔧 Construído com SDKs da AWS

Este projeto aproveita os SDKs oficiais da AWS para fornecer experiências autênticas do AWS IoT Core:

### **Boto3 - SDK da AWS para Python**
- **Propósito**: Alimenta todas as operações do Registro AWS IoT, gerenciamento de certificados e interações do Rules Engine
- **Versão**: `>=1.26.0`
- **Documentação**: [Documentação do Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **APIs do AWS IoT Core**: [Cliente IoT do Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **SDK de Dispositivos AWS IoT para Python**
- **Propósito**: Permite comunicação MQTT autêntica com AWS IoT Core usando certificados X.509
- **Versão**: `>=1.11.0`
- **Documentação**: [SDK de Dispositivos AWS IoT para Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Por Que Esses SDKs Importam:**
- **Prontos para Produção**: Os mesmos SDKs usados em aplicações IoT reais
- **Segurança**: Suporte integrado para melhores práticas de segurança do AWS IoT
- **Confiabilidade**: Bibliotecas oficiais mantidas pela AWS com tratamento abrangente de erros
- **Valor de Aprendizagem**: Experimente padrões autênticos de desenvolvimento AWS IoT

## Índice

- 🚀 [Início Rápido](#-início-rápido---caminho-de-aprendizagem-completo)
- ⚙️ [Instalação e Configuração](#️-instalação-e-configuração)
- 📚 [Scripts de Aprendizagem](#-scripts-de-aprendizagem)
- 🧹 [Limpeza de Recursos](#-limpeza-de-recursos)
- 🛠️ [Solução de Problemas](#-solução-de-problemas)
- 📖 [Documentação Avançada](#-documentação-avançada)

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.10+
- Conta AWS com permissões IoT
- Acesso a terminal/linha de comando
- OpenSSL (para recursos de certificados)

**⚠️ NOTA IMPORTANTE DE SEGURANÇA**: Use uma conta AWS dedicada para desenvolvimento/aprendizagem. Não execute estes scripts em contas que contenham recursos IoT de produção. Embora o script de limpeza tenha múltiplos mecanismos de segurança, a melhor prática é usar ambientes isolados para atividades de aprendizagem.

### Informações de Custo

**Este projeto cria recursos reais da AWS que incorrerão em custos (~$0.17 total).**

| Serviço | Uso | Custo Estimado (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100 mensagens, 20 dispositivos | $0.10 |
| **AWS IoT Device Shadow service** | ~30 operações shadow | $0.04 |
| **IoT Rules Engine** | ~50 execuções de regras | $0.01 |
| **Armazenamento de Certificados** | 20 certificados por 1 dia | $0.01 |
| **Amazon CloudWatch Logs** | Logging básico | $0.01 |
| **Total Estimado** | **Sessão completa de aprendizagem** | **~$0.17** |

**⚠️ Importante**: Sempre execute o script de limpeza quando terminar para evitar custos contínuos.

### Instalação Detalhada

**1. Clonar Repositório:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Instalar OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Baixar do [site do OpenSSL](https://www.openssl.org/)

**3. Ambiente Virtual (Recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Configuração de Idioma (Opcional):**
```bash
# Definir preferência de idioma para todos os scripts
export AWS_IOT_LANG=pt-BR  # Português (recomendado)
export AWS_IOT_LANG=en     # Inglês
export AWS_IOT_LANG=es     # Espanhol
export AWS_IOT_LANG=ja     # Japonês
export AWS_IOT_LANG=zh-CN  # Chinês

# Alternativa: Scripts perguntarão pelo idioma se não estiver definido
```

**Idiomas Suportados:**
- **Português** (`pt-BR`, `portuguese`, `português`, `pt`) - Tradução completa disponível
- **Inglês** (`en`, `english`) - Padrão
- **Espanhol** (`es`, `spanish`, `español`) - Tradução completa disponível
- **Japonês** (`ja`, `japanese`, `日本語`, `jp`) - Tradução completa disponível
- **Chinês** (`zh-CN`, `chinese`, `中文`, `zh`) - Tradução completa disponível

## 🌍 Suporte Multi-Idioma

Todos os scripts de aprendizagem suportam interfaces em inglês, espanhol, japonês, chinês e português. O idioma afeta:

**✅ O que é Traduzido:**
- Mensagens de boas-vindas e conteúdo educacional
- Opções de menu e prompts do usuário
- Momentos de aprendizagem e explicações
- Mensagens de erro e confirmações
- Indicadores de progresso e mensagens de status

**❌ O que Permanece no Idioma Original:**
- Respostas da API AWS (dados JSON)
- Nomes e valores de parâmetros técnicos
- Métodos HTTP e endpoints
- Informações de debug e logs
- Nomes de recursos AWS e identificadores

**Opções de Uso:**

**Opção 1: Variável de Ambiente (Recomendada)**
```bash
# Definir preferência de idioma para todos os scripts
export AWS_IOT_LANG=pt-BR  # Português
export AWS_IOT_LANG=en     # Inglês
export AWS_IOT_LANG=es     # Espanhol
export AWS_IOT_LANG=ja     # Japonês
export AWS_IOT_LANG=zh-CN  # Chinês

# Executar qualquer script - idioma será aplicado automaticamente
python scripts/iot_registry_explorer.py
```

**Opção 2: Seleção Interativa**
```bash
# Executar sem variável de ambiente - script perguntará pelo idioma
python scripts/setup_sample_data.py

# Exemplo de saída:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择 / Seleção de Idioma
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# 5. Português (Portuguese)
# Selecionar idioma (1-5): 5
```

**Scripts Suportados:**
- ✅ `setup_sample_data.py` - Criação de dados de exemplo
- ✅ `iot_registry_explorer.py` - Exploração de API
- ✅ `certificate_manager.py` - Gerenciamento de certificados
- ✅ `mqtt_client_explorer.py` - Comunicação MQTT
- ✅ `mqtt_websocket_explorer.py` - MQTT WebSocket
- ✅ `device_shadow_explorer.py` - Operações AWS IoT Device Shadow service
- ✅ `iot_rules_explorer.py` - Exploração Rules Engine
- ✅ `cleanup_sample_data.py` - Limpeza de recursos



## 📚 Scripts de Aprendizagem

**Caminho de Aprendizagem Recomendado:**

### 1. 📊 Configuração de Dados de Exemplo
**Arquivo**: `scripts/setup_sample_data.py`
**Propósito**: Cria recursos IoT realistas para aprendizagem prática
**Cria**: 20 Things, 3 Thing Types, 4 Thing Groups

### 2. 🔍 Explorador de API do Registro IoT
**Arquivo**: `scripts/iot_registry_explorer.py`
**Propósito**: Ferramenta interativa para aprender APIs do Registro AWS IoT
**Recursos**: 8 APIs principais com explicações detalhadas e chamadas de API reais

### 3. 🔐 Gerenciador de Certificados e Políticas
**Arquivo**: `scripts/certificate_manager.py`
**Propósito**: Aprender segurança AWS IoT através do gerenciamento de certificados e políticas
**Recursos**: Criação de certificados, anexação de políticas, registro de certificados externos

### 4. 📡 Comunicação MQTT
**Arquivos**: 
- `scripts/mqtt_client_explorer.py` (Baseado em certificados, recomendado)
- `scripts/mqtt_websocket_explorer.py` (Alternativa baseada em WebSocket)

**Propósito**: Experimentar comunicação IoT em tempo real usando protocolo MQTT
**Recursos**: Interface de linha de comando interativa, assinatura de tópicos, publicação de mensagens

### 5. 🌟 Explorador de AWS IoT Device Shadow service
**Arquivo**: `scripts/device_shadow_explorer.py`
**Propósito**: Aprender sincronização de estado de dispositivos com AWS IoT Device Shadow
**Recursos**: Gerenciamento interativo de shadow, atualizações de estado, processamento de delta

### 6. ⚙️ Explorador do IoT Rules Engine
**Arquivo**: `scripts/iot_rules_explorer.py`
**Propósito**: Aprender roteamento e processamento de mensagens com IoT Rules Engine
**Recursos**: Criação de regras, filtragem SQL, configuração automática de AWS IAM

### 7. 🧹 Limpeza de Dados de Exemplo
**Arquivo**: `scripts/cleanup_sample_data.py`
**Propósito**: Limpar todos os recursos de aprendizagem para evitar custos
**Recursos**: Limpeza segura com tratamento de dependências

## 🧹 Limpeza de Recursos

**⚠️ IMPORTANTE**: Sempre execute a limpeza quando terminar de aprender para evitar custos contínuos da AWS.

### Uso Básico

```bash
# Limpeza padrão - remove todos os recursos do workshop
python scripts/cleanup_sample_data.py

# Visualizar o que será excluído (etapa recomendada primeiro)
python scripts/cleanup_sample_data.py --dry-run

# Limpeza com prefixo personalizado
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"

# Ativar modo debug para registro detalhado de API
python scripts/cleanup_sample_data.py --debug
```

### Parâmetros de Linha de Comando

| Parâmetro | Descrição | Padrão | Exemplo |
|-----------|-------------|---------|---------|
| `--things-prefix` | Prefixo personalizado para nomes de things | `Vehicle-VIN-` | `--things-prefix "TestDevice-"` |
| `--dry-run` | Visualizar limpeza sem excluir | `False` | `--dry-run` |
| `--debug` | Ativar registro detalhado de API | `False` | `--debug` |

### Como Funciona a Identificação de Recursos

O script de limpeza usa um **sistema de identificação dupla** para identificar com segurança os recursos do workshop:

**1. Identificação Baseada em Tags (Método Principal)**
- Recursos criados por scripts de configuração são automaticamente marcados com:
  - `workshop-resource: true` - Identifica recursos criados pelo workshop
  - `created-by: setup-script` - Rastreia qual script criou o recurso
  - `workshop-name: iot-core-basics` - Agrupa recursos por workshop
- **Vantagem**: Método mais confiável, funciona independentemente da nomenclatura

**2. Convenção de Nomenclatura de Fallback (Método Secundário)**
- Se as tags não estiverem presentes, o script identifica recursos por padrões de nomenclatura:
  - Things: Correspondem ao padrão `--things-prefix` (padrão: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - Regras IoT: Correspondem aos padrões `*Rule`, `rule_*`, ou `*_workshop_*`
- **Vantagem**: Funciona com recursos criados antes da implementação de tags

### Modo Dry-Run (Etapa Recomendada Primeiro)

**Sempre visualize as operações de limpeza antes de executá-las:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**O modo dry-run:**
- ✅ Identifica todos os recursos do workshop que seriam excluídos
- ✅ Exibe uma lista detalhada de recursos por tipo
- ✅ Mostra a ordem de exclusão (respeita dependências)
- ✅ Gera um relatório resumido
- ❌ **NÃO exclui nenhum recurso**

**Exemplo de saída dry-run:**
```
🔍 MODO DRY RUN - Nenhum recurso será excluído

Recursos Identificados:
  Things: 20 recursos
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Certificados: 20 recursos
  Thing Groups: 4 recursos
  Thing Types: 3 recursos
  Regras IoT: 1 recurso

Total: 48 recursos seriam excluídos
```

### Uso de Prefixo Personalizado

Se você criou recursos com um prefixo personalizado durante a configuração, use o mesmo prefixo para limpeza:

```bash
# Configuração com prefixo personalizado
python scripts/setup_sample_data.py --things-prefix "MyDevice-"

# Limpeza com prefixo correspondente
python scripts/cleanup_sample_data.py --things-prefix "MyDevice-"
```

**Importante**: O prefixo deve corresponder exatamente entre configuração e limpeza para que a identificação baseada em nomenclatura funcione corretamente.

### O Que é Limpo

**Recursos Excluídos (em ordem de dependência):**
1. ✅ Thing Shadows (dados de estado do dispositivo)
2. ✅ Certificados (desanexados de things primeiro)
3. ✅ Things (dispositivos IoT)
4. ✅ Regras IoT (regras de roteamento de mensagens)
5. ✅ Thing Groups (coleções de dispositivos)
6. ✅ Thing Types (modelos de dispositivos)
7. ✅ Políticas (políticas de segurança)
8. ✅ Arquivos de certificados locais (do diretório `certs/`)

**Recursos Protegidos:**
- ❌ Recursos IoT de produção (sem tags de workshop)
- ❌ Recursos com padrões de nomenclatura diferentes
- ❌ Certificados e políticas não associados a things do workshop
- ❌ Recursos criados fora dos scripts do workshop

### Exclusão com Reconhecimento de Dependências

O script de limpeza trata automaticamente as dependências de recursos do AWS IoT:

**Ordem de Exclusão:**
```
Thing Shadows → Certificados → Things → Regras IoT → Thing Groups → Thing Types → Políticas
```

**Por que esta ordem importa:**
- Thing Shadows devem ser excluídos antes dos certificados
- Certificados devem ser desanexados antes que things possam ser excluídos
- Things devem ser removidos de grupos antes que grupos possam ser excluídos
- Políticas devem ser desanexadas antes da exclusão

**O script trata disso automaticamente** - você não precisa se preocupar com conflitos de dependências.

### Entendendo o Relatório Resumido

Após a conclusão da limpeza, você verá um relatório resumido:

```
📊 Resumo da Limpeza

Tipo de Recurso | Identificados | Excluídos | Falhados
----------------|---------------|-----------|----------
Things          |            20 |        20 |        0
Certificados    |            20 |        20 |        0
Thing Groups    |             4 |         4 |        0
Thing Types     |             3 |         3 |        0
Regras IoT      |             1 |         1 |        0
Políticas       |            20 |        20 |        0
----------------|---------------|-----------|----------
Total           |            68 |        68 |        0

✅ Limpeza concluída com sucesso!
```

**Campos do Relatório:**
- **Identificados**: Recursos encontrados correspondendo aos critérios do workshop
- **Excluídos**: Recursos removidos com sucesso
- **Falhados**: Recursos que não puderam ser excluídos (com detalhes de erro)

### Solução de Problemas de Limpeza

**Problema: "Nenhum recurso encontrado"**
- **Causa**: Recursos podem não ter tags de workshop ou não correspondem ao prefixo
- **Solução**: 
  - Verifique se você usou um prefixo personalizado durante a configuração
  - Use `--things-prefix` com o prefixo correto
  - Verifique se os recursos existem no Console AWS

**Problema: Erros de "Permissão negada"**
- **Causa**: Credenciais AWS não têm as permissões IoT necessárias
- **Solução**: Certifique-se de que seu usuário/função IAM tenha permissões de acesso completo ao IoT

**Problema: Erros de "Conflito de dependência"**
- **Causa**: Recursos têm dependências que não foram tratadas
- **Solução**: O script deve tratar isso automaticamente. Se persistir, execute com `--debug` para ver detalhes

**Problema: Alguns recursos não foram excluídos**
- **Causa**: Recursos podem estar em uso ou ter dependências externas
- **Solução**: 
  - Verifique o relatório resumido para recursos falhados
  - Use o Console AWS para inspecionar e excluir manualmente os recursos restantes
  - Execute a limpeza novamente após resolver as dependências

### Melhores Práticas

1. **Sempre use dry-run primeiro**: Visualize o que será excluído antes de executar
2. **Corresponda os prefixos**: Use o mesmo `--things-prefix` para configuração e limpeza
3. **Revise o resumo**: Verifique o relatório para garantir que todos os recursos foram excluídos
4. **Execute a limpeza prontamente**: Não deixe recursos do workshop em execução para evitar custos
5. **Mantenha as credenciais seguras**: Nunca faça commit de credenciais AWS no controle de versão

## 🛠️ Solução de Problemas

### Problemas Comuns

**Credenciais AWS:**
```bash
# Definir credenciais
export AWS_ACCESS_KEY_ID=<sua-chave>
export AWS_SECRET_ACCESS_KEY=<sua-chave-secreta>
export AWS_DEFAULT_REGION=us-east-1
```

**Dependências Python:**
```bash
pip install -r requirements.txt
```

**Problemas com OpenSSL:**
- **macOS**: `brew install openssl`
- **Ubuntu**: `sudo apt-get install openssl`

### Modo Debug

Todos os scripts suportam modo debug para logging detalhado da API:
```bash
python scripts/<nome_do_script>.py --debug
```

## 📖 Documentação Avançada

### Documentação Detalhada
- **[Guia Detalhado de Scripts](docs/pt-BR/DETAILED_SCRIPTS.md)** - Documentação aprofundada dos scripts
- **[Exemplos Completos](docs/pt-BR/EXAMPLES.md)** - Fluxos de trabalho completos e saídas de exemplo
- **[Guia de Solução de Problemas](docs/pt-BR/TROUBLESHOOTING.md)** - Problemas comuns e soluções

### Recursos de Aprendizagem

#### Documentação do AWS IoT Core
- **[Guia do Desenvolvedor AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/)**
- **[Referência da API AWS IoT Core](https://docs.aws.amazon.com/iot/latest/apireference/)**

#### SDKs da AWS Usados Neste Projeto
- **[Documentação do Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Documentação completa do SDK Python
- **[Referência do Cliente IoT do Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - Métodos de API específicos do IoT
- **[SDK de Dispositivos AWS IoT para Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - Documentação do cliente MQTT
- **[GitHub do SDK de Dispositivos AWS IoT](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Código fonte e exemplos

#### Protocolos e Padrões
- **[Especificação do Protocolo MQTT](https://mqtt.org/)** - Documentação oficial do MQTT
- **[Padrão de Certificados X.509](https://tools.ietf.org/html/rfc5280)** - Especificação do formato de certificados

## 🤝 Contribuindo

Este é um projeto educacional. Contribuições que melhorem a experiência de aprendizagem são bem-vindas:

- **Correções de bugs** para problemas de scripts
- **Melhorias de tradução** para melhor localização
- **Aprimoramentos de documentação** para clareza
- **Cenários de aprendizagem adicionais** que se adequem ao nível básico

## 📄 Licença

Este projeto está licenciado sob a Licença MIT-0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🏷️ Tags

`aws-iot` `iot-core` `mqtt` `device-shadow` `certificates` `python` `learning` `tutorial` `hands-on` `interactive`