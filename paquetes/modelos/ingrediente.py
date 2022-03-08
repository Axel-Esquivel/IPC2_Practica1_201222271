class Ingrediente:
    __nombre: str = None
    __tiempo_preparacion: int = None
    
    def __init__(self, nombre: str = None, tiempo_preparacion: int = None):
        self.set_nombre(nombre)
        self.set_tiempo(tiempo_preparacion)
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def set_tiempo_preparacion(self, tiempo_preparacion: int):
        self.__tiempo_preparacion = tiempo_preparacion
        
    def get_nombre(self):
        return self.__nombre
    
    def get_tiempo_preparacion(self):
        return self.__tiempo_preparacion