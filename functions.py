import hashlib,re,os,time,msvcrt,random
from manageDB import insertRow,validationLogIn,namePetition,obtainMail
import smtplib,ssl
from email.message import EmailMessage
from dotenv import load_dotenv

def generateCode():
    nums = '0123456789'
    verificationCode = ''

    for i in range(6):
        verificationCode += random.choice(nums)

    return verificationCode

def sendmail(email_reciver):

    # Datos del remitente
    load_dotenv()

    email_sender = os.getenv('EMAIL')

    password = os.getenv('PASSWORD')

    verificationCode = generateCode()

    # Crear el mensaje
    body = f'Su codigo de verificación es: {verificationCode}'
    mensaje = EmailMessage()
    mensaje['From'] = email_sender
    mensaje['To'] = email_reciver
    mensaje['Subject'] = 'Tu código de verificación'
    mensaje.set_content(body)

    # Configurar el servidor SMTP
    smtp_servidor = 'smtp.gmail.com'
    puerto_smtp = 465

    context = ssl.create_default_context()
    # Iniciar sesión en el servidor SMTP
    with smtplib.SMTP_SSL(smtp_servidor, puerto_smtp, context=context) as smtp:
        smtp.login(email_sender,password)
        smtp.sendmail(email_sender,email_reciver,mensaje.as_string())

    return verificationCode


def encode(data):
    hash_object = hashlib.md5(data.encode())

    hash_hex = hash_object.hexdigest()

    return hash_hex

def getpass(prompt="Introduce tu contraseña: "):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        key = msvcrt.getwch()  # Lee un carácter sin eco en Windows
        if key == '\r' or key == '\n':
            print('')
            break
        elif key == '\b':
            if password:
                password = password[:-1]  # Elimina el último carácter
                print('\b \b', end='', flush=True)  # Borra el carácter en la consola
        else:
            password += key
            print('*', end='', flush=True)  # Muestra asterisco en lugar del carácter
    return password

def testMail(mail):
    filt = lambda pal,where: re.search(pal,where)

    textoEnc = (filt('@', mail), filt('.com', mail))

    if textoEnc[0] != None and textoEnc[1] != None:
        return True
    else:
        return False 

def register():
    while True:
        print('Debe registrarse.')

        mail = input('Ingrese su Mail: ')
        user = input('Ingrese su nombre de Usuario: ')
        passwd = getpass("Ingrese tu contraseña: ")

        passHashed = encode(passwd)

        if testMail(mail):
            print('Registro satisfactorio!')
            break
        else:
            print('Correo Inválido')
            time.sleep(3)
            os.system('cls')
            
    insertRow(mail,user,passHashed)

def logIn():
    while True:
        print('Debe iniciar Sesión.')

        user = input('Ingrese su nombre de Usuario: ')
        passwd = getpass("Ingrese tu contraseña: ")

        passHashed = encode(passwd)

        if validationLogIn(user,passHashed):
            mail = obtainMail(user,passHashed)
            verifyCode = sendmail(mail)
            
            print('Hemos enviado un código de verificación')
            code = input('Ingrese su código aquí: ')

            if code == verifyCode:
                name = namePetition(user)
                print(f'Bienvenido/a {name[0]}!')
                break
            else:
                print('Código erróneo')
        else:
            print('Usuario o Contraseña Inválido')
            time.sleep(3)
            os.system('cls')

if __name__ == '__main__':
    pass
