class Persona:
    edad = 0
    nombre = ""

    def presentacion(self):
        print("Hola soy {} y tengo {} años"
        .format(self.nombre, self.edad))

    def __init__(self, edad, nombre="NN"):
        self.nombre = nombre
        self.edad = edad

# manera de escribir codigo para que al importarlo, el codigo no se ejecute
if __name__ == "__main__":

    #Forma de pasar Pametros

    params = (22, "Lau")
    myPerson = Persona(*params) #Asterisco para 'desarmar' la tupla

    params = {"nombre": 'Laura', "edad":22}
    myPerson = Persona(**params) #Doble asterisco para 'desarmar' la tupla

    myPerson = Persona(22)
    myPerson = Persona(edad=22, nombre="Laura")
    myPerson = Persona(nombre="Laura", edad=22)
    myPerson.presentacion()

    # comentar ctrl k c
    # descomentar ctrl k u
