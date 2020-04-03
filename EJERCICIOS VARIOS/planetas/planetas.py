#Universidad del Valle de Guatemala
#Silvio Orozco Vizquerra 18282
#13/04/2018
#Planetas.py

#Importamos nuestro modulo
from modulosplaneta import *

#Declaramos nuestro diccionario de planetas.
planetas = {
    'MERCURIO': 'Recibió este nombre de los romanos por el mensajero de pies alados de los dioses, ya que parecía moverse más rápido que ningún otro planeta. ',
    'VENUS': 'Es el objeto más brillante del cielo, después del Sol y la Luna. A este planeta se le llama el lucero del alba cuando aparece por el Este al amanecer y el lucero de la tarde cuando está situado al Oeste al atardecer',
    'MARTE': 'Suele recibir el nombre de Planeta Rojo ya que contiene altas cantidades de óxido de hierro, conocido también como Hematita. ',
    'JUPITER': 'Jupiter es 1.400 veces más voluminoso que la Tierra, pero su masa es sólo 318 veces la de nuestro planeta, esto se debe que es un plantea prácticamente gaseoso.',
}
print(planetashas_key("MERCURIO",planetas))

#Llamamos al menu y verificamos opcion.
opcion=menu()
opcion=verificaropcion(opcion)
#Ya verificada, sabemos que es numero.
opcion=int(opcion)
#Ahora segun su opcion escogida. Realiza cierta accion.
#Mientras opcion no sea 4(salir ) se realizara el programa.





while opcion!=5:
    for p in planetas:
        planetas[p]=planetas[p].upper()
    #Ver los planetas que existen
    if opcion==1:
        print("")
        for p in planetas:
           print("---------------------------------------------")
           print ("PLANETA: " ,p)
           print("---------------------------------------------")
           print("DESCRIPCION: " ,planetas[p])
           print("---------------------------------------------")
           print("")
           
    #Ver una planeta especifico
    elif opcion==2:
        planetaabuscar=planetaaver()
        planetaabuscar=planetaabuscar.upper()
        while planetashas_key(planetaabuscar,planetas)==False:
            #Si el planeta no existe, pregunta de nuevo.
            print("El planeta no se encuentra en la base de datos")
            planetaabuscar=planetaaver()
            planetaabuscar=planetaabuscar.upper()
        if planetashas_key(planetaabuscar,planetas)==True:
            #Si el planeta esta, muestra sus datos.
           print("---------------------------------------------")
           print ("PLANETA: " ,planetaabuscar)
           print("---------------------------------------------")
           print("DESCRIPCION: " ,planetas[planetaabuscar])
           print("---------------------------------------------")
           print("")
            
    #Agregar un planeta    
    elif opcion==3:
        planetaagregar=agregarplaneta()
        planetaagregar=planetaagregar.upper()
        while planetashas_key(planetaagregar,planetas)==True:
            print("Este planeta ya se encuentra en el sistema. Ingrese otro planeta.")
            planetaagregar=agregarplaneta()
            planetaagregar=planetaagregar.upper()
        descripcion= agregardescripcion()
        decripcion=descripcion.upper()
        planetas[planetaagregar]=descripcion
        print("Usted ha agregado el planeta ", planetaagregar)
        print("")

    #Eliminar un planeta    
    elif opcion==4:
        planetaaeliminar=eliminarplaneta()
        planetaaeliminar=planetaaeliminar.upper()
        while planetashas_key(planetaaeliminar,planetas)==False:
            print("Este planeta no se encuentra en el sistema. Ingrese otro planeta.")
            planetaaeliminar=eliminarplaneta()
            planetaaeliminar=planetaaeliminar.upper()
        if planetashas_key(planetaaeliminar,planetas)==True:
            del planetas[planetaaeliminar]
        print("Usted ha elimnado el planeta ", planetaaeliminar)
        print("")
    #Se visualiza hasta que se presiona enter.
    input("")
    #Repetimos el ciclo
    opcion=menu()
    opcion=verificaropcion(opcion)
    opcion=int(opcion)
    print("")
#Termina el programa
print("Gracias por usar el programa.")
