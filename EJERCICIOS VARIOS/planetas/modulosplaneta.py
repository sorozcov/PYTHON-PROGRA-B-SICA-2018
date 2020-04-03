#Universidad del Valle de Guatemala
#Silvio Orozco Vizquerra 18282
#13/04/2018
#modulosplanetas.py

#Funcion del menu para tener una opcion de lo que desea hacer.
def menu():
    opcion = input("""
---------------------------------------------
                SISTEMA DE PLANETAS
---------------------------------------------

1. Ver todos los planetas.
2. Buscar un planeta.
3. Ingresar un nuevo planeta.
4. Eliminar un planeta.
5. Salir.
---------------------------------------------
Su opcion es : 
""")
    return opcion

#Verificar si la opcion ingresada es numero y esta en el rango de opciones.
def verificaropcion(opcion):
    if opcion.isnumeric()==True:
        opcion=int(opcion)
        if (opcion in range(1,6))==False:
            print("Su opcion ingresada no esta en el rango de opciones")
            opcion=menu()
            opcion=verificaropcion(opcion)
        else:
            opcion=opcion
    else:
        print("Su opcion ingresada no es un numero")
        opcion=menu()
        opcion=verificaropcion(opcion)
    return opcion

#Llamar a un planeta
def planetaaver():
      planetaaver=input("Ingrese el nombre del planeta que desea ver: ")
      return planetaaver
    
#Agregar un planeta
def agregarplaneta():
    planetaagregar=input("Ingrese el nombre del planeta que desea agregar: ")
    return planetaagregar

#Agregar descripcion
def agregardescripcion():
    descripcion=input("Ingrese la descripcion del planeta que desea agregar: ")
    return descripcion

#Eliminar planeta
def eliminarplaneta():
    planetaaeliminar=input("Ingrese el nombre del planeta que desea eliminar: ")
    return planetaaeliminar

#Ver si tiene el planeta en la base de datos
def planetashas_key(planeta, planetas):
    if (planeta in planetas)==True:
        tiene=True
    else:
        tiene=False
    return tiene
    
