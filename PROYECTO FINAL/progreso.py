from tkinter import ttk
import tkinter as tk
import time

def cargando():
    global cargando
    cargando=tk.Tk()
    cargando.title('')
    cargando.geometry('600x600')
    cargando.configure(bg='black')
    global carga
    carga = ttk.Progressbar(cargando,orient="horizontal", length=100, mode="determinate", maximum=100)
    carga.place(relx=0.25, rely=0.3, relwidth=0.55, relheight=0.15,)
    carga.start()
    for x in range(0,9):
        carga.step(10)
        carga.update()
        a=carga['value']
        cargando.title(str(a)+'%')
        if carga['value']>90:
            cargando.destroy()
            inicio.deiconify()
        else:
            time.sleep(1)



    


    
    

    
