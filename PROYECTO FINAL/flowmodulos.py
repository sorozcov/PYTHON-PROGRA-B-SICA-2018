#Universidad del Valle de Guatemala
#Silvio Orozco 18282
#Pablo Ruiz 18259
#Pablo Valenzuela 18057
#Julio Padilla  18461
#Marco Trujillo 18069

#Flow
#Prototipo Programado Final
#En este prototipo las funciones se encuentran del mismo programa, por cuestiones de facilidad.


#Importamos tkinter
#Y las demas librerias que se utilizan en el programa
import tkinter as tk
from tkinter import messagebox
import pymongo

import progreso
from tkinter import ttk
import time
import calendar as cal
import datetime as date



global t
t="1280x680"


#Nos conectamos a la base de datos
conexion= pymongo.MongoClient()
#Buscamos la db que queremos.
db = conexion['flow']
#Seleccionamos la coleccion
coleccionusuarios= db.pi
colcarreras= db.carreras
colpromedio= db.promedio
colhor= db.horario

#FuncionesEnterparaquefuncionecomoboton
def onEnterEH(event):
    editadohorario()
def onEnterEN(event):
    editado()
def onEnterEstad(event):
    verestadi()
    
 #Funcion horario editado   
def editadohorario():
    if clasess.get()=='Escoger clase':
        messagebox.showwarning("Clase","Debe escoger una clase.",parent=editarhorario)
        #ARREGLAR IS NUMERIC PUES SOLO CUENTA ENTEROS, esto sera en el prototipo final
    elif hs.get()=='Escoger horario':
        messagebox.showwarning("Horario","Debe escoger un horario",parent=editarhorario)
    else:
        #Se actualiza la base de datos
        usuarioadentro['horario'][semet.get()][diah.get()][hs.get()]= clasess.get()
        coleccionusuarios.delete_one({'usuario':(usuarioadentro['usuario'])})
        bdn=({'usuario':(usuarioadentro['usuario']),'contra':(usuarioadentro['contra']),'nombre':(usuarioadentro['nombre']),'carrera':(usuarioadentro['carrera']),'calendario':(usuarioadentro['calendario']),'clases':(usuarioadentro['clases']),'promedios':(usuarioadentro['promedios']),'horario':(usuarioadentro['horario'])})
        coleccionusuarios.insert(bdn)
        messagebox.showinfo("Horario","Ha editado su horario",parent=editarhorario)
        verhorario()
        editarhorario.withdraw()
        horario.deiconify()
        
#Funcion para editar horario.        
def editarhorarios():
        if semet.get()=="Escoger semestre":
            messagebox.showwarning("Semestre","Debe escoger un semestre.",parent=horario)
        elif diah.get()=="Escoger dia":
            messagebox.showwarning("Dia","Debe escoger un dia para ver el horario.",parent=horario)
        else:
            horario.withdraw()
            global editarhorario
            editarhorario=tk.Tk()
            editarhorario.title('NOTAS')
            editarhorario.geometry(t)
            editarhorario.configure(bg='white')
            tituloflow(editarhorario)
            x=0.42
            a=0
            global case
            global clasess
            clasess = tk.StringVar(editarhorario)
            a=semet.get()
            clasess.set("Escoger clase") # default value
            f=['7:00-7:45','7:50-8:35','8:40-9:25','9:30-10:15','10:40-11:25','11:30-12:15', '12:20-13:05', '13:10-13:55', '14:00-14:45','14:50-15:35','15:40-16:25']
            case = tk.OptionMenu(editarhorario, clasess, *usuarioadentro['clases'][a])
            case.place(relx=0.35, rely=0.6, relwidth=0.35, relheight=0.15)
            cm= tk.Label(editarhorario,text="HORARIO:     ",bg='black',fg="white",font=30,justify='center')
            cm.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.15)
            global hs
            global hd
            hs = tk.StringVar(editarhorario)
            hs.set("Escoger horario") # default value
            hcs = tk.OptionMenu(editarhorario, hs, *(f))
            hcs.place(relx=0.35, rely=0.4, relwidth=0.35, relheight=0.15)
            hd= tk.Label(editarhorario,text="CLASE:     ",bg='black',fg="white",font=30,justify='center')
            hd.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.15)
            beditados= tk.Button(editarhorario,relief="raised", borderwidth=5 ,text="EDITAR", font=30, bg='dodger blue',command=editadohorario)
            beditados.place(relx=0.05, rely=0.8, relwidth=0.2, relheight=0.15)
            editarhorario.bind("<Return>",onEnterEH)
            #Termina funcion, luego de ingresar datos
#Funcion para ver el horario.
def verhorario():
    #DIA SE ESCOGE
    p= tk.Label(horario,bg='white',fg="black",font=30,justify='center')
    p.place(relx=0.31, rely=0.48, relwidth=0.69, relheight=0.5)
    if semet.get()=="Escoger semestre":
            messagebox.showwarning("Semestre","Debe escoger un semestre para ver el horario.",parent=horario)
    elif diah.get()=="Escoger dia":
            messagebox.showwarning("Dia","Debe escoger un dia para ver el horario.",parent=horario)
    else:
        dia=diah.get()
        d= tk.Label(horario,text=dia,bg='firebrick1',fg="black",font=30,justify='center')
        d.place(relx=0.3, rely=0.4, relwidth=0.6, relheight=0.07)
        hor=usuarioadentro['horario']
        x=0.48
        for uno in hor[semet.get()][dia]:
                if (hor[semet.get()][dia][uno]!=''):
                    h= tk.Label(horario,text=uno,bg='chocolate3',fg="black",font=30,justify='center')
                    h.place(relx=0.31, rely=x, relwidth=0.23, relheight=0.04)
                    c= tk.Label(horario,text=(hor[semet.get()][dia][uno]),bg='deep sky blue',fg="black",font=30,justify='center')
                    c.place(relx=0.55, rely=x, relwidth=0.34, relheight=0.04)
                    x=x+0.05

        ##    
        ##h= tk.Label(horario,text=hora,bg='khaki1',fg="black",font=30,justify='center')
        ##h.place(relx=0.02, rely=x, relwidth=0.08, relheight=0.05)
        ##x=x+0.07

            
        ##for hor in hola:
        ##    clase= tk.Label(horario,text=hor,bg='lawn green',fg="black",font=30,justify='center')
        ##    clase.place(relx=0.3, rely=x, relwidth=0.3, relheight=0.07)
        ##    nota= tk.Label(horario,text=(hola[hor]),bg='orange red',fg="black",font=30,justify='center')
        ##    nota.place(relx=0.65, rely=x, relwidth=0.1, relheight=0.07)
        ##    x=x+0.08



