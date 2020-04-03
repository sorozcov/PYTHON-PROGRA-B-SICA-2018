#Universidad del Valle de Guatemala
#Silvio Orozco 18282
#Pablo Ruiz 18259
#Fecha 09/02/18
#Ejercicio que ingresa longitud de onda en menu centinela.
#Pedimos longitud de onda la primera vez
print("Algoritmo de Ramanujar")
numero= input("Ingrese el numero para verificar si es un numero taxi o 'Fin' para terminar el programa: ")
#Creamos el ciclo while para que mientras no se ingrese Fin se puedan consultar mas numeros

while numero!= "Fin":
#Convertimos el dato ingresa a integer
    numero=int(numero)
    numero=a**3 + b**3
    numero=c**3+b**3
    if numero==(a**3+b**3) and numero==(c**3+d**3)and (a!=b and b!=c and c!=d):
        print ("El numero es un numero taxi")
        print ("Un componente es", a)
        print ("Un componente es", b)
        print ("Un componente es", c)
        print ("Un componente es", d)
    else:
        print ("El numero no es un numero taxi")
    

#Pedimos que ingrese de nuevo un dato para el menu centinela   
    numero= input("Ingrese el numero para verificar si es un numero taxi o 'Fin' para terminar el programa: ")
  




