"""
    CRUD Básico realizado en Python utilizando MySQL
    paradigma utilizado: Estructurado
    fecha: 29.01.21
"""
#importar modulo conexión
import os
import sys
import time
from CRUD import crud

#Menu
print("\n********** CRUD BASICO *********")
print("1.-Mostrar")
print("2.-Insertar")
print("3.-Actualizar")
print("4.-Eliminar")
print("5.-Salir")
print("6.-Limpiar Pantalla")
print("7.-Buscar por id")
print("8.-Buscar por username")
print("9.-Buscar por letra")

opcion = int(input("Ingrese su opción: "))

while True:
    if opcion == 1:
        crud.mostrar()
    elif opcion == 2:
        crud.insertar()
    elif opcion == 3:
        crud.actualizar()
    elif opcion == 4:
        crud.eliminar()
    elif opcion == 5:
        print("Termiando ejecución")
        time.sleep(1) #retrar salida
        sys.exit(0) #cerrar programa
    elif opcion == 6:
        os.system('cls')
    elif opcion == 7:
        crud.buscarPorId()
    elif opcion == 8:
        crud.buscarPorNombre()
    elif opcion == 9:
        crud.buscarPorLetra()
    else:
        print("Opcion incorrecta")
        time.sleep(0.5)
    

    print("\n********** CRUD BASICO *********")
    print("1.-Mostrar")
    print("2.-Insertar")
    print("3.-Actualizar")
    print("4.-Eliminar")
    print("5.-Salir")
    print("6.-Limpiar Pantalla")
    print("7.-Buscar por Id")
    print("8.-Buscar por username")
    print("9.-Buscar por letra")
    opcion = int(input("Ingrese su opción: "))



