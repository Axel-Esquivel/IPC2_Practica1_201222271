from .listas import Listas
from ..modelos.pizza import Pizza
from ..modelos.nodo_pizza import NodoPizza

class Pizzas(Listas):
    __puntero: NodoPizza = None
    __temporal: NodoPizza = None
    
    def __init__(self):
        super()
        self.__puntero = NodoPizza()
        
    def agregar(self, pizza: Pizza) -> Pizza:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            self.__temporal = self.__temporal.get_siguiente()
        
        self.__conteo += 1
        nuevo_nodo = NodoPizza()
        nuevo_nodo.set_pizza(pizza)
        self.__temporal.set_siguiente(nuevo_nodo)
        return pizza
        
    def eliminar_indice(self, indice: int) -> Pizza:
        self.__temporal = self.__puntero
        
        indice_recorrido = -1
        while indice_recorrido != indice:
            indice_recorrido += 1
            if self.__temporal.get_siguiente() != None:
                self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido == indice and self.__temporal.get_siguiente() != None:
            self.__conteo -= 1
            return self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
    
    def eliminar_elemento(self, pizza: Pizza) -> Pizza:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            if self.__temporal.get_siguiente() != None and self.__temporal.get_siguiente().get_pizza() == pizza:
                self.__conteo -= 1
                self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
            
            self.__temporal = self.__temporal.get_siguiente()
            
        return pizza
    
    def elemento(self, indice: int) -> Pizza:
        self.__temporal = self.__puntero
        
        indice_recorrido = -1
        while indice_recorrido != indice:
            indice_recorrido += 1
            self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido == indice and self.__temporal != None:
            return self.__temporal.get_pizza()