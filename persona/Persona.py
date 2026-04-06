class Persona:
    edad = 0
    nombre = ""

    def presentacion(self):
        print("Hola soy {} y tengo {} años"
        .format(self.nombre, self.edad))

    def __init__(self, edad, nombre="NN"): #Asignacion del valor por defecto a nombre
        self.nombre = nombre
        self.edad = edad


if __name__ == "__main__":# manera de escribir codigo para que al importarlo, el codigo no se ejecute

    #Forma de pasar Pametros
    #Definir una tupla con los parametros, para asignarlos explicitamente a cada parametro del constructor

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
