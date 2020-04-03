#UVG
#Silvio Orozco Vizquerra
#Carne 18282
#Fecha 24/03/2018
#MODULOS
import random
import os

#Pregunta si deseamos jugar, ver el marcador, ver las reglas o salir.
def jugarreglasosalir():
    a=input("Desea comenzar un juego, ver las reglas, ver el marcador o salir. (JUGAR, REGLAS, MARCADOR O SALIR): ")
    a=a.upper()
    return a

#Muestra las reglas del juego
def reglas():
 print("-------------------------------------------------------------")
 print("|                        GO FISH                            |")
 print("-------------------------------------------------------------")
 print("------------------------------------------------------------")
 print("|                        REGLAS                             |")
 print("------------------------------------------------------------")
 print("|Las reglas del juego son:                                  |")
 print("|El objetivo es ganar la mayoría de “libros” de cartas      |")
 print("|Un “libro” es cualquier conjunto de cuatro iguales.        |")
 print("|Esto dara 1 punto al jugador. Quien tengas mas puntos gana.|")
 print("|Se reparten 7 cartas cara abajo a los jugadores.           |")
 print("|El resto de cartas formará la pila para agarrar cartas     |")
 print("|En tu turno, debes preguntar si tu oponente tiene una carta|")
 print("|Solo puedes preguntar por cartas que tienes en tu baraja.  |")
 print("|Si la tiene puedes seguir preguntando                      |")
 print("|Pierdes el turno si tu oponente no tiene esa carta.        |")
 print("|Cuando pierdes el turno, debes agarrar una carta.          |")
 print("------------------------------------------------------------")
 
#Cartas que existen
def cartasd():
    cartas=["A" , 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return cartas

#Opciones de carta para evaluar
def opcion(cartas):
    opc=[]
    for c in cartas:
        d=str(c)
        if c!=10:
           d=d+" "
        opc.append(d)
    return opc

#Para realizar 1 palo de las cartas
def palo13cartas(cartas,palo):
    palos=[]
    for carta in cartas:
        p=(str(carta)+" "+str(palo))
        palos.append(p)
    return palos
        
#Muestra todas las cartas de 1 paquete.
def paqueted(cartas):
    palo1=palo13cartas(cartas,"CORAZON")
    palo2=palo13cartas(cartas,"TREBOL")
    palo3=palo13cartas(cartas,"DIAMANTE")
    palo4=palo13cartas(cartas,"ESPADA")
    paquete=palo1+palo2+palo3+palo4
    return paquete

#Conseguir 1 carta random del paquete/pila.    
def cartarandom(paquete):
    carta=random.choice(paquete)
    paquete.remove(carta)
    return carta

#Brinda las cartas iniciales para cada jugador
def jugadord(paquete):
    jugador=[]
    for x in range(0,7):
        carta=cartarandom(paquete)
        jugador.append(carta)
    return jugador

#Muestra cartas del jugador
def cartasdeljugador(jugador):
    for carta in jugador:
        print (carta)

#Muestra las opciones del jugador
def opciones(jugador):
    opciones=[]
    for x in jugador:
        a=x[:2]
        opciones.append((a))
    return opciones

#Pregunta sobre carta a su oponente        
def pregunta(opciones):
    print("Sus opciones son:")
    print(opciones)
    preg=input("De sus opciones en sus cartas, ¿Cual numero de carta desea preguntar a su oponente?: ")
    if preg!="10":
        preg=preg+str(" ")
    return preg

#Verifica si 1 libro, para obtener 1 punto, al principio del turno y despues de cambio de cartas
def punto(opciones,jugador,puntosjugador):
    jugador.sort()
    for o in opciones:
        a=opciones.count(o)
        if a==4:
            puntosjugador=int(puntosjugador)+1
            print("----------------------------------------")
            print("|Ha ganado 1 punto con la carta "+str(o)+" |")
            print("----------------------------------------")
            b=opciones.index(o)
            for i in range(1,5):
                jugador.remove(jugador[b])
                opciones.remove(o)
    return(puntosjugador)

#Hace todas las verificaciones necesarias para que la pregunta del jugador sea valida y genere o no puntos.
def verificar(cartas,opcionesj,opcioneso,jugadorj,jugadoro,puntosjugador,paquete):
    puntosjugador=punto(opcionesj,jugadorj,puntosjugador)
    if(jugadorj==[])==True and (paquete==[])==True:
       print("No tiene cartas para preguntar. Cambio de turno.")
    else:
        if(jugadorj==[])==True and (paquete==[])==False:
               jugadorj.append(cartarandom(paquete))
               opcionesj=opciones(jugadorj)
               res=pregunta(opcionesj) 
        elif(jugadorj==[])==False:
               res=pregunta(opcionesj)
        opc=opcion(cartas)
        if(res in opcionesj)==False and (res in opc)==True:
           print("Su carta ingresada no esta en su baraja")
           puntosjugador=verificar(cartas,opcionesj,opcioneso,jugadorj,jugadoro,puntosjugador,paquete)
        elif (res in opcionesj)==True and (res in opcioneso)==False:
           os.system('cls')
           print("Su oponente no tiene la carta. A pescar.")
        elif(res in opcionesj)==True and (res in opcioneso)==True:
                     b=opcioneso.count(res)
                     c=opcioneso.index(res)
                     for i in range(1,b+1):
                             jugadorj.append(jugadoro[c])
                             jugadoro.remove(jugadoro[c])
                     os.system('cls')
                     print("Sus oponente tiene la carta. Sigue su turno.  ")
                     print("Sus nuevas cartas son  ")
                     jugadorj.sort()
                     cartasdeljugador(jugadorj)
                     opcionesj=opciones(jugadorj)
                     opcioneso=opciones(jugadoro)
                     puntosjugador=punto(opcionesj,jugadorj,puntosjugador)
                     puntosjugador=verificar(cartas,opcionesj,opcioneso,jugadorj,jugadoro,puntosjugador,paquete)
        else: 
          print("Su opcion ingresada no es una carta")
          puntosjugador=verificar(cartas,opcionesj,opcioneso,jugadorj,jugadoro,puntosjugador,paquete)
    return puntosjugador

    

#Muestra el marcador
def marcador(juegosjugador1,juegosjugador2):
 print("----------------------------------------")
 print("|              GO FISH                  |")
 print("----------------------------------------")
 print("|              MARCADOR                 |")
 print("----------------------------------------")
 print("|   JUGADOR 1             JUGADOR 2     |")
 print("----------------------------------------")
 print("|       "+str(juegosjugador1)+"                     "+str(juegosjugador2)+"         |")
 print("----------------------------------------")

#Muestra las cartas que estan en juego. Se eliminan 4 por cada libro.
def cartaseneljuego(paquete,jugador1,jugador2):
    print("La pila tiene " +str(len(paquete))+" cartas restantes.")
    print("El jugador 1 tiene " +str(len(jugador1))+" cartas.")
    print("El jugador 2 tiene " +str(len(jugador2))+" cartas.")


                    
                    
                


