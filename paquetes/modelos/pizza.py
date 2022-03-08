from ..listas.ingredientes import Ingredientes

class Pizza:
    __nombre: str = None
    __precio: float = None
    __cantidad: int = None
    __ingredientes: Ingredientes = None
    
    def __init__(self, nombre: str = None, precio: float = None, cantidad: int = None, ingredientes: Ingredientes = None):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
        self.__ingredientes = ingredientes
        if self.__ingredientes == None: self.__ingredientes = Ingredientes()
        
    def set_nombre(self, nombre: str):
        self.__nombre = nombre
        
    def set_precio(self, precio: float):
        self.__precio = precio
        
    def set_cantidad(self, cantidad: int):
        self.__cantidad = cantidad
        
    def set_ingredientes(self, ingredientes: Ingredientes):
        self.__ingredientes = ingredientes
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_precio(self) -> float:
        return self.__precio
    
    def get_cantidad(self) -> int:
        return self.__cantidad
    
    def get_ingredientes(self) -> Ingredientes:
        return self.__ingredientes