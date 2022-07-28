c = input('Ingrese una contraseña: ')
if c.isalpha():
    False
    print('La contraseña debe comenzar con un numero')
    c = input('Ingrese una contraseña: ')

c1 =input('Ingrese la contraseña nuevamente: ')
if c != c1:
    print('Las contraseñas no coinciden')
    c1 =input('Ingrese la contraseña nuevamente: ')
    if c1 !=c:
        print('Las contraseñas no coinciden')
        print('Fin del programa')
    if c1 == c:
        print('Contraseña correcta')
        print('Fin del programa')

elif c == c1 :
    print('contraseña correcta')
    print('Fin del programa')