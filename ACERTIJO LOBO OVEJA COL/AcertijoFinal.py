#Universidad del Valle de Guatemala
#Silvio Orozco Vizquerra 18282
#23/02/2018
#Programa Acertijo Logico  Evaluacion
#1.Declaramos variables
mini=0
maxi=0
mov=0
ladoinicial=1
ladofinal=2
hombre=ladoinicial
lobo=ladoinicial
cabra=ladoinicial
col=ladoinicial
perdio= False
revisar= True
#2.Mostramos instruciones
print("Acertijo Lobo, Cabra y Col.")
print("Usted necesita llevar el lobo, la cabra y el col al otro lado del rio.")
print("-No puede dejar solos a la cabra y el col.")
print("-No puede dejar solos al lobo y a la cabra.")
print("-Necesita llevar los 3 objetos al otro lado del río.")
print("-Tiene cantidad de movimientos ilimitados.")
print("-Solo puede llevar un animal consigo en la balsa.")
print("-Puede desear no mover ningún animal; y regresar solo; siempre y cuando se cumplan los primeras 2 condiciones.")
print("-Al escoger mover un animal lo dejará del otro lado.")
print("-No puede realizar el acertijo en mas movimientos de lo deseado o menos movimientos de los deseados.")
#3. Pedimos que ingrese la cantidad minima y maxima de movimientos.
print ("Inicio de juego")
print("Los valores de maximo y minimo deben ser mayores a 0 y maximo debe ser mayor a mini.")
mini=int(input("Ingrese el minimo de movimientos: "))
maxi=int(input("Ingrese el maximo de movimientos: "))
while maxi<=0 or mini<0 or mini>maxi:
      print("Se necesita que los valores de maximo y minimo deben ser mayores a 0 y maximo debe ser mayor a mini.")
      mini=int(input("Ingrese el minimo de movimientos: "))
      maxi=int(input("Ingrese el maximo de movimientos: "))
