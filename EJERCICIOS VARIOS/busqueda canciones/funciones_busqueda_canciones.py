import json
from urllib.parse import urlencode
from urllib.request import urlopen

def buscar_canciones(termino):
    parameters = urlencode({'term': termino, 'limit': 5})
    url = "https://itunes.apple.com/search?"+parameters
    response = urlopen(url)
    contents = response.read()

    text = contents.decode('utf8')
    data = json.loads(text)
    return data['results']


def menu():
    menu_str = """
---------------------------------------------
Bienvenido a la busqueda de canciones
Sus opciones son:

1. Buscar canciones
2. Agregar palabra al diccionario
3. Traducir fase
4. Salir
---------------------------------------------
"""
    return menu_str
