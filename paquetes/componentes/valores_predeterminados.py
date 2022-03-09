from ..modelos.pizza import Pizza
from ..listas.pizzas import Pizzas
from ..modelos.ingrediente import Ingrediente
from ..listas.ingredientes import Ingredientes

class ValoresPredeterminados:
    __pizzas: Pizzas = None
    __ingredientes: Ingredientes = None
    
    def __init__(self, ingredientes: Ingredientes, pizzas: Pizzas):
        self.__pizzas = pizzas
        self.__ingredientes = ingredientes
        self.__crear_ingredientes()
        
    def __crear_ingredientes(self):
        self.__ingredientes.agregar(Ingrediente('Pepperoni', 3))
        self.__ingredientes.agregar(Ingrediente('Salchicha', 4))
        self.__ingredientes.agregar(Ingrediente('Carne', 10))
        self.__ingredientes.agregar(Ingrediente('Queso', 5))
        self.__ingredientes.agregar(Ingrediente('Piña', 2))