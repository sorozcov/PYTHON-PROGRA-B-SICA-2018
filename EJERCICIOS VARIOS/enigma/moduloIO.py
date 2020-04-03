#UVG
#Silvio Orozco Vizquerra
#Carne 18282
#Fecha 16/03/2018
#Archivo moduloIO.py

#Abrimos un archivo
def leer(codigo):
  try:
     with open(codigo)as archivo:
        codigo=archivo.read()
  except (FileNotFoundError):
         codigo=("El archivo no fue encontrado")
  return codigo
#Hacemos en reversa el codigo
def reversa(cadena):
    cadena=list(cadena)
    rever=""
    for x in range((len(cadena)-1),-1,-1):
         rever=rever+cadena[x]
    return rever
#Buscamos Inicio
def inicio(ini,codigo):
    inicia=codigo.find(ini)
    inicia=inicia+len(ini)
    return inicia
#Buscamos el final
def final(fin,codigo):
    ter=codigo.find(fin)
    return ter
def escribir(mensaje, archivo):
    arch = open(archivo , "w")
    arch.write("El mensaje descrifrado es \n")
    arch.write(str(mensaje))
    arch.close()
