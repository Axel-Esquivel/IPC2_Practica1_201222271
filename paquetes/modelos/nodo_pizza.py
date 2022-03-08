from .nodo import Nodo
from .pizza import Pizza

class NodoPizza(Nodo):
    __valor: Pizza = None
    
    def __init__(self):
        super()
        
    def set_pizza(self, pizza: Pizza):
        self.__valor = pizza
    
    def get_pizza(self) -> Pizza:
        return self.__valor