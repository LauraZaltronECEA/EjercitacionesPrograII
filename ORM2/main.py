import sqlobject as SO
from dotenv import load_dotenv
import os

#conexion db
load_dotenv()

database = "mysql://{}:{}@{}/{}".format(os.getenv("USER"), os.getenv("PASSWORD"), os.getenv("SERVER"), os.getenv("DB"))

__connection__ = SO.connectionForURI(database)

#creacion de clases
class Area(SO.SQLObject):
    nombre = SO.StringCol(length=40, varchar=True)
    empleados = SO.MultipleJoin("Empleado")

class Empleado(SO.SQLObject):
    nombre = SO.StringCol(length=40, varchar=True)
    apellido = SO.StringCol(length=40, varchar=True)
    hijos = SO.IntCol()
    activo = SO.BoolCol()
    area = SO.ForeignKey("Area",default=None,cascade=False) #Cascade modifica a todo lo que interpele este empleado
    habilidades = SO.RelatedJoin("Habilidad")

class Habilidad(SO.SQLObject):
    nombre = SO.StringCol(length=40, varchar=True)
    peso =  SO.FloatCol()
    empleados = SO.RelatedJoin("Empleado")


#borro las tablas para ir testeando
Habilidad.dropTable(ifExists = True)
Empleado.dropTable(ifExists = True)
Area.dropTable(ifExists = True)

#creacion de tablas
Area.createTable()
Empleado.createTable()
Habilidad.createTable() 
# Por ser una relacion muchos a muchos, se crea automaticamente en la bd empleado_habilidad
# tambien crea automaticamente dos metodos a la clase empleado (addHabilidad, removeHabilidad)
# y otros dos para la clase Habilidad (addEmpleado, removeEmpleado)

#creacion de habilidades
calculo = Habilidad(nombre="CALCULO", peso = 8.9)
programacion = Habilidad(nombre="PROGRAMACION", peso = 9.5)
relacionesInterp = Habilidad(nombre="RELACIONES INTERPERSONALES", peso = 6.2)

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

#Trae los empleados que trabajan en el area del id otorgado
area = Area.get(2)
print(area.empleados)

#Seleccionar varios de un area especifica
areaRRHH = Area.selectBy(nombre = "RECURSOS HUMANOS")

for emp in areaRRHH.getOne().empleados:
    emp.activo = False

#como saber en q area trabaja un empleado
emp = Empleado.get(1)
print(emp.area.nombre)

#agregar empleados a habilidades
programacion.addEmpleado(Empleado.get(1))
relacionesInterp.addEmpleado(Empleado.get(2))

#agregar habilidad a un empleado
Empleado.get(3).addHabilidad(Habilidad.get(1))