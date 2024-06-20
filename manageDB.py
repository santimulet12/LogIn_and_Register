import sqlite3 as sql

def createDB():
    conection = sql.connect('UserData.db')
    conection.commit()
    conection.close()

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

def insertRow(mail,user,passwordHash):
    conection = sql.connect('UserData.db')

    cursor = conection.cursor()
    instruction = f'INSERT INTO accounts VALUES("{mail}", "{user}", "{passwordHash}")'
    cursor.execute(instruction)

    conection.commit()
    conection.close()

def deletRow(user):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    instruction = f'DELETE FROM accounts WHERE user = "{user}"'
    cursor.execute(instruction)

    conection.commit()
    conection.close()

def validationLogIn(user,passwordHash):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT * FROM accounts WHERE user = "{user}" AND password = "{passwordHash}"') #PETICION A LA BASE DE DATOS

    us_pass = cursor.fetchone() #OBTENGO LA RESPUESTA

    conection.commit()
    conection.close()
    
    return us_pass is not None #RETORNA TRUE O FALSE

def namePetition(user):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT user FROM accounts WHERE user = "{user}"') #PETICION A LA BASE DE DATOS

    response = cursor.fetchone() #OBTENGO LA RESPUESTA

    conection.commit()
    conection.close()

    return response

def obtainMail(user,passwordHash):
    conection = sql.connect('UserData.db')
    cursor = conection.cursor()

    cursor.execute(f'SELECT mail FROM accounts WHERE user = "{user}" AND password = "{passwordHash}"')

    mail_reciver = cursor.fetchone()

    conection.commit()
    conection.close()

    return mail_reciver

if __name__ == '__main__':
    pass