def regresarhorario():
    horario.withdraw()
    menuprincipal.deiconify()
    
#Esto llama a la ventana de horario.
def horarioo():
    menuprincipal.withdraw()
    global horario
    horario=tk.Tk()
    horario.title('HORARIO')
    horario.geometry(t)
    horario.configure(bg='white')
    tituloflow(horario)
    sem= tk.Label(horario,text="SEMESTRE:     ",bg='black',fg="white",font=30,justify='center')
    sem.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.07)
    dss= tk.Label(horario,text="DIA:     ",bg='black',fg="white",font=30,justify='center')
    dss.place(relx=0.05, rely=0.5, relwidth=0.2, relheight=0.07)
    global semer
    global semet
    semet = tk.StringVar(horario)
    #Escoge un semestre, ya bien para editar horarios o consultar horario
    semet.set("Escoger semestre") # default value
    semer = tk.OptionMenu(horario, semet, *(usuarioadentro['clases']))
    semer.place(relx=0.05, rely=0.4, relwidth=0.2, relheight=0.07)
    global diah
    global dh
    diah = tk.StringVar(horario)
    diaaa=['LUNES','MARTES','MIERCOLES','JUEVES','VIERNES']
    #Escoge un semestre, ya bien para editar notas o consultar notas
    diah.set("Escoger dia") # default value
    dian = tk.OptionMenu(horario, diah, *diaaa)
    dian.place(relx=0.05, rely=0.6, relwidth=0.2, relheight=0.07)
    bhor = tk.Button(horario,relief="raised", borderwidth=5 ,text="VER HORARIO", font=30, bg='dodger blue',command=verhorario) 
    bhor.place(relx=0.35, rely=0.3, relwidth=0.25, relheight=0.07)
    bedithor = tk.Button(horario,relief="raised", borderwidth=5 ,text="EDITAR HORARIO", font=30, bg='dodger blue', command=editarhorarios) 
    bedithor.place(relx=0.65, rely=0.3, relwidth=0.25, relheight=0.07)
    bregresarhor= tk.Button(horario,relief="raised", borderwidth=5 ,text="MENU PRINCIPAL", font=30, bg='dodger blue', command=regresarhorario)
    bregresarhor.place(relx=0.05, rely=0.85, relwidth=0.2, relheight=0.10)

#Funcion para saber si es numero o no
def esnota(valor):
    try:
      valor=float(valor)
      if valor>=0 and valor<=100:
          num=True
      else:
          num=False 
    except ValueError:
      num=False
    return num

#Funcion para regresar del menu principal dentro del usuario a notas.
def regresarmenunotas():
    notassss.withdraw()
    menuprincipal.deiconify()
    
#Funcion para mostrar el titulo en todas las pantallas de una manera predeterminada.
def tituloflow(app):
    titulodeaplicacion=tk.Label(app, text="FLOW", fg="blue", bg='dodger blue',font=("bold, 30"),justify='center')
    titulodeaplicacion.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)


#Regresar de ver estadistica a todas estadisticas
def regresarverestad():
    verestad.withdraw()
    estad.deiconify()

#Regresar de estadisticas a inicio
def regresarestad():
    estad.withdraw()
    inicio.deiconify()

#Comparar 2 carreras
def comparar():
        for x in colcarreras.find():
            carreras=x
        
        ciguales=0
        cdiferente=0
        c1=car1.get()
        c2=car2.get()
        cursosiguales=[]
        cursosdiferentesc1=[]
        cursosdiferentesc2=[]
        if car1.get()=='Escoger carrera' or car2.get()=='Escoger carrera':
            messagebox.showwarning("Carreras","Debe escoger carreras para comparar.",parent=verestad)
        elif car1.get()==car2.get():
            messagebox.showwarning("Carreras","Usted escogio la misma carrera, escoja carreras diferentes.",parent=verestad)
        else:
            c1=car1.get()
            c2=car2.get()
            for n in range (1,(len(carreras[c1])+1)):
                for h in range (1,(len(carreras[c2])+1)):
                    for clasecar1 in (carreras[c1][('Semestre '+str(n))]):
                        for clasecar2 in (carreras[c2][('Semestre '+str(h))]):
                            if clasecar1==clasecar2:
                                    cursosiguales.append(clasecar1)
                                    ciguales=ciguales+1
            f=0                            
            for h in range (1,(len(carreras[c1])+1)):
             for clasecar1 in (carreras[c1][('Semestre '+str(h))]):
                f=f+1
                if (clasecar1 in cursosiguales)==False:
                     cursosdiferentesc1.append(clasecar1)                         
            for h in range (1,(len(carreras[c2])+1)):
             for clasecar2 in (carreras[c2][('Semestre '+str(h))]):
                 f=f+1
                 if (clasecar2 in cursosiguales)==False:
                     cursosdiferentesc2.append(clasecar2)
            cdiferente=len(cursosdiferentesc1)+len(cursosdiferentesc2)-2
            iguales= tk.Label(verestad,text=(
        "CANTIDAD CURSOS IGUALES: "+str(ciguales)),bg='red',fg="white",font=55,justify='center')
            iguales.place(relx=0.2, rely=0.52, relwidth=0.6, relheight=0.05)
            #COMBO 1
            i=tk.StringVar(verestad)
            cigual= ttk.Combobox(verestad,textvariable=i,state="readonly",justify='center')
            cigual.place(relx=0.2, rely=0.58, relwidth=0.6, relheight=0.05)
            cigual['values']=cursosiguales
            diferentes= tk.Label(verestad,text=(
        "CANTIDAD CURSOS DIFERENTES: "+str(cdiferente)),bg='red',fg="white",font=55,justify='center')
            diferentes.place(relx=0.2, rely=0.64, relwidth=0.6, relheight=0.05)
            #COMBO 2
            d1=tk.StringVar(verestad)
            d1.set(c1)
            cdifc1= ttk.Combobox(verestad,textvariable=d1,state="readonly",justify='center')
            cdifc1.place(relx=0.2, rely=0.7, relwidth=0.25, relheight=0.05)
            cdifc1['values']=cursosdiferentesc1
            cdifc1.current(0)
            #COMBO 2
            d2=tk.StringVar(verestad)
            d2.set(c2)
            cdifc2= ttk.Combobox(verestad,textvariable=d2,state="readonly",justify='center')
            cdifc2.place(relx=0.55, rely=0.7, relwidth=0.25, relheight=0.045)
            cdifc2['values']=cursosdiferentesc2
            cdifc2.current(0)
            porcentaje1=round(ciguales*100/(len(cursosdiferentesc1)+2*ciguales),2)
            porcentaje2=round(ciguales*100/(len(cursosdiferentesc2)+2*ciguales),2)
            c1= tk.Label(verestad,text=(
        "% DE CURSOS IGUALES: "+str(porcentaje1)+"%"),bg='red',fg="white",font=55,justify='center')
            c1.place(relx=0.2, rely=0.77, relwidth=0.25, relheight=0.1)
            c2= tk.Label(verestad,text=(
        "% DE CURSOS IGUALES: "+str(porcentaje2)+"%"),bg='red',fg="white",font=55,justify='center')
            c2.place(relx=0.55, rely=0.77, relwidth=0.25, relheight=0.1)

