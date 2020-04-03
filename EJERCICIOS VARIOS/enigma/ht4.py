#UVG
#Silvio Orozco Vizquerra
#Carne 18282
#Fecha 16/03/2018
#Archivo Hoja Principal

from moduloIO import *

#Leemos nuestro codigo a nuestro programa
codigo=leer("enigma-d.txt")
#Ahora llamamos al codigo en reversa
codigo=reversa(codigo)


#Ahora debemos encontrar las palabras de inicio y fin.
#Convertimos nuestro codigo a mayusculas para que sea mas facil encontrar las palabras
codigo=codigo.upper()
#Convertimos nuestro codigo en lista
#Separamos nuestro codigo total en palabras
codigofinal=codigo.split(" ")
#Buscamos el inicio y el final en la cadena completa
ini="ANFANG"
fin="ENDE"
ini=int(inicio(ini,codigo))
ter=int(final(fin,codigo))
descifrado=codigo[ini:ter]

#Lllamamos a nuestro archivo
archivo="respuesta.txt"

#Enviamos nuestro mensaje descifrado
escribir(descifrado,archivo)
