from ..listas.ordenes import Ordenes

class MenuOrdenes:
    __ordenes: Ordenes = None
    
    def __init__(self, ordenes: Ordenes):
        self.__ordenes = ordenes
    
    def mostrar_menu(self):
        volver = False