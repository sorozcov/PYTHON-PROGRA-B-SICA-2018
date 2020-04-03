#UVG
#Silvio Orozco Vizquerra
#Carne 18282
#Fecha 16/03/2018
#Archivo sistemaUVG.py

print("**********************************************")
print("            SISTEMA BIBLIOTECA UVG")
print("**********************************************")
print("                REGISTRO ACTUAL       ")
separacion=("******************************************\n")
tab=("ISBN             LIBRO             EJEMP.\n")
print(separacion+tab+separacion)
print("Este es el sistema de bibioteca de la UVG.")
decision=input("Desea input un libro o desea salir. (libro o salir): ")
decision=decision.upper()
x=-1
librof=[]
isbnf=[]
nombref=[]
ejemf=[]
while decision!="SALIR":
    x=x+1 
    if decision!="LIBRO":
        print("La opcion ingresada no fue valida")
        decision=input("Desea ingresar un libro o desea salir. (libro o salir): ")
        decision=decision.upper()
        x=x-1
    else:
        isbn=input("Ingrese el ISBN del libro (Comienza con ISBN:): ")
        isbnf.insert(x,isbn.upper())
        while isbnf[x][0:5]!="ISBN:":
            print("El ISBN, debe comenzar con 'ISBN:'")
            isbn=input("Ingrese el ISBN del libro (Comienza con ISBN:): ")
            isbnf.insert(x,isbn.upper())
        isbnf.insert(x,isbnf[x][5:])
        nombre=input("Ingrese el nombre del libro(Maximo de 10 caracteres): ")
        nombref.insert(x,nombre.upper())
        while len(nombref[x])>10:
            print("La longitud del libro debe ser maximo de 10 caracteres: ")
            nombre=input("Ingrese el nombre del libro(Maximo de 10 caracteres): ")
            nombref.insert(x,nombre.upper())
        ejem=input("Ingrese el numero de ejemplares del libro (Debe ser un entero mayor a 0.): ")
        ejemf.insert(x,ejem)
        while ejemf[x].isnumeric()==False:
                  print("El valor ingresado debe ser un numero entero mayor a 0((Usted no ingreso un numero)")
                  ejem=input("Ingrese el numero de ejemplares del libro (Debe ser un entero mayor a 0.): ")
                  ejemf.insert(x,ejem)     
        print("Se ha anadido un nuevo registro")
        print(separacion+tab+separacion)
        libro=(str(isbnf[x])+"           "+str(nombref[x])+"          "+str(ejemf[x])+"\n")
        librof.insert(x,libro)    
        for x in range(0,x+1):
            print(librof[x])
        print(separacion)
        decision=input("Desea ingresar un libro o desea salir. (libro o salir): ")
        decision=decision.upper()
arch = open("sistemauvg.txt" , "w")
print("Gracias por usar el programa de bibioteca UVG")
print(separacion)
print("                REGISTRO FINAL       \n")                                 
print(separacion)
arch.write("                REGISTRO FINAL       ")  
arch.write(separacion+tab+separacion)
for x in range(0,x+1):
    print(librof[x])
    arch.write(librof[x])
print(separacion)
arch.write(separacion)
arch.close()