#Ver una solo estadistica
def verestadi():
    if etd.get()=='Escoger estadistica':
        messagebox.showwarning("Estadistica","Debe escoger una estadistica",parent=estad)
    else:
        estad.withdraw()
        global verestad
        verestad = tk.Tk()
        verestad.title("ESTADISTICAS")
        verestad.geometry(t)
        verestad.configure(background="black")
        tituloflow(verestad)
        if etd.get()=='Promedios por semestre de todos los estudiantes':
            ccc=0
            m=0
            n=0
            pm= tk.Label(verestad,text=(
    """ PROMEDIOS POR SEMESTRE DE TODOS LOS ESTUDIANTES."""),bg='red',fg="white",font=70,justify='center')
            pm.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.08)
            for ss in range(1,11):
                ccc=0
                m=0
                for pro in coleccionusuarios.find():
                    y=pro['promedios']["Semestre " + str(ss)]
                    ccc=ccc+1
                    m=m+y
                ppp=round(m/ccc,2)
                pm= tk.Label(verestad,text=("Semestre " +str(ss) + ":  "+str(ppp)),bg='red',fg="white",font=70,justify='center')
                n=n+0.05
                pm.place(relx=0.25, rely=0.35+n, relwidth=0.5, relheight=0.05)
        elif etd.get()=='Ver estudiantes':
            user=[]
            nombre=[]
            promedios=[]
            for usx in coleccionusuarios.find():
                user.append(usx['usuario'])
                nombre.append(usx['nombre'])
            datos= tk.Label(verestad,text=(
    "                 USUARIOS                  "),bg='red',fg="white",font=400)            
            datos.place(relx=0.25, rely=0.30, relwidth=0.5, relheight=0.18)
            global u
            u = tk.StringVar(verestad)
            u.set('USUARIOS')
            semer = tk.OptionMenu(verestad, u, *user)
            semer.place(relx=0.25, rely=0.50, relwidth=0.5, relheight=0.18)
            global nm
            nm = tk.StringVar(verestad)
            nm.set('NOMBRES')
            #Escoge una carrera para comparar # default value
            semer2 = tk.OptionMenu(verestad, nm, *nombre)
            semer2.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.18)

            
            
        elif etd.get()=='Comparar carreras':
            es1= tk.Label(verestad,text="CARRERA 1:     ",bg='black',fg="white",font=110,justify='center')
            es1.place(relx=0.2, rely=0.3, relwidth=0.25, relheight=0.1)
            es2= tk.Label(verestad,text="CARRERA 2:     ",bg='black',fg="white",font=110,justify='center')
            es2.place(relx=0.55, rely=0.3, relwidth=0.25, relheight=0.1)
            global car1
            car1 = tk.StringVar(verestad)
            #Escoge una carrera para comparar
            car1.set("Escoger carrera") # default value
            opciones=['Ingenieria en computacion','Ingenieria en mecatronica','Ingenieria quimica','Ingenieria industrial']
            semer = tk.OptionMenu(verestad, car1, *opciones)
            semer.place(relx=0.2, rely=0.41, relwidth=0.25, relheight=0.1)
            global car2
            car2 = tk.StringVar(verestad)
            #Escoge una carrera para comparar
            car2.set("Escoger carrera") # default value
            semer2 = tk.OptionMenu(verestad, car2, *opciones)
            semer2.place(relx=0.55, rely=0.41, relwidth=0.25, relheight=0.1)
            bcomparar = tk.Button(verestad,relief="raised", borderwidth=5 ,text="COMPARAR", font=30, bg='dodger blue', command=comparar )
            bcomparar.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.08)           
        elif etd.get()=='Cantidad de usuarios':
            usmec=int(coleccionusuarios.count({'carrera':'Ingenieria en mecatronica'}))
            uscom=int(coleccionusuarios.count({'carrera':'Ingenieria en computacion'}))
            usqui=int(coleccionusuarios.count({'carrera':'Ingenieria quimica'}))
            usind=(coleccionusuarios.count({'carrera':'Ingenieria industrial'}))
            total=int(coleccionusuarios.count())
            pormec=round(usmec*100/total,2)
            porcom=round(uscom*100/total,2)
            porqui=round(usqui*100/total,2)
            porind=round(usind*100/total,2)
            maximo=max(usmec,uscom,usind,usqui)
            if maximo==usmec:
                may='MECATRONICA'
            elif maximo==uscom:
                may='COMPUTACION'
            elif maximo==usqui:
                may='QUIMICA'
            elif maximo==usind:
                may='INDUSTRIAL'
            datos= tk.Label(verestad,text=(
    "                        CANTIDAD DE USUARIOS                  "+
    "\n\n"+
    "         CARRERA                    USUARIOS                      %     "+
    "\n\n"+
    "     MECATRONICA:                       "+ str(usmec)+ "                             "+str(pormec)+ "%"+
    "\n"+
    "     COMPUTACION:                       "+ str(uscom)+ "                             "+str(porcom)+ "%"+
    "\n"+
    "     QUIMICA :                                 "+ str(usqui)+ "                             "+str(porqui)+ "%"+
    "\n"+
    "     INDUSTRIAL  :                          "+ str(usind)+ "                             "+str(porind)+ "%"+
    "\n\n"+
    "             TOTALES: "+str(total)+" ESTUDIANTES EN LA APLICACION"
    "\n"+
    "LA CARRERA CON MAYOR CANTIDAD DE ESTUDIANTES ES "+str(may)),bg='red',fg="white",font=400)
            datos.place(relx=0.25, rely=0.35, relwidth=0.6, relheight=0.5)
            
            #Boton regresar
        bregresarA= tk.Button(verestad,relief="raised", borderwidth=5 ,text="REGRESAR", font=30, bg='dodger blue', command=regresarverestad)
        bregresarA.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.10)
    

        
