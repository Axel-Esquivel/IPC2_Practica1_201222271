from ..modelos.ingrediente import Ingrediente
from ..modelos.nodo_ingrediente import NodoIngrediente

class Ingredientes:
    __puntero: NodoIngrediente = None
    __temporal: NodoIngrediente = None
    __temporal_siguiente: NodoIngrediente = None
    
    def __init__(self):
        self.__puntero = NodoIngrediente()
        
    def __iter__(self):
        self.__temporal = self.__puntero
        
        while self.__temporal:
            if self.__temporal.get_ingrediente() != None: yield self.__temporal.get_ingrediente()
            self.__temporal = self.__temporal.get_siguiente()
        
    def agregar(self, ingrediente: Ingrediente) -> None:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            self.__temporal = self.__temporal.get_siguiente()
            
        nuevo_nodo = NodoIngrediente()
        nuevo_nodo.set_ingrediente(ingrediente)
        self.__temporal.set_siguiente(nuevo_nodo)
        
    def eliminar_indice(self, indice: int) -> Ingrediente:
        self.__temporal = self.__puntero
        
        indice_recorrido = 0
        while indice_recorrido != indice:
            indice_recorrido += 1
            if self.__temporal.get_siguiente() != None:
                self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido - 1 == indice and self.__temporal != None:
            return self.__temporal.get_ingrediente()
    
    def eliminar_elemento(self, ingrediente: Ingrediente) -> Ingrediente:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            if self.__temporal.get_siguiente() != None and self.__temporal.get_siguiente().get_ingrediente() != None:
                
                if self.__temporal.get_siguiente().get_ingrediente() == ingrediente:
                    self.__temporal_siguiente = self.__temporal.get_siguiente()
                    
                    
            
            self.__temporal = self.__temporal.get_siguiente()
        
        return ingrediente