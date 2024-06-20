<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Registro y Autenticación con Verificación por Correo Electrónico</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1 {
            color: #333;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        h2 {
            color: #555;
            margin-top: 20px;
        }
        p {
            margin-bottom: 10px;
        }
        code {
            font-family: Consolas, monospace;
            background-color: #f0f0f0;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>Sistema de Registro y Autenticación con Verificación por Correo Electrónico</h1>

    <h2>Funcionalidades</h2>

    <ol>
        <li><strong><code>manageDB.py</code></strong>: Gestiona la base de datos SQLite para almacenar información de usuarios.</li>
        <ul>
            <li><code>createDB()</code>: Crea la base de datos <code>UserData.db</code> si no existe.</li>
            <li><code>createTable()</code>: Crea la tabla <code>accounts</code> dentro de la base de datos para almacenar información de usuarios.</li>
            <li><code>insertRow(mail, user, passwordHash)</code>: Inserta un nuevo usuario en la tabla <code>accounts</code>.</li>
            <li><code>deleteRow(user)</code>: Elimina un usuario de la tabla <code>accounts</code> basado en el nombre de usuario.</li>
            <li><code>validationLogIn(user, passwordHash)</code>: Valida el inicio de sesión comparando el nombre de usuario y el hash de la contraseña.</li>
            <li><code>namePetition(user)</code>: Obtiene el nombre de usuario asociado a un nombre de usuario dado.</li>
            <li><code>obtainMail(user, passwordHash)</code>: Obtiene el correo electrónico asociado a un nombre de usuario y hash de contraseña dados.</li>
        </ul>
        <li><strong><code>main.py</code></strong>: Contiene las funciones principales para el registro, inicio de sesión y verificación por correo electrónico.</li>
        <ul>
            <li><code>generateCode()</code>: Genera un código de verificación de 6 dígitos aleatorio.</li>
            <li><code>sendmail(email_reciver)</code>: Envía un correo electrónico con un código de verificación utilizando SMTP.</li>
            <li><code>encode(data)</code>: Codifica una cadena de datos usando el algoritmo MD5.</li>
            <li><code>getpass(prompt)</code>: Obtiene una contraseña de manera segura sin mostrarla en pantalla.</li>
            <li><code>testMail(mail)</code>: Valida el formato de una dirección de correo electrónico.</li>
            <li><code>register()</code>: Permite a un usuario registrarse, validando el correo electrónico y almacenando la información en la base de datos.</li>
            <li><code>logIn()</code>: Gestiona el inicio de sesión de un usuario, verifica la contraseña y envía un código de verificación por correo electrónico.</li>
        </ul>
        <li><strong>Configuración de Variables de Entorno</strong>:</li>
        <ul>
            <li>Antes de ejecutar el script, asegúrate de configurar tus credenciales de correo electrónico y contraseña en un archivo <code>.env</code> para proteger la información sensible. Ejemplo de contenido del archivo <code>.env</code>:</li>
            <pre>
EMAIL="tucorreo@gmail.com"
PASSWORD="tucontraseña"
            </pre>
        </ul>
        <li><strong>Instrucciones de Uso</strong>:</li>
        <ul>
            <li>Clona o descarga el repositorio en tu máquina local.</li>
            <li>Configura las variables de entorno <code>EMAIL</code> y <code>PASSWORD</code> en un archivo <code>.env</code> como se mencionó anteriormente.</li>
            <li>Instala las dependencias necesarias ejecutando <code>pip install -r requirements.txt</code>, donde <code>requirements.txt</code> contiene <code>hashlib</code>, <code>re</code>, <code>os</code>, <code>time</code>, <code>msvcrt</code>, <code>random</code>, <code>smtplib</code>, <code>ssl</code>, y <code>dotenv</code>.</li>
            <li>Ejecuta <code>main.py</code> para iniciar el programa y probar las funcionalidades de registro, inicio de sesión y verificación por correo electrónico.</li>
        </ul>
    </ol>

</body>
</html>
