#Universidad del Valle de Guatemala
#Silvio Orozco Vizquerra 18282
#13/04/2018
#modulososcars.py

#Funcion del menu para tener una opcion de lo que desea hacer.
def menu():
    opcion = input("""
---------------------------------------------
                   OSCARS
---------------------------------------------

1.   Agregar nueva categoría de premios.
2.   Agregar nominado a una categoría.
3.   Eliminar nominado.
4.   Eliminar categoria.
5.   Listar todos los nominados de una categoria.
6.   Imprimir todas las categorias y sus nominados.
7.   Salir.

---------------------------------------------
Su opcion es : 
""")
    return opcion

#Verificar si la opcion ingresada es numero y esta en el rango de opciones.
def verificaropcion(opcion):
    if opcion.isnumeric()==True:
        opcion=int(opcion)
        if (opcion in range(1,8))==False:
            print("Su opcion ingresada no esta en el rango de opciones")
            opcion=menu()
            opcion=verificaropcion(opcion)
        else:
            opcion=opcion
    else:
        print("Su opcion ingresada no es un numero")
        opcion=menu()
        opcion=verificaropcion(opcion)
    return opcion


    
#Agregar una categoria
def agregarcategoria(oscars):
    cnueva=input("Ingrese el nombre de la categoria que desea agregar: ")
    cnueva=cnueva.upper()
    existe=existecategoria(cnueva,oscars)
    #Verificar si la categoria existe.
    if (existe==True):
            print("La categoria ingresada ya existe.")
            oscars=agregarcategoria(oscars)
    else:
       print("Usted ha agregado la categoria ", cnueva, ". Si desea agregar nominados, puede hacerlo en la opcion 2.")    
       oscars[cnueva]=[]
    return oscars

#Agregar un nominado
def agregarnominado(oscars):
    if (oscars=={})==True:
        print("No se puede agregar nominados ya que no hay ninguna categoria.")
        oscars=oscars
    else:
      categoria=input("Ingrese el nombre de la categoria a las cual desea agregar un nominado: ")
      categoria=categoria.upper()
      existe=existecategoria(categoria,oscars)
      #Verificar si categoria existe
      if (existe==False):
            print("La categoria ingresada no existe.")
            oscars=agregarnominado(oscars)
      else:
        nominadon=input("Ingrese el nombre del nominado a agregar: ")
        nominadon=nominadon.upper()
        #Verificar si nominado existe
        while (nominadon in oscars[categoria])==True :
           print("El nominado ya existe.")
           nominadon=input("Ingrese el nombre de un nominado nuevo a agregar: ")
           nominadon=nominadon.upper()
        print("Usted ha agregado el nominado ", nominadon, " a la categoria ", categoria)
        oscars[categoria].append(nominadon)
    return oscars

#Eliminar un nominado
def eliminarnominado(oscars):
    if (oscars=={})==True:
        print("No se puede eliminar nominados ya que no hay ninguna categoria.")
        oscars=oscars
    else:
     categoria=input("Ingrese el nombre de la categoria a las cual desea eliminar un nominado: ")
     categoria=categoria.upper()
     existe=existecategoria(categoria,oscars)
     #Verificar si categoria existe
     if (existe==False):
            print("La categoria ingresada no existe.")
            oscars=eliminarnominado(oscars)
     else:
        if (oscars[categoria]==[])==True:
            print("La categoria esta vacia. No se puede  eliminar.")
            oscars=eliminarnominado(oscars)
        else:
            nominadoe=input("Ingrese el nombre del nominado que desea eliminar: ")
            nominadoe=nominadoe.upper()
            
            #Verificar si nominado existe
            while (nominadoe in oscars[categoria])==False:
                print("El nominado no existe denrtro de la categoria para ser eliminado.")
                nominadoe=input("Ingrese el nombre de un nominado que desea eliminar: ")
                nominadoe=nominadoe.upper()
            print("Usted ha eliminado el nominado ", nominadoe, " a la categoria ", categoria)
            oscars[categoria].remove(nominadoe)
    return oscars

#Eliminar una categoria
def eliminarcategoria(oscars):
    if (oscars=={})==True:
        print("No se puede eliminar categorias ya que no hay ninguna categoria.")
        oscars=oscars
    else:
     celiminar=input("Ingrese el nombre de la categoria que desea eliminar: ")
     celiminar=celiminar.upper()
     existe=existecategoria(celiminar,oscars)
     #Verificar si la categoria existe.
     if (existe==False):
            print("La categoria ingresada no existe.")
            oscars=eliminarcategoria(oscars)
     else:
        print("Usted ha eliminado la categoria ", celiminar, ".")
        del oscars[celiminar]
    return oscars

#Ver una categoria
def vercategoria(oscars):
    if (oscars=={})==True:
        print("Aun no existe ninguna categoria. Estan vacias.")
        oscars=oscars
    else:
      categoria=input("Ingrese el nombre de la categoria que desea ver los nominados: ")
      categoria=categoria.upper()
      existe=existecategoria(categoria,oscars)
      #Verificar si categoria existe
      if (existe==False):
            print("La categoria ingresada no existe. Debe ser una opcion valida.")
            vercategoria(oscars)
      else:
           mostrarcategoria(categoria,oscars)

#Ver todas las categorias y nominados.
def vertodaslascategorias(oscars):
     if (oscars=={})==True:
           print("Aun no existe ninguna categoria. Estan vacias.")
           oscars=oscars
     else:
         for categoria in oscars:
             mostrarcategoria(categoria,oscars)
        
#Mostrar categoria
def mostrarcategoria(categoria,oscars):
    print("---------------------------------------------")
    print("CATEGORIA: " ,categoria)
    print("---------------------------------------------")
    print ("NOMINADOS: ")
    for nominado in  oscars[categoria]:
           print("-" ,nominado)
    print("---------------------------------------------")
    print("")
    

#Ver si la categoria existe.
def existecategoria(categoria, oscars):
    if (categoria in oscars)==True:
        existe=True
    else:
        existe=False
    return existe
    
