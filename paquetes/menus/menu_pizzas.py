from ..listas.pizzas import Pizzas

class MenuPizzas:
    __pizzas: Pizzas = None
    
    def __init__(self, pizzas: Pizzas):
        self.__pizzas = pizzas
    
    def mostrar_menu(self):
        volver = False