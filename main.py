import tkinter as tk
from tkinter import messagebox
from functions import *
from tkinter import simpledialog

def register():
    def register_user():
        email = entry_mail.get()
        username = entry_user.get()
        password = entry_pass.get()

        passHashed = encode(password)

        if testMail(email):
            messagebox.showinfo("Registro", "Registro satisfactorio!")
            insertRow(email, username, passHashed)
        else:
            messagebox.showerror("Error", "Correo Inválido")

    register_window = tk.Toplevel(root)
    register_window.title("Registro")

    register_window.geometry('400x200')
    register_window.resizable(False,False)

    tk.Label(register_window, text="Ingrese su Mail:").pack()
    entry_mail = tk.Entry(register_window)
    entry_mail.pack()

    tk.Label(register_window, text="Ingrese su nombre de Usuario:").pack()
    entry_user = tk.Entry(register_window)
    entry_user.pack()

    tk.Label(register_window, text="Ingrese su contraseña:").pack()
    entry_pass = tk.Entry(register_window, show="*")
    entry_pass.pack()

    tk.Button(register_window, text="Registrarse", command=register_user).pack()

def logIn():
    def login_user():
        username = entry_user.get()
        password = entry_pass.get()

        passHashed = encode(password)

        if validationLogIn(username, passHashed):
            mail = obtainMail(username,passHashed)  # Simulamos obtener el correo del usuario
            verifyCode = sendmail(mail)

            messagebox.showinfo("Código de verificación", "Hemos enviado un código de verificación")

            code = simpledialog.askstring("Código de Verificación", "Ingrese su código aquí:")

            if code == verifyCode:
                name = namePetition(username)
                messagebox.showinfo("Bienvenida", f"Bienvenido/a {name[0]}!")
            else:
                messagebox.showerror("Error", "Código erróneo")
        else:
            messagebox.showerror("Error", "Usuario o Contraseña Inválido")

    login_window = tk.Toplevel(root)
    login_window.title("Inicio de Sesión")

    login_window.geometry('400x200')
    login_window.resizable(False,False)

    tk.Label(login_window, text="Ingrese su nombre de Usuario:").pack()
    entry_user = tk.Entry(login_window)
    entry_user.pack()

    tk.Label(login_window, text="Ingrese su contraseña:").pack()
    entry_pass = tk.Entry(login_window, show="*")
    entry_pass.pack()

    tk.Button(login_window, text="Iniciar Sesión", command=login_user).pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión y Registro")
root.geometry('400x200')
root.resizable(False,False)

# Botones para registro e inicio de sesión
tk.Button(root, text="Registrarse", command=register).pack(pady=10)
tk.Button(root, text="Iniciar Sesión", command=logIn).pack(pady=10)

if __name__ == '__main__':
    root.mainloop()
