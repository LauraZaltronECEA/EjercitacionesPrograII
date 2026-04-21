import json
from pais import pais

def serialize(data, file): #convertir un objeto en un archivo
    with open(file, "w") as f:
        text = json.dumps(data,indent=4)#utiliza ese valor (4 o 2) para indentar la informacion y q el file pais.json quede lindo. 
        f.write(text)

def deserialize(file):
    with open(file) as f:
        text = f.read()
        return json.loads(text)
    
myPais = pais()
file = "pais.json"

serialize(myPais.toDict(), file) #Serializa en json, cambio el archivo a mano y cuando deserealizo me tinee q mostrar los nuevos valores
input("Presione una tecla para continuar...")
myPais.fromDict(deserialize(file))
print(myPais.name, myPais.capital, myPais.football_teams)
#python serialJson.py
#reescribo manualmente en pais.json
#enter
#muestra el dict cambiado
