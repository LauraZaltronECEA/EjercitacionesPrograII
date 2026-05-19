from factory import FabricaNotificadores

notif = FabricaNotificadores().crearNotificador("email")
notif.notificar("esta es una notificacion de email")

notif = FabricaNotificadores().crearNotificador("whatsapp")
notif.notificar("esta es una notificacion de whatsapp")

notif = FabricaNotificadores().crearNotificador("slack")
notif.notificar("esta es una notificacion de slack")