from ..listas.pizzas import Pizzas
from .menu_pizzas import MenuPizzas
from ..listas.ordenes import Ordenes
from .menu_ordenes import MenuOrdenes
from ..componentes.consola import Consola
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
        mostar_desarrollador = False
        Consola.limpiar_consola()
        
        while salir == False:
            if mostar_desarrollador == True:
                mostar_desarrollador = False
                print('-'*20 + 'DESARROLLADOR' + '-'*20)
                print('201222271 Axel Josué Esquivel Cuy')
            
            print('-'*20 + 'MENU PRINCIPAL' + '-'*20)
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Ingredientes.value, OpcionesMenuPrincipal.Ingredientes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Pizzas.value, OpcionesMenuPrincipal.Pizzas.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Ordenes.value, OpcionesMenuPrincipal.Ordenes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Desarrollador.value, OpcionesMenuPrincipal.Desarrollador.name.replace('_', ' ')))
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Salir.value, OpcionesMenuPrincipal.Salir.name.replace('_', ' ')))
            
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OpcionesMenuPrincipal.Ingredientes.value):
                    MenuIngredientes(self.__ingredientes).mostrar_menu()
                elif int(opcion) == int(OpcionesMenuPrincipal.Pizzas.value):
                    MenuPizzas(self.__pizzas).mostrar_menu()
                elif int(opcion) == int(OpcionesMenuPrincipal.Ordenes.value):
                    MenuOrdenes(self.__ordenes).mostrar_menu()
                elif int(opcion) == int(OpcionesMenuPrincipal.Desarrollador.value):
                    mostar_desarrollador = True
                elif int(opcion) == int(OpcionesMenuPrincipal.Salir.value):
                    salir = True