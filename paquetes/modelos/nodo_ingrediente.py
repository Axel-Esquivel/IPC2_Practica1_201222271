from .nodo import Nodo
from .ingrediente import Ingrediente

class NodoIngrediente(Nodo):
    __ingrediente: Ingrediente
    
    def set_ingrediente(self, ingrediente: Ingrediente):
        self.__ingrediente = ingrediente
        
    def get_ingrediente(self):
        return self.__ingrediente