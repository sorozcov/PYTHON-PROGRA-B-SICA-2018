import arte_astericos

decision=input("Desea imprimir un rectangulo, (Si para si, cualquier otra tecla para no)")
while decision=="Si":
  base=int(input("Ingrese la base del rectangulo"))
  altura=int(input("Ingrese la altura del rectangulo"))
  caracter=input("Ingrese el caracter del rectangulo del rectangulo")
  arte_astericos.dibujar_triangulo(base,altura,caracter)
print("Gracias por usar el programa")