#Mostrar estadisticas
def estadisticas():
    inicio.withdraw()
    global estad
    estad = tk.Tk()
    estad.title("ESTADISTICAS")
    estad.geometry(t)
    estad.configure(background="black")
    tituloflow(estad)
    es= tk.Label(estad,text="ESTADISTICA:     ",bg='black',fg="white",font=110,justify='center')
    es.place(relx=0.3, rely=0.35, relwidth=0.4, relheight=0.1)
    global etd
    global semet
    etd = tk.StringVar(estad)
    opciones=['Cantidad de usuarios','Promedios por semestre de todos los estudiantes','Ver estudiantes','Comparar carreras']
    #Escoge un semestre, ya bien para editar notas o consultar notas
    etd.set("Escoger estadistica") # default value
    semer = tk.OptionMenu(estad, etd, *opciones)
    semer.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
    bestadistica = tk.Button(estad,relief="raised", borderwidth=5 ,text="VER ESTADISTICA", font=30, bg='dodger blue', command=verestadi )
    bestadistica.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.1)
    bregresarA= tk.Button(estad,relief="raised", borderwidth=5 ,text="REGRESAR", font=30, bg='dodger blue', command=regresarestad)
    bregresarA.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.10)
    estad.bind("<Return>",onEnterEstad)

def onEnterI(event):
    ingresar()

def onEnterC(event):
    crear()
    
#Funcion de la pantalla de inicio.
def iniciar():
#Se inicia con la pantalla de inicio.
    global inicio
    inicio= tk.Tk()
    inicio.title("INGRESO FLOW")
    #Tamano de la venta ancho x alto
    inicio.geometry(t)
    #Color de la ventana
    inicio.configure(background="black")
    tituloflow(inicio)
    #Ingresar
    us= tk.Label(inicio,text="USUARIO:     ",bg='black',fg="white",font=30,justify='center')
    us.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.15)
    global usuario
    global contrasena
    usuario = tk.Entry(inicio,font=30,justify='center',text='')
    usuario.place(relx=0.4, rely=0.3, relwidth=0.35, relheight=0.10)
    con= tk.Label(inicio,text="CONTRASENA:  ",bg='black',fg="white",font=30,justify='center')
    con.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.15)
    contrasena = tk.Entry(inicio,font=30,show='*',justify='center',text='')
    contrasena.place(relx=0.4, rely=0.5, relwidth=0.35, relheight=0.10)
    #Botones para ingresar
    bestadistica = tk.Button(inicio,relief="raised", borderwidth=5 ,text="ESTADISTICAS", font=30, bg='dodger blue', command=estadisticas)
    bestadistica.place(relx=0.05, rely=0.3, relwidth=0.15, relheight=0.10)
    bingresar = tk.Button(inicio,relief="raised", borderwidth=5 ,text="INGRESAR", font=30, bg='dodger blue', command=ingresar )
    bingresar.place(relx=0.4, rely=0.65, relwidth=0.35, relheight=0.10)
    inicio.bind("<Return>",onEnterI)
    #Boton de ayuda
    bayuda = tk.Button(inicio,relief="raised", borderwidth=5 ,text="?", font=30, bg='dodger blue',command=ayudar )
    bayuda.place(relx=0.05, rely=0.80, relwidth=0.15, relheight=0.10)
    #Botones para ingresar
    bcrearcuenta = tk.Button(inicio,relief="raised", borderwidth=5 ,text="CREAR CUENTA", font=30, bg='dodger blue',command=crearusuario )
    bcrearcuenta.place(relx=0.6, rely=0.8, relwidth=0.25, relheight=0.10)


#Funcion para limpiar las entradas de datos.
def limpiar(a):
    a.delete(0,'end')

#Funcion para cerrar sesion.    
def cerrarsesion():
    inicio.deiconify()
    menuprincipal.withdraw()

#Funcion para verificar que el usuario y la contrasena se encuentre en la base de datos y sean correctas
def verificarusuarioycontra():
    entrar=False
    for usuarios in coleccionusuarios.find():
        if usuarios['usuario']==usuario.get() and usuarios['contra']==contrasena.get():
            entrar=True
            global usuarioadentro
            usuarioadentro=usuarios
            limpiar(usuario)
            limpiar(contrasena)
    
    return entrar

