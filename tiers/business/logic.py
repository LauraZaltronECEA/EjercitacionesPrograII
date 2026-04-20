from data.dataHelper import DataHelper

class Logic:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def validate(self):
        if  self.dni.find(".") > 0 or self.dni.find(",") > 0:
            return False
        if self.dni.isdigit() == False:
            return False
        
        self.nombre = self.nombre.lower().strip()
        return True

    def check(self):
        dh = DataHelper()
        res = dh.getOne(self.dni)

        if dh.getOne(self.dni) == False:
            return "No Hay Datos"
        if res == self.nombre:
            return "Hay Match"
        else:
            return "No hay match"

