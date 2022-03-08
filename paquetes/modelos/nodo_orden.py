from .nodo import Nodo
from .orden import Orden

class NodoOrden(Nodo):
    __valor: Orden = None
    
    def __init__(self):
        super()
        
    def set_orden(self, orden: Orden):
        self.__valor = orden
    
    def get_orden(self) -> Orden:
        return self.__valor