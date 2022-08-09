lista = []

alumnos = 0 
while alumnos <= 10:
    opcion = input('Agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre de los alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        calificacion3 = int(input(f'Ingrese la primera calificacion de {nombre}: '))
        promedio = (calificacion3 + calificacion2 + calificacion1) / 3
        alumno = [nombre, calificacion1, calificacion2, calificacion3,'Promedio - ''{:.1f}'.format(promedio)]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'El programa ha terminado con {alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opcion invalida. ')
        continue
print('La lista de alumnos es: ')
print(lista)
