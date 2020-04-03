
#Universidad del Valle de Guatemala
#Silvio Orozco Vizquerra 18282
#13/04/2018
#Planetas.py

#Importamos nuestro modulo
from modulososcars import *
import os

#Declaramos nuestro diccionario de las categorias existentes por el momento.
oscars = {
    'MEJOR PELICULA' : ['THE SHAPE OF WATER','LADY BIRD','DUNKIRK'],
    'MEJOR ACTRIZ' : ['MERYL STREEP','FRANCES MCDORMAND'],
    'MEJOR ACTOR' : ['GARY OLDMAN','DENZEL WASHINGTON']
   
}

#Llamamos al menu y verificamos opcion.
opcion=menu()
opcion=verificaropcion(opcion)
#Ya verificada, sabemos que es numero.
opcion=int(opcion)
#Ahora segun su opcion escogida. Realiza cierta accion.
#Mientras opcion no sea 7(salir ) se realizara el programa.


while opcion!=7:
    #Agregar una categoria
    if opcion==1:
        print("")
        oscars=agregarcategoria(oscars)

    #Agregar un nominado
    elif opcion==2:
        print("")
        oscars=agregarnominado(oscars)
            
    #Agregar un planeta    
    elif opcion==3:
        print("")
        oscars=eliminarnominado(oscars)

    #Eliminar un cateria   
    elif opcion==4:
        print("")
        oscars=eliminarcategoria(oscars)

    #Se puede ver una sola categoria.    
    elif opcion==5:
        print("")
        vercategoria(oscars)
        
    elif opcion==6:
        print("")
        vertodaslascategorias(oscars)
        
    #Se visualiza hasta que se presiona enter.
    input("")
    os.system('cls')
    #Repetimos el ciclo
    opcion=menu()
    opcion=verificaropcion(opcion)
    opcion=int(opcion)
    print("")
    
#Termina el programa
print("El programa ha terminado.")
print("Gracias por usar el programa.")
input("")