#Funcion para ver notas segun el semestre escogido llamando a la BD
def vernotas():
    if semestre.get()=="Escoger semestre":
        messagebox.showwarning("Semestre","Debe escoger un semestre.",parent=notassss)
    else: 
        x=0.39
        a=0
        for clas in usuarioadentro['clases'][semestre.get()]:
            clase= tk.Label(notassss,text=clas,bg='lawn green',fg="black",font=30,justify='center')
            clase.place(relx=0.3, rely=x, relwidth=0.3, relheight=0.07)
            nota= tk.Label(notassss,text=float(usuarioadentro['clases'][semestre.get()][clas]),bg='orange red',fg="black",font=30,justify='center')
            nota.place(relx=0.65, rely=x, relwidth=0.1, relheight=0.07)
            a=a+float(usuarioadentro['clases'][semestre.get()][clas])
            x=x+0.08
        prom=round(a/6,2)
        usuarioadentro['promedios'][semestre.get()]=prom
        coleccionusuarios.delete_one({'usuario':(usuarioadentro['usuario'])})
        bdn=({'usuario':(usuarioadentro['usuario']),'contra':(usuarioadentro['contra']),'nombre':(usuarioadentro['nombre']),'carrera':(usuarioadentro['carrera']),'calendario':(usuarioadentro['calendario']),'clases':(usuarioadentro['clases']),'promedios':(usuarioadentro['promedios']),'horario':(usuarioadentro['horario'])})
        coleccionusuarios.insert(bdn)    
        promedio=tk.Label(notassss,text='Promedio',bg='black',fg="white",font=30,justify='center')
        promedio.place(relx=0.3, rely=x, relwidth=0.3, relheight=0.07)
        prome= tk.Label(notassss,text=(prom),bg='orange red',fg="black",font=30,justify='center')
        prome.place(relx=0.65, rely=x, relwidth=0.1, relheight=0.07)

#Funcion para cambiar la nota de una clase, luego de haber llenado los campos necesarios.
def editado():
    if clasess.get()=='Escoger clase':
        messagebox.showwarning("Clase","Debe escoger una clase.",parent=editar)
        #ARREGLAR IS NUMERIC PUES SOLO CUENTA ENTEROS, esto sera en el prototipo final
    elif esnota(noa.get())==False:
        messagebox.showwarning("Nota","Debe ingresar una nota numerica. Debe estar entre 0 y 100",parent=editar)
    else:
        c=float(noa.get())
        b=round(c,2)
        #Se actualiza la base de datos
        usuarioadentro['clases'][semestre.get()][clasess.get()]= b
        coleccionusuarios.delete_one({'usuario':(usuarioadentro['usuario'])})
        bdn=({'usuario':(usuarioadentro['usuario']),'contra':(usuarioadentro['contra']),'nombre':(usuarioadentro['nombre']),'carrera':(usuarioadentro['carrera']),'calendario':(usuarioadentro['calendario']),'clases':(usuarioadentro['clases']),'promedios':(usuarioadentro['promedios']),'horario':(usuarioadentro['horario'])})

        coleccionusuarios.insert(bdn)
        messagebox.showinfo("Nota","Ha cambiado la nota",parent=editar)
        vernotas()
        editar.withdraw()
        notassss.deiconify()

#Funcion que se llama para editar la nota de una clase.        
def editarnotas():
        if semestre.get()=="Escoger semestre":
            messagebox.showwarning("Semestre","Debe escoger un semestre.",parent=notassss)
        else:
            notassss.withdraw()
            global editar
            editar=tk.Tk()
            editar.title('NOTAS')
            editar.geometry(t)
            editar.configure(bg='white')
            tituloflow(editar)
            x=0.42
            a=0
            global case
            global clasess
            clasess = tk.StringVar(editar)
            a=semestre.get()
            clasess.set("Escoger clase") # default value
            case = tk.OptionMenu(editar, clasess, *(usuarioadentro['clases'][a]))
            case.place(relx=0.35, rely=0.4, relwidth=0.35, relheight=0.15)
            cm= tk.Label(editar,text="CLASE:     ",bg='black',fg="white",font=30,justify='center')
            cm.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.15)
            no= tk.Label(editar,text="NOTA:     ",bg='black',fg="white",font=30,justify='center')
            no.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.15)
            global noa
            noa = tk.Entry(editar,font=30,justify='center')
            noa.place(relx=0.35, rely=0.6, relwidth=0.35, relheight=0.15)
            beditado= tk.Button(editar,relief="raised", borderwidth=5 ,text="EDITAR", font=30, bg='dodger blue',command=editado)
            beditado.place(relx=0.05, rely=0.8, relwidth=0.2, relheight=0.15)
            editar.bind("<Return>",onEnterEN)
            #Termina funcion, luego de ingresar datos
            
#Esto llama a la ventana de notas, y muestre los botones iniciales para escoger las opciones de semestres y clases
def notas():
    menuprincipal.withdraw()
    global notassss
    notassss=tk.Tk()
    notassss.title('NOTAS')
    notassss.geometry(t)
    notassss.configure(bg='white')
    tituloflow(notassss)
    sem= tk.Label(notassss,text="SEMESTRE:     ",bg='black',fg="white",font=30,justify='center')
    sem.place(relx=0.05, rely=0.3, relwidth=0.2, relheight=0.07)
    global seme
    global semestre
    semestre = tk.StringVar(notassss)
    #Escoge un semestre, ya bien para editar notas o consultar notas
    semestre.set("Escoger semestre") # default value
    seme = tk.OptionMenu(notassss, semestre, *(usuarioadentro['clases']))
    seme.place(relx=0.05, rely=0.4, relwidth=0.2, relheight=0.07)
    bnot = tk.Button(notassss,relief="raised", borderwidth=5 ,text="VER NOTAS", font=30, bg='dodger blue', command=vernotas) 
    bnot.place(relx=0.35, rely=0.3, relwidth=0.25, relheight=0.07)
    bedit = tk.Button(notassss,relief="raised", borderwidth=5 ,text="EDITARNOTAS", font=30, bg='dodger blue', command=editarnotas) 
    bedit.place(relx=0.65, rely=0.3, relwidth=0.25, relheight=0.07)
    bregresarnotas= tk.Button(notassss,relief="raised", borderwidth=5 ,text="MENU PRINCIPAL", font=30, bg='dodger blue', command=regresarmenunotas)
    bregresarnotas.place(relx=0.05, rely=0.85, relwidth=0.2, relheight=0.10)

