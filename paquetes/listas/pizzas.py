from ..modelos.pizza import Pizza
from ..modelos.nodo_pizza import NodoPizza

class Pizzas:
    __conteo: int = None
    __puntero: NodoPizza = None
    __temporal: NodoPizza = None
    
    def __init__(self):
        self.__conteo = 0
        self.__puntero = NodoPizza()
        
    def __iter__(self):
        self.__temporal = self.__puntero
        
        while self.__temporal:
            if self.__temporal.get_pizza() != None: yield self.__temporal.get_pizza()
            self.__temporal = self.__temporal.get_siguiente()
    
        return self.__conteo
        
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
        
    def contar(self):
        return self.__conteo