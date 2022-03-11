class Cliente:
    __nombre: str = None
    __direccion: str = None
    __NIT: str = None
    
    def __init__(self):
        self.set_direccion('Ciudad')
        self.set_NIT('CF')
    
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def set_direccion(self, direccion: str):
        self.__direccion = direccion
        
    def set_NIT(self, NIT: str):
        self.__NIT = NIT
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_direccion(self) -> str:
        return self.__direccion
    
    def get_NIT(self) -> str:
        return self.__NIT