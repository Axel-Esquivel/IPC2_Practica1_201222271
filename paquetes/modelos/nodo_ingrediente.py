from .nodo import Nodo
from .ingrediente import Ingrediente

class NodoIngrediente(Nodo):
    __valor: Ingrediente = None
    
    def __init__(self):
        super()
        
    def set_ingrediente(self, ingrediente: Ingrediente):
        self.__valor = ingrediente
    
    def get_ingrediente(self):
        return self.__valor