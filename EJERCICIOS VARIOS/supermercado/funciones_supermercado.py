def menu():
    menu_str = """
---------------------------------------------
Bienvenido al sistema de control del supermercado
Sus opciones son:

1. Imprimir articulos, existencia y precios
2. Agregar articulo
3. Modificar existencia
4. Salir
---------------------------------------------
"""
    return menu_str
    
def es_float(numero):
    resultado = True
    try:
        float(numero)
    except:
        resultado = False
    return resultado