#Ingresar es para entrar al sistema, verificando usuario y mostrando el menu principal.
def ingresar():
    if verificarusuarioycontra()==True:
        inicio.withdraw()
        global menuprincipal
        menuprincipal=tk.Tk()
        menuprincipal.title('MENU PRINCIPAL')
        menuprincipal.geometry(t)
        menuprincipal.configure(bg='white')
        tituloflow(menuprincipal)
        bienvenido= tk.Label(menuprincipal,text=("Bienvenido " +str(usuarioadentro['nombre'])),bg='white',fg="black",font=40,justify='center')
        bienvenido.place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.15)
        #Boton para notas
        bnotas = tk.Button(menuprincipal,relief="raised", borderwidth=5 ,text="NOTAS", font=30, bg='lawn green',command=notas )
        bnotas.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.10)
        #Boton para horario
        bhorario = tk.Button(menuprincipal,relief="raised", borderwidth=5 ,text="HORARIO", font=30, bg='lawn green', command=horarioo)
        bhorario.place(relx=0.35, rely=0.55, relwidth=0.3, relheight=0.10)
        #Boton para calendario
        bcalendario = tk.Button(menuprincipal,relief="raised", borderwidth=5 ,text="CALENDARIO", font=30, bg='lawn green', command=calendario)
        bcalendario.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.10)
        #Boton de editar datos, para el siguiente
        #beditar = tk.Button(menuprincipal,relief="raised", borderwidth=5 ,text="EDITAR DATOS", font=30, bg='dodger blue', )
        #beditar.place(relx=0.1, rely=0.85, relwidth=0.20, relheight=0.10)
        #Botones para cerrar sesion
        bcerrar = tk.Button(menuprincipal,relief="raised", borderwidth=5 ,text="CERRAR SESION", font=30, bg='dodger blue', command=cerrarsesion)
        bcerrar.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.10)
    else:
        messagebox.showwarning("ENTRAR", "USUARIO Y/O CONTRASENA INCORRECTAS. INTENTE DE NUEVO", parent=inicio)


#La funcion que verifica los campos para crear un usuario
def crear():
    if variable.get()=="Escoger carrera":
        messagebox.showwarning("Carrera","Debe escoger una carrera",parent=crearcuenta)
    elif contrasena1.get()=='' or contrasena2.get()=='' or usuarion.get()=='' or nombre.get()=='':
        messagebox.showwarning("Campos","Debe llenar todos los campos para crear un usuario",parent=crearcuenta)
    elif contrasena1.get()!=contrasena2.get():
        messagebox.showwarning("CONTRASENA", "LAS CONTRASENAS NO COINCIDEN. INTENTE DE NUEVO",parent=crearcuenta)
    elif coleccionusuarios.count({'usuario':(usuarion.get())})>0:
        messagebox.showwarning("USUARIO", "EL NOMBRE DE USUARIO YA EXISTE. INTENTE DE NUEVO CON OTRO USUARIO",parent=crearcuenta)
    else:
        messagebox.showinfo("CUENTA CREADA", "Su cuenta fue creada.",parent=crearcuenta)
        global pensum
        if variable.get()=='Ingenieria en mecatronica':
            for x in colcarreras.find():
                pensum=x['Ingenieria en mecatronica']
        elif variable.get()=='Ingenieria en computacion':
            for x in colcarreras.find():
                pensum=x['Ingenieria en computacion']
        elif variable.get()=='Ingenieria quimica':
            for x in colcarreras.find():
                pensum=x['Ingenieria quimica']
        elif variable.get()=='Ingenieria industrial':
            for x in colcarreras.find():
                pensum=x['Ingenieria industrial']
        for pr in colpromedio.find():
            p=pr
        for col in colhor.find():
            hh=col
        dm={}
        c=contrasena1.get()
        bdn=({'usuario':usuarion.get(),'contra':c,'nombre':nombre.get(),'calendario':{mesActual:dm},'carrera':variable.get(),'clases':pensum, 'promedios':p,'horario':hh})
        coleccionusuarios.insert(bdn)
        crearcuenta.withdraw()
        inicio.deiconify()
        crearcuenta.withdraw()
        limpiar(nombre)
        limpiar(contrasena1)
        limpiar(contrasena2)
        limpiar(usuarion)

#Regresar de crear cuenta a inicio.
def regresarcc():
    crearcuenta.withdraw()
    inicio.deiconify()

#Regresar de ayuda a inicio
def regresarayuda():
    ayuda.withdraw()
    inicio.deiconify()
    
#Define lo que se mostrara al dar click en ayuda. Esta opcion se programara con mas informacion en el prototipo final.
def ayudar():
    inicio.withdraw()
    global ayuda
    ayuda=tk.Tk()
    ayuda.title('MENU PRINCIPAL')
    ayuda.geometry(t)
    ayuda.configure(bg='white')
    tituloflow(ayuda)
    bienvenido= tk.Label(ayuda,text=(
""" FLOW ES UNA APLICACION PARA AYUDARTE
    A ADMINISTRARTU TIEMPO, HORARIO Y NOTAS,
    POR Y PARA LOS ESTUDIANTES DE LA UVG."""),bg='red',fg="white",font=400,justify='center')
    bienvenido.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.5)


    #Boton regresar
    bregresarA= tk.Button(ayuda,relief="raised", borderwidth=5 ,text="REGRESAR", font=30, bg='dodger blue', command=regresarayuda)
    bregresarA.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.10)
    

