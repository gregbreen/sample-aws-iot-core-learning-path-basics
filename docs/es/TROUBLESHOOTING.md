# Guía de Solución de Problemas

> 🌍 **Idiomas Disponibles**: [English](../en/TROUBLESHOOTING.md) | **Español** (Actual)

Esta guía te ayudará a resolver los problemas más comunes que puedes encontrar mientras usas los scripts de aprendizaje de AWS IoT Core.

## Tabla de Contenidos

- [Problemas de Configuración](#problemas-de-configuración)
- [Errores de Credenciales AWS](#errores-de-credenciales-aws)
- [Problemas de Conexión MQTT](#problemas-de-conexión-mqtt)
- [Errores de Certificados](#errores-de-certificados)
- [Problemas del Motor de Reglas IoT](#problemas-del-motor-de-reglas-iot)
- [Errores de Permisos](#errores-de-permisos)
- [Problemas de Limpieza](#problemas-de-limpieza)

## Problemas de Configuración

### Error: "ModuleNotFoundError: No module named 'boto3'"

**Síntoma:**
```
ModuleNotFoundError: No module named 'boto3'
```

**Solución:**
```bash
# Asegúrate de que el entorno virtual esté activado
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Instala las dependencias
pip install -r requirements.txt
```

### Error: "python: command not found"

**Síntoma:**
```
python: command not found
```

**Solución:**
```bash
# Usa python3 en su lugar
python3 scripts/setup_sample_data.py

# O crea un alias
alias python=python3
```

### Error: Versión de Python Incorrecta

**Síntoma:**
```
SyntaxError: invalid syntax (f-strings require Python 3.6+)
```

**Solución:**
```bash
# Verifica tu versión de Python
python --version

# Debe ser 3.7 o superior
# Si no lo es, instala una versión más reciente o usa python3
python3 --version
```

## Errores de Credenciales AWS

### Error: "NoCredentialsError"

**Síntoma:**
```
botocore.exceptions.NoCredentialsError: Unable to locate credentials
```

**Solución:**
```bash
# Opción 1: Variables de entorno
export AWS_ACCESS_KEY_ID=<tu-clave>
export AWS_SECRET_ACCESS_KEY=<tu-clave-secreta>
export AWS_DEFAULT_REGION=us-east-1

# Opción 2: AWS CLI
aws configure

# Opción 3: Verifica tus credenciales existentes
aws sts get-caller-identity
```

### Error: "AccessDenied" o "UnauthorizedOperation"

**Síntoma:**
```
ClientError: An error occurred (AccessDenied) when calling the ListThings operation
```

**Solución:**
1. **Verifica los permisos de AWS IAM** - Tu usuario o rol necesita permisos de AWS IoT
2. **Política AWS IAM mínima requerida:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iot:*",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": "*"
        }
    ]
}
```

### Error: Región Incorrecta

**Síntoma:**
```
EndpointConnectionError: Could not connect to the endpoint URL
```

**Solución:**
```bash
# Verifica tu región actual
aws configure get region

# Establece la región correcta
export AWS_DEFAULT_REGION=us-east-1

# O usa aws configure
aws configure set region us-east-1
```

## Problemas de Conexión MQTT

### Error: "Connection refused" o "Timeout"

**Síntoma:**
```
Connection failed: Connection refused
```

**Soluciones:**
1. **Verifica tu endpoint IoT:**
```bash
aws iot describe-endpoint --endpoint-type iot:Data-ATS
```

2. **Verifica tus certificados:**
```bash
ls -la certificates/
# Debe mostrar archivos .crt, .key, .pub
```

3. **Verifica la política adjunta:**
```bash
aws iot list-attached-policies --target <certificate-arn>
```

### Error: "SSL/TLS handshake failed"

**Síntoma:**
```
SSL: CERTIFICATE_VERIFY_FAILED
```

**Soluciones:**
1. **Verifica tus archivos de certificado:**
```bash
# El certificado debe ser válido
openssl x509 -in certificates/thing-name/cert.crt -text -noout
```

2. **Verifica los permisos de archivos:**
```bash
chmod 600 certificates/*/private.key
chmod 644 certificates/*/certificate.crt
```

3. **Regenera los certificados si es necesario:**
```bash
python scripts/certificate_manager.py
# Selecciona la opción 1 para crear un nuevo certificado
```

### Error: "MQTT connection lost"

**Síntoma:**
```
Connection lost: The connection was lost
```

**Soluciones:**
1. **Verifica tu conectividad de red**
2. **Verifica que el certificado esté activo:**
```bash
aws iot describe-certificate --certificate-id <cert-id>
```

3. **Verifica los límites de conexión** - AWS IoT tiene límites de conexiones concurrentes

## Errores de Certificados

### Error: "Certificate not found"

**Síntoma:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'certificates/...'
```

**Solución:**
```bash
# Ejecuta primero el gestor de certificados
python scripts/certificate_manager.py

# Selecciona la opción 1 para crear un certificado
```

### Error: "Invalid certificate format"

**Síntoma:**
```
SSL: PEM lib error
```

**Soluciones:**
1. **Verifica el formato del certificado:**
```bash
head -1 certificates/*/certificate.crt
# Debe comenzar con -----BEGIN CERTIFICATE-----
```

2. **Regenera el certificado si está corrupto:**
```bash
rm -rf certificates/thing-name/
python scripts/certificate_manager.py
```

### Error: "Certificate already exists"

**Síntoma:**
```
ResourceAlreadyExistsException: Certificate already exists
```

**Solución:**
- Esto es normal - el script continuará usando el certificado existente
- O puedes eliminar los certificados existentes y crear nuevos

## Problemas del Motor de Reglas IoT

### Error: "Invalid SQL syntax"

**Síntoma:**
```
InvalidRequestException: Invalid SQL
```

**Soluciones:**
1. **Verifica la sintaxis SQL:**
```sql
-- Correcto
SELECT * FROM 'topic/+/temperature' WHERE temperature > 25

-- Incorrecto (faltan comillas en el tópico)
SELECT * FROM topic/+/temperature WHERE temperature > 25
```

2. **Usa el modo debug para ver el SQL generado:**
```bash
python scripts/iot_rules_explorer.py --debug
```

### Error: "Role does not exist"

**Síntoma:**
```
InvalidRequestException: The role does not exist
```

**Solución:**
- El script debería crear el rol automáticamente
- Si falla, verifica los permisos de AWS IAM para crear roles
- Espera unos segundos para que se propague en AWS IAM

### Error: "Rule already exists"

**Síntoma:**
```
ResourceAlreadyExistsException: Rule already exists
```

**Solución:**
```bash
# Lista las reglas existentes
aws iot list-topic-rules

# Elimina la regla existente si es necesario
aws iot delete-topic-rule --rule-name <rule-name>
```

## Errores de Permisos

### Error: "Access denied to IoT service"

**Síntoma:**
```
AccessDenied: User is not authorized to perform iot:CreateThing
```

**Solución:**
Agrega una política AWS IAM con permisos IoT:
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
                "iot:CreateThingType",
                "iot:CreateThingGroup",
                "iot:CreateKeysAndCertificate",
                "iot:AttachThingPrincipal",
                "iot:CreatePolicy",
                "iot:AttachPrincipalPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

### Error: "Cannot create IAM role"

**Síntoma:**
```
AccessDenied: User is not authorized to perform iam:CreateRole
```

**Solución:**
Agrega permisos AWS IAM:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": "*"
        }
    ]
}
```

## Problemas de Limpieza

### Error: "Cannot delete Thing with attached certificates"

**Síntoma:**
```
InvalidRequestException: Cannot delete thing with attached certificates
```

**Solución:**
```bash
# El script de limpieza maneja esto automáticamente
python scripts/cleanup_sample_data.py

# O manualmente:
# 1. Desadjunta los certificados
aws iot detach-thing-principal --thing-name <thing-name> --principal <cert-arn>

# 2. Elimina el Thing
aws iot delete-thing --thing-name <thing-name>
```

### Error: "Thing Type in use"

**Síntoma:**
```
InvalidRequestException: Cannot delete thing type while things of this type exist
```

**Solución:**
1. **Elimina primero todos los Things de ese tipo**
2. **Depreca el Thing Type:**
```bash
aws iot deprecate-thing-type --thing-type-name <type-name>
```
3. **Espera 5 minutos, luego elimínalo:**
```bash
aws iot delete-thing-type --thing-type-name <type-name>
```

## Comandos de Diagnóstico Útiles

### Verifica el Estado General
```bash
# Verifica tus credenciales
aws sts get-caller-identity

# Verifica tu región
aws configure get region

# Verifica el endpoint IoT
aws iot describe-endpoint --endpoint-type iot:Data-ATS

# Lista los recursos IoT
aws iot list-things
aws iot list-certificates
aws iot list-thing-types
aws iot list-thing-groups
```

### Verifica la Conectividad
```bash
# Prueba la conectividad al endpoint IoT
curl -I https://$(aws iot describe-endpoint --endpoint-type iot:Data-ATS --query endpointAddress --output text)

# Verifica los puertos (MQTT usa 8883, WebSocket usa 443)
telnet $(aws iot describe-endpoint --endpoint-type iot:Data-ATS --query endpointAddress --output text) 8883
```

### Logs de Debug
```bash
# Ejecuta cualquier script con modo debug
python scripts/setup_sample_data.py --debug
python scripts/iot_registry_explorer.py --debug
python scripts/certificate_manager.py --debug
python scripts/mqtt_client_explorer.py --debug
```

## Obtén Ayuda Adicional

Si los problemas persisten:

1. **Verifica los logs de AWS CloudTrail** para errores de API
2. **Consulta la documentación de AWS IoT**: https://docs.aws.amazon.com/iot/
3. **Foros de AWS**: https://forums.aws.amazon.com/forum.jspa?forumID=210
4. **Crea un issue en GitHub**: Incluye logs de debug y pasos para reproducir

## Información de Contacto de Soporte

- **GitHub Issues**: [Reporta problemas](https://github.com/aws-samples/sample-aws-iot-core-learning-path-basics/issues)
- **Documentación AWS**: [Guía del Desarrollador de AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/)
- **Soporte AWS**: [Centro de Soporte AWS](https://console.aws.amazon.com/support/)