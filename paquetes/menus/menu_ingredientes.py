from ..listas.ingredientes import Ingredientes

class MenuIngredientes:
    __ingredientes: Ingredientes = None
    
    def __init__(self, ingredientes: Ingredientes):
        self.__ingredientes = ingredientes
    
    def mostrar_menu(self):
        volver = False