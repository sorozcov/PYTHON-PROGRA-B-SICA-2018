#Silvio Orozco 18282
#Pablo Ruiz 18259
#UVG. 03-02-2017
#MascotaInteligente

#Preguntamos usuarios y cantidad de beepers por habitaciones 4.
usuario= input("Ingrese el nombre del usuario: ")
hab1= input("Ingrese el numero de beepers en la habitación 1: ")
hab2= input("Ingrese el numero de beepers en la habitación 2: ")
hab3= input("Ingrese el numero de beepers en la habitación 3: ")
hab4= input("Ingrese el numero de beepers en la habitación 4: ")
#Preguntamos cuantos beepers fueron encontrados afuera de la habitacion
afuera= input("Ingrese el numero de beepers en los pasillos(afuera de las habitaciones): ")
#Convertimos los datos de las habitaciones y beepers afuera de la habitacion a datos numericos y luego sumamos los beepers en la habitacion
hab1= int(hab1)
hab2= int(hab2)
hab3= int(hab3)
hab4= int(hab4)
afuera = int(afuera)
habt = hab1+hab2+hab3+hab4 
#Sumamos el total de beepers
beept= habt+afuera
#Mostramos reporte
#Cantidad de beepers en habitacion
#Beepers en toda la historia
#Habitacionconmenosbeepers
#True si la suma es mayor a 13
print("REPORTE")
print(usuario, "encontro un total de",habt, "beepers en las habitaciones")
print(usuario, "encontro un total de",beept, "beepers en todo la historia")
hab=[hab1,hab2,hab3,hab4]
while (min(hab)<=0):
    del(hab[min(hab)])
if min(hab)== hab1:
       minhab=1
elif min(hab)==hab2:
       minhab=2
elif min(hab)==hab3:
       minhab=3
elif min(hab)==hab4:
       minhab=4
print(usuario, " encontro menos beepers en la habitacion ",minhab)
mayora13= bool(beept>13)
print(usuario, " encontro mas de 13 beepers: ",mayora13)
input("")
