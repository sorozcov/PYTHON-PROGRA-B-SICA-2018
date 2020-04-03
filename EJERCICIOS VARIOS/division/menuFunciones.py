#Silvio Orozco
#UVG Carne 18282
#menuFunciones.py
from funcionesUtiles import *

#Primero se importa el menu y se pide una decision
decision=(armarMenu())

#Mientras la decision no sea 2 que es salir se ejecutrara el programa
while decision!="2":
   #Se verifica si la decision fue un numero o no
    if esNumero(decision)==True :
    #Si es numero, se traslada a variable numero
     decision=int(decision)
    #Si el numero esta en el rango de opciones
     if opcionEnRango(decision,1,3):
      #Si la decision es 1 se ingrese el divisor y el dividendo
      if decision==1:
       a=input("Ingrese el divisor: ")
       b=input("Ingrese el dividendo: ")
      #Si ambos son numeros se entra a la siguiente condicion
       if (esNumero(a)==True and esNumero(b)==True):
        #Si la division b no es cero, se imprime el resultado   
         if noEsDivisionPorCero(a,b)==True:
           division=float(a)/float(b)
           print(division)
         else:
        #Si b es cero se imprime el mensaje de error
           print("Error el dividendo no puede ser 0")
       #Si se ingresan letras, se hace la observacion que ambos deben ser numeros
       else:
           print("Los dos valores ingresados ambos deben de ser numeros")
     #Si la opcion no esta en el rango, se imprime que la decision no esta en el rango
     else:
        print("Su opcion no esta en el rango")           
    #Si no es numero la opcion, se imprime que la opcion debe ser un numero
    if esNumero(decision)==False :
       print("Su opcion debe ser un numero de las opciones.")
    #Se sigue con el menu centinela
    decision=(armarMenu())
#Al escribir 2, sale del programa
print("Gracias por usar el programa")
input("")


         
    
