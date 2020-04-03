#Universidad del Valle de Guatemala
#Jose Huerta Carne 18216
#Silvio Orozco Carne 18282
#22/04/2018
#modulosspotify.py

#Funcion del menu para tener una opcion de lo que desea hacer.
def menu():
    opcion = input("""
---------------------------------------------
                   SPOTIFY
---------------------------------------------

1.   Agregar nueva cancion.
2.   Mostrar todas las canciones.
3.   Salir

---------------------------------------------
Su opcion es : 
""")
    return opcion

#Verificar si la opcion ingresada es numero y esta en el rango de opciones.
def verificaropcion(opcion):
    #Es un numero en el rango.
    if opcion.isnumeric()==True:
        opcion=int(opcion)
        if (opcion in range(1,4))==False:
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


