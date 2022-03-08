from ..modelos.nodo import Nodo

class Listas:
    __puntero: Nodo
    __temporal: Nodo
    __conteo: int = None
    
    def __init__(self):
        self.__conteo = 0
        self.__puntero = Nodo()
        
    def __iter__(self):
        self.__temporal = self.__puntero
        
        while self.__temporal:
            if self.__temporal.valor != None: yield self.__temporal.valor
            self.__temporal = self.__temporal.siguiente
      
    def contar(self):
        return self.__conteo