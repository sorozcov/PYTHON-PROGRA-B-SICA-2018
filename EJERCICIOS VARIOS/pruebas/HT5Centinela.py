#ejercicio 1 Repeticion con centinela
#Silvio Orozco 18282
#Pablo Ruiz 18259
#Fecha 9 de febrero de 2018

#Calculadora de calorias

#Definicion de variables
suma = 0
caloria = input("ingrese el numero de calorias, o 'fin' para terminar: ")
cantidad = 0

#Ciclo while
#Mientras no se ingrese 'fin', el ciclo sigue corriendo
while caloria!= "fin":
    #Se convierte la variable caloria a un entero 
    caloria = int(caloria)
    #La suma de calorias es igual a la suma previa mas la caloria ingresada, suma = suma + caloria
    suma += caloria
    #Se le suma uno a la cantidad de elementos ingresados
    cantidad+=1
    #Se repite el ingreso de datos
    caloria = input("ingrese el numero de calorias, o 'fin' para terminar: ")
    
#Resultados del ciclo
#se imprimen una vez el usuario ha ingresado 'fin'
print("")
print("Resultados \n")
print("La suma total de calorias es:",suma)
print("Cantidad de calorias leidas:",cantidad)
print("El promedio de calorias es:",suma/cantidad)
#Se añade esto para que no se cierre el programa al finalizar
input("")

