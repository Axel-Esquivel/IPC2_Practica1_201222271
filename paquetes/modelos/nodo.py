class Nodo:
    __siguiente: None
    
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
        
    def get_siguiente(self):
        return self.__siguiente