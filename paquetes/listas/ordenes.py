from ..modelos.orden import Orden
from ..modelos.nodo_orden import NodoOrden

class Ordenes:
    __conteo: int = None
    __puntero: NodoOrden = None
    __temporal: NodoOrden = None
    
    def __init__(self):
        self.__conteo = 0
        self.__puntero = NodoOrden()
        
    def __iter__(self):
        self.__temporal = self.__puntero
        
        while self.__temporal:
            if self.__temporal.get_orden() != None: yield self.__temporal.get_orden()
            self.__temporal = self.__temporal.get_siguiente()
    
        return self.__conteo
        
    def encolar(self, orden: Orden) -> Orden:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            self.__temporal = self.__temporal.get_siguiente()
        
        self.__conteo += 1
        nuevo_nodo = NodoOrden()
        nuevo_nodo.set_orden(orden)
        self.__temporal.set_siguiente(nuevo_nodo)
        return orden
    
    def desencolar(self) -> Orden:
        return self.eliminar_indice(0)
    
    def eliminar_indice(self, indice: int) -> Orden:
        self.__temporal = self.__puntero
        
        indice_recorrido = -1
        while indice_recorrido != indice:
            indice_recorrido += 1
            if self.__temporal.get_siguiente() != None:
                self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido == indice and self.__temporal.get_siguiente() != None:
            self.__conteo -= 1
            return self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
    
    def eliminar_elemento(self, orden: Orden) -> Orden:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            if self.__temporal.get_siguiente() != None and self.__temporal.get_siguiente().get_orden() == orden:
                self.__conteo -= 1
                self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
            
            self.__temporal = self.__temporal.get_siguiente()
            
        return orden
    
    def elemento(self, indice: int) -> Orden:
        self.__temporal = self.__puntero
        
        indice_recorrido = -1
        while indice_recorrido != indice:
            indice_recorrido += 1
            self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido == indice and self.__temporal != None:
            return self.__temporal.get_orden()
        
    def contar(self):
        return self.__conteo