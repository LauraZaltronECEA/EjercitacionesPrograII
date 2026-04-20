import conf

class DataHelper:
    def __init__(self):
        self.__file = conf.file #el __ al principio del nombre, genera la ilusion de privacidad de los atributos

    def getOne(self, dni):
        rv = "" #return value
        with open(self.__file, "r") as f:
            for line in f.readlines():
                splitted = line.split(",") #splitted es una lista donde [0] es dni y [1] es el nombre
                if splitted[0] ==  dni:
                    rv = splitted[1].strip() #devuelvo el nombre    
                    break
            else: #si rompe con el break no entra en el else, pero si no ejecuta el break, retorna false.
                rv = False
            return rv
