from Logger import Logger
from activity import otraActividad

my_log = Logger()
my_log.log("Inicio del programa")

my_log.log("A punto de realizar otra actividad")
otraActividad()

my_log.show_logs()