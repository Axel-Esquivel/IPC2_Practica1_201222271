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
        self.__crear_pizzas()
        
    def __crear_ingredientes(self):
        self.__ingredientes.agregar(Ingrediente('Pepperoni', 3))
        self.__ingredientes.agregar(Ingrediente('Salchicha', 4))
        self.__ingredientes.agregar(Ingrediente('Carne', 10))
        self.__ingredientes.agregar(Ingrediente('Queso', 5))
        self.__ingredientes.agregar(Ingrediente('Piña', 2))
        
    def __crear_pizzas(self):
        ingredientes_pepperoni = Ingredientes()
        ingredientes_pepperoni.agregar(self.__ingredientes.elemento(0))
        ingredientes_pepperoni.agregar(self.__ingredientes.elemento(3))
        self.__pizzas.agregar(Pizza('Pepperoni', 45.00, 1, ingredientes_pepperoni))
        
        ingredientes_carnes = Ingredientes()
        ingredientes_carnes.agregar(self.__ingredientes.elemento(1))
        ingredientes_carnes.agregar(self.__ingredientes.elemento(2))
        ingredientes_carnes.agregar(self.__ingredientes.elemento(3))
        self.__pizzas.agregar(Pizza('Carnes', 90.00, 1, ingredientes_carnes))
        
        ingredientes_piña = Ingredientes()
        ingredientes_piña.agregar(self.__ingredientes.elemento(3))
        ingredientes_piña.agregar(self.__ingredientes.elemento(4))
        self.__pizzas.agregar(Pizza('Piña', 45.00, 1, ingredientes_piña))