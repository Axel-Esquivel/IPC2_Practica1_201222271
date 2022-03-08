from ..modelos.ingrediente import Ingrediente
from ..modelos.nodo_ingrediente import NodoIngrediente

class Ingredientes:
    __puntero: NodoIngrediente = None
    __temporal: NodoIngrediente = None
    
    def __init__(self):
        self.__puntero = NodoIngrediente()
        
    def __iter__(self):
        self.__temporal = self.__puntero
        
        while self.__temporal:
            if self.__temporal.valor != None: yield self.__temporal.valor
            self.__temporal = self.__temporal.get_siguiente()
        
    def agregar(self, ingrediente: Ingrediente):
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            self.__temporal = self.__temporal.get_siguiente()
            
        nuevo_nodo = NodoIngrediente()
        nuevo_nodo.set_ingrediente(ingrediente)
        self.__temporal.set_siguiente(nuevo_nodo)
        
    def eliminar(self):
        pass