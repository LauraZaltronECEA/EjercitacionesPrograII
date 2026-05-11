#LOGGER / LOG : registro de movimientos con fecha, hora y descripcion.
class Logger:
    _instance = None #para SINGLETON primero se le asigna un value 'privado' llamado _instance de valor None
    
    def __new__(cls):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls) #si no existe una instancia, se crea una nueva instancia de la clase Logger
            cls._instance.logs = [] #se inicializa una lista vacía para almacenar los logs

        return cls._instance #si ya existe una instancia, se devuelve la instancia existente

    def log(self, msg):
        self.logs.append(msg)

    def show_logs(self):
        for log in self.logs:
            print(log)