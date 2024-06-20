import sqlite3 as sql

# Función para crear la base de datos si no existe
def createDB():
    conection = sql.connect('UserData.db')
    conection.commit()
    conection.close()

# Función para crear la tabla 'accounts' dentro de la base de datos
def createTable():
    conection = sql.connect('UserData.db')

    cursor = conection.cursor()
    cursor.execute(
        '''CREATE TABLE accounts (
            mail text,
            user text,
            password text
        )'''
    )

    conection.commit()
    conection.close()

# Función para insertar una nueva fila (registro) en la tabla 'accounts'
def insertRow(mail, user, passwordHash):
    conection = sql.connect('UserData.db')

    cursor = conection.cursor()
    instruction = f'INSERT INTO accounts VALUES("{mail}", "{user}", "{passwordHash}")'
    cursor.execute(instruction)

    conection.commit()
    conection.close()

# Función para eliminar una fila (registro) de la tabla 'accounts' por usuario
def deleteRow(user):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    instruction = f'DELETE FROM accounts WHERE user = "{user}"'
    cursor.execute(instruction)

    conection.commit()
    conection.close()

# Función para validar el inicio de sesión comparando usuario y contraseña
def validationLogIn(user, passwordHash):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT * FROM accounts WHERE user = "{user}" AND password = "{passwordHash}"')

    user_password = cursor.fetchone()

    conection.commit()
    conection.close()
    
    return user_password is not None  # Retorna True si se encontró una coincidencia, False si no

# Función para obtener el nombre de usuario
def namePetition(user):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT user FROM accounts WHERE user = "{user}"')

    response = cursor.fetchone()

    conection.commit()
    conection.close()

    return response  # Retorna el nombre de usuario como una tupla

# Función para obtener el correo electrónico asociado a un usuario y contraseña
def obtainMail(user, passwordHash):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT mail FROM accounts WHERE user = "{user}" AND password = "{passwordHash}"')

    mail_receiver = cursor.fetchone()

    conection.commit()
    conection.close()

    return mail_receiver  # Retorna el correo electrónico como una tupla
