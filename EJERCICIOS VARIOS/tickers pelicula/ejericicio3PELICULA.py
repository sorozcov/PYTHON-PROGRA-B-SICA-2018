#Universidad del Valle de Guatemala
#Silvio Orozco 18282
#Fecha 16/02/18
#CineUVG

#Damos la bienvenida al cine de manera ordenada
print("-------------------------------------------------------------------")
print ("Bienvenido al cine UVG")
print("-------------------------------------------------------------------")
#Brindamos las opciones de funcione que existen. Pensamos que hay asientos ilimitados y una unica funcion
print("Las opciones de película son las siguientes:")
print ("Funcion1 : Toy Story")
print ("Funcion2 : 50 Sombras de Grey")
print ("Funcion3 : Ted")
print("-------------------------------------------------------------------")
#El precio de los tickets es 30
tic=30
print ("El precio de todos los tickets es Q.30.00")
#Damos instrucciones sobre que se debe hacer.
print ("Ingrese el nombre de la pelicula para agregar o eliminar tickers.")
print("Ingrese 'Fin' para salir y ver sus elecciones")
print("Ingrese 'Funciones' par mostrar de nuevo las funciones")
print("-------------------------------------------------------------------")
menu=0
pel1=0
pel2=0
pel3=0
print("")
#Ingresamos opcion de pelicula,fin o funciones
pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")
#Mientras lo ingresado no sea fin
while pel!="Fin":

#Si la pelicula es Toy Story sera la variable pel1
        if pel=="Toy Story":
           print ("La cantidad de tickets para ",pel," función en este momento es ",pel1)
           opc=input("Desea agregar o eliminar tickets(Ingresa 'agregar'  o 'eliminar' tickets): ")
#Se pueden agregar o eliminar tickets
#Si se eliminan mas tickets y hay numero de tickers negativo entonces tickets sera igual 0
#Al inicio muestra la cantidad de tickets antes de agregar o eliminar y luego muestra la cantidad de tickets final luego de editar.
           if opc=="agregar":
               agre=int(input ("Ingrese la cantidad a agregar: "))
               pel1=pel1+agre
           elif opc=="eliminar":
               eli=agre=int(input ("Ingrese la cantidad a eliminar: "))
               pel1=pel1-eli
               if pel1<0:
                pel1=0 
           else:
               print("Opción elegida no es valida solo puede ser agregar o eliminar")
           print ("La nueva cantidad de tickets para ",pel," función en este momento es ",pel1)
           print("")
           pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")

#Si la pelicula es 50 Sombras de Grey sera la variable pel2
        elif pel=="50 Sombras de Grey":
           print ("La cantidad de tickets para ",pel," función en este momento es ",pel2)
           opc=input("Desea agregar o eliminar tickets(Ingresa 'agregar'  o 'eliminar' tickets): ")
#Se pueden agregar o eliminar tickets
#Si se eliminan mas tickets y hay numero de tickers negativo entonces tickets sera igual 0
#Al inicio muestra la cantidad de tickets antes de agregar o eliminar y luego muestra la cantidad de tickets final luego de editar.
           if opc=="agregar":
               agre=int(input ("Ingrese la cantidad a agregar: "))
               pel2=pel2+agre
           elif opc=="eliminar":
               eli=agre=int(input ("Ingrese la cantidad a eliminar: "))
               pel2=pel2-eli
               if pel2<0:
                pel2=0 
           else:
               print("Opción elegida no es valida solo puede ser agregar o eliminar")
           print ("La nueva cantidad de tickets para ",pel," función en este momento es ",pel2)
           print("")
           pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")

#Si la pelicula es Ted sera la variable pel3   
        elif pel=="Ted":
           print ("La cantidad de tickets para ",pel," función en este momento es ",pel3)
           opc=input("Desea agregar o eliminar tickets(Ingresa 'agregar'  o 'eliminar' tickets): ")
#Se pueden agregar o eliminar tickets
#Si se eliminan mas tickets y hay numero de tickers negativo entonces tickets sera igual 0
#Al inicio muestra la cantidad de tickets antes de agregar o eliminar y luego muestra la cantidad de tickets final luego de editar.
           if opc=="agregar":
               agre=int(input ("Ingrese la cantidad a agregar: "))
               pel3=pel3+agre
           elif opc=="eliminar":
               eli=agre=int(input ("Ingrese la cantidad a eliminar: "))
               pel3=pel3-eli
               if pel3<0:
                pel3=0 
           else:
               print("Opción elegida no es valida solo puede ser agregar o eliminar")
           print ("La nueva cantidad de tickets para ",pel," función en este momento es ",pel3)
           print("")
           pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")

#Si ingresa funciones mostrara las funciones de nuevo
        elif pel=="Funciones":
            print("-------------------------------------------------------------------")
            print("Las opciones de película son las siguientes:")
            print ("Funcion1 : Toy Story")
            print ("Funcion2 : 50 Sombras de Grey")
            print ("Funcion3 : Ted")
            print("-------------------------------------------------------------------")
            print ("El precio de todos los tickets es Q.30.00")
            pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")
#Cualquier otro valor sera erroneo y pedire que ingrese un valor correcto de nuevo.
        else:
              print("El valor ingresado es erroneo. Solo puede ser Toy Story, 50 Sombras de Grey, Ted, o fin")
              print("")
              pel=input("Ingrese su opción de pelicula para agregar o eliminar tickets, Fin para terminar o Funciones para ver funciones: ")

#Finalmente mostramos los resultados
print("------------------------------------------------------")
print("                     CINE UVG                         ")
print("------------------------------------------------------")
print("                     FACTURA                          ")
print("------------------------------------------------------")
#Declaramos las variables de totales por pelicula y el total de todas las peliculas
fun1=float(pel1*tic)
fun2=float(pel2*tic)
fun3=float(pel3*tic)
total=fun1+fun2+fun3
#Imprimimos cantidad por funcion y precio por funcion
#Luego el total a pagar
print("CANTIDAD    FUNCION           PRECIO UNITARIO   TOTAL")
print(str(pel1)+"           Toy Story"+ "              Q30.00"+ "      Q.",fun1)
print(str(pel2)+"           50 Sombras de Grey"+ "     Q30.00"+ "      Q.",fun2)
print(str(pel3)+"           Ted"+ "                    Q30.00"+ "      Q.",fun3)
print("------------------------------------------------------")
print("TOTAL                                         Q.", total)

           