#Se muestra como se encuentran los animales al inicio del juego.
print("")
print("Lado Inicial                                Lado Final")
print("Hombre                                                           ")
print("Lobo                                                          ")
print("Cabra                                                           ")
print("Col                                                          ")
#4. Pedimos que ingrese que animal desea mover en la balsa con el hombre ('Lobo','Cabra', 'Col' o 'Ninguno')Si tiene alguna otra respuesta mostrara error.
mover=input("Ingrese animal a mover al lado final('Lobo','Cabra', 'Col' o 'Ninguno'): ")
#5. Mientras en ladofinal no esten nuestros 4 objetos(Hombre, lobo, cabra y col; se pueden realizar movimientos)                  
while not(hombre==ladofinal and cabra==ladofinal and lobo==ladofinal and col==ladofinal):
  mov=mov+1
  #Mientras que se ingrese algo a mover se debe revisar si el movimiento sera hacia al lado final del rio o el lado inicial segun si el movimiento es par o impar
  while revisar== True:
   if mov%2==1:
     #Dentro de esto se revisar si es igual a lobo,cabra,col o ninguno, de lo contrario muestra error.
     if mover=="Lobo":
        #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if lobo==ladoinicial:
         lobo=ladofinal
         hombre=ladofinal
         revisar=False
        else:
          print("")
          print("El lobo se encuentra del otro lado. Su movimiento no conto.")
          mover=input(("Ingrese animal a mover al lado final del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta
     elif mover=="Cabra":
        #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if cabra==ladoinicial:
         cabra=ladofinal
         hombre=ladofinal
         revisar=False
        else:
          print("")
          print("La cabra se encuentra del otro lado. Su movimiento no conto.")
          mover=input(("Ingrese animal a mover al lado final del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta
     elif mover=="Col":
        #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if col==ladoinicial:
         col=ladofinal
         hombre=ladofinal
         revisar=False
        else:
          print("")
          print("El col se encuentra del otro lado.Su movimiento no conto")
          mover=input(("Ingrese animal a mover al lado final del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta
     elif mover=="Ninguno":
         #Si es ninguno solo se mueve el hombre
         hombre=ladofinal
         revisar=False
     else :
           #Mensaje de error
         print("Error objeto no encontrado ('Lobo','Cabra', 'Col' o 'Ninguno')")
         mover=input(("Ingrese animal a mover al lado final del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))   
   elif mov%2==0:
      #Dentro de esto se revisar si es igual a lobo,cabra,col o ninguno, de lo contrario muestra error.
     if mover=="Lobo":
      #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if lobo==ladofinal:
          lobo=ladoinicial
          hombre=ladoinicial
          revisar=False
        else:
          print("")
          print("El lobo se encuentra del otro lado. Su movimiento no conto.")
          mover=input(("Ingrese animal a mover al lado inicial del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta

     elif mover=="Cabra":
      #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if cabra==ladofinal:
          cabra=ladoinicial
          hombre=ladoinicial
          revisar=False
        else:
          print("")
          print("La cabra se encuentra del otro lado. Su movimiento no conto")
          mover=input(("Ingrese animal a mover al lado inicial del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta
     elif mover=="Col":
      #Verifica si el objeto se encuentra del lado que estamos para moverlo, de lo contrario lo indica y el mov no cuenta, pregunta de nuevo que desea mover
        if col==ladofinal:
          col=ladoinicial
          hombre=ladoinicial
          revisar=False
        else:
          print("")
          print("El col se encuentra del otro lado. Su movimiento no conto")
          mover=input(("Ingrese animal a mover al lado inicial del rio ('Lobo','Cabra', 'Col' o 'Ninguno'): "))
          #Esto porque el movimiento no cuenta

     elif mover=="Ninguno":
           #Si no mueve ninguno, solo se mueve el hombre.
          hombre=ladoinicial
          revisar=False
     else :
           #Mensaje de error
         print("Error objeto no encontrado('Lobo','Cabra', 'Col' o 'Ninguno')")
         mover=input(("Ingrese animal a mover al lado inicial del rio ('Lobo','Cabra', 'Col' o 'Ninguno': "))
#Si el lobo se encuentro solo con la cabra o la cabra solo con el col o solos los 3 objetos sin el hombre, se pierde. Tambien si se excede el maximo de movimientos
  if (lobo==ladoinicial and cabra==ladoinicial and hombre==ladofinal and col==ladoinicial) or (lobo==ladofinal and cabra==ladofinal and hombre==ladoinicial) or  (lobo==ladoinicial and cabra==ladoinicial and hombre==ladofinal)or  (col==ladoinicial and cabra==ladoinicial and hombre==ladofinal) or   (col==ladofinal and cabra==ladofinal and hombre==ladoinicial) or mov>=maxi :
        if (lobo==ladofinal and cabra==ladofinal and hombre==ladoinicial) or (lobo==ladoinicial and cabra==ladoinicial and hombre==ladofinal):
          perdio=True
          print("")
          print("Usted ha perdido. Ha dejado solos al lobo y a la cabra,y se lo ha comido")
        elif (col==ladoinicial and cabra==ladoinicial and hombre==ladofinal) or   (col==ladofinal and cabra==ladofinal and hombre==ladoinicial) :
          perdio=True
          print("")
          print("Usted ha perdido. Ha dejado solos a la cabra y al lobo, y se lo ha comido")
        elif (lobo==ladoinicial and cabra==ladoinicial and hombre==ladofinal and col==ladoinicial):
          perdio=True
          print("")
          print("Usted ha perdido. Ha dejado solos al col, la cabra y al lobo. Se han comido")            
        elif mov>maxi:
          perdio=True
          print("")
          print("Usted ha perdido. Ha excedido la cantidad de movimientos")
        else:
            print("")
 #Imprime como se ven los objetos, si son igual a lado inicial, los colocamos del lado inicial, de lo contrario los movemos al lado final
  print("Lado Inicial                                Lado Final")
  if hombre==ladoinicial:
     print("  Hombre                                     ")
  else:
     print("                                               Hombre                                 ")
  if lobo==ladoinicial:
     print("  Lobo                                     ")
  else:
     print("                                               Lobo                                    ")
  if cabra==ladoinicial:
     print("  Cabra                                    ")
  else:
     print("                                               Cabra                                    ")
  if col==ladoinicial:
     print("  Col                                     ")
  else:
     print("                                               Col                                   ")
  #Si pierde se reinicia el juego
  if perdio== True:
         mini=-1
         maxi=-1
         mov=0
         hombre=ladoinicial
         lobo=ladoinicial
         cabra=ladoinicial
         col=ladoinicial
         while maxi<=0 or mini<0 or mini>maxi:
           print("Reinicio de juego")
           print("Los valores de maximo y minimo deben ser mayores a 0 y maximo debe ser mayor a mini.")
           mini=int(input("Ingrese el minimo de movimientos: "))
           maxi=int(input("Ingrese el maximo de movimientos: "))
           print("")
           print("Lado Inicial                                Lado Final")
           print("Hombre                                                           ")
           print("Lobo                                                          ")
           print("Cabra                                                           ")
           print("Col                                                          ")

           perdio= False 
  else:
      print("")
  #Se imprime el numero de movimiento
  if mov>0:
    print("Movimiento" ,mov)
    print("")
  #Se pide que siga moviendo animales siempre y cuando no se haya cumplido nuestro objetivo
  if mov%2==1 and not(hombre==ladofinal and cabra==ladofinal and lobo==ladofinal and col==ladofinal):
       mover=input(("Ingrese animal a mover al lado inicial del rio ('Lobo','Cabra', 'Col' o 'Ninguno':"))
       revisar=True
  elif mov%2==0and not(hombre==ladofinal and cabra==ladofinal and lobo==ladofinal and col==ladofinal):
       mover=input(("Ingrese animal a mover al lado final del rio('Lobo','Cabra', 'Col' o 'Ninguno':"))
       revisar=True
  else:
       revisar=False
#Si se gana hay que verificar que haya tenido el minimo de movimientos, de lo contrario pierde       
if mov>=mini:
 print("Su cantidad de movimientos final fue: ",mov)
 print("Su cantidad minima de movimientos era: ",mini)
 print("Su cantidad maxima de movimientos era: ",maxi)
 print("Felicidades.Usted ha completado el acertijo:).")
else:
 print("Su cantidad de movimientos final fue: ",mov)
 print("Su cantidad minima de movimientos era: ",mini)
 print("Su cantidad maxima de movimientos era: ",maxi)
 print("Usted perdio ya que su cantidad de movimientos no fue la minima indicada al principio")

input("")
          
  
