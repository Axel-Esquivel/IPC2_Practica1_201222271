from ..listas.pizzas import Pizzas
from .menu_pizzas import MenuPizzas
from ..listas.ordenes import Ordenes
from .menu_ordenes import MenuOrdenes
from ..componentes.consola import Consola
from ..listas.ingredientes import Ingredientes
from .menu_ingredientes import MenuIngredientes
from ..enums.o_menu_principal import OMenuPrincipal

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
        
        while salir == False:
            Consola.limpiar_consola()
            if mostar_desarrollador == True:
                mostar_desarrollador = False
                print('-'*20 + 'DESARROLLADOR' + '-'*20)
                print('201222271 Axel Josué Esquivel Cuy')
            
            print('-'*20 + 'MENU PRINCIPAL' + '-'*20)
            print('{0}. {1}'.format(OMenuPrincipal.Ingredientes.value, OMenuPrincipal.Ingredientes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Pizzas.value, OMenuPrincipal.Pizzas.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Ordenes.value, OMenuPrincipal.Ordenes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Desarrollador.value, OMenuPrincipal.Desarrollador.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Salir.value, OMenuPrincipal.Salir.name.replace('_', ' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuPrincipal.Ingredientes.value):
                    MenuIngredientes(self.__ingredientes).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Pizzas.value):
                    MenuPizzas(self.__pizzas).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Ordenes.value):
                    MenuOrdenes(self.__ordenes).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Desarrollador.value):
                    mostar_desarrollador = True
                elif int(opcion) == int(OMenuPrincipal.Salir.value):
                    salir = True