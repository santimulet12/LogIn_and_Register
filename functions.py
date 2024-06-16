import hashlib,base64,re,os,time,msvcrt
from manageDB import insertRow,validationLogIn,namePetition

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
            name = namePetition(user)
            print(f'Bienvenido {name[0]}!')
            break
        else:
            print('Usuario o Contraseña Inválido')
            time.sleep(3)
            os.system('cls')
