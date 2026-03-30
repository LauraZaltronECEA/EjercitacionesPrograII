class Persona:
    edad = 0
    nombre = ""

    def presentacion(self):
        print("Hola soy {} y tengo {} años"
        .format(self.nombre, self.edad))

    def __init__(self, nombre, edad)
        self.nombre = nombre
        self.edad = edad


myPerson = Persona("Lau", 22)