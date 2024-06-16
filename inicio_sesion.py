from functions import register,logIn

print('¡BIENVENIDO!')

do = input('1)Iniciar Sesión\n2)Registrarse\n-----------------\nIngrese 1 o 2: ')

if do == '1':
    logIn()
    
elif do == '2':
    register()
else:
    print('opcion inválida')