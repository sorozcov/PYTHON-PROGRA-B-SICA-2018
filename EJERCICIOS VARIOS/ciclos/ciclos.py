#Universidad del Valle
#Silvio Orozco Carne 18282
#Fecha 16-02-18
#El programa pedira ingresar start, stop y setp
inicio=int(input("Ingrese un numero con el cual generar e iniciar el ciclo: "))
fin=int(input("Ingrese un numero con el cual finalizara: "))
paso=int(input("Ingrese el paso con el que se incrementara el valor de inicio hasta llegar al valor final: "))
#ahora el programa iniciara con inicio hasta llegar a fin con step paso
#si es par y divisible entre 5 mostrara un mensaje
#si es par y no divisble mostrara ese mensaje
#si es impar y divisble en 9 mostrara mensaje
#si es impar y no divisble entre 9 mostrara mensaje
for i in range (inicio,fin+1,paso):
        if i%2==0 and i%5==0:
            #par y div5
            print (str(i)+ " es par y divisible entre 5")
        elif i%2==0 and i%5!=0:
            #par y no div5
            print (str(i)+ " es par pero no divisible entre 5")
        elif i%2==1 and i%9==0:
            #imp y div9
            print(str(i)+ " es impar y divisible entre 9")
        elif i%2==1 and i%9!=0:
            #imp y no div9
            print(str(i)+ " es impar pero no es divisible entre 9")
#fin del programa
a=input("")
