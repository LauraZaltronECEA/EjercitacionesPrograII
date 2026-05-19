from abc import ABC, abstractmethod

#########PRODUCTO ABSTRACTO###########
class Notificador(ABC):
    @abstractmethod
    def notificar(self, msg):
        pass

#########PRODUCTO CONCRETO###########
class NotificadorWhatsapp(Notificador):
    def __init__(self):
        print("Se ejecutan los mecanisos de construccion de un notificador de whatsapp")
    
    def notificar(self, msg):
        print("Whatsapp --> {}".format(msg))

class NotificadorSlack(Notificador):
    def __init__(self):
        print("Se ejecutan los mecanisos de construccion de un notificador de Slack")
    
    def notificar(self, msg):
        print("Slack --> {}".format(msg))

class NotificadorEmail(Notificador):
    def __init__(self):
        print("Se ejecutan los mecanisos de construccion de un notificador de Email")
    
    def notificar(self, msg):
        print("Email --> {}".format(msg))