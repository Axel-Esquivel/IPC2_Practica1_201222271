class Ingrediente:
    __nombre: str = None
    __tiempo_preparacion: int = None
    
    def __init__(self, nombre: str, tiempo: int):
        self.set_nombre(nombre)
        self.set_tiempo(tiempo)
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def set_tiempo(self, tiempo_preparacion: int):
        self.__tiempo_preparacion = tiempo_preparacion
        
    def get_nombre(self):
        return self.__nombre
    
    def get_tiempo(self):
        return self.__tiempo_preparacion