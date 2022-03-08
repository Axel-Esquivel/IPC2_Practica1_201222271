from .cliente import Cliente
from ..listas.pizzas import Pizzas

class Orden:
    __numero: int = None
    __pizzas: Pizzas = None
    __cliente: Cliente = None
    
    def set_numero(self, numero: int):
        self.__numero = numero
        
    def set_pizzas(self, pizzas: Pizzas):
        self.__pizzas = pizzas
        
    def set_cliente(self, cliente: Cliente):
        self.__cliente = cliente
        
    def get_numero(self):
        return self.__numero
    
    def get_pizzas(self):
        return self.__pizzas
    
    def get_cliente(self):
        return self.__cliente