# Sistema de Registro y Autenticación con Verificación por Correo Electrónico

Este proyecto consiste en varios scripts en Python diseñados para implementar un sistema básico de registro, autenticación y verificación por correo electrónico utilizando SQLite como base de datos y SMTP para el envío de correos electrónicos.

## Funcionalidades

1. **`manageDB.py`**: Gestiona la base de datos SQLite para almacenar información de usuarios.

   - `createDB()`: Crea la base de datos `UserData.db` si no existe.
   - `createTable()`: Crea la tabla `accounts` dentro de la base de datos para almacenar información de usuarios.
   - `insertRow(mail, user, passwordHash)`: Inserta un nuevo usuario en la tabla `accounts`.
   - `deleteRow(user)`: Elimina un usuario de la tabla `accounts` basado en el nombre de usuario.
   - `validationLogIn(user, passwordHash)`: Valida el inicio de sesión comparando el nombre de usuario y el hash de la contraseña.
   - `namePetition(user)`: Obtiene el nombre de usuario asociado a un nombre de usuario dado.
   - `obtainMail(user, passwordHash)`: Obtiene el correo electrónico asociado a un nombre de usuario y hash de contraseña dados.

2. **`main.py`**: Contiene las funciones principales para el registro, inicio de sesión y verificación por correo electrónico.

   - `generateCode()`: Genera un código de verificación de 6 dígitos aleatorio.
   - `sendmail(email_reciver)`: Envía un correo electrónico con un código de verificación utilizando SMTP.
   - `encode(data)`: Codifica una cadena de datos usando el algoritmo MD5.
   - `getpass(prompt)`: Obtiene una contraseña de manera segura sin mostrarla en pantalla.
   - `testMail(mail)`: Valida el formato de una dirección de correo electrónico.
   - `register()`: Permite a un usuario registrarse, validando el correo electrónico y almacenando la información en la base de datos.
   - `logIn()`: Gestiona el inicio de sesión de un usuario, verifica la contraseña y envía un código de verificación por correo electrónico.

3. **Configuración de Variables de Entorno**:
   
   - Antes de ejecutar el script, asegúrate de configurar tus credenciales de correo electrónico y contraseña en un archivo `.env` para proteger la información sensible. Ejemplo de contenido del archivo `.env`:

     ```
     EMAIL="tucorreo@gmail.com"
     PASSWORD="tucontraseña"
     ```

4. **Instrucciones de Uso**:
   
   - Clona o descarga el repositorio en tu máquina local.
   - Configura las variables de entorno `EMAIL` y `PASSWORD` en un archivo `.env` como se mencionó anteriormente.
   - Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`, donde `requirements.txt` contiene `hashlib`, `re`, `os`, `time`, `msvcrt`, `random`, `smtplib`, `ssl`, y `dotenv`.
   - Ejecuta `main.py` para iniciar el programa y probar las funcionalidades de registro, inicio de sesión y verificación por correo electrónico.

