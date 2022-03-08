from ..listas.pizzas import Pizzas
from .menu_pizzas import MenuPizzas
from ..listas.ordenes import Ordenes
from .menu_ordenes import MenuOrdenes
from ..listas.ingredientes import Ingredientes
from .menu_ingredientes import MenuIngredientes
from ..enums.opciones_menu_principal import OpcionesMenuPrincipal

class MenuPrincipal:
    __pizzas: Pizzas = None
    __ordenes: Ordenes = None
    __ingredientes: Ingredientes = None
        
    def __init__(self):
        self.__pizzas = Pizzas()
        self.__ordenes = Ordenes()
        self.__ingredientes = Ingredientes()
    
    def mostrar_menu(self):
        salir = False
        
        while salir == False:
            print('-'*20 + 'MENU PRINCIPAL' + '-'*20)
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Ingredientes.value, OpcionesMenuPrincipal.Ingredientes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Pizzas.value, OpcionesMenuPrincipal.Pizzas.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Ordenes.value, OpcionesMenuPrincipal.Ordenes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Salir.value, OpcionesMenuPrincipal.Salir.name.replace('_', ' ')))
            
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OpcionesMenuPrincipal.Ingredientes.value):
                    MenuIngredientes(self.__ingredientes).mostrar_menu()
                if int(opcion) == int(OpcionesMenuPrincipal.Pizzas.value):
                    MenuPizzas(self.__pizzas).mostrar_menu()
                if int(opcion) == int(OpcionesMenuPrincipal.Ordenes.value):
                    MenuOrdenes(self.__ordenes).mostrar_menu()
                if int(opcion) == int(OpcionesMenuPrincipal.Salir.value):
                    salir = True