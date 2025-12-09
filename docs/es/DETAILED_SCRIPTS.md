# Documentación Detallada de Scripts

> 🌍 **Idiomas Disponibles**: [English](../en/DETAILED_SCRIPTS.md) | **Español** (Actual)

Este documento proporciona documentación completa para todos los scripts de aprendizaje en el proyecto AWS IoT Core - Conceptos Básicos.

## Tabla de Contenidos

- [Configuración de Datos de Ejemplo](#configuración-de-datos-de-ejemplo)
- [Limpieza de Datos de Ejemplo](#limpieza-de-datos-de-ejemplo)
- [Explorador de API del Registro IoT](#explorador-de-api-del-registro-iot)
- [Gestor de Certificados y Políticas](#gestor-de-certificados-y-políticas)
- [Comunicación MQTT](#comunicación-mqtt)
- [Explorador de AWS IoT Device Shadow service](#explorador-de-device-shadow)
- [Explorador del Motor de Reglas IoT](#explorador-del-motor-de-reglas-iot)

## Configuración de Datos de Ejemplo

### Propósito
Crea un entorno de aprendizaje completo de AWS IoT con Thing Types, Thing Groups y Things de ejemplo. Este script configura una flota simulada de vehículos con jerarquías organizacionales apropiadas, permitiéndote explorar las APIs de AWS IoT Core sin necesidad de dispositivos físicos.

### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/setup_sample_data.py
```

**Con Modo Debug (operaciones detalladas de API):**
```bash
python scripts/setup_sample_data.py --debug
```

**Con Prefijo Personalizado (para múltiples entornos):**
```bash
python scripts/setup_sample_data.py --things-prefix MyTest
```

### Opciones de Línea de Comandos

#### `--things-prefix PREFIX`
Personaliza el prefijo del nombre del Thing para crear múltiples entornos aislados o evitar conflictos de nombres.

**Reglas de Validación:**
- Debe tener entre 3-20 caracteres
- Solo caracteres alfanuméricos (a-z, A-Z, 0-9)
- Sin espacios ni caracteres especiales
- Distingue entre mayúsculas y minúsculas

**Ejemplos:**
```bash
# Entorno de desarrollo
python scripts/setup_sample_data.py --things-prefix Dev

# Entorno de pruebas
python scripts/setup_sample_data.py --things-prefix Test

# Entorno de equipo
python scripts/setup_sample_data.py --things-prefix TeamA
```

**Nomenclatura de Things Resultante:**
- Prefijo predeterminado: `Vehicle-VIN-001`, `Vehicle-VIN-002`, ...
- Con `--things-prefix Dev`: `Dev-VIN-001`, `Dev-VIN-002`, ...
- Con `--things-prefix Test`: `Test-VIN-001`, `Test-VIN-002`, ...

#### `--debug`
Habilita el logging detallado mostrando todas las llamadas de API de AWS, parámetros de solicitud y cargas útiles de respuesta. Útil para aprender las APIs de AWS IoT o solucionar problemas.

### Recursos Creados

El script crea una jerarquía completa de recursos de AWS IoT:

#### Thing Types (3)
Plantillas que definen categorías de vehículos con atributos buscables:
- **SedanVehicle** - Vehículos de pasajeros estándar
- **SUVVehicle** - Vehículos utilitarios deportivos
- **TruckVehicle** - Vehículos comerciales

#### Thing Groups (4)
Contenedores organizacionales para gestión de flotas:
- **CustomerFleet** - Grupo principal para todos los vehículos de clientes
- **TestFleet** - Vehículos de prueba y desarrollo
- **MaintenanceFleet** - Vehículos que requieren servicio
- **DealerFleet** - Inventario del concesionario

#### Things (20)
Representaciones de dispositivos individuales con atributos:
- Nombres: `{prefix}-VIN-001` a `{prefix}-VIN-020`
- Atributos: VIN, modelo, año, color, ubicación
- Distribución de tipos: Mezcla de Sedan, SUV y Truck
- Membresía de grupos: Asignados a grupos apropiados

### Características de Seguridad

**Verificación de Duplicados:**
- Verifica recursos existentes antes de crear
- Omite la creación si los recursos ya existen
- Previene errores de nombres duplicados

**Validación de Entrada:**
- Valida el formato del prefijo antes de la creación
- Proporciona mensajes de error claros
- Sugiere formatos correctos si la validación falla

**Operación Idempotente:**
- Seguro ejecutar múltiples veces
- No crea recursos duplicados
- Reporta el estado existente de recursos

### Casos de Uso

#### Caso de Uso 1: Entorno de Aprendizaje Estándar
```bash
# Crear datos de ejemplo predeterminados
python scripts/setup_sample_data.py

# Explorar con scripts de aprendizaje
python scripts/iot_registry_explorer.py
python scripts/certificate_manager.py
```

#### Caso de Uso 2: Múltiples Entornos Aislados
```bash
# Entorno de desarrollo
python scripts/setup_sample_data.py --things-prefix Dev

# Entorno de pruebas
python scripts/setup_sample_data.py --things-prefix Test

# Entorno de producción
python scripts/setup_sample_data.py --things-prefix Prod
```

#### Caso de Uso 3: Configuración de Taller de Equipo
```bash
# Crear entornos separados para miembros del equipo
python scripts/setup_sample_data.py --things-prefix Alice
python scripts/setup_sample_data.py --things-prefix Bob
python scripts/setup_sample_data.py --things-prefix Carol
```

### Salida de Ejemplo

```
🚀 Configurando Datos de Ejemplo de AWS IoT Core
================================================

🔧 Paso 1: Creando Thing Types
Creating Thing Type: SedanVehicle
✅ Created Thing Type: SedanVehicle
Creating Thing Type: SUVVehicle
✅ Created Thing Type: SUVVehicle
Creating Thing Type: TruckVehicle
✅ Created Thing Type: TruckVehicle

🔧 Paso 2: Creando Thing Groups
Creating Thing Group: CustomerFleet
✅ Created Thing Group: CustomerFleet
Creating Thing Group: TestFleet
✅ Created Thing Group: TestFleet
Creating Thing Group: MaintenanceFleet
✅ Created Thing Group: MaintenanceFleet
Creating Thing Group: DealerFleet
✅ Created Thing Group: DealerFleet

🔧 Paso 3: Creando Things
Creating Thing: Vehicle-VIN-001
✅ Created Thing: Vehicle-VIN-001
Creating Thing: Vehicle-VIN-002
✅ Created Thing: Vehicle-VIN-002
...
Creating Thing: Vehicle-VIN-020
✅ Created Thing: Vehicle-VIN-020

🎉 Configuración completada exitosamente!
📊 Resumen de recursos creados:
   • Thing Types: 3
   • Thing Groups: 4
   • Things: 20

💡 Próximos pasos:
   1. Explorar recursos: python scripts/iot_registry_explorer.py
   2. Crear certificados: python scripts/certificate_manager.py
   3. Probar MQTT: python scripts/mqtt_client_explorer.py
```

### Solución de Problemas

**Error: "Thing name already exists"**
- Causa: Los recursos ya fueron creados
- Solución: Usar un prefijo diferente o ejecutar el script de limpieza primero

**Error: "Invalid prefix format"**
- Causa: El prefijo no cumple con los requisitos de validación
- Solución: Usar 3-20 caracteres alfanuméricos sin espacios

**Error: "Access denied"**
- Causa: Permisos insuficientes de AWS IAM
- Solución: Asegurar que las credenciales de AWS tengan permisos de IoT

## Limpieza de Datos de Ejemplo

### Propósito
Elimina de forma segura todos los recursos de AWS IoT creados por el script de configuración. Este script proporciona limpieza completa con características de seguridad para prevenir eliminaciones accidentales, incluyendo modo de ejecución en seco para vista previa y soporte de prefijos para limpieza dirigida.

### Cómo Ejecutar

**Uso Básico (Limpieza Interactiva):**
```bash
python scripts/cleanup_sample_data.py
```

**Modo de Ejecución en Seco (Vista Previa sin Eliminar):**
```bash
python scripts/cleanup_sample_data.py --dry-run
```

**Limpieza Dirigida con Prefijo:**
```bash
python scripts/cleanup_sample_data.py --things-prefix Dev
```

**Combinación de Opciones:**
```bash
# Vista previa de limpieza para prefijo específico
python scripts/cleanup_sample_data.py --dry-run --things-prefix Test

# Limpieza con logging detallado
python scripts/cleanup_sample_data.py --debug --things-prefix Prod
```

### Opciones de Línea de Comandos

#### `--dry-run`
Modo de vista previa que muestra qué recursos serían eliminados sin realizar eliminaciones reales.

**Características:**
- Identifica todos los recursos que coinciden con los criterios
- Muestra resumen detallado de recursos
- No realiza cambios en AWS
- Útil para verificar antes de la limpieza real

**Ejemplo de Salida:**
```
🔍 MODO DE EJECUCIÓN EN SECO - No se eliminarán recursos
================================================

📊 Recursos que serían eliminados:
   • Things: 20 (Vehicle-VIN-001 a Vehicle-VIN-020)
   • Certificados: 5
   • Thing Types: 3 (SedanVehicle, SUVVehicle, TruckVehicle)
   • Thing Groups: 4 (CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet)

💡 Para realizar la limpieza real, ejecutar sin --dry-run
```

#### `--things-prefix PREFIX`
Dirige la limpieza a Things con un prefijo específico, permitiendo limpieza selectiva de entornos.

**Reglas de Validación:**
- Debe tener entre 3-20 caracteres
- Solo caracteres alfanuméricos (a-z, A-Z, 0-9)
- Sin espacios ni caracteres especiales
- Distingue entre mayúsculas y minúsculas
- Debe coincidir con el prefijo usado durante la configuración

**Comportamiento:**
- Limpia solo Things que comienzan con el prefijo especificado
- Limpia certificados asociados con esos Things
- Preserva Thing Types y Thing Groups (compartidos entre entornos)
- Proporciona resumen de recursos específicos del prefijo

**Ejemplos:**
```bash
# Limpiar solo entorno de desarrollo
python scripts/cleanup_sample_data.py --things-prefix Dev

# Vista previa de limpieza de entorno de pruebas
python scripts/cleanup_sample_data.py --dry-run --things-prefix Test

# Limpiar entorno de equipo específico
python scripts/cleanup_sample_data.py --things-prefix TeamA
```

#### `--debug`
Habilita el logging detallado mostrando todas las llamadas de API de AWS, parámetros de solicitud y cargas útiles de respuesta.

### Proceso de Limpieza

El script sigue un orden específico para manejar dependencias de recursos:

#### Paso 1: Certificados
- Desadjunta certificados de Things
- Desadjunta políticas de certificados
- Desactiva certificados
- Elimina certificados
- Elimina archivos de certificados locales

#### Paso 2: Things
- Elimina Things del Registro de IoT
- Maneja dependencias de Thing Group
- Limpia metadatos de Thing

#### Paso 3: Thing Groups
- Elimina Thing Groups vacíos
- Respeta jerarquías de grupos
- Maneja relaciones padre-hijo

#### Paso 4: Thing Types
- Deprecia Thing Types (no se pueden eliminar)
- Marca tipos como no utilizables
- Preserva datos históricos

### Características de Seguridad

**Confirmación Interactiva:**
```
⚠️ Esta operación eliminará:
   • 20 Things (Vehicle-VIN-001 a Vehicle-VIN-020)
   • 5 Certificados y archivos locales
   • 3 Thing Types (serán depreciados)
   • 4 Thing Groups

¿Continuar con la limpieza? (y/N):
```

**Modo de Ejecución en Seco:**
- Vista previa de cambios antes de ejecutar
- Verifica el alcance de la limpieza
- Previene eliminaciones accidentales

**Limpieza Dirigida por Prefijo:**
- Limpia solo recursos específicos del entorno
- Preserva otros entornos
- Reduce el riesgo de eliminación de recursos incorrectos

**Manejo de Errores:**
- Continúa con otros recursos si uno falla
- Reporta errores claramente
- Proporciona resumen de operaciones exitosas/fallidas

### Casos de Uso

#### Caso de Uso 1: Limpieza Completa del Entorno
```bash
# Vista previa de qué se eliminará
python scripts/cleanup_sample_data.py --dry-run

# Realizar limpieza completa
python scripts/cleanup_sample_data.py
```

#### Caso de Uso 2: Limpieza de Entorno Específico
```bash
# Vista previa de limpieza de entorno de desarrollo
python scripts/cleanup_sample_data.py --dry-run --things-prefix Dev

# Limpiar solo entorno de desarrollo
python scripts/cleanup_sample_data.py --things-prefix Dev

# Entornos de pruebas y producción permanecen intactos
```

#### Caso de Uso 3: Limpieza de Taller de Equipo
```bash
# Cada miembro del equipo limpia su propio entorno
python scripts/cleanup_sample_data.py --things-prefix Alice
python scripts/cleanup_sample_data.py --things-prefix Bob
python scripts/cleanup_sample_data.py --things-prefix Carol
```

#### Caso de Uso 4: Verificación Antes de Limpieza
```bash
# Paso 1: Vista previa en modo de ejecución en seco
python scripts/cleanup_sample_data.py --dry-run --things-prefix Test

# Paso 2: Revisar salida y confirmar alcance

# Paso 3: Realizar limpieza real
python scripts/cleanup_sample_data.py --things-prefix Test
```

### Salida de Ejemplo

**Modo de Ejecución en Seco:**
```
🔍 MODO DE EJECUCIÓN EN SECO - No se eliminarán recursos
================================================

📊 Recursos que serían eliminados:
   • Things: 20 (Vehicle-VIN-001 a Vehicle-VIN-020)
   • Certificados: 5
   • Thing Types: 3 (SedanVehicle, SUVVehicle, TruckVehicle)
   • Thing Groups: 4 (CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet)

💡 Para realizar la limpieza real, ejecutar sin --dry-run
```

**Limpieza Real:**
```
🧹 Limpieza de Datos de Ejemplo de AWS IoT
==========================================

⚠️ Esta operación eliminará:
   • 20 Things (Vehicle-VIN-001 a Vehicle-VIN-020)
   • 5 Certificados y archivos locales
   • 3 Thing Types (serán depreciados)
   • 4 Thing Groups

¿Continuar con la limpieza? (y/N): y

🔧 Paso 1: Desadjuntando y eliminando certificados
✅ Certificado desadjuntado y eliminado para Vehicle-VIN-001
✅ Certificado desadjuntado y eliminado para Vehicle-VIN-002
...

🔧 Paso 2: Eliminando Things
✅ Thing eliminado: Vehicle-VIN-001
✅ Thing eliminado: Vehicle-VIN-002
...

🔧 Paso 3: Eliminando Thing Groups
✅ Thing Group eliminado: CustomerFleet
✅ Thing Group eliminado: TestFleet
✅ Thing Group eliminado: MaintenanceFleet
✅ Thing Group eliminado: DealerFleet

🔧 Paso 4: Depreciando Thing Types
✅ Thing Type depreciado: SedanVehicle
✅ Thing Type depreciado: SUVVehicle
✅ Thing Type depreciado: TruckVehicle

🎉 Limpieza completada exitosamente!
📊 Resumen:
   • Things eliminados: 20
   • Certificados eliminados: 5
   • Thing Groups eliminados: 4
   • Thing Types depreciados: 3
```

**Limpieza con Prefijo:**
```
🧹 Limpieza de Datos de Ejemplo de AWS IoT
==========================================
🎯 Dirigido a Things con prefijo: Dev

⚠️ Esta operación eliminará:
   • 20 Things (Dev-VIN-001 a Dev-VIN-020)
   • 3 Certificados asociados
   • Thing Types y Groups compartidos permanecerán

¿Continuar con la limpieza? (y/N): y

🔧 Limpiando recursos con prefijo 'Dev'...
✅ Thing eliminado: Dev-VIN-001
✅ Thing eliminado: Dev-VIN-002
...

🎉 Limpieza completada exitosamente!
📊 Resumen:
   • Things eliminados: 20 (prefijo: Dev)
   • Certificados eliminados: 3
```

### Solución de Problemas

**Error: "Resource has dependencies"**
- Causa: El Thing tiene certificados o políticas adjuntos
- Solución: El script maneja esto automáticamente, desadjuntando primero

**Error: "Thing Type cannot be deleted"**
- Causa: Los Thing Types de AWS IoT no se pueden eliminar, solo depreciar
- Solución: Esto es comportamiento esperado, el script deprecia en su lugar

**Error: "Access denied"**
- Causa: Permisos insuficientes de AWS IAM
- Solución: Asegurar que las credenciales de AWS tengan permisos de IoT

**Advertencia: "Certificate files not found locally"**
- Causa: Los archivos de certificados ya fueron eliminados o nunca se crearon
- Solución: Esto es seguro de ignorar, el script continúa con la limpieza

### Mejores Prácticas

1. **Siempre usar --dry-run primero** para vista previa de cambios
2. **Usar prefijos** para entornos múltiples para habilitar limpieza selectiva
3. **Verificar el alcance** antes de confirmar la limpieza
4. **Mantener respaldos** de certificados importantes antes de limpiar
5. **Documentar prefijos** usados para diferentes entornos
6. **Limpiar regularmente** entornos de prueba no utilizados

## Explorador de API del Registro IoT

### Propósito
Herramienta interactiva para aprender las APIs del Registro de AWS IoT a través de llamadas reales de API con explicaciones detalladas. Este script te enseña las operaciones del Plano de Control utilizadas para gestionar dispositivos IoT, certificados y políticas.

**Nota**: AWS IoT Core proporciona muchas APIs a través de la gestión de dispositivos y seguridad. Este explorador se enfoca en 8 APIs centrales del Registro que son esenciales para entender la gestión del ciclo de vida de dispositivos IoT.

### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/iot_registry_explorer.py
```

**Con Modo Debug (detalles mejorados de API):**
```bash
python scripts/iot_registry_explorer.py --debug
```

### Sistema de Menú Interactivo

Cuando ejecutes el script, verás:
```
📋 Operaciones Disponibles:
1. Listar Things
2. Listar Certificados
3. Listar Thing Groups
4. Listar Thing Types
5. Describir Thing
6. Describir Thing Group
7. Describir Thing Type
8. Describir Endpoint
9. Salir

Seleccionar operación (1-9):
```

### APIs Soportadas con Detalles de Aprendizaje

#### 1. Listar Things
- **Propósito**: Recuperar todos los dispositivos IoT (Things) en tu cuenta
- **HTTP**: `GET /things`
- **Aprender**: Descubrimiento de dispositivos con opciones de paginación y filtrado
- **Opciones Disponibles**:
  - **Listado básico**: Muestra todos los Things
  - **Paginación**: Recuperar Things en lotes más pequeños
  - **Filtrar por Thing Type**: Encontrar vehículos de categorías específicas
  - **Filtrar por Atributo**: Encontrar vehículos con atributos específicos
- **Salida**: Array de objetos Thing con nombres, tipos, atributos

#### 2. Listar Certificados
- **Propósito**: Ver todos los certificados X.509 para autenticación de dispositivos
- **HTTP**: `GET /certificates`
- **Aprender**: Ciclo de vida de certificados, gestión de estado
- **Salida**: IDs de certificados, ARNs, fechas de creación, estado

#### 3. Listar Thing Groups
- **Propósito**: Ver organización de dispositivos y jerarquías
- **HTTP**: `GET /thing-groups`
- **Aprender**: Estrategias de agrupación de dispositivos, gestión a escala
- **Salida**: Nombres de grupos, ARNs, propiedades básicas

#### 4. Listar Thing Types
- **Propósito**: Ver plantillas de dispositivos y categorías
- **HTTP**: `GET /thing-types`
- **Aprender**: Clasificación de dispositivos, esquemas de atributos
- **Salida**: Nombres de tipos, descripciones, atributos buscables

#### 5. Describir Thing
- **Propósito**: Obtener información detallada sobre un dispositivo específico
- **HTTP**: `GET /things/{thingName}`
- **Entrada Requerida**: Nombre del Thing (ej. "Vehicle-VIN-001")
- **Aprender**: Metadatos de dispositivos, atributos, relaciones
- **Salida**: Detalles completos del Thing, versión, ARN

#### 6. Describir Thing Group
- **Propósito**: Ver detalles y propiedades del grupo
- **HTTP**: `GET /thing-groups/{thingGroupName}`
- **Entrada Requerida**: Nombre del grupo (ej. "CustomerFleet")
- **Aprender**: Jerarquías de grupos, políticas, atributos
- **Salida**: Propiedades del grupo, relaciones padre/hijo

#### 7. Describir Thing Type
- **Propósito**: Ver especificaciones y plantillas de tipos
- **HTTP**: `GET /thing-types/{thingTypeName}`
- **Entrada Requerida**: Nombre del tipo (ej. "SedanVehicle")
- **Aprender**: Definiciones de tipos, atributos buscables
- **Salida**: Propiedades del tipo, metadatos de creación

#### 8. Describir Endpoint
- **Propósito**: Obtener URLs de endpoint IoT para tu cuenta
- **HTTP**: `GET /endpoint`
- **Opciones de Entrada**: Tipo de endpoint (iot:Data-ATS, iot:CredentialProvider, iot:Jobs)
- **Aprender**: Diferentes tipos de endpoint y sus propósitos (iot:Jobs es para AWS IoT Jobs service)
- **Salida**: URL de endpoint HTTPS para conexiones de dispositivos
- **Salida**: URL de endpoint HTTPS para conexiones de dispositivos

### Características de Aprendizaje

**Para cada llamada de API, verás:**
- 🔄 **Nombre de llamada API** y descripción
- 🌐 **Solicitud HTTP** método y ruta completa
- ℹ️ **Explicación de operación** - qué hace y por qué
- 📥 **Parámetros de entrada** - qué datos estás enviando
- 💡 **Explicación de respuesta** - qué significa la salida
- 📤 **Payload de respuesta** - datos JSON reales devueltos

## Gestor de Certificados y Políticas

### Propósito
Aprender conceptos de seguridad de AWS IoT a través de gestión práctica de certificados y políticas. Este script enseña el modelo de seguridad completo: identidad de dispositivo (certificados) y autorización (políticas).

### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/certificate_manager.py
```

**Con Modo Debug (logging detallado de API):**
```bash
python scripts/certificate_manager.py --debug
```

### Menú Principal Interactivo

Cuando ejecutes el script, verás:
```
🔐 Gestor de Certificados y Políticas de AWS IoT
==================================================
Este script te enseña conceptos de seguridad de AWS IoT:
• Certificados X.509 para autenticación de dispositivos
• Adjuntar certificado a Thing
• Políticas IoT para autorización
• Adjuntar y desadjuntar políticas
• Registro de certificados externos
• Detalles completos de API para cada operación
==================================================

📋 Menú Principal:
1. Crear Certificado AWS IoT y Adjuntar a Thing (+ Política Opcional)
2. Registrar Certificado Externo y Adjuntar a Thing (+ Política Opcional)
3. Adjuntar Política a Certificado Existente
4. Desadjuntar Política de Certificado
5. Habilitar/Deshabilitar Certificado
6. Salir

Seleccionar opción (1-6):
```

### Áreas Clave de Aprendizaje

**Gestión de Certificados:**
- Creación y ciclo de vida de certificados X.509
- Adjuntar certificado-Thing para identidad de dispositivo
- Almacenamiento y organización de archivos locales
- Mejores prácticas de seguridad

**Gestión de Políticas:**
- Creación de políticas IoT con plantillas
- Adjuntar políticas a certificados
- Conceptos de control de permisos
- Consideraciones de seguridad de producción

**⚠️ Nota de Seguridad de Producción**: Las plantillas de políticas usan `"Resource": "*"` para propósitos de demostración. En producción, usa ARNs de recursos específicos y variables de política como `${iot:Connection.Thing.ThingName}` para restringir el acceso de dispositivos solo a sus recursos específicos.

## Comunicación MQTT

### Propósito
Experimentar comunicación IoT en tiempo real usando el protocolo MQTT. Aprender cómo los dispositivos se conectan a AWS IoT Core e intercambian mensajes de forma segura.

### Dos Opciones MQTT Disponibles

#### Opción A: MQTT Basado en Certificados (Recomendado para Aprendizaje)
**Archivo**: `scripts/mqtt_client_explorer.py`
**Autenticación**: Certificados X.509 (TLS mutuo)
**Mejor para**: Entender seguridad IoT de producción

#### Opción B: MQTT WebSocket (Método Alternativo)
**Archivo**: `scripts/mqtt_websocket_explorer.py`
**Autenticación**: Credenciales AWS IAM (SigV4)
**Mejor para**: Aplicaciones web y conexiones amigables con firewall

### Cliente MQTT Basado en Certificados

#### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/mqtt_client_explorer.py
```

**Con Modo Debug (diagnósticos de conexión):**
```bash
python scripts/mqtt_client_explorer.py --debug
```

#### Prerrequisitos
- **Los certificados deben existir** - Ejecutar `certificate_manager.py` primero
- **Política adjunta** - El certificado necesita permisos IoT
- **Asociación Thing** - El certificado debe estar adjunto a un Thing

#### Comandos Interactivos

Una vez conectado, usa estos comandos:

```bash
# Suscripción a Tópicos
📡 MQTT> sub device/+/temperature                  # Suscribirse con QoS 0
📡 MQTT> sub1 device/alerts/#                      # Suscribirse con QoS 1
📡 MQTT> unsub device/+/temperature               # Desuscribirse del tópico

# Publicación de Mensajes
📡 MQTT> pub device/sensor/temperature 23.5        # Publicar con QoS 0
📡 MQTT> pub1 device/alert "High temp!"            # Publicar con QoS 1
📡 MQTT> json device/data temp=23.5 humidity=65    # Publicar objeto JSON

# Comandos de Utilidad
📡 MQTT> test                                      # Enviar mensaje de prueba
📡 MQTT> status                                    # Mostrar info de conexión
📡 MQTT> messages                                  # Mostrar historial de mensajes
📡 MQTT> debug                                     # Diagnósticos de conexión
📡 MQTT> help                                      # Mostrar todos los comandos
📡 MQTT> quit                                      # Salir del cliente
```

## Explorador de AWS IoT Device Shadow service

### Propósito
Aprender el servicio AWS IoT Device Shadow a través de exploración práctica de sincronización de estado de dispositivos. Este script enseña el ciclo de vida completo del shadow: estado deseado, estado reportado y procesamiento delta.

### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/device_shadow_explorer.py
```

**Con Modo Debug (análisis detallado de mensajes shadow):**
```bash
python scripts/device_shadow_explorer.py --debug
```

### Prerrequisitos
- **Los certificados deben existir** - Ejecutar `certificate_manager.py` primero
- **Política con permisos shadow** - El certificado necesita permisos IoT shadow
- **Asociación Thing** - El certificado debe estar adjunto a un Thing

### Características Clave de Aprendizaje

#### Estructura del Documento Shadow
```json
{
  "state": {
    "desired": {
      "temperature": 25.0,
      "status": "active"
    },
    "reported": {
      "temperature": 22.5,
      "status": "online",
      "firmware_version": "1.0.0"
    },
    "delta": {
      "temperature": 25.0,
      "status": "active"
    }
  },
  "metadata": {
    "desired": {
      "temperature": {
        "timestamp": 1642248600
      }
    },
    "reported": {
      "temperature": {
        "timestamp": 1642248500
      }
    }
  },
  "version": 15,
  "timestamp": 1642248600
}
```

#### Comandos Interactivos

Una vez conectado, usa estos comandos:

```bash
# Operaciones Shadow
🌟 Shadow> get                                    # Solicitar documento shadow actual
🌟 Shadow> report                                 # Reportar estado local al shadow
🌟 Shadow> desire temperature=25.0 status=active # Establecer estado deseado

# Gestión de Dispositivo Local
🌟 Shadow> local                                  # Mostrar estado actual del dispositivo local
🌟 Shadow> edit                                   # Editar estado del dispositivo local interactivamente

# Comandos de Utilidad
🌟 Shadow> status                                 # Mostrar estado de conexión y shadow
🌟 Shadow> messages                               # Mostrar historial de mensajes shadow
🌟 Shadow> debug                                  # Diagnósticos de conexión
🌟 Shadow> help                                   # Mostrar todos los comandos
🌟 Shadow> quit                                   # Salir del explorador
```

## Explorador del Motor de Reglas IoT

### Propósito
Aprender el Motor de Reglas de AWS IoT a través de creación y gestión práctica de reglas. Este script enseña enrutamiento de mensajes, filtrado basado en SQL y configuración de acciones con configuración automática de roles AWS IAM.

### Cómo Ejecutar

**Uso Básico:**
```bash
python scripts/iot_rules_explorer.py
```

**Con Modo Debug (operaciones detalladas de API e AWS IAM):**
```bash
python scripts/iot_rules_explorer.py --debug
```

### Prerrequisitos
- **Credenciales AWS** - Permisos AWS IAM para Reglas IoT y gestión de roles AWS IAM
- **No se necesitan certificados** - El Motor de Reglas opera a nivel de servicio

### Características Clave de Aprendizaje

#### Flujo de Trabajo de Creación de Reglas
**Creación Guiada Paso a Paso:**
1. **Nomenclatura de Reglas** - Aprender convenciones de nomenclatura y requisitos de unicidad
2. **Selección de Tipo de Evento** - Elegir entre tipos de eventos IoT comunes o personalizados
3. **Construcción de Declaración SQL** - Construcción interactiva de cláusulas SELECT, FROM, WHERE
4. **Configuración de Acciones** - Configurar objetivos de republicación con roles AWS IAM apropiados
5. **Configuración Automática de AWS IAM** - El script crea y configura permisos necesarios

#### Ejemplos Completos de SQL
**Monitoreo de Temperatura:**
```sql
SELECT deviceId, timestamp, value 
FROM 'testRulesEngineTopic/+/temperature' 
WHERE value > 30
```

**Alertas de Batería:**
```sql
SELECT deviceId, battery, status 
FROM 'testRulesEngineTopic/+/battery' 
WHERE battery < 15
```

**Detección de Movimiento:**
```sql
SELECT * 
FROM 'testRulesEngineTopic/+/motion' 
WHERE value = 'detected'
```

### Configuración Automática de AWS IAM

#### Creación de Rol AWS IAM
**Configuración Automática:**
- Crea `IoTRulesEngineRole` si no existe
- Configura política de confianza para `iot.amazonaws.com`
- Adjunta permisos necesarios para acciones de republicación
- Maneja retrasos de consistencia eventual de AWS IAM

**📚 Aprender Más**: [Motor de Reglas de AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) | [Referencia SQL del Motor de Reglas](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html)