#Define las pantallas para crear un usuario.
def crearusuario():
    inicio.withdraw()
    global crearcuenta
    crearcuenta=tk.Tk()
    crearcuenta.title('CREAR CUENTA')
    crearcuenta.geometry(t)
    crearcuenta.configure(bg='black')
    tituloflow(crearcuenta)
    global contrasena1
    global contrasena2
    global usuarion
    global nombre
    nombr= tk.Label(crearcuenta,text="NOMBRE:    ",bg='black',fg="white",font=30,justify='center')
    nombr.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.07)
    nombre = tk.Entry(crearcuenta,font=30,justify='center')
    nombre.place(relx=0.4, rely=0.3, relwidth=0.35, relheight=0.07)
    us= tk.Label(crearcuenta,text="USUARIO:     ",bg='black',fg="white",font=30,justify='center')
    us.place(relx=0.2, rely=0.40, relwidth=0.2, relheight=0.07)
    usuarion = tk.Entry(crearcuenta,font=30,justify='center')
    usuarion.place(relx=0.4, rely=0.4, relwidth=0.35, relheight=0.07)
    con1= tk.Label(crearcuenta,text="CONTRASENA:  ",bg='black',fg="white",font=30,justify='center')
    con1.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.07)
    contrasena1 = tk.Entry(crearcuenta,font=30,show='*',justify='center')
    contrasena1.place(relx=0.4, rely=0.5, relwidth=0.35, relheight=0.07)
    con2= tk.Label(crearcuenta,text="CONTRASENA:  ",bg='black',fg="white",font=30,justify='center')
    con2.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=0.07)
    contrasena2 = tk.Entry(crearcuenta,font=30,show='*',justify='center')
    contrasena2.place(relx=0.4, rely=0.6, relwidth=0.35, relheight=0.07)
    car= tk.Label(crearcuenta,text="CARRERA:     ",bg='black',fg="white",font=30,justify='center')
    car.place(relx=0.15, rely=0.7, relwidth=0.3, relheight=0.07)
    global carreras
    global variable
    variable = tk.StringVar(crearcuenta)
    variable.set("Escoger carrera") # default value
    opciones=['Ingenieria en computacion', 'Ingenieria en mecatronica','Ingenieria quimica','Ingenieria industrial']
    carrera = tk.OptionMenu(crearcuenta, variable, *opciones)
    carrera.place(relx=0.4, rely=0.7, relwidth=0.35, relheight=0.07)
    crearcuenta.bind("<Return>",onEnterC)


    #Botones crearusuario
    bcrear = tk.Button(crearcuenta,relief="raised", borderwidth=5 ,text="CREAR CUENTA", font=30, bg='dodger blue', command=crear) 
    bcrear.place(relx=0.4, rely=0.8, relwidth=0.3, relheight=0.10)

    #Boton regresar
    bregresar= tk.Button(crearcuenta,relief="raised", borderwidth=5 ,text="REGRESAR", font=30, bg='dodger blue', command=regresarcc)
    bregresar.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.10)


#Para cargar la pagina principal.
def cargando():
    global cargando
    cargando=tk.Tk()
    cargando.title('')
    cargando.geometry(t)
    cargando.configure(bg='black')
    fl=tk.PhotoImage(file="ffflow.gif")
    fl.subsample(2,2)
    ima=tk.Label(cargando, image=fl)
    ima.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.3)
    global carga    
    carga = ttk.Progressbar(cargando,orient="horizontal", length=100, mode="determinate", maximum=101)
    carga.place(relx=0.25, rely=0.6, relwidth=0.5, relheight=0.15)
    carga.start(10)
    for x in range(0,9):
        carga.step(9)
        carga.update()
        cargando.title(str(carga['value'])+'%')
        if carga['value']>90:
            time.sleep(1)
            cargando.destroy()
            iniciar()
        else:
            time.sleep(1)

#import funciones_graficas as gra
def regresarcalendario():
    app.withdraw()
    menuprincipal.deiconify()
    
def actualizar():
   eventos.withdraw()
   messagebox.showinfo("Actualizado","Ha actualizado eventos en " +str(mesActual)+" "+str(var),parent=app)
   usuarioadentro['calendario'][mesActual][var]=(entrada.get("1.0","end"))
   coleccionusuarios.delete_one({'usuario':(usuarioadentro['usuario'])})
   bdn=({'usuario':(usuarioadentro['usuario']),'contra':(usuarioadentro['contra']),'nombre':(usuarioadentro['nombre']),'carrera':(usuarioadentro['carrera']),'calendario':(usuarioadentro['calendario']),'clases':(usuarioadentro['clases']),'promedios':(usuarioadentro['promedios']),'horario':(usuarioadentro['horario'])})
   coleccionusuarios.insert(bdn)
   
#Definimos las funciones:
def ventanilla(boton):
    global eventos
    eventos= tk.Tk()
    eventos.geometry("400x400")
    eventos.title = "Agregar o quitar eventos"
    global var
    var=boton['text']
    global info
    tituloEventos = tk.Label(eventos, text=("Evento "+str(mesActual)+str(var)), font=("cambria", 20), fg="Black",
                justify="center", bg="light sky blue", relief="groove", borderwidth=4)
 
    if (mesActual in usuarioadentro['calendario'])==True:
       if (var in usuarioadentro['calendario'][mesActual])==True:
                info=usuarioadentro['calendario'][mesActual][var]
       else:
                info='Agregue eventos'
    else:
                info='Agregue eventos'
    global entrada
    entrada = tk.Text(eventos,font=30)
    entrada.insert('end',info)
    entrada.place(relx=0.1,rely=0.25,relw=0.8,relh=0.5)
    tituloEventos.place(relx=0.1, rely=0.1, relwidth=0.8)
    botonActualizar= tk.Button(eventos, text='ACTUALIZAR', font=("cambria", 12), bg="light sky blue", relief="groove",command=actualizar)
    botonActualizar.place(relx=0.1,rely=0.8,relw=0.8,relh=0.1)
    
