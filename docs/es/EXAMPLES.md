# Ejemplos de Uso

> 🌍 **Idiomas Disponibles**: [English](../en/EXAMPLES.md) | **Español** (Actual)

Esta guía proporciona ejemplos completos de flujos de trabajo y escenarios de uso para los scripts de aprendizaje de AWS IoT Core.

## Tabla de Contenidos

- [Flujo de Trabajo Completo](#flujo-de-trabajo-completo)
- [Ejemplos de Configuración y Limpieza](#ejemplos-de-configuración-y-limpieza)
- [Escenarios de Aprendizaje](#escenarios-de-aprendizaje)
- [Ejemplos de MQTT](#ejemplos-de-mqtt)
- [Ejemplos de AWS IoT Device Shadow service](#ejemplos-de-device-shadow)
- [Ejemplos del Motor de Reglas](#ejemplos-del-motor-de-reglas)
- [Casos de Uso del Mundo Real](#casos-de-uso-del-mundo-real)

## Flujo de Trabajo Completo

### Escenario: Configuración Completa de Aprendizaje IoT

Este ejemplo te guía a través de la experiencia completa de aprendizaje desde la configuración hasta la limpieza.

#### Paso 1: Configuración del Entorno
```bash
# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar credenciales AWS
export AWS_ACCESS_KEY_ID=<tu-clave>
export AWS_SECRET_ACCESS_KEY=<tu-clave-secreta>
export AWS_DEFAULT_REGION=us-east-1
```

#### Paso 2: Crear Datos de Ejemplo
```bash
python scripts/setup_sample_data.py --debug
```

**Salida Esperada:**
```
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
...

🔧 Paso 3: Creando Things
Creating Thing: Vehicle-VIN-001
✅ Created Thing: Vehicle-VIN-001
...

🎉 Configuración completada exitosamente!
📊 Resumen de recursos creados:
   • Thing Types: 3
   • Thing Groups: 4  
   • Things: 20
```

#### Paso 3: Explorar APIs del Registro
```bash
python scripts/iot_registry_explorer.py
```

**Ejemplo de Sesión Interactiva:**
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

Seleccionar operación (1-9): 1

📊 Encontrados 20 Things
   Nombres de Things:
   • Vehicle-VIN-001 (SedanVehicle)
   • Vehicle-VIN-002 (SUVVehicle)
   • Vehicle-VIN-003 (TruckVehicle)
   ...
```

#### Paso 4: Configurar Seguridad
```bash
python scripts/certificate_manager.py
```

**Ejemplo de Flujo de Certificados:**
```
📋 Menú Principal:
1. Crear Certificado AWS IoT y Adjuntar a Thing (+ Política Opcional)
...

Seleccionar opción (1-6): 1

📱 Things Disponibles (20 encontrados):
   1. Vehicle-VIN-001 (Tipo: SedanVehicle)
   2. Vehicle-VIN-002 (Tipo: SUVVehicle)
   ...

Tu elección: 1

✅ Thing seleccionado: Vehicle-VIN-001

🔐 Paso 1: Creando Certificado y Par de Claves
🔄 Creando certificado y par de claves...
✅ Creando certificado y par de claves completado

💾 Guardando archivos de certificado localmente...
✅ Archivos guardados en: certificates/Vehicle-VIN-001/

🔗 Adjuntando certificado a Thing: Vehicle-VIN-001
✅ Certificado adjuntado exitosamente
```

#### Paso 5: Comunicación MQTT
```bash
python scripts/mqtt_client_explorer.py
```

**Ejemplo de Sesión MQTT:**
```
📱 Dispositivos Disponibles con Certificados:
   1. Vehicle-VIN-001

Seleccionar dispositivo (1): 1

🔗 Conectando a AWS IoT Core...
✅ Conectado exitosamente como Vehicle-VIN-001

📡 MQTT> sub vehicle/+/temperature
✅ [14:30:10.123] SUSCRITO a vehicle/+/temperature (QoS: 0)

📡 MQTT> pub vehicle/001/temperature 23.5
✅ [14:30:15.456] PUBLICADO
   📤 Tópico: vehicle/001/temperature
   🏷️  QoS: 0 | ID de Paquete: 1
   📊 Tamaño: 4 bytes

======================================================================
🔔 MENSAJE ENTRANTE #1 [14:30:15.789]
======================================================================
📥 Tópico: vehicle/001/temperature
🏷️  QoS: 0 (A lo sumo una vez)
📊 Tamaño del Payload: 4 bytes
💬 Mensaje: 23.5
======================================================================
```

#### Paso 6: Explorar AWS IoT Device Shadow service
```bash
python scripts/device_shadow_explorer.py
```

**Ejemplo de Operaciones Shadow:**
```
🌟 Shadow> get
📥 Documento Shadow actual:
{
  "state": {
    "reported": {
      "temperature": 22.5,
      "status": "online"
    }
  },
  "version": 1
}

🌟 Shadow> desire temperature=25.0 status=active
✅ Estado deseado actualizado

🌟 Shadow> get
📥 Documento Shadow actual:
{
  "state": {
    "desired": {
      "temperature": 25.0,
      "status": "active"
    },
    "reported": {
      "temperature": 22.5,
      "status": "online"
    },
    "delta": {
      "temperature": 25.0,
      "status": "active"
    }
  },
  "version": 2
}
```

#### Paso 7: Crear Reglas IoT
```bash
python scripts/iot_rules_explorer.py
```

**Ejemplo de Creación de Regla:**
```
📋 Menú del Motor de Reglas IoT:
1. Listar todas las Reglas IoT
2. Describir Regla IoT específica
3. Crear nueva Regla IoT
...

Seleccionar opción (1-6): 3

📝 Ingresa nombre de regla: TemperatureAlert

🎯 Tipos de Eventos Disponibles:
   1. temperature
   2. humidity
   3. pressure
   ...

Seleccionar tipo de evento (1-8): 1

✅ Patrón de tópico: testRulesEngineTopic/+/temperature

🔍 Cláusula SELECT - Atributos para eventos temperature:
   1. *
   2. deviceId, timestamp, temperature
   3. deviceId, temperature, location

Seleccionar atributos (1-4): 2

✅ SELECT: deviceId, timestamp, temperature

🔍 Cláusula WHERE (Opcional) - Filtrar mensajes temperature:
💡 Ejemplos para temperature:
   • temperature > 25
   • temperature < 0
   • location = 'warehouse'

¿Agregar condición WHERE? (y/N): y
Ingresa condición WHERE: temperature > 30

✅ WHERE: temperature > 30

📝 Declaración SQL Completa:
   SELECT deviceId, timestamp, temperature FROM 'testRulesEngineTopic/+/temperature' WHERE temperature > 30

🎉 Regla 'TemperatureAlert' creada exitosamente!
```

#### Paso 8: Limpieza
```bash
python scripts/cleanup_sample_data.py
```

**Salida de Limpieza:**
```
🧹 Limpieza de Datos de Ejemplo de AWS IoT
==========================================

⚠️ Esta operación eliminará:
   • 20 Things (Vehicle-VIN-001 a Vehicle-VIN-020)
   • 3 Thing Types (SedanVehicle, SUVVehicle, TruckVehicle)
   • 4 Thing Groups (CustomerFleet, TestFleet, MaintenanceFleet, DealerFleet)
   • Certificados asociados y archivos locales

¿Continuar con la limpieza? (y/N): y

🔧 Paso 1: Desadjuntando y eliminando certificados
✅ Certificado desadjuntado y eliminado para Vehicle-VIN-001
...

🔧 Paso 2: Eliminando Things
✅ Thing eliminado: Vehicle-VIN-001
...

🔧 Paso 3: Eliminando Thing Groups
✅ Thing Group eliminado: CustomerFleet
...

🔧 Paso 4: Depreciando Thing Types
✅ Thing Type depreciado: SedanVehicle
...

🎉 Limpieza completada exitosamente!
```

## Ejemplos de Configuración y Limpieza

### Ejemplo 1: Configuración con Prefijo Personalizado

**Escenario:** Crear un entorno de desarrollo separado con nomenclatura personalizada.

```bash
# Crear entorno de desarrollo con prefijo personalizado
python scripts/setup_sample_data.py --things-prefix Dev

# Verificar recursos creados
python scripts/iot_registry_explorer.py
# Seleccionar opción 1 (Listar Things)
# Verás: Dev-VIN-001, Dev-VIN-002, etc.
```

**Salida Esperada:**
```
🚀 Configurando Datos de Ejemplo de AWS IoT Core
================================================
🎯 Usando prefijo de Thing: Dev

🔧 Paso 1: Creando Thing Types
✅ Created Thing Type: SedanVehicle
✅ Created Thing Type: SUVVehicle
✅ Created Thing Type: TruckVehicle

🔧 Paso 2: Creando Thing Groups
✅ Created Thing Group: CustomerFleet
✅ Created Thing Group: TestFleet
✅ Created Thing Group: MaintenanceFleet
✅ Created Thing Group: DealerFleet

🔧 Paso 3: Creando Things
✅ Created Thing: Dev-VIN-001
✅ Created Thing: Dev-VIN-002
...
✅ Created Thing: Dev-VIN-020

🎉 Configuración completada exitosamente!
📊 Resumen de recursos creados:
   • Thing Types: 3
   • Thing Groups: 4
   • Things: 20 (prefijo: Dev)
```

### Ejemplo 2: Configuración de Múltiples Entornos

**Escenario:** Crear entornos separados para desarrollo, pruebas y producción.

```bash
# Entorno de desarrollo
python scripts/setup_sample_data.py --things-prefix Dev

# Entorno de pruebas
python scripts/setup_sample_data.py --things-prefix Test

# Entorno de producción
python scripts/setup_sample_data.py --things-prefix Prod
```

**Resultado:**
- Entorno Dev: Dev-VIN-001 a Dev-VIN-020
- Entorno Test: Test-VIN-001 a Test-VIN-020
- Entorno Prod: Prod-VIN-001 a Prod-VIN-020
- Thing Types y Groups compartidos entre entornos

### Ejemplo 3: Modo de Ejecución en Seco para Vista Previa de Limpieza

**Escenario:** Verificar qué recursos serían eliminados antes de realizar la limpieza real.

```bash
# Vista previa de limpieza sin eliminar nada
python scripts/cleanup_sample_data.py --dry-run
```

**Salida Esperada:**
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

### Ejemplo 4: Limpieza Dirigida de Entorno Específico

**Escenario:** Limpiar solo el entorno de desarrollo mientras se preservan pruebas y producción.

```bash
# Paso 1: Vista previa de limpieza de entorno de desarrollo
python scripts/cleanup_sample_data.py --dry-run --things-prefix Dev

# Paso 2: Revisar salida y confirmar alcance

# Paso 3: Limpiar solo entorno de desarrollo
python scripts/cleanup_sample_data.py --things-prefix Dev
```

**Salida Esperada:**
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
✅ Thing eliminado: Dev-VIN-020

🎉 Limpieza completada exitosamente!
📊 Resumen:
   • Things eliminados: 20 (prefijo: Dev)
   • Certificados eliminados: 3
   • Thing Types y Groups preservados para otros entornos
```

### Ejemplo 5: Flujo de Trabajo Completo con Prefijos

**Escenario:** Ciclo completo de configuración, uso y limpieza con prefijos personalizados.

```bash
# 1. Crear entorno de prueba
python scripts/setup_sample_data.py --things-prefix Test

# 2. Explorar recursos
python scripts/iot_registry_explorer.py
# Verás Things con prefijo Test

# 3. Crear certificados para dispositivos de prueba
python scripts/certificate_manager.py
# Seleccionar Test-VIN-001, Test-VIN-002, etc.

# 4. Probar comunicación MQTT
python scripts/mqtt_client_explorer.py
# Conectar como dispositivos de prueba

# 5. Vista previa de limpieza
python scripts/cleanup_sample_data.py --dry-run --things-prefix Test

# 6. Limpiar entorno de prueba
python scripts/cleanup_sample_data.py --things-prefix Test
```

### Ejemplo 6: Configuración de Taller de Equipo

**Escenario:** Cada miembro del equipo tiene su propio entorno aislado.

```bash
# Alice crea su entorno
python scripts/setup_sample_data.py --things-prefix Alice

# Bob crea su entorno
python scripts/setup_sample_data.py --things-prefix Bob

# Carol crea su entorno
python scripts/setup_sample_data.py --things-prefix Carol

# Cada persona trabaja independientemente
# Alice explora sus recursos
python scripts/iot_registry_explorer.py
# Ve: Alice-VIN-001, Alice-VIN-002, etc.

# Al final del taller, cada persona limpia su propio entorno
python scripts/cleanup_sample_data.py --things-prefix Alice
python scripts/cleanup_sample_data.py --things-prefix Bob
python scripts/cleanup_sample_data.py --things-prefix Carol
```

### Ejemplo 7: Validación de Prefijo

**Escenario:** Entender las reglas de validación de prefijos.

```bash
# ✅ Prefijos válidos
python scripts/setup_sample_data.py --things-prefix Dev
python scripts/setup_sample_data.py --things-prefix Test123
python scripts/setup_sample_data.py --things-prefix MyTeam

# ❌ Prefijos inválidos
python scripts/setup_sample_data.py --things-prefix AB
# Error: Prefijo debe tener al menos 3 caracteres

python scripts/setup_sample_data.py --things-prefix My-Team
# Error: Solo caracteres alfanuméricos permitidos

python scripts/setup_sample_data.py --things-prefix "My Team"
# Error: Sin espacios permitidos

python scripts/setup_sample_data.py --things-prefix VeryLongPrefixNameThatExceedsLimit
# Error: Prefijo debe tener máximo 20 caracteres
```

### Ejemplo 8: Modo Debug para Aprendizaje

**Escenario:** Aprender las APIs de AWS IoT viendo llamadas detalladas de API.

```bash
# Configuración con logging detallado de API
python scripts/setup_sample_data.py --debug --things-prefix Learn

# Verás salida detallada como:
# 🔄 API Call: CreateThingType
# 📤 Request: {"thingTypeName": "SedanVehicle", ...}
# 📥 Response: {"thingTypeName": "SedanVehicle", "thingTypeArn": "...", ...}
```

### Ejemplo 9: Limpieza con Modo Debug

**Escenario:** Solucionar problemas de limpieza con logging detallado.

```bash
# Limpieza con logging detallado de API
python scripts/cleanup_sample_data.py --debug --things-prefix Test

# Verás operaciones detalladas:
# 🔄 API Call: DetachThingPrincipal
# 📤 Request: {"thingName": "Test-VIN-001", "principal": "..."}
# 📥 Response: {}
# ✅ Certificado desadjuntado de Test-VIN-001
```

### Ejemplo 10: Combinación de Todas las Opciones

**Escenario:** Usar todas las características juntas para máximo control.

```bash
# Vista previa de limpieza con prefijo y debug
python scripts/cleanup_sample_data.py --dry-run --things-prefix Dev --debug

# Esto proporciona:
# - Vista previa sin eliminaciones (--dry-run)
# - Dirigido a entorno específico (--things-prefix Dev)
# - Logging detallado de API (--debug)
```

## Escenarios de Aprendizaje

### Escenario 1: Monitoreo de Flota de Vehículos

**Objetivo:** Configurar monitoreo para una flota de vehículos con alertas de temperatura.

#### Configuración:
```bash
# 1. Crear datos de ejemplo
python scripts/setup_sample_data.py

# 2. Configurar certificados para 3 vehículos
python scripts/certificate_manager.py
# Seleccionar Vehicle-VIN-001, Vehicle-VIN-002, Vehicle-VIN-003
```

#### Regla de Monitoreo:
```sql
SELECT deviceId, timestamp, temperature, location 
FROM 'fleet/+/telemetry' 
WHERE temperature > 80
```

#### Prueba MQTT:
```bash
# Terminal 1: Suscribirse a alertas
📡 MQTT> sub alerts/temperature

# Terminal 2: Simular datos de vehículo
📡 MQTT> json fleet/vehicle001/telemetry deviceId=vehicle001 temperature=85 location=highway
```

### Escenario 2: Gestión de Estado de Dispositivos

**Objetivo:** Usar AWS IoT Device Shadow service para sincronizar configuración de dispositivos.

#### Configuración de Shadow:
```bash
python scripts/device_shadow_explorer.py
```

#### Ejemplo de Flujo:
```bash
# 1. Establecer configuración deseada (desde la nube)
🌟 Shadow> desire targetTemp=22 mode=auto fanSpeed=medium

# 2. Dispositivo reporta estado actual
🌟 Shadow> report currentTemp=25 mode=manual fanSpeed=high

# 3. Ver diferencias (delta)
🌟 Shadow> get
# Muestra qué necesita cambiar el dispositivo
```

### Escenario 3: Procesamiento de Datos en Tiempo Real

**Objetivo:** Crear pipeline de procesamiento de datos con múltiples reglas.

#### Reglas en Cascada:
```sql
-- Regla 1: Filtrar datos válidos
SELECT * FROM 'sensors/+/raw' WHERE temperature IS NOT NULL

-- Regla 2: Detectar anomalías
SELECT deviceId, temperature FROM 'sensors/processed' WHERE temperature > 50 OR temperature < -10

-- Regla 3: Agregar datos por hora
SELECT AVG(temperature) as avgTemp, COUNT(*) as readings 
FROM 'sensors/processed' 
GROUP BY deviceId, HOUR(timestamp)
```

## Ejemplos de MQTT

### Ejemplo 1: Publicación de Datos de Sensores

```bash
# Conectar como dispositivo
python scripts/mqtt_client_explorer.py

# Publicar datos estructurados
📡 MQTT> json sensors/device001/data temperature=23.5 humidity=65 pressure=1013.25 timestamp=1642248600

# Publicar alerta simple
📡 MQTT> pub alerts/device001 "Battery low: 15%"

# Publicar con QoS 1 (garantía de entrega)
📡 MQTT> pub1 critical/device001 "System failure detected"
```

### Ejemplo 2: Patrones de Suscripción

```bash
# Suscribirse a todos los sensores de temperatura
📡 MQTT> sub sensors/+/temperature

# Suscribirse a todas las alertas
📡 MQTT> sub alerts/#

# Suscribirse a dispositivo específico
📡 MQTT> sub sensors/device001/+

# Suscribirse con QoS 1
📡 MQTT> sub1 critical/#
```

### Ejemplo 3: Simulación de Múltiples Dispositivos

```bash
# Simular datos de múltiples sensores
📡 MQTT> json sensors/temp001/data value=23.5 unit=celsius location=room1
📡 MQTT> json sensors/temp002/data value=24.1 unit=celsius location=room2
📡 MQTT> json sensors/humid001/data value=65 unit=percent location=room1
📡 MQTT> json sensors/pressure001/data value=1013.25 unit=hPa location=outdoor
```

## Ejemplos de AWS IoT Device Shadow service

### Ejemplo 1: Configuración de Termostato

```bash
# Estado inicial del dispositivo
🌟 Shadow> report currentTemp=20 targetTemp=22 mode=heat fanSpeed=low

# Cambio de configuración desde la aplicación
🌟 Shadow> desire targetTemp=24 mode=auto

# Dispositivo procesa el cambio
🌟 Shadow> report targetTemp=24 mode=auto currentTemp=20.5

# Ver historial de cambios
🌟 Shadow> get
```

### Ejemplo 2: Control de Iluminación

```bash
# Estado inicial
🌟 Shadow> report brightness=50 color=white power=on

# Comando desde aplicación móvil
🌟 Shadow> desire brightness=80 color=blue

# Dispositivo confirma cambio
🌟 Shadow> report brightness=80 color=blue

# Apagar luces
🌟 Shadow> desire power=off
🌟 Shadow> report power=off brightness=0
```

### Ejemplo 3: Monitoreo de Batería

```bash
# Reporte inicial de batería
🌟 Shadow> report batteryLevel=100 charging=false voltage=4.2

# Actualizaciones periódicas
🌟 Shadow> report batteryLevel=85 voltage=4.0
🌟 Shadow> report batteryLevel=70 voltage=3.8

# Alerta de batería baja
🌟 Shadow> report batteryLevel=15 voltage=3.4 lowBatteryAlert=true

# Inicio de carga
🌟 Shadow> report charging=true voltage=3.5
```

## Ejemplos del Motor de Reglas

### Ejemplo 1: Sistema de Alertas por Temperatura

```sql
-- Regla: HighTemperatureAlert
SELECT deviceId, temperature, timestamp, location 
FROM 'sensors/+/temperature' 
WHERE temperature > 35

-- Acción: Republicar a tópico de alertas
-- Tópico objetivo: alerts/temperature/high
```

**Prueba:**
```bash
📡 MQTT> sub alerts/temperature/high
📡 MQTT> json sensors/device001/temperature deviceId=device001 temperature=40 location=warehouse
# Debería aparecer en alerts/temperature/high
```

### Ejemplo 2: Filtrado de Datos por Ubicación

```sql
-- Regla: WarehouseDataFilter
SELECT * 
FROM 'sensors/+/data' 
WHERE location = 'warehouse' AND temperature IS NOT NULL

-- Acción: Republicar a tópico específico de warehouse
-- Tópico objetivo: warehouse/filtered/data
```

### Ejemplo 3: Agregación de Datos

```sql
-- Regla: HourlyAverages
SELECT 
    deviceId,
    AVG(temperature) as avgTemp,
    MAX(temperature) as maxTemp,
    MIN(temperature) as minTemp,
    COUNT(*) as readings
FROM 'sensors/+/temperature' 
WHERE timestamp > timestamp() - 3600000
GROUP BY deviceId

-- Acción: Enviar a sistema de análisis
-- Tópico objetivo: analytics/hourly/temperature
```

## Casos de Uso del Mundo Real

### Caso de Uso 1: Smart Building

**Escenario:** Sistema de gestión de edificio inteligente con múltiples sensores.

#### Arquitectura:
```
Sensores → AWS IoT Core → Reglas → Acciones
├── Temperatura/Humedad → Regla HVAC → Control automático
├── Ocupación → Regla Iluminación → Control de luces
├── Seguridad → Regla Alertas → Notificaciones
└── Energía → Regla Análisis → Dashboard
```

#### Implementación:
```bash
# 1. Configurar tipos de dispositivos
# Thing Types: TemperatureSensor, OccupancySensor, SecuritySensor

# 2. Crear reglas específicas
# - HVAC: temperature > 25 OR humidity > 70
# - Lighting: occupancy = true AND lightLevel < 50
# - Security: motion = detected AND authorized = false

# 3. Usar Device Shadow para configuración
# - Horarios de operación
# - Umbrales de temperatura
# - Configuración de seguridad
```

### Caso de Uso 2: Monitoreo Industrial

**Escenario:** Monitoreo de maquinaria industrial con mantenimiento predictivo.

#### Datos Monitoreados:
- Vibración de motores
- Temperatura de rodamientos
- Presión de sistemas hidráulicos
- Consumo de energía

#### Reglas de Negocio:
```sql
-- Alerta de mantenimiento
SELECT equipmentId, vibration, temperature 
FROM 'factory/+/telemetry' 
WHERE vibration > 5.0 OR temperature > 80

-- Parada de emergencia
SELECT * 
FROM 'factory/+/telemetry' 
WHERE pressure > 150 OR temperature > 100
```

### Caso de Uso 3: Agricultura Inteligente

**Escenario:** Sistema de riego automático basado en sensores de suelo.

#### Sensores:
- Humedad del suelo
- Temperatura ambiente
- Nivel de luz
- pH del suelo

#### Lógica de Riego:
```sql
-- Activar riego
SELECT sensorId, soilMoisture, temperature 
FROM 'farm/+/sensors' 
WHERE soilMoisture < 30 AND temperature > 25 AND lightLevel > 500

-- Parar riego
SELECT sensorId, soilMoisture 
FROM 'farm/+/sensors' 
WHERE soilMoisture > 70
```

#### AWS IoT Device Shadow service para Configuración:
```json
{
  "desired": {
    "irrigationSchedule": "06:00-08:00,18:00-20:00",
    "moistureThreshold": 30,
    "temperatureThreshold": 25,
    "irrigationDuration": 1800
  }
}
```

## Mejores Prácticas Demostradas

### 1. Nomenclatura de Tópicos
```
✅ Bueno: sensors/device001/temperature
✅ Bueno: alerts/high-temperature/warehouse
✅ Bueno: fleet/vehicle/VIN123/telemetry

❌ Malo: temp
❌ Malo: device-data
❌ Malo: alert123
```

### 2. Estructura de Mensajes JSON
```json
✅ Bueno:
{
  "deviceId": "sensor001",
  "timestamp": 1642248600,
  "temperature": 23.5,
  "unit": "celsius",
  "location": "warehouse"
}

❌ Malo:
{
  "t": 23.5,
  "d": "s001"
}
```

### 3. Gestión de Errores
```sql
-- Incluir validación en reglas
SELECT * FROM 'sensors/+/data' 
WHERE temperature IS NOT NULL 
  AND temperature > -50 
  AND temperature < 100
```

### 4. Seguridad
```json
// Política restrictiva por dispositivo
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["iot:Connect"],
      "Resource": "arn:aws:iot:region:account:client/${iot:Connection.Thing.ThingName}"
    },
    {
      "Effect": "Allow",
      "Action": ["iot:Publish"],
      "Resource": "arn:aws:iot:region:account:topic/sensors/${iot:Connection.Thing.ThingName}/*"
    }
  ]
}
```

Estos ejemplos proporcionan una base sólida para entender y implementar soluciones IoT usando AWS IoT Core. Cada ejemplo incluye código funcional que puedes ejecutar y modificar según tus necesidades específicas.