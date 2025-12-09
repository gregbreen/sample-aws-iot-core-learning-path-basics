# AWS IoT Core - Ruta de Aprendizaje - Conceptos Básicos

> 🌍 **Idiomas Disponibles** | **Available Languages** | **利用可能な言語** | **可用语言**
> 
> - [English](README.md) | **Español** (Actual) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [Português](README.pt-BR.md)
> - **Documentación**: [English](docs/en/) | [Español](docs/es/) | [中文](docs/zh-CN/) | [日本語](docs/ja/) | [Português](docs/pt-BR/)

Un conjunto completo de herramientas en Python para aprender los conceptos básicos de Amazon Web Services (AWS) AWS IoT Core a través de exploración práctica. Los scripts interactivos demuestran gestión de dispositivos, seguridad, operaciones de API y comunicación MQTT con explicaciones detalladas.

## 🚀 Resumen Rápido - Ruta de Aprendizaje Completa

```bash
# 1. Clonar y configurar
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics

# 2. Configurar entorno
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Configurar credenciales de AWS
export AWS_ACCESS_KEY_ID=<tu-clave>
export AWS_SECRET_ACCESS_KEY=<tu-clave-secreta>
export AWS_DEFAULT_REGION=<tu-region (ej. us-east-1)>

# 4. Opcional: Configurar preferencia de idioma
export AWS_IOT_LANG=es  # 'en' para inglés, 'ja' para japonés, 'zh-CN' para chino

# 5. Secuencia completa de aprendizaje
python scripts/setup_sample_data.py          # Crear recursos IoT de ejemplo
python scripts/iot_registry_explorer.py      # Explorar APIs de AWS IoT
python scripts/certificate_manager.py        # Aprender seguridad IoT
python scripts/mqtt_client_explorer.py       # Comunicación MQTT en tiempo real
python scripts/device_shadow_explorer.py     # Sincronización de estado de dispositivos
python scripts/iot_rules_explorer.py         # Enrutamiento y procesamiento de mensajes
python scripts/cleanup_sample_data.py        # Limpiar recursos (¡IMPORTANTE!)
```

**⚠️ Advertencia de Costos**: Esto crea recursos reales de AWS (~$0.17 total). ¡Ejecuta la limpieza cuando termines!

## Audiencia Objetivo

**Audiencia Principal:** Desarrolladores cloud, arquitectos de soluciones, ingenieros DevOps nuevos en AWS IoT Core

**Prerrequisitos:** Conocimiento básico de AWS, fundamentos de Python, uso de línea de comandos

**Nivel de Aprendizaje:** Nivel asociado con enfoque práctico

## 🔧 Construido con SDKs de AWS

Este proyecto aprovecha los SDKs oficiales de AWS para proporcionar experiencias auténticas de AWS IoT Core:

### **Boto3 - SDK de AWS para Python**
- **Propósito**: Potencia todas las operaciones del Registro de AWS IoT, gestión de certificados e interacciones del Motor de Reglas
- **Versión**: `>=1.26.0`
- **Documentación**: [Documentación de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- **APIs de AWS IoT Core**: [Cliente IoT de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)

### **SDK de Dispositivos AWS IoT para Python**
- **Propósito**: Permite comunicación MQTT auténtica con AWS IoT Core usando certificados X.509
- **Versión**: `>=1.11.0`
- **Documentación**: [SDK de Dispositivos AWS IoT para Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)
- **GitHub**: [aws-iot-device-sdk-python-v2](https://github.com/aws/aws-iot-device-sdk-python-v2)

**Por Qué Importan Estos SDKs:**
- **Listos para Producción**: Los mismos SDKs utilizados en aplicaciones IoT reales
- **Seguridad**: Soporte integrado para las mejores prácticas de seguridad de AWS IoT
- **Confiabilidad**: Bibliotecas oficiales mantenidas por AWS con manejo integral de errores
- **Valor de Aprendizaje**: Experimenta patrones auténticos de desarrollo de AWS IoT

## Tabla de Contenidos

- 🚀 [Inicio Rápido](#-resumen-rápido---ruta-de-aprendizaje-completa)
- ⚙️ [Instalación y Configuración](#️-instalación-y-configuración)
- 📚 [Scripts de Aprendizaje](#-scripts-de-aprendizaje)
- 🧹 [Limpieza de Recursos](#limpieza-de-recursos)
- 🛠️ [Solución de Problemas](#solución-de-problemas)
- 📖 [Documentación Avanzada](#-documentación-avanzada)

## ⚙️ Instalación y Configuración

### Prerrequisitos
- Python 3.10+
- Cuenta de AWS con permisos de IoT
- Acceso a terminal/línea de comandos
- OpenSSL (para funciones de certificados)

**⚠️ NOTA IMPORTANTE DE SEGURIDAD**: Usa una cuenta de AWS dedicada para desarrollo/aprendizaje. No ejecutes estos scripts en cuentas que contengan recursos IoT de producción. Aunque el script de limpieza tiene múltiples mecanismos de seguridad, la mejor práctica es usar entornos aislados para actividades de aprendizaje.

<details>
<summary>💰 <strong>Detalles de Costos de AWS</strong></summary>

**Este proyecto crea recursos reales de AWS que incurrirán en cargos (~$0.17 total).**

| Servicio | Uso | Costo Estimado (USD) |
|---------|-------|---------------------|
| **AWS IoT Core** | ~100 mensajes, 20 dispositivos | $0.10 |
| **AWS IoT Device Shadow service** | ~30 operaciones shadow | $0.04 |
| **IoT Rules Engine** | ~50 ejecuciones de reglas | $0.01 |
| **Almacenamiento de Certificados** | 20 certificados por 1 día | $0.01 |
| **Amazon CloudWatch Logs** | Logging básico | $0.01 |
| **Total Estimado** | **Sesión completa de aprendizaje** | **~$0.17** |

**Gestión de Costos:**
- ✅ Script de limpieza automática proporcionado
- ✅ Creación mínima de recursos
- ✅ Recursos de corta duración (sesión única)
- ⚠️ **Tu responsabilidad** ejecutar script de limpieza

**📊 Monitorear costos:** [Panel de Facturación de AWS](https://console.aws.amazon.com/billing/)

</details>



<details>
<summary>🔧 <strong>Pasos de Instalación Detallados</strong></summary>

**1. Clonar el Repositorio:**
```bash
git clone https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics.git
cd sample-aws-iot-core-learning-path-basics
```

**2. Instalar OpenSSL:**
- **macOS:** `brew install openssl`
- **Ubuntu/Debian:** `sudo apt-get install openssl`
- **Windows:** Descargar desde [Win32/Win64 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)

**3. Entorno Virtual (Recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

**4. Credenciales de AWS:**
```bash
export AWS_ACCESS_KEY_ID=<tu-clave-de-acceso>
export AWS_SECRET_ACCESS_KEY=<tu-clave-secreta>
export AWS_SESSION_TOKEN=<tu-token-de-sesion>  # Opcional
export AWS_DEFAULT_REGION=us-east-1
```

**5. Configuración de Idioma (Opcional):**
```bash
# Configurar preferencia de idioma para todos los scripts
export AWS_IOT_LANG=es     # Español (recomendado)
export AWS_IOT_LANG=en     # Inglés
export AWS_IOT_LANG=ja     # Japonés
export AWS_IOT_LANG=zh-CN  # Chino

# Alternativa: Los scripts preguntarán por el idioma si no está configurado
```

**Idiomas Soportados:**
- **Español** (`es`, `spanish`, `español`) - Traducción completa disponible
- **Inglés** (`en`, `english`) - Idioma por defecto
- **Japonés** (`ja`, `japanese`, `日本語`, `jp`) - Traducción completa disponible
- **Chino** (`zh-CN`, `chinese`, `中文`, `zh`) - Traducción completa disponible

## 🌍 Soporte Multi-Idioma

Todos los scripts de aprendizaje soportan interfaces en inglés, español, japonés y chino. El idioma afecta:

**✅ Lo que se Traduce:**
- Mensajes de bienvenida y contenido educativo
- Opciones de menú y prompts de usuario
- Momentos de aprendizaje y explicaciones
- Mensajes de error y confirmaciones
- Indicadores de progreso y mensajes de estado

**❌ Lo que Permanece en Idioma Original:**
- Respuestas de API de AWS (datos JSON)
- Nombres y valores de parámetros técnicos
- Métodos HTTP y endpoints
- Información de debug y logs
- Nombres de recursos de AWS e identificadores

**Opciones de Uso:**

**Opción 1: Variable de Entorno (Recomendada)**
```bash
# Configurar preferencia de idioma para todos los scripts
export AWS_IOT_LANG=es     # Español
export AWS_IOT_LANG=en     # Inglés
export AWS_IOT_LANG=ja     # Japonés
export AWS_IOT_LANG=zh-CN  # Chino

# Ejecutar cualquier script - el idioma se aplicará automáticamente
python scripts/iot_registry_explorer.py
```

**Opción 2: Selección Interactiva**
```bash
# Ejecutar sin variable de entorno - el script preguntará por el idioma
python scripts/setup_sample_data.py

# Ejemplo de salida:
# 🌍 Language Selection / Selección de Idioma / 言語選択 / 语言选择
# 1. English
# 2. Español (Spanish)
# 3. 日本語 (Japanese)
# 4. 中文 (Chinese)
# Seleccionar idioma (1-4): 2
```

**Scripts Soportados:**
- ✅ `setup_sample_data.py` - Creación de datos de ejemplo
- ✅ `iot_registry_explorer.py` - Exploración de API
- ✅ `certificate_manager.py` - Gestión de certificados
- ✅ `mqtt_client_explorer.py` - Comunicación MQTT
- ✅ `mqtt_websocket_explorer.py` - MQTT WebSocket
- ✅ `device_shadow_explorer.py` - Operaciones AWS IoT Device Shadow service
- ✅ `iot_rules_explorer.py` - Exploración Rules Engine
- ✅ `cleanup_sample_data.py` - Limpieza de recursos

**Alternativa:** Usar configuración de AWS CLI o roles de AWS Identity and Access Management (AWS IAM).

</details>

## 📚 Scripts de Aprendizaje

**Ruta de Aprendizaje Recomendada:**

### 1. 📊 Configuración de Datos de Ejemplo
**Archivo**: `scripts/setup_sample_data.py`
**Propósito**: Crea recursos IoT realistas para aprendizaje práctico con etiquetado automático
**Crea**: 20 Things, 3 Thing Types, 4 Thing Groups, Reglas IoT (con etiquetas de taller)

**Características Clave:**
- **Etiquetado Automático**: Todos los recursos se etiquetan para identificación segura durante la limpieza
- **Prefijos Personalizados**: Soporte para prefijos personalizados de nombres de things
- **Multi-Idioma**: Soporte completo de internacionalización

**Ejemplos de Uso:**
```bash
# Configuración básica con prefijo predeterminado (Vehicle-VIN-)
python scripts/setup_sample_data.py

# Configuración con prefijo personalizado
python scripts/setup_sample_data.py --things-prefix "MiDispositivo-"

# Configuración con selección de idioma
export AWS_IOT_LANG=es
python scripts/setup_sample_data.py
```

**Etiquetado de Recursos:**
Todos los recursos creados reciben estas etiquetas para identificación segura:
- `workshop-resource: true` - Marca como creado por el taller
- `created-by: setup-script` - Identifica el script creador
- `workshop-name: iot-core-basics` - Agrupa por nombre del taller

Estas etiquetas permiten que el script de limpieza identifique y elimine de forma segura solo los recursos del taller, protegiendo tu infraestructura IoT de producción.

### 2. 🔍 Explorador de API del Registro IoT
**Archivo**: `scripts/iot_registry_explorer.py`
**Propósito**: Herramienta interactiva para aprender APIs del Registro AWS IoT
**Características**: 8 APIs principales con explicaciones detalladas y llamadas de API reales

### 3. 🔐 Gerenciador de Certificados y Políticas
**Archivo**: `scripts/certificate_manager.py`
**Propósito**: Aprender seguridad AWS IoT a través del gerenciamiento de certificados y políticas
**Características**: Creación de certificados, anexación de políticas, registro de certificados externos

### 4. 📡 Comunicación MQTT
**Archivos**: 
- `scripts/mqtt_client_explorer.py` (Basado en certificados, recomendado)
- `scripts/mqtt_websocket_explorer.py` (Alternativa basada en WebSocket)

**Propósito**: Experimentar comunicación IoT en tiempo real usando protocolo MQTT
**Características**: Interfaz de línea de comandos interactiva, suscripción de tópicos, publicación de mensajes

### 5. 🌟 Explorador de AWS IoT Device Shadow service
**Archivo**: `scripts/device_shadow_explorer.py`
**Propósito**: Aprender sincronización de estado de dispositivos con AWS IoT Device Shadow
**Características**: Gerenciamiento interactivo de shadow, actualizaciones de estado, procesamiento de delta

### 6. ⚙️ Explorador del IoT Rules Engine
**Archivo**: `scripts/iot_rules_explorer.py`
**Propósito**: Aprender enrutamiento y procesamiento de mensajes con IoT Rules Engine
**Características**: Creación de reglas, filtrado SQL, configuración automática de AWS IAM

### 7. 🧹 Limpieza de Datos de Ejemplo
**Archivo**: `scripts/cleanup_sample_data.py`
**Propósito**: Limpiar todos los recursos de aprendizaje para evitar costos
**Características**: Limpieza segura con tratamiento de dependencias

## 🧹 Limpieza de Recursos

**⚠️ IMPORTANTE**: Siempre ejecuta la limpieza cuando termines de aprender para evitar cargos continuos de AWS.

### Uso Básico

```bash
# Limpieza estándar - elimina todos los recursos del taller
python scripts/cleanup_sample_data.py

# Vista previa de lo que se eliminará (paso recomendado primero)
python scripts/cleanup_sample_data.py --dry-run

# Limpieza con prefijo personalizado
python scripts/cleanup_sample_data.py --things-prefix "MiDispositivo-"

# Habilitar modo debug para registro detallado de API
python scripts/cleanup_sample_data.py --debug
```

### Parámetros de Línea de Comandos

| Parámetro | Descripción | Predeterminado | Ejemplo |
|-----------|-------------|---------|---------|
| `--things-prefix` | Prefijo personalizado para nombres de things | `Vehicle-VIN-` | `--things-prefix "DispositivoPrueba-"` |
| `--dry-run` | Vista previa de limpieza sin eliminar | `False` | `--dry-run` |
| `--debug` | Habilitar registro detallado de API | `False` | `--debug` |

### Cómo Funciona la Identificación de Recursos

El script de limpieza utiliza un **sistema de identificación dual** para identificar de forma segura los recursos del taller:

**1. Identificación Basada en Etiquetas (Método Principal)**
- Los recursos creados por los scripts de configuración se etiquetan automáticamente con:
  - `workshop-resource: true` - Identifica recursos creados por el taller
  - `created-by: setup-script` - Rastrea qué script creó el recurso
  - `workshop-name: iot-core-basics` - Agrupa recursos por taller
- **Ventaja**: Método más confiable, funciona independientemente del nombre

**2. Convención de Nombres de Respaldo (Método Secundario)**
- Si las etiquetas no están presentes, el script identifica recursos por patrones de nombres:
  - Things: Coinciden con el patrón `--things-prefix` (predeterminado: `Vehicle-VIN-`)
  - Thing Types: `SedanVehicle`, `SUVVehicle`, `TruckVehicle`
  - Thing Groups: `CustomerFleet`, `TestFleet`, `MaintenanceFleet`, `DealerFleet`
  - Reglas IoT: Coinciden con patrones `*Rule`, `rule_*`, o `*_workshop_*`
- **Ventaja**: Funciona con recursos creados antes de implementar el etiquetado

### Modo Dry-Run (Paso Recomendado Primero)

**Siempre previsualiza las operaciones de limpieza antes de ejecutarlas:**

```bash
python scripts/cleanup_sample_data.py --dry-run
```

**El modo dry-run:**
- ✅ Identifica todos los recursos del taller que se eliminarían
- ✅ Muestra una lista detallada de recursos por tipo
- ✅ Muestra el orden de eliminación (respeta dependencias)
- ✅ Genera un informe resumen
- ❌ **NO elimina ningún recurso**

**Ejemplo de salida dry-run:**
```
🔍 MODO DRY RUN - No se eliminarán recursos

Recursos Identificados:
  Things: 20 recursos
    - Vehicle-VIN-001
    - Vehicle-VIN-002
    ...
  Certificados: 20 recursos
  Thing Groups: 4 recursos
  Thing Types: 3 recursos
  Reglas IoT: 1 recurso

Total: 48 recursos se eliminarían
```

### Uso de Prefijo Personalizado

Si creaste recursos con un prefijo personalizado durante la configuración, usa el mismo prefijo para la limpieza:

```bash
# Configuración con prefijo personalizado
python scripts/setup_sample_data.py --things-prefix "MiDispositivo-"

# Limpieza con prefijo coincidente
python scripts/cleanup_sample_data.py --things-prefix "MiDispositivo-"
```

**Importante**: El prefijo debe coincidir exactamente entre configuración y limpieza para que la identificación basada en nombres funcione correctamente.

### Qué se Limpia

**Recursos Eliminados (en orden de dependencia):**
1. ✅ Thing Shadows (datos de estado del dispositivo)
2. ✅ Certificados (desconectados de things primero)
3. ✅ Things (dispositivos IoT)
4. ✅ Reglas IoT (reglas de enrutamiento de mensajes)
5. ✅ Thing Groups (colecciones de dispositivos)
6. ✅ Thing Types (plantillas de dispositivos)
7. ✅ Políticas (políticas de seguridad)
8. ✅ Archivos de certificados locales (del directorio `certs/`)

**Recursos Protegidos:**
- ❌ Recursos IoT de producción (sin etiquetas de taller)
- ❌ Recursos con patrones de nombres diferentes
- ❌ Certificados y políticas no asociados con things del taller
- ❌ Recursos creados fuera de los scripts del taller

### Eliminación Consciente de Dependencias

El script de limpieza maneja automáticamente las dependencias de recursos de AWS IoT:

**Orden de Eliminación:**
```
Thing Shadows → Certificados → Things → Reglas IoT → Thing Groups → Thing Types → Políticas
```

**Por qué importa este orden:**
- Thing Shadows deben eliminarse antes que los certificados
- Los certificados deben desconectarse antes de que se puedan eliminar los things
- Los things deben eliminarse de los grupos antes de que se puedan eliminar los grupos
- Las políticas deben desconectarse antes de la eliminación

**El script maneja esto automáticamente** - no necesitas preocuparte por conflictos de dependencias.

### Entendiendo el Informe Resumen

Después de completar la limpieza, verás un informe resumen:

```
📊 Resumen de Limpieza

Tipo de Recurso  | Identificados | Eliminados | Fallidos
-----------------|---------------|------------|----------
Things           |            20 |         20 |        0
Certificados     |            20 |         20 |        0
Thing Groups     |             4 |          4 |        0
Thing Types      |             3 |          3 |        0
Reglas IoT       |             1 |          1 |        0
Políticas        |            20 |         20 |        0
-----------------|---------------|------------|----------
Total            |            68 |         68 |        0

✅ ¡Limpieza completada exitosamente!
```

**Campos del Informe:**
- **Identificados**: Recursos encontrados que coinciden con los criterios del taller
- **Eliminados**: Recursos eliminados exitosamente
- **Fallidos**: Recursos que no pudieron eliminarse (con detalles de error)

### Solución de Problemas de Limpieza

**Problema: "No se encontraron recursos"**
- **Causa**: Los recursos pueden no tener etiquetas de taller o no coinciden con el prefijo
- **Solución**: 
  - Verifica si usaste un prefijo personalizado durante la configuración
  - Usa `--things-prefix` con el prefijo correcto
  - Verifica que los recursos existan en la Consola de AWS

**Problema: Errores de "Permiso denegado"**
- **Causa**: Las credenciales de AWS carecen de los permisos IoT necesarios
- **Solución**: Asegúrate de que tu usuario/rol IAM tenga permisos de acceso completo a IoT

**Problema: Errores de "Conflicto de dependencia"**
- **Causa**: Los recursos tienen dependencias que no se manejaron
- **Solución**: El script debería manejar esto automáticamente. Si persiste, ejecuta con `--debug` para ver detalles

**Problema: Algunos recursos no se eliminaron**
- **Causa**: Los recursos pueden estar en uso o tener dependencias externas
- **Solución**: 
  - Verifica el informe resumen para recursos fallidos
  - Usa la Consola de AWS para inspeccionar y eliminar manualmente los recursos restantes
  - Ejecuta la limpieza nuevamente después de resolver las dependencias

### Mejores Prácticas

1. **Siempre usa dry-run primero**: Previsualiza lo que se eliminará antes de ejecutar
2. **Coincide los prefijos**: Usa el mismo `--things-prefix` para configuración y limpieza
3. **Revisa el resumen**: Verifica el informe para asegurarte de que todos los recursos se eliminaron
4. **Ejecuta la limpieza prontamente**: No dejes recursos del taller ejecutándose para evitar cargos
5. **Mantén las credenciales seguras**: Nunca confirmes credenciales de AWS en control de versiones

## ❓ Preguntas Frecuentes (FAQ)

### Preguntas Generales

**P: ¿Qué recursos eliminará el script de limpieza?**
R: El script de limpieza identifica y elimina recursos creados por los scripts de configuración del taller. Esto incluye Things, Certificados, Thing Groups, Thing Types, Reglas IoT y Políticas que tienen etiquetas de taller o coinciden con los patrones de nombres. Los recursos de producción están protegidos.

**P: ¿Cómo puedo previsualizar la limpieza sin eliminar nada?**
R: Usa la bandera `--dry-run`:
```bash
python scripts/cleanup_sample_data.py --dry-run
```
Esto muestra exactamente lo que se eliminaría sin hacer ningún cambio.

**P: ¿Puedo usar un prefijo personalizado para los nombres de things?**
R: ¡Sí! Usa el parámetro `--things-prefix` tanto en configuración como en limpieza:
```bash
# Configuración
python scripts/setup_sample_data.py --things-prefix "MiDispositivo-"

# Limpieza
python scripts/cleanup_sample_data.py --things-prefix "MiDispositivo-"
```

**P: ¿Qué pasa si no tengo etiquetas en mis recursos?**
R: El script de limpieza tiene un mecanismo de respaldo. Si las etiquetas no están presentes, usa convenciones de nombres para identificar recursos del taller. Los recursos que coincidan con el patrón de prefijo de thing (predeterminado: `Vehicle-VIN-`) o nombres estándar del taller serán identificados.

**P: ¿Cómo cambio el idioma?**
R: Establece la variable de entorno `AWS_IOT_LANG`:
```bash
export AWS_IOT_LANG=es  # Español
export AWS_IOT_LANG=ja  # Japonés
export AWS_IOT_LANG=zh-CN  # Chino
export AWS_IOT_LANG=pt-BR  # Portugués
export AWS_IOT_LANG=ko  # Coreano
```
O ejecuta el script sin establecerla - se te pedirá que selecciones un idioma interactivamente.

**P: ¿Qué pasa si la limpieza falla a mitad de camino?**
R: El script de limpieza está diseñado para ser idempotente - puedes ejecutarlo múltiples veces de forma segura. Si la limpieza falla:
1. Verifica el informe resumen para ver qué recursos fallaron
2. Ejecuta el script nuevamente - omitirá los recursos ya eliminados
3. Usa el modo `--debug` para ver mensajes de error detallados
4. Elimina manualmente los recursos restantes a través de la Consola de AWS si es necesario

**P: ¿Cómo verifico que los recursos fueron eliminados?**
R: Verifica el informe resumen al final de la limpieza. También puedes verificar en la Consola de AWS IoT:
- Navega a AWS IoT Core → Administrar → Things
- Verifica que los things del taller (Vehicle-VIN-*) se hayan ido
- Verifica que Thing Groups, Thing Types y Certificados se hayan eliminado

### Preguntas Técnicas

**P: ¿Por qué el script de limpieza elimina recursos en un orden específico?**
R: Los recursos de AWS IoT tienen dependencias. Por ejemplo, no puedes eliminar un Thing que todavía tiene certificados adjuntos. El script sigue este orden:
1. Thing Shadows (sin dependencias)
2. Certificados (deben desconectarse de things)
3. Things (deben eliminarse de grupos)
4. Reglas IoT (sin dependencias en things)
5. Thing Groups (deben estar vacíos)
6. Thing Types (no deben estar en uso)
7. Políticas (deben estar desconectadas)

**P: ¿Cuál es la diferencia entre identificación basada en etiquetas y basada en nombres?**
R: 
- **Basada en etiquetas** (principal): Usa etiquetas de recursos de AWS (`workshop-resource: true`). Más confiable, funciona independientemente del nombre.
- **Basada en nombres** (respaldo): Usa patrones de nombres (ej., `Vehicle-VIN-*`). Funciona con recursos antiguos creados antes de implementar el etiquetado.

El script intenta primero basado en etiquetas, luego recurre a patrones de nombres si las etiquetas no están presentes.

**P: ¿Puedo usar esto en una cuenta de AWS de producción?**
R: Aunque el script de limpieza tiene múltiples mecanismos de seguridad (etiquetas, patrones de nombres, modo dry-run), **recomendamos encarecidamente usar una cuenta de AWS dedicada para desarrollo/aprendizaje**. Esto sigue las mejores prácticas de AWS para aislamiento de entornos.

**P: ¿Qué pasa si interrumpo la limpieza con Ctrl+C?**
R: El script maneja las interrupciones con gracia. Los recursos eliminados antes de la interrupción permanecen eliminados. Simplemente ejecuta el script de limpieza nuevamente para continuar - omitirá los recursos ya eliminados y completará las eliminaciones restantes.

**P: ¿Cuánto cuesta ejecutar estos scripts de aprendizaje?**
R: Aproximadamente $0.17 USD por una sesión completa de aprendizaje. Consulta la sección [Información de Costos](#información-de-costos) para un desglose detallado. Siempre ejecuta la limpieza cuando termines para evitar cargos continuos.

## 🛠️ Solución de Problemas

**Soluciones Rápidas:**
- **Credenciales**: `aws sts get-caller-identity`
- **Región**: `export AWS_DEFAULT_REGION=us-east-1`
- **Dependencias**: `pip install --upgrade -r requirements.txt`
- **Modo debug**: Agregar bandera `--debug` a cualquier script

**📋 Guía Completa de Solución de Problemas**: Ver [Documentación de Solución de Problemas](docs/es/TROUBLESHOOTING.md) para soluciones detalladas a problemas comunes, problemas de conexión MQTT, errores de certificados y más.

## 📖 Documentación Avanzada

### Documentación Detallada

- **[📚 Documentación Detallada de Scripts](docs/es/DETAILED_SCRIPTS.md)** - Guías completas para cada script de aprendizaje
- **[🛠️ Guía de Solución de Problemas](docs/es/TROUBLESHOOTING.md)** - Soluciones para problemas y errores comunes
- **[📋 Ejemplos de Uso](docs/es/EXAMPLES.md)** - Flujos de trabajo completos y ejemplos interactivos


### Estructura del Proyecto

```
├── scripts/
│   ├── setup_sample_data.py          # Crea recursos IoT de ejemplo
│   ├── iot_registry_explorer.py      # Explorador interactivo de API
│   ├── certificate_manager.py        # Gestión de certificados y políticas
│   ├── mqtt_client_explorer.py       # Cliente MQTT basado en certificados
│   ├── mqtt_websocket_explorer.py    # Cliente MQTT WebSocket
│   ├── device_shadow_explorer.py     # Herramienta de aprendizaje Device Shadow
│   ├── iot_rules_explorer.py         # Herramienta de aprendizaje IoT Rules Engine
│   └── cleanup_sample_data.py        # Limpieza segura de recursos de ejemplo
├── docs/
│   ├── es/                           # Documentación en español
│   └── en/                           # Documentación en inglés
├── requirements.txt                   # Dependencias de Python
├── certificates/                      # Almacenamiento local de certificados (auto-creado)
└── README.md                         # Documentación principal del proyecto
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee nuestras [pautas de contribución](CONTRIBUTING.md) antes de enviar pull requests.

### Recursos de Aprendizaje

#### Documentación de AWS IoT Core
- **[Guía del Desarrollador de AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/)** - Guía completa del desarrollador
- **[Referencia de API de AWS IoT Core](https://docs.aws.amazon.com/iot/latest/apireference/)** - Documentación de API

#### SDKs de AWS Utilizados en Este Proyecto
- **[Documentación de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - Documentación completa del SDK de Python
- **[Referencia del Cliente IoT de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html)** - Métodos de API específicos de IoT
- **[SDK de Dispositivos AWS IoT para Python v2](https://aws.github.io/aws-iot-device-sdk-python-v2/)** - Documentación del cliente MQTT
- **[GitHub del SDK de Dispositivos AWS IoT](https://github.com/aws/aws-iot-device-sdk-python-v2)** - Código fuente y ejemplos

#### Protocolos y Estándares
- **[Especificación del Protocolo MQTT](https://mqtt.org/)** - Documentación oficial de MQTT
- **[Estándar de Certificados X.509](https://tools.ietf.org/html/rfc5280)** - Especificación del formato de certificados

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT-0. Ver el archivo [LICENSE](LICENSE) para detalles.

## 🆘 Soporte

- **Problemas**: [GitHub Issues](https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics/issues)
- **Documentación**: [AWS IoT Core Developer Guide](https://docs.aws.amazon.com/iot/latest/developerguide/)
- **Foros de AWS**: [AWS IoT Forum](https://forums.aws.amazon.com/forum.jspa?forumID=210)