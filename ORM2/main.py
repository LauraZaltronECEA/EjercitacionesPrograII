import sqlobject as SO
from dotenv import load_dotenv
import os

load_dotenv()

database = "mysql://{}:{}@{}/{}".format(os.getenv("USER"), os.getenv("PASSWORD"), os.getenv("SERVER"), os.getenv("DB"))

__connection__ = SO.connectionForURI(database)

class Area(SO.SQLObject):
    nombre = SO.StringCol(length=40, varchar=True)
    empleados = SO.MultipleJoin("Empleado")

class Empleado(SO.SQLObject):
    nombre = SO.StringCol(length=40, varchar=True)
    apellido = SO.StringCol(length=40, varchar=True)
    hijos = SO.IntCol()
    activo = SO.BoolCol()
    area = SO.ForeignKey("Area",default=None,cascade=False) #Cascade modifica a todo lo que interpele este empleado

#borro las tablas para ir testeando
Empleado.dropTable(ifExists = True)
Area.dropTable(ifExists = True)

#creacion de tablas
Area.createTable()
Empleado.createTable()

#creacion de areas
contabilidad = Area(nombre="CONTABILIDAD")
ingenieria = Area(nombre="INGENIERIA")
maestranza = Area(nombre="MAESTRANZA")
rrhh = Area(nombre="RECURSOS HUMANOS")

#creacion de empleado
Empleado(nombre="Manuel", apellido="Alvarez", hijos=2, activo= True, area = ingenieria)
Empleado(nombre="Silvia", apellido="Menin", hijos=4, activo= True, area = rrhh)
Empleado(nombre="Mauro", apellido="Zaltron", hijos=0, activo= True)

#modificacion de empleado
mauro = Empleado.get(3)
mauro.area = maestranza