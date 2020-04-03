#Universidad del Valle de Guatemala
#Jose Huerta Carne 18216
#Silvio Orozco Carne 18282
#20/04/2018
#Base de Datos Spotify

from modulosspotify import*
import pymongo

#Nos conectamos a la base de datos
conexion= pymongo.MongoClient()
#Buscamos la db que queremos.
db = conexion['spotify']
#Seleccionamos la coleccion
coleccion= db.MusicaSpotify

#Mostramos menu
opcion=menu()
opcion=verificaropcion(opcion)
opcion=int(opcion)
#Mientras la opcion no sea salir

while opcion!=3:
    #Pedimos toda la informacion para agregar una nueva cancion y realizamos todas las verificaciones.
    if opcion==1:
        print("Necesitamos algunos datos para ingresar una nueva cancion.")
        nombre=input("Ingrese el nombre: ")
        album=input("Ingrese el album: ")
        artistas=[]
        #Pregunta cuantos artistas hay para agregarlos a una lista.
        pregartista=input("Cuantos artistas tiene la cancion?")
        while pregartista.isnumeric()==False:
           pregartista=input("Cuantos artistas tiene la cancion?: ")
        pregartista=int(pregartista)
        if  (pregartista)!=0:
            for x in range(1,pregartista+1):
                art=input("Ingrese el nombre de uno de los artistas: ")
                artistas.append(art)
        else:
            artistas.append("")
        pregresena=input("Desea ingresar una resena, si o no: ")
        pregresena=pregresena.lower()
        #Pregunta si desea la resena o no.
        if pregresena!='no' and pregresena=='si':
            puntuacion=input("Ingrese su puntuacion de 0 a 5: ")
            puntuacion=float(puntuacion)
            while (puntuacion in range(0,6))==False and puntuacion!='':
                puntuacion=input("Ingrese su puntuacion de 0 a 5: ")
                puntuacion=float(puntuacion)
            comentario=input("Ingrese su comentario: ")
            usuario=input("Ingrese su usuario: ")
            resena= {'Puntuacion' : puntuacion,
                    'Comentario' : comentario,
                    'Usuario' : usuario
                }
        else:
            
            resena= {'Puntuacion' : '',
                    'Comentario' : '',
                    'Usuario' : ''
                }
        print('Para ingresar duracion')
        minutos=input('Ingrese minutos: ')
        segundos=input("Ingrese segundos: ")
        while (minutos.isnumeric()==False or segundos.isnumeric()==False) and (minutos!='' or segundos!=''):
            print("Los minutos y segundos deben ser numeros")
            minutos=input('Ingrese minutos: ')
            segundos=input("Ingrese segundos: ")
        duracion=(''+str(minutos)+':'+str(segundos))
        lanzamiento=input("Ingrese anio de lanzamiento: ")
        while lanzamiento.isnumeric()==False and lanzamiento!='':
            print("El anio de lanzamiento debe ser un numero")
            lanzamiento=input("Ingrese anio de lanzamiento: ")
        genero=input("Ingrese el genero: ")
        pais=input('Ingrese el pais: ')
        idioma=input('Ingrese el idioma: ')
        #Se crea un nuevo diccionario, con la informacion de dicha cancion.
        cancion=    {
        'Nombre': nombre,
        'Album': album,
        'Artistas': artistas,
        'Resenas': resena,
        #Con comentario, puntuacion y nombre de usuario.
        'Duracion': duracion,
        'Lanzamiento':lanzamiento,
        'Genero':genero,
        'Pais' :pais,
        'Idioma' : idioma,
        }
        #Enviamos nuestra nueva informacion a la base de datos
        coleccion.insert(cancion)
    
    elif opcion==2:
        numero=1
        #Mostramos canciones una por una. Si no tienen los datos , se muestra espacio vacio.
        
        for cancion in coleccion.find():
            #De esta manera se ve ordenada y se llama a los datos guardados en la base de datos.
         print("-------------------------------------")
         print("Cancion ",numero)
         print('Nombre: ' ,cancion['Nombre'])
         print('Album: ' ,cancion['Album'])
         print('Artistas: ')
         for artista in cancion['Artistas']:
               print(artista)
         print ('Resenas: ' )
         print('Puntuacion: ', cancion['Resenas']['Puntuacion'])
         print("Comentario: ", cancion['Resenas']['Comentario'])
         print('Usuario: ', cancion['Resenas']['Usuario'])
        #Con comentario, puntuacion y nombre de usuario.
         print('Duracion: ', cancion['Duracion'])
         print('Lanzamiento: ',cancion['Lanzamiento'])
         print('Genero: ',cancion['Genero'])
         print('Pais: ' ,cancion['Pais'])
         print('Idioma: ', cancion['Idioma'])
         print("-------------------------------------")
         numero=numero+1
    opcion=menu()
    opcion=verificaropcion(opcion)
    opcion=int(opcion)
#Salimos del programa
print("Gracias por utilizar el programa.")

