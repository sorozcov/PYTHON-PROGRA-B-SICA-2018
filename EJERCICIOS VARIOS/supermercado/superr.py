#supermercado.py
#autor: Reeborg
#fecha: 9 de abril 2018
#descripcion: programa que lleva el control del precio y del inventario de
#articulos del supermercado

#Importa las funciones del siguiente documento.
from funciones_supermercado import *

#Diccionario de items dentro del super.
items_super = {
    'manzanas': {
        'cantidad': 5,
        'precio': 1.25
    },
    'arroz': {
        'cantidad': 6,
        'precio': 5.75
    },
    'leche': {
        'cantidad': 12,
        'precio': 12.25
    }
}


opcion = 0
while opcion != 4:
    print(menu())
    opcion = input("Ingrese su opcion ")
    while not opcion.isdigit():
        opcion = "Ingrese su opcion: "

    opcion = int(opcion)
    if opcion == 1:
        print()
        print("El inventario es")
        print()
        for nombre in items_super:
            print (nombre, ' cantidad ', items_super[nombre]['cantidad'], ' precio ', items_super[nombre]['precio'])
        print()

    elif opcion == 2:
        nombre = input("Ingrese el nombre del articulo: ")
        cantidad = input("Ingrese la cantidad: ")
        while not cantidad.isdigit():
            cantidad = input("Ingrese la cantidad: ")
        cantidad = int(cantidad)
        precio = input("Ingrese el precio: ")
        while not es_float(precio):
            precio = input("Ingrese el precio: ")
        precio = float(precio)
        items_super[nombre] = {'cantidad': cantidad, 'precio': precio}
        print ("Se agrego el producto ", nombre , " al diccionario ")

        
    elif opcion == 3:
        nombre = input("Ingrese el producto que desea modificar: ")
        if nombre in items_super:
            cantidad = input("Ingrese la nueva cantidad: ")
            while not cantidad.isdigit():
                cantidad = input("Ingrese la nueva cantidad: ")
            #Aqui debe ser la cantidad igual al entero de la cantidad
            cantidad = int(cantidad)
            items_super[nombre]['cantidad']=cantidad
        else:
            print("Ese articulo no se encuentra en el inventario")

                  
    elif opcion == 4:
        print ("Gracias por utilizar nuestro servicio")
    else:
        print("Opcion no valida")
                





