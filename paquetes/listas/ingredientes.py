from ..modelos.ingrediente import Ingrediente
from ..modelos.nodo_ingrediente import NodoIngrediente

class Ingredientes:
    __conteo: int = None
    __puntero: NodoIngrediente = None
    __temporal: NodoIngrediente = None
    
    def __init__(self):
        self.__conteo = 0
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
        
        self.__conteo += 1
        nuevo_nodo = NodoIngrediente()
        nuevo_nodo.set_ingrediente(ingrediente)
        self.__temporal.set_siguiente(nuevo_nodo)
        
    def eliminar_indice(self, indice: int) -> Ingrediente:
        self.__temporal = self.__puntero
        
        indice_recorrido = 0
        while indice_recorrido != indice:
            if self.__temporal.get_siguiente() != None:
                self.__temporal = self.__temporal.get_siguiente()
            indice_recorrido += 1
        
        if indice_recorrido == indice and self.__temporal.get_siguiente() != None:
            self.__conteo -= 1
            return self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
    
    def eliminar_elemento(self, ingrediente: Ingrediente) -> Ingrediente:
        self.__temporal = self.__puntero
        
        while self.__temporal.get_siguiente() != None:
            if self.__temporal.get_siguiente() != None and self.__temporal.get_siguiente().get_ingrediente() == ingrediente:
                self.__conteo -= 1
                self.__temporal.set_siguiente(self.__temporal.get_siguiente().get_siguiente())
            
            self.__temporal = self.__temporal.get_siguiente()
            
        return ingrediente
    
    def elemento(self, indice: int) -> Ingrediente:
        self.__temporal = self.__puntero
        
        indice_recorrido = -1
        while indice_recorrido != indice:
            indice_recorrido += 1
            self.__temporal = self.__temporal.get_siguiente()
        
        if indice_recorrido == indice and self.__temporal != None:
            return self.__temporal.get_ingrediente()
    
    def existe(self, ingrediente: Ingrediente) -> bool:
        self.__temporal = self.__puntero
        
        existe = False
        while self.__temporal.get_siguiente() != None:
            if self.__temporal.get_ingrediente() == ingrediente: existe = True
            
            self.__temporal = self.__temporal.get_siguiente()
        
        
        
        return existe
    
    def contar(self) -> int:
        return self.__conteo