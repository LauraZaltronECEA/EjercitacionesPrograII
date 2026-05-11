class Persona:

    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def presentacion(self):
        print("Hola soy, {} {}".format(self.nombre, self.apellido))

class Mamifero:
    especie = "Homo sapiens"
    def presentacion(self):
        print("Hola soy un {}".format(self.especie))

class Profesor(Persona, Mamifero):
    def presentacion(self):
        super().presentacion() #Super devuelve la clase, no un objeto.  
        print("y soy profesora")

persona = Profesor("laura","zaltron")
persona.presentacion() #La herencia se resuelve de izq a derecha. Primero busca en profesor, si no esta presentacion(), busca en los padres.
print(persona.nombre, persona.apellido, persona.especie)