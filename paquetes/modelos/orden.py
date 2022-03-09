from datetime import datetime

from .cliente import Cliente
from ..listas.pizzas import Pizzas

class Orden:
    __numero: int = None
    __pizzas: Pizzas = None
    __cliente: Cliente = None
    __hora_pedido: datetime = None
    __hora_entrega: datetime = None
    
    def __init__(self):
        self.__pizzas = Pizzas()
        
    def set_numero(self, numero: int):
        self.__numero = numero
        
    def set_pizzas(self, pizzas: Pizzas):
        self.__pizzas = pizzas
        
    def set_cliente(self, cliente: Cliente):
        self.__cliente = cliente
        
    def set_hora_pedido(self):
        self.__hora_pedido = datetime.now()
        
    def set_hora_entrega(self):
        self.__hora_entrega = datetime.now()
        
    def get_numero(self):
        return self.__numero
    
    def get_pizzas(self):
        return self.__pizzas
    
    def get_cliente(self):
        return self.__cliente
    
    def get_hora_pedido(self) -> datetime:
        return self.__hora_pedido
    
    def get_hora_entrega(self) -> datetime:
        return self.__hora_entrega