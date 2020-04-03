#Universidad del Valle de Guatemala
#Silvio Orozco 18282
#Pablo Ruiz 18259
#Fecha 09/02/18
#Ejercicio para saber si es un numero taxicab
print("Bienvenido a la calculadora de numeros taxicab. Si su numero no produce un resultado, no es taxicab.")
#Pedimos que ingrese un numero para conocer si es taxicab o fin para terminar
numero=input("Ingrese el numero que desea probar o 'fin' para terminar: ")
#Creamos nuestro menu centinela
suma=0
while numero != "fin":
    #Cambios la entrada a numero y creamos una variable que es la raiz cubica de dicho numero
    numero=int(numero)
    cubica=round(pow(numero,1/3))
    x=0
    #Nuestro rango de numeros sera entre 1 y dicha raiz cubica
    for a in range(1,cubica+1):
        for b in range(1,cubica+1):
            numero=int(numero)
            #Si a3+b3= numero y a distinto de b entonces es numero taxi y mostrara los sumados que lo compones
            if a**3+b**3 == numero and a**3 != b**3:
                 x=x+1
                 if x==1 and numero>=1729:
                  print("Si es un numero taxicab")
                  print("Los números al cubo sumados que componen a",numero,"son:")
                 if x<=2 and numero>=1729 and suma!=a+b:
                  print(a)
                  print(b)
                  suma=a+b
                 if x==2 and numero>=1729:
                  print("Pueden existir mas de 2 posibilidades, este programa fue disenado para mostrar las primeras 2 posibilidades de combinacion de numeros")
    #Si nuestro codigo no encuentra ningun sumanda, mostrara que no es un taxicab.
    if x==0 or suma!=a+b:
     print("No es un numero taxicab")
    #Se repite el menu centinela de nuevo
    numero=input("Ingrese el numero que desea probar o 'fin' para terminar: ")
print("Gracias buscar números taxicab con este código, esperamos que haya sido de su agrado")
print("Presione cualquier tecla para salir.")
input("")
