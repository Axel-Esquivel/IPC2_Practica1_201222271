class Nodo:
    __valor: None
    __siguiente: None
    
    def set_valor(self, valor):
        self.__valor = valor
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def get_valor(self):
        return self.__valor
        
    def get_siguiente(self):
        return self.__siguiente