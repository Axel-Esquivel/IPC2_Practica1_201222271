from ..listas.pizzas import Pizzas
from ..listas.ordenes import Ordenes
from ..componentes.consola import Consola
from ..listas.ingredientes import Ingredientes

class MenuOrdenes:
    __pizzas: Pizzas = None
    __ordenes: Ordenes = None
    __ingredientes: Ingredientes = None
    
    def __init__(self, ordenes: Ordenes, pizzas: Pizzas, ingredientes: Ingredientes):
        self.__pizzas = pizzas
        self.__ordenes = ordenes
        self.__ingredientes = ingredientes
    
    def mostrar_menu(self):
        volver = False
        
        while volver == False:
            Consola.limpiar_consola()
            print('-'*20 + 'MENU ORDENES'  + + '-'*20)
            