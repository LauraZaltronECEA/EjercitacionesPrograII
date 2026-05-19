######### FABRICA    ##########
from products import NotificadorEmail, NotificadorSlack, NotificadorWhatsapp

class FabricaNotificadores:

    Notificadores = {"email":NotificadorEmail, #el value es la clase NotificadorEmail
                     "whatsapp":NotificadorWhatsapp,
                     "slack":NotificadorSlack
                    }

    def crearNotificador(self,tipo):
        return self.Notificadores[tipo]() # el () para q la clase se convierta en un objeto