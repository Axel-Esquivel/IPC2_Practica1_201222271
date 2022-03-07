class Ingrediente:
    __nombre: str = None
    __tiempo_preparacion: int = None
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def set_tiempo(self, tiempo_preparacion: int):
        self.__tiempo_preparacion = tiempo_preparacion
        
    def get_nombre(self):
        return self.__nombre
    
    def get_tiempo(self):
        return self.__tiempo_preparacion