def calendario():
   menuprincipal.withdraw() 
   global app
   #import funciones_graficas as gra
   ahora = cal.datetime.datetime.now()
   app = tk.Tk()


   app.title("Calendario Flow")
   app.configure(background="white")
   app.geometry("1280x620")

   ahora = str(ahora)
   mes = int(ahora[5:7])
   anio = int(ahora[0:4])
   dias_mes = list(range(1,cal.monthrange(anio,mes)[1]+1))

   nombreMes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
          10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

   mesActual = nombreMes[mes]
   mesImpresion = cal.monthcalendar(anio, mes)
   #ventana.place(x=0, y=0, relwidth=16, relheight=9)
   tituloPrincipal = tk.Label(app, text=("Calendario de " + mesActual), font=("cambria", 50), fg="Black", justify="center", bg="dodger blue",
   relief="sunken", borderwidth=4)
   tituloPrincipal.place(relx=0.1, rely=0.1, relwidth=0.8)


   #Se crea una lista con todos los botones de los dias de la semana
   dias = [tk.Label(app, text="Lunes", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Martes", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Miércoles", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Jueves", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Viernes", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Sábado", font=("cambria", 12), bg="dodger blue", relief="ridge"),
       tk.Label(app, text="Domingo", font=("cambria", 12), bg="dodger blue", relief="ridge")
           ]

   boton1 = tk.Button(app, text="1", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton1))
   boton2 = tk.Button(app, text="2", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton2))
   boton3 = tk.Button(app, text="3", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton3))
   boton4 = tk.Button(app, text="4", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton4))
   boton5 = tk.Button(app, text="5", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton5))
   boton6 = tk.Button(app, text="6", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton6))
   boton7 = tk.Button(app, text="7", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton7))
   boton8 = tk.Button(app, text="8", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton8))
   boton9 = tk.Button(app, text="9", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton9))
   boton10 = tk.Button(app, text="10", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton10))
   boton11 = tk.Button(app, text="11", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton11))
   boton12 = tk.Button(app, text="12", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton12))
   boton13 = tk.Button(app, text="13", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton13))
   boton14 = tk.Button(app, text="14", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton14))
   boton15 = tk.Button(app, text="15", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton15))
   boton16 = tk.Button(app, text="16", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton16))
   boton17 = tk.Button(app, text="17", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton17))
   boton18 = tk.Button(app, text="18", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton18))
   boton19 = tk.Button(app, text="19", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton19))
   boton20 = tk.Button(app, text="20", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton20))
   boton21 = tk.Button(app, text="21", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton21))
   boton22 = tk.Button(app, text="22", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton22))
   boton23 = tk.Button(app, text="23", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton23))
   boton24 = tk.Button(app, text="24", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton24))
   boton25 = tk.Button(app, text="25", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton25))
   boton26 = tk.Button(app, text="26", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton26))
   boton27 = tk.Button(app, text="27", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton27))
   boton28 = tk.Button(app, text="28", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton28))
   boton29 = tk.Button(app, text="29", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton29))
   boton30 = tk.Button(app, text="30", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton30))
   boton31 = tk.Button(app, text="31", font=("cambria", 12), bg="light sky blue", relief="groove", command= lambda: ventanilla(boton31))

   lista_botones= [ 0,
       boton1,
       boton2,
       boton3,
       boton4,
       boton5,
       boton6,
       boton7,
       boton8,
       boton9,
       boton10,
       boton11,
       boton12,
       boton13, 
       boton14,
       boton15,
       boton16, 
       boton17,
       boton18,
       boton19,
       boton20,
       boton21,
       boton22,
       boton23, 
       boton24,
       boton25,
       boton26,
       boton27,
       boton28,
       boton29,
       boton30,
       boton31
       ]


   #Se define la variable de posicion inicial
   posx = 0.08
   bregresarcal= tk.Button(app,relief="raised", borderwidth=5 ,text="MENU PRINCIPAL", font=30, bg='dodger blue', command=regresarcalendario)
   bregresarcal.place(relx=0.05, rely=0.9, relwidth=0.2, relheight=0.07)
   #Se crea un ciclo for para introducir los dias de la semana en la ventana
   for dia in dias:
       dia.place(relx=posx, rely=0.30, relw=0.12)
       posx = posx +0.12

   botonDias = tk.Button(app, font=("cambria", 12), bg="gray", relief="groove")

   posx = 0.20
   posy = 0.34
   x = 0
   ##for dia in mesImpresion:
   ##    for dia in mesImpresion[x]:
   ##        botonDias = tk.Button(app, text=str(dia), font=("cambria", 12), bg="light sky blue", relief="groove",command=lambda: ventanilla(botonDias), textvariable=int(dia))
   ##        if dia != 0:
   ##            botonDias.place(relx= posx, rely=posy, relw=0.12, relh=0.10)
   ##        posx = posx +0.12
   ##    if posx == 0.92:
   ##        x = x + 1
   ##        posy = posy + 0.11
   ##        posx = 0.08


   #añadimos los botones
   for i in dias_mes:
       lista_botones[i].place(relx= posx, rely=posy, relw=0.12, relh=0.10)
       posx+=0.12
       if posx==(0.92):
           posx=0.08
           posy+=0.11





   app.mainloop()

#global mes actual
ahora = cal.datetime.datetime.now()
ahora = str(ahora)
mes = int(ahora[5:7])
anio = int(ahora[0:4])
dias_mes = list(range(1,cal.monthrange(anio,mes)[1]+1))

nombreMes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
      10:"Octubre", 11:"Noviembre", 12:"Diciembre"}

global mesActual
mesActual = nombreMes[mes]
mesImpresion = cal.monthcalendar(anio, mes)

