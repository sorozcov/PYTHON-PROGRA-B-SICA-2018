#Universidad del Valle de Guatemala
#Silvio Orozco 18282
#Pablo Ruiz 18259
#Fecha 09/02/18
#Ejercicio que ingresa longitud de onda en menu centinela.
#Pedimos longitud de onda la primera vez
print("Longitud de onda")
londa= input("Ingrese la longitud de onda o 'Fin' para terminar el programa: ")
#Creamos el ciclo while para que mientras no se ingrese Fin se puedan consultar mas longitudes de onda

while londa!= "Fin":
#Cambiamos la longitud de onda a integer
 londa=int(londa)
 color= "El color de onda de"
#Creamos un if para mostrar un mensaje segun longitud de onda
 if londa<380 or londa>750:
     print("El color de onda no puede ser menor a 450 ni tampoco puede ser mayor a 750")
 elif londa>=380 and londa<450:
     print(color+"",londa,"es violeta")
 elif londa>=450 and londa<495:
     print(color+"",londa,"es azul")
 elif londa>=495 and londa<570:
     print(color+"",londa,"es verde")
 elif londa>=570 and londa<590:
     print(color+"",londa," es amarillo")
 elif londa>=590 and londa<620:
     print(color+"",londa,"es naranja")
 elif londa>=620 and londa<750:
     print(color+"",londa,"es rojo")
     #Volvemos a pedir la longitud de onda o fin para seguir con el programa
 londa= input("Ingrese la longitud de onda o 'Fin' para terminar el programa: ")

input("")
