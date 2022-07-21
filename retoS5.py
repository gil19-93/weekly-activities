primer = input('Introduce el año actual: ')


if primer.isnumeric():
    primer1 = int(primer)
else:
    print('Dato incorrecto, debes introducir el año actual')
    exit()
if primer1 < 2022 :
    print('Eso fue en el pasado')
elif primer1 > 2022:
    print('Eso aun no pasa')


año = input('Introduce otro año para calcular: ')

if año.isnumeric():
    año1 = int(año)
else:
    print('Ingresa un año')
    exit()
if año1 <= 0 :
    print('No se puede antes de cristo')
if año1 > 2022 :
       print('Faltan ' + (str(año1 - 2022)) + ' años para llegar al año que has introducido')
if año1 < 2022:
    print('Han pasado ' + (str(2022 - año1)) + ' años desde el año que has introducido')
if año1 == 2021:
    print('Desde el año 2021 ha pasado un 1 año')
if año1 == 2023:
    print('Para llegar a 2023 hace falta 1 año')
if año1 == 2022:
    print('Has introducido el mismo año que el actual')