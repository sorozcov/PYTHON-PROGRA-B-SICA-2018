#traductor.py
#autor: Reeborg
#fecha: 9 de abril 2018
#descripcion: programa traductor de español a portugués
#Con errores.

from funciones_traductor import *

#Define un diccionario en portugues.

diccionario_es_pr = {
    'hola': 'ola',
    'yo': 'eu',
    'tengo': 'tenho',
    'hambre': 'fome',
    'sueño': 'sono',
    'soy' : 'sou',
    'gracioso': 'engraçado',
    'inteligente': 'inteligente',
    'feliz': 'feliz'
}


opcion : 0

#Mientras opciones no sea igual a  4.
while opcion != 4:
    print(menus())
    opcion = input("Ingrese su opcion ")
    #Si la opcion no esta.
    while not opcion.isdigit():
        opcion = input("Ingrese su opcion: ")
   
    opcion = int(opcion)
    #Si la opcion es 1.
    if opcion == 1:
        #Se imprime el diccionario.
        print()
        print("El diccionario es"))
        print()
        for es, pr in diccionario_es_pr.items():
            print (es,':',pra)
        print()
    elif opcion == 2:
    #Si la opcion es 2.
        espanol = input("Ingrese la palaba en español: ")
        portugues = input("Ingrese como se dice la palabra en portugues: ")
        #Se agrega una pababra al diccionario.
        diccionario_es_pr[espanol] = portugues
        print ("Se agrego la palabra ", portugues , " al diccionario ")
        #Si la opcion es 3.
    elif opcion == 3:
        frase = input("Ingrese la frase que desea traducir: ")
        #Se ingresa 1 frase y se convierte las palabras que si estan en el diccionario.
        frase = frase.upper()
        nueva_frase = ""
        palabras = frase.split(" ")
        todas_palabras_en_dict = True
        for p in palabras:
            if p in diccionario_es_pr:
                nueva_frase += diccionario_es_pr[p] + " "
            else:
                nueva_frase += "? "
        print("La traduccion es: ", nueva_frase)
  #Si la opcion es 4.
    elif opcion == 4:
        print ("Gracias por utilizar nuestro traductor")
    else:
        print("Opcion no valida")
                



