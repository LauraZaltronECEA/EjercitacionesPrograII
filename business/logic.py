class Logic:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def validate(self):
        if  self.dni.contains(".") or self.dni.contains(","):
            return False
        if self.dni.isDigit() == False:
            return False
        
        self.nombre = self.nombre.lower().strip()
        return True

    def check(self):
        