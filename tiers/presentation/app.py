from business.logic import Logic


class App:

    def prompt(self):
        print(20*"*", "Bienvenidos a la aplicacion",20*"*")
        dni = input("Ingrese DNI, solo numeros, sin puntos ni comas: ")
        nombre = input("Ingrese nombre: ")

        myLogic = Logic(dni, nombre)

        if myLogic.validate() == False:
            print("Datos Erroneos")
            return
        
        print(myLogic.check())
        