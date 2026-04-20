import xmlrpc.client as xml
from pais import pais

def serialize(data, file): #convertir un objeto en un archivo
    with open(file, "w") as f:
        text = xml.dumps((data,)) #tupla de un solo elemento. dumps tiene que recibir tuplas.
        f.write(text)

def deserialize(file):
    with open(file) as f:
        text = f.read()
        return xml.loads(text)[0][0] #devuelve una lista de listas, donde tener diferentes sets de datos. Tenemos que tomar el primer elemento de laprimer lista

myPais = pais()

serialize(myPais.toDict(), "pais.xml") #Serializa en xml, cambio el archivo a mano y cuando deserealizo me tinee q mostrar los nuevos valores
input("Presione una tecla para continuar...")
myPais.fromDict(deserialize("pais.xml"))
print(myPais.name, myPais.capital, myPais.football_teams)
#python serialXml.py
# reescribo manualmente en pais.xml
#enter
#muestra el dict cambiado

#Solo puedo, por el momento, serializar y deserealizar Diccionarios.

# data = {
#     "name":"Argentina",
#     "population":500000000,
#     "sup":278000000,
#     "capital":"CABA",
#     "football_teams":[
#         {
#             "name":"Boca Campeon"
#         },
#         {
#             "name":"San Lorenzo"
#         },
#         {
#             "name":"River Gay"
#         }
#     ],
#     "BestCountryEver":  True
# }

# serialize(data, "pais.xml")
# input("Presione una tecla para continuar...")
# print(deserialize("pais.xml"))

#Reflection: Acceder a los atributos de un objeto en tiempo de Ejecucion. (Leer el objeto y armarlo serializado con sus atributos)