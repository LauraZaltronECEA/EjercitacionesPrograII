#venv -> pip install pyyaml
import yaml
from pais import pais

def serialize(data, file): #convertir un objeto en un archivo
    with open(file, "w") as f:
        text = yaml.dump(data,explicit_end=True, explicit_start= True)
        f.write(text)

def deserialize(file):
    with open(file) as f:
        text = f.read()
        return yaml.safe_load(text)
    
myPais = pais()
file = "pais.yaml"

serialize(myPais.toDict(), file) #Serializa en json, cambio el archivo a mano y cuando deserealizo me tinee q mostrar los nuevos valores
input("Presione una tecla para continuar...")
myPais.fromDict(deserialize(file))
print(myPais.name, myPais.capital, myPais.football_teams)
#python serialYAML.py
#reescribo manualmente en pais.yaml
#enter
#muestra el dict cambiado

#existen adaptadores para nombres de atributos y pasar numeros de notacion cientifica a enteros (o viceversa). 
