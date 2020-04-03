#Silvio Orozco
#UVG Carne 18282
#funcionesUtiles.py



#1.Recibe una variable y validad que sea un float.
def esNumero(x):
    try:
        #Si x, se puede convertir en float entonces real es verdadero
        x=float(x)
        real=True
    except ValueError:
        #De lo contrario es falso
        real=False
    return real

#2.Recibe 2 numeros y el segundo numero no puede ser 0
def noEsDivisionPorCero(a,b):
    try:
      #Si b es distinto de 0, a/b si se puede
       y=float(a)/float(b)
       division=True
    except ZeroDivisionError:
      #De lo contrario no se puede realizar la division
      division=False
    return division

#3.Opcion en rango
def opcionEnRango(x,a,b):
        if (x in range(a,b))==True:
        #Si x esta entre a y b
         rango=True
        else:
        #Si x no esta entre a y b
         rango=False
        return rango

#4.ArmarMenu
def armarMenu():
    #Imprime el menu
   print("""
Ingrese 1 para realizar la division.
Ingrese 2 salir del menu.""")
   decision=(input("Opcion: "))

 
   #Imprime que desea hacer
   return decision

