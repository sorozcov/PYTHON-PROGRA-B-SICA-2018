#Universidad del Valle de Guatemala 
#Kenneth Aldana 18435
#Victor Martinez 18579
#Silvio Orozco Vizquerra 18282 
#Fecha 11-05-2018 
#actualizartienda.py

#Importamos la base de datos y nos conectamos
import pymongo 
BASE_DE_DATOS = 'supermercado'
COLECCION = 'listado_compras'

conexion = pymongo.MongoClient()
coleccion_compras = conexion[BASE_DE_DATOS][COLECCION]
producto=input("Ingrese el nombre del producto que desea cambiar:")
#Ingresa el producto y si encuentra una coincidencia en el programa, puede ingresar la nueva tienda, sino entra a un ciclo que muestra error y pregunta de nuevo.
while (coleccion_compras.count({"producto":producto})>0)==False:
    print("El producto ingresado no existe")
    producto=input("Ingrese el nombre del producto que desea cambiar:")
#Se agrega a la nueva tienda y se actualiza la base de datos.
if (coleccion_compras.count({"producto":producto})>0)==True:
    tienda=input("Ingresa el nombre de la tienda para actualizar el producto: ")
    resultado = coleccion_compras.update_one({"producto":producto},{"$set":{"tienda":tienda}})
    print("Se ha actualiza la tienda del producto " +str(producto)+" a la tienda " +str(tienda)+".")

#Se muestra el producto actualizado
print("El producto actualizado es: ")
for producto in coleccion_compras.find({"producto":producto}):
   print(str(producto['cantidad'])+","+ str(producto['producto'])+","+str(producto['precio'])+"C/U ," +str(producto['categoria'])+","+str(producto['tienda'])) 
nocerrar=input("")
