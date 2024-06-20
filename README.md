# Sistema de Registro y Autenticación con Verificación por Correo Electrónico

Este proyecto implementa un sistema de registro y autenticación con verificación por correo electrónico utilizando Python, SQLite y SMTP.

## Funcionalidades

### `manageDB.py`

Gestiona la base de datos SQLite para almacenar información de usuarios.

- **`createDB()`**: Crea la base de datos `UserData.db` si no existe.
- **`createTable()`**: Crea la tabla `accounts` para almacenar información de usuarios.
- **`insertRow(mail, user, passwordHash)`**: Inserta un nuevo usuario en la tabla `accounts`.
- **`deleteRow(user)`**: Elimina un usuario de la tabla `accounts` por nombre de usuario.
- **`validationLogIn(user, passwordHash)`**: Valida el inicio de sesión comparando usuario y contraseña.
- **`namePetition(user)`**: Obtiene el nombre de usuario asociado a un usuario dado.
- **`obtainMail(user, passwordHash)`**: Obtiene el correo electrónico asociado a un usuario y contraseña dados.

### `main.py`

Contiene las funciones principales para el registro, inicio de sesión y verificación por correo electrónico.

- **`generateCode()`**: Genera un código de verificación de 6 dígitos aleatorio.
- **`sendmail(email_reciver)`**: Envía un correo electrónico con un código de verificación utilizando SMTP.
- **`encode(data)`**: Codifica una cadena de datos usando MD5 para almacenamiento seguro de contraseñas.
- **`getpass(prompt)`**: Obtiene una contraseña de manera segura sin mostrarla en pantalla.
- **`testMail(mail)`**: Valida el formato de una dirección de correo electrónico.
- **`register()`**: Permite a un usuario registrarse, validando el correo electrónico y almacenando la información en la base de datos.
- **`logIn()`**: Gestiona el inicio de sesión de un usuario, verifica la contraseña y envía un código de verificación por correo electrónico.

## Configuración de Variables de Entorno

Antes de ejecutar el script, configura tus credenciales de correo electrónico y contraseña en un archivo `.env` para proteger la información sensible. Ejemplo de contenido del archivo `.env`:

     ```
     EMAIL="tucorreo@gmail.com"
     PASSWORD="tucontraseña"
     ```

## Instrucciones de Uso

1. Clona o descarga el repositorio en tu máquina local.
2. Configura las variables de entorno `EMAIL` y `PASSWORD` en `.env`.
3. Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`, donde `requirements.txt` contiene `hashlib`, `re`, `os`, `time`, `msvcrt`, `random`, `smtplib`, `ssl`, y `dotenv`.
4. Ejecuta `main.py` para probar las funcionalidades de registro, inicio de sesión y verificación por correo electrónico.

¡Disfruta utilizando el sistema de registro y autenticación con verificación por correo electrónico!

