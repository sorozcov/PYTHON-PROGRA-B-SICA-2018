#busqueda_canciones.py
#autor: Reeborg
#fecha: 9 de abril 2018
#descripcion: programa que busca canciones en itunes
from funciones_busqueda_canciones import *


termino = "Radiohead"
print("Buscando canciones con el termino ", termino)
#Buscar canciones
dict_canciones = buscar_canciones(termino)
#Imprimir resultado
print(dict_canciones)

#Modifique el programa para que en lugar de imprimir las listas y/o diccionarios
#imprima el nombre del artista (artistName), el nombre de la cancion
#(trackName), el nombre del album (collectionName) y el genero musical
#(primaryGenreName) para todos los resultados de la busqueda



