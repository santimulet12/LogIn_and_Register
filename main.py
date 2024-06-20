import tkinter as tk  # Importa la biblioteca tkinter para crear interfaces gráficas
from tkinter import messagebox  # Importa la clase messagebox de tkinter para mostrar mensajes emergentes
from functions import *  # Importa todas las funciones definidas en el módulo functions
from tkinter import simpledialog  # Importa simpledialog de tkinter para obtener datos del usuario de manera interactiva

# Función para el registro de usuarios
def register():
    # Función interna para procesar el registro de usuario
    def register_user():
        # Obtiene los datos ingresados por el usuario
        email = entry_mail.get()
        username = entry_user.get()
        password = entry_pass.get()

        # Codifica la contraseña ingresada
        passHashed = encode(password)

        # Verifica si el correo electrónico ingresado es válido
        if testMail(email):
            # Muestra un mensaje informativo de registro exitoso
            messagebox.showinfo("Registro", "Registro satisfactorio!")
            # Inserta la información del usuario en la base de datos
            insertRow(email, username, passHashed)
        else:
            # Muestra un mensaje de error si el correo electrónico no es válido
            messagebox.showerror("Error", "Correo Inválido")

    # Crea una ventana secundaria para el registro
    register_window = tk.Toplevel(root)
    register_window.title("Registro")

    # Configura las dimensiones y fija que la ventana no sea redimensionable
    register_window.geometry('400x200')
    register_window.resizable(False,False)

    # Etiquetas y campos de entrada para correo electrónico, usuario y contraseña
    tk.Label(register_window, text="Ingrese su Mail:").pack()
    entry_mail = tk.Entry(register_window)
    entry_mail.pack()

    tk.Label(register_window, text="Ingrese su nombre de Usuario:").pack()
    entry_user = tk.Entry(register_window)
    entry_user.pack()

    tk.Label(register_window, text="Ingrese su contraseña:").pack()
    entry_pass = tk.Entry(register_window, show="*")
    entry_pass.pack()

    # Botón para ejecutar la función de registro de usuario al hacer clic
    tk.Button(register_window, text="Registrarse", command=register_user).pack()

# Función para iniciar sesión
def logIn():
    # Función interna para procesar el inicio de sesión
    def login_user():
        # Obtiene los datos ingresados por el usuario
        username = entry_user.get()
        password = entry_pass.get()

        # Codifica la contraseña ingresada
        passHashed = encode(password)

        # Verifica si el nombre de usuario y la contraseña son válidos
        if validationLogIn(username, passHashed):
            # Simula obtener el correo asociado al nombre de usuario y contraseña
            mail = obtainMail(username, passHashed)
            # Envía un correo con un código de verificación
            verifyCode = sendmail(mail)

            # Muestra un mensaje informativo indicando que se envió el código de verificación
            messagebox.showinfo("Código de verificación", "Hemos enviado un código de verificación")

            # Solicita al usuario ingresar el código de verificación
            code = simpledialog.askstring("Código de Verificación", "Ingrese su código aquí:")

            # Compara el código ingresado por el usuario con el código generado
            if code == verifyCode:
                # Obtiene el nombre del usuario y muestra un mensaje de bienvenida
                name = namePetition(username)
                messagebox.showinfo("Bienvenida", f"Bienvenido/a {name[0]}!")
            else:
                # Muestra un mensaje de error si el código ingresado es incorrecto
                messagebox.showerror("Error", "Código erróneo")
        else:
            # Muestra un mensaje de error si el nombre de usuario o contraseña son incorrectos
            messagebox.showerror("Error", "Usuario o Contraseña Inválido")

    # Crea una ventana secundaria para el inicio de sesión
    login_window = tk.Toplevel(root)
    login_window.title("Inicio de Sesión")

    # Configura las dimensiones y fija que la ventana no sea redimensionable
    login_window.geometry('400x200')
    login_window.resizable(False,False)

    # Etiquetas y campos de entrada para nombre de usuario y contraseña
    tk.Label(login_window, text="Ingrese su nombre de Usuario:").pack()
    entry_user = tk.Entry(login_window)
    entry_user.pack()

    tk.Label(login_window, text="Ingrese su contraseña:").pack()
    entry_pass = tk.Entry(login_window, show="*")
    entry_pass.pack()

    # Botón para ejecutar la función de inicio de sesión al hacer clic
    tk.Button(login_window, text="Iniciar Sesión", command=login_user).pack()

# Crea la ventana principal de la aplicación
root = tk.Tk()
root.title("Inicio de Sesión y Registro")
root.geometry('400x200')
root.resizable(False,False)

# Botones para abrir las ventanas de registro e inicio de sesión
tk.Button(root, text="Registrarse", command=register).pack(pady=10)
tk.Button(root, text="Iniciar Sesión", command=logIn).pack(pady=10)

# Inicia el bucle principal de la aplicación
if __name__ == '__main__':
    root.mainloop()

