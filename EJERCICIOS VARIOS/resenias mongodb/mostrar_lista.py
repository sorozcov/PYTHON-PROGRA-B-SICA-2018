#Universidad del Valle de Guatemala 
#Kenneth Aldana 18435
#Victor Martinez 18579
#Silvio Orozco Vizquerra 18282 
#Fecha 11-05-2018 
#mostrar_lista.py

#Nos conectamos a la base de datos.
import pymongo 
BASE_DE_DATOS = 'supermercado'
COLECCION = 'listado_compras'

conexion = pymongo.MongoClient()
coleccion_compras = conexion[BASE_DE_DATOS][COLECCION]

#Imprimimos todo el listado de compras
print("---------------------------------------")
print("         LISTADO DE COMPRAS")
print("---------------------------------------")

#Se impreme cada producto encontrado en la base de datos
for producto in coleccion_compras.find():
    print(str(producto['cantidad'])+","+ str(producto['producto'])+","+str(producto['precio'])+"C/U ," +str(producto['categoria'])+","+str(producto['tienda']))
nocerrar=input("")
