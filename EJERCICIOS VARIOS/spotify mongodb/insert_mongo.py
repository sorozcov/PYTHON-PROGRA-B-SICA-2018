#Universidad del Valle de Guatemala
#Jose Huerta Carne 18216
#Silvio Orozco Carne 18282
#Fecha 20/04/2018
#Base de Datos Spotify

import pymongo

#Creamos nuestra lista con 4 canciones.
diccionariomusica = [
    #Damos campos iniciales
    {
        'Nombre': 'Mujeres',
        'Album': 'Animal Nocturno',
        'Artistas':['Ricardo Arjona'],
        'Resenas':{'Puntuacion' : '5.0',
                    'Comentario' : 'Bonita cancion',
                    'Usuario' : 'Huerta'},
        #Con comentario, puntuacion y nombre de usuario.
        'Duracion':'3:26',
        'Lanzamiento':'1999',
        'Genero':'Balada',
        'Pais' :'Guatemala',
        'Idioma' : 'Espanol',
    },
    {
        'Nombre': 'Perfect',
        'Album': 'Deluxe',
        'Artistas':['Ed Sheeran'],
        'Resenas':{'Puntuacion' : '',
                    'Comentario' : '',
                    'Usuario' : ''
                },
        #Con comentario, puntuacion y nombre de usuario.
        'Duracion':'4:22',
        'Lanzamiento':'2017',
        'Genero':'Balada/Pop',
        'Pais' :'Estados Unidos',
        'Idioma' : 'Ingles',
    },
    {
        'Nombre': 'Mujeres Divinas',
        'Album': 'Mujeres Divinas',
        'Artistas':['Vicente Fernandez'],
        'Resenas':{'Puntuacion' : '',
                    'Comentario' : '',
                    'Usuario' : ''
                },
        
        #Con comentario, puntuacion y nombre de usuario.
        'Duracion':'3:13',
        'Lanzamiento':'2003',
        'Genero':'Rancheras',
        'Pais' :'Mexico',
        'Idioma' : 'Espanol',
    },
    {
        'Nombre': 'Back in Black',
        'Album': 'Back in Black',
        'Artistas':['ACDC'],
        'Resenas':{'Puntuacion' : '',
                    'Comentario' : '',
                    'Usuario' : ''
                },
        #Con comentario, puntuacion y nombre de usuario.
        'Duracion':'4:15',
        'Lanzamiento':'1980',
        'Genero':'Rock',
        'Pais' :'Estados Unidos',
        'Idioma' : 'Ingles',
    },
    ]

#Nos conectamos a la base de datos
conexion= pymongo.MongoClient()
#Buscamos la db que queremos.
db = conexion['spotify']
#Seleccionamos la coleccion
coleccion= db.MusicaSpotify

#Recorremos el diccionario y lo guardamos en la coleccion
for musica in diccionariomusica:
    coleccion.insert(musica)
    


