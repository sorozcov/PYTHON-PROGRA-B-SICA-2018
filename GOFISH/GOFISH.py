#UVG
#Silvio Orozco Vizquerra
#Carne 18282
#Fecha 24/03/2018
#GOFISHPRINCIPAL

from modulosGOFISH import*
import os
juegosjugador1=0
juegosjugador2=0
#Da bienvenida a go fish y se inician variables de juegos ganados por jugador
print("------------------------------------------------------------")
print("|               BIENVENIDO A GO FISH                       |")
print("------------------------------------------------------------")
#Pregunta si desea jugar o salir.
desea=jugarreglasosalir()
#Mientras no pida salir:
while desea!="SALIR":
    #Si desea jugar, iniciara un juego
    if desea=="JUGAR":
        #Se reparten cartas y se inician variables de puntos
        cartas=cartasd()
        paquete=paqueted(cartas)
        jugador1=jugadord(paquete)
        jugador2=jugadord(paquete)
        puntosjugador1=0
        puntosjugador2=0
        turno=1
        #Se inicia con turnos, si es turno impar turno de 1 y si es par turno de 2
        #Mientras no se acaben las cartas dentro del juego, es decir se consigan 13 puntos, se continuara jugando.
        while  (puntosjugador1+puntosjugador2)!=13 :
         #Turno jugador 1
         while turno%2==1 and (puntosjugador1+puntosjugador2)!=13 :
            os.system('cls')
            #Se muestra marcador y de quien es turno.
            marcador(puntosjugador1,puntosjugador2)
            print("|Turno del jugador    : 1  |")
            #Se ordenan las cartas
            jugador1.sort()
            jugador2.sort()
            #Se muestran las cartas del jugador y se generan las opciones posibles
            cartasdeljugador(jugador1)
            opciones1=opciones(jugador1)
            opciones2=opciones(jugador2)
            #Se verifica respuesta
            puntosjugador1=verificar(cartas,opciones1,opciones2,jugador1,jugador2,puntosjugador1,paquete)
            if (paquete==[])==False:
                #Cada vez que termina su turno, va a pescar agregando una carta, siempre y cuando hayan cartas
                jugador1.append(cartarandom(paquete))
            else:
                print("El paquete esta vacio. Debe jugar con sus mismas cartas")
            input("")
            #Muesta las nuevas cartas
            print("Sus nuevas cartas son  ")
            cartasdeljugador(jugador1)
            print("Cambiara su turno")
            input("")
            #Muestra cantidad de cartas en el juego
            cartaseneljuego(paquete,jugador1,jugador2)
            input("")
            int(puntosjugador1)
            int(puntosjugador2)
            #Se cambia de turno
            turno=turno+1
         #Turno jugador 2           
         while turno%2==0 and (puntosjugador1+puntosjugador2)!=13:
            os.system('cls')
            #Se muestra marcador y de quien es turno.
            marcador(puntosjugador1,puntosjugador2)
            print("|Turno del jugador    : 2 |")
            #Se ordenan las cartas
            jugador1.sort()
            jugador2.sort()
            #Se muestran las cartas del jugador y se generan las opciones posibles
            cartasdeljugador(jugador2)
            opciones1=opciones(jugador1)
            opciones2=opciones(jugador2)
            #Se verifica la respuesta
            puntosjugador2=verificar(cartas,opciones2,opciones1,jugador2,jugador1,puntosjugador2,paquete)
            if (paquete==[])==False:
                #Cada vez que termina su turno, va a pescar agregando una carta, siempre y cuando hayan cartas
                jugador2.append(cartarandom(paquete))
            else:
                print("El paquete esta vacio. Debe jugar con sus mismas cartas")
            input("")
            #Muestra las nuevas cartas
            print("Sus nuevas cartas son  ")
            cartasdeljugador(jugador2)
            print("Cambiara su turno")
            input("")
            cartaseneljuego(paquete,jugador1,jugador2)
            input("")
            int(puntosjugador1)
            int(puntosjugador2)
            #Se cambia de turno
            turno=turno+1
       #Al final muestra quien gana el juego, segun quien tenga mas puntos.
        if puntosjugador1>puntosjugador2:
            marcador(puntosjugador1,puntosjugador2)
            print("El jugador 1 ha ganado este juego")
            juegosjugador1=juegosjugador1+1
        else:
            marcador(puntosjugador1,puntosjugador2)
            print("El jugador 2 ha ganado este juego")
            juegosjugador2=juegosjugador2+1
        input("")
        #Reseteamos variables para el siguiente juego.
        cartas= None
        paquete= None
        jugador1= None
        jugador2= None
        os.system('cls')
        #Se pregunta si desea jugar o salir
        desea=jugarreglasosalir()
    #Muestra reglas en menu centinela
    elif desea=="REGLAS":
        os.system('cls')
        reglas()
        desea=jugarreglasosalir()
    #Muestra marcador en menu centinela
    elif desea=="MARCADOR":
        os.system('cls')
        marcador(juegosjugador1,juegosjugador2)
        desea=jugarreglasosalir()
    else:
        #Muestra si lo ingresado no es opcion valida
        print("Ha ingresado una opcion no valida")
        desea=jugarreglasosalir()
os.system('cls')
#Al salir, muestra el marcado finales de juegos.
print("El juego ha terminado")
marcador(juegosjugador1,juegosjugador2)
input("")  
