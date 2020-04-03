import pymongo
#Nos conectamos a la base de datos
conexion= pymongo.MongoClient()
#Buscamos la db que queremos.
db = conexion['flow']
#Seleccionamos la coleccion
colpromedio= db.promedio
prom={'Semestre 1': 100,
             'Semestre 2':100,
               'Semestre 3': 100,
             'Semestre 4':100,
               'Semestre 5': 100,
             'Semestre 6':100,
               'Semestre 7': 100,
             'Semestre 8':100,
               'Semestre 9': 100,
             'Semestre 10':100,}
                  
colpromedio.insert(prom)

