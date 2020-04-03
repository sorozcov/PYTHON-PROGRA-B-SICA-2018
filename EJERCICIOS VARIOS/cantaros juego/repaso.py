#UVG SILVIO OROZCO
#ALGORITMO NARRATIVO CANTAROS
#Se dan instrucciones
#Mostrar Instrucciones
#INSTRUCCIONES Usted necesita tener 4 litros en el cantaro de 5 litros. Para ello tiene 8 litros de leche en un cantaro de leche, un cantaro vacio de 5 litros y un cantaro vacio de 3 litros.
print("INSTRUCCIONES Usted necesita tener 4 litros en el cantaro de 5 litros. Para ello tiene 8 litros de leche en un cantaro de leche, un cantaro vacio de 5 litros y un cantaro vacio de 3 litros.")
#Se declaran variables.
cantaro8=8
cantaro5=5
cantaro3=3
c8actual=8
c5actual=0
c3actual=0
transf=0
cantaroOrigen=0
cantaroDestino=0
pasos=0
#Se pide el ingreso de cantaroOrigen y cantaroFinal.
#Mientras cantaro 5 no contenga 4 litros el programa se continuara ejecutando
#Se pide el ingreso del cantaro de origen y el cantaro de destino
print("------")
print("|    |   ----")
print("|    |   |  |   --- ")
print("|  8 |   |5 |   | | ")
print("|    |   |  |   |3| ")
print("|    |   |  |   | | ")
print("------   ----   ---")
print("Cantaro 8=",c8actual,"/8")
print("Cantaro 5=",c5actual,"/5")
print("Cantaro 3=",c3actual,"/3")
cantaroOrigen=int(input("Ingrese el cantaro de origen: "))
cantaroDestino=int(input("Ingrese el cantaro final: "))
while c5actual!=4:
    #Se hacen las verificaciones correspondientes en el cual el cantaro de origen tiene por lo menos 1 litro de leche y el cantaro de destino aun no tiene el limite de su capacidad
    #Por tanto se crea un ciclo if para cada cantaro de origen
    if cantaroOrigen==8:     
        if c8actual>0:
            if cantaroDestino==8:
               print("El cantaro de origen no puede ser el mismo que el cantaro destino.")
            elif cantaroDestino==5:
                    transf=5-c5actual
                    if c5actual<5:
                     if transf<c8actual:
                        c5actual=c5actual+transf
                        c8actual=c8actual-transf
                     elif transf>=c8actual:
                        transf=c8actual
                        c8actual=0
                        c5actual=c5actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")    
            elif cantaroDestino==3:
                    transf=3-c3actual
                    if c3actual<3:
                     if transf<c8actual:
                        c3actual=c3actual+transf
                        c8actual=c8actual-transf
                     elif transf>=c8actual:
                        transf=c8actual
                        c8actual=0
                        c3actual=c3actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")
                    
        else:
            print("El cantaro de origen esta vacio, y debe contener leche para ser traspada")
            
    if cantaroOrigen==5:
        if c5actual>0:
            if cantaroDestino==5:
               print("El cantaro de origen no puede ser el mismo que el cantaro destino.")
            elif cantaroDestino==8:
                    transf=8-c8actual
                    if c8actual<8:
                     if transf<c5actual:
                        c5actual=c5actual-transf
                        c8actual=c8actual+transf
                     elif transf>=c5actual:
                        transf=c5actual
                        c5actual=0
                        c8actual=c8actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")    
            elif cantaroDestino==3:
                    transf=3-c3actual
                    if c3actual<3:
                     if transf<c5actual:
                        c3actual=c3actual+transf
                        c5actual=c5actual-transf
                     elif transf>=c5actual:
                        transf=c5actual
                        c5actual=0
                        c3actual=c3actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")
                    
            else:
                print("El cantaro de origen esta vacio, y debe contener leche para ser traspada")
    if cantaroOrigen==3:
        if c3actual>0:
            if cantaroDestino==3:
               print("El cantaro de origen no puede ser el mismo que el cantaro destino.")
            elif cantaroDestino==8:
                    transf=8-c8actual
                    if c8actual<8:
                     if transf<c3actual:
                        c3actual=c3actual-transf
                        c8actual=c8actual+transf
                     elif transf>=c3actual:
                        transf=c3actual
                        c3actual=0
                        c8actual=c8actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")    
            elif cantaroDestino==5:
                    transf=5-c5actual
                    if c5actual<5:
                     if transf<c3actual:
                        c5actual=c5actual+transf
                        c3actual=c3actual-transf
                     elif transf>=c3actual:
                        transf=c3actual
                        c3actual=0
                        c5actual=c5actual+transf
                    else:
                        print("El cantaro de destino esta lleno y este no puede estar lleno.")
        else:
            print("El cantaro de origen esta vacio, y debe contener leche para ser traspada")
    elif (cantaroOrigen!=3 and cantaroOrigen!=5 and cantaroOrigen!=8) or  (cantaroDestino!=3 and cantaroDestino!=5 and cantaroDestino!=8) :
        print("Solo existen 3  valores posibles de cantaro '8','5'y '3'")
    #Muestra los traspasos generados y pide de nuevo un cantaro de origen y un cantaro final
    print("------")
    print("|    |   ----")
    print("|    |   |  |   --- ")
    print("| 8  |   |5 |   | | ")
    print("|    |   |  |   |3| ")
    print("|    |   |  |   | | ")
    print("------   ----   ---")
    print("Cantaro 8=",c8actual,"/8")
    print("Cantaro 5=",c5actual,"/5")
    print("Cantaro 3=",c3actual,"/3")
    if c5actual!=4:
     cantaroOrigen=int(input("Ingrese el cantaro de origen: "))
     cantaroDestino=int(input("Ingrese el cantaro final: "))
#Si el cantaro final logra lo estipulado, muestra un mensaje que dice que ha logrado el objetivo    
print("Felicidades Usted ha logrado su objetivo")
print("")
print("     --------")
print("     | O  O |")
print("     |  D   |")
print("     --------")
input("")


