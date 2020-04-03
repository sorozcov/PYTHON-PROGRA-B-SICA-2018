#Universidad del Valle de Guatemala 
#Kenneth Aldana 18435
#Victor Martinez 18579
#Silvio Orozco Vizquerra 18282 
#Fecha 11-05-2018 
#preciotoalhogar.py

#Nos conectamos a la base de datos
import pymongo 
BASE_DE_DATOS = 'supermercado'
COLECCION = 'listado_compras'

conexion = pymongo.MongoClient()
coleccion_compras = conexion[BASE_DE_DATOS][COLECCION]

#Mostramos el listado de compras unicamente de hogar
print("---------------------------------------")
print("       LISTADO DE COMPRAS HOGAR")
print("---------------------------------------")
total=0
#El total al principio es 0
#Para cada producto con categoria hogar, lo imprimeremos
#Costo es igual a cantidad*producto
#Se suma el total en  cada iteracion
for producto in coleccion_compras.find({"categoria":'hogar'}):
    print(str(producto['cantidad'])+","+ str(producto['producto'])+","+str(producto['precio'])+"C/U ," +str(producto['categoria'])+","+str(producto['tienda']))
    costo=producto['cantidad']*producto['precio']
    total=total+costo
#Se muestra el total
print("---------------------------------------")
print("El precio total es ", total)
print("---------------------------------------")
nocerrar=input("")
