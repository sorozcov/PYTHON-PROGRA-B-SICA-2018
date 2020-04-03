import pymongo

BASE_DE_DATOS = 'supermercado'
COLECCION = 'listado_compras'

conexion = pymongo.MongoClient()
conexion[BASE_DE_DATOS][COLECCION].delete_many({})

listado_compras = [{
	'producto': 'cerchas',
	'cantidad': 6,
	'precio': 2.5,
	'categoria': 'hogar',
	'tienda': 'walmart'
}, {
	'producto': 'jeans',
	'cantidad': 2,
	'precio': 150,
	'categoria': 'ropa',
	'tienda': 'siman'
}, {
	'producto': 'playeras',
	'cantidad': 4,
	'precio': 40,
	'categoria': 'ropa',
	'tienda': 'siman'
}, {
	'producto': 'playeras',
	'cantidad': 4,
	'precio': 40,
	'categoria': 'ropa',
	'tienda': 'siman'
}, {
	'producto': 'jarrones de vidrio',
	'cantidad': 3,
	'precio': 45,
	'categoria': 'hogar',
	'tienda': 'la torre'
}, {
	'producto': 'bombillos',
	'cantidad': 8,
	'precio': 16,
	'categoria': 'hogar',
	'tienda': 'la torre'
}, {
	'producto': 'pijamas',
	'cantidad': 2,
	'precio': 37.50,
	'categoria': 'ropa',
	'tienda': 'siman'
}, {
	'producto': 'pantalones casuales',
	'cantidad': 1,
	'precio': 85,
	'categoria': 'ropa',
	'tienda': 'siman'
}, {
	'producto': 'cremas para cuerpo',
	'cantidad': 4,
	'precio': 59.90,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'cremas para cara',
	'cantidad': 3,
	'precio': 25,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'cremas para cara',
	'cantidad': 3,
	'precio': 25,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'pastas de dientes',
	'cantidad': 3,
	'precio': 19.50,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'cepillos de dientes',
	'cantidad': 4,
	'precio': 20,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'desodorantes',
	'cantidad': 6,
	'precio': 20,
	'categoria': 'higiene',
	'tienda': 'la torre'
}, {
	'producto': 'papel higienico (docena)',
	'cantidad': 1,
	'precio': 85,
	'categoria': 'hogar',
	'tienda': 'walmart'
}, {
	'producto': 'libras de pechuga de pollo',
	'cantidad': 3,
	'precio': 17.95,
	'categoria': 'comida',
	'tienda': 'walmart'
}, {
	'producto': 'libras de frijoles',
	'cantidad': 2,
	'precio': 7.30,
	'categoria': 'comida',
	'tienda': 'walmart'
}, {
	'producto': 'pan sandwich',
	'cantidad': 3,
	'precio': 18.5,
	'categoria': 'comida',
	'tienda': 'walmart'
}, {
	'producto': 'libras de arroz',
	'cantidad': 5,
	'precio': 8.25,
	'categoria': 'comida',
	'tienda': 'walmart'
}, {
	'producto': 'lt de jugo de naranja',
	'cantidad': 3,
	'precio': 21.50,
	'categoria': 'comida',
	'tienda': 'walmart'
}]

conexion[BASE_DE_DATOS][COLECCION].insert_many(listado_compras)
