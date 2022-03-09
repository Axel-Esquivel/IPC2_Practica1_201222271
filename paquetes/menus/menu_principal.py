import datetime
from ..modelos.orden import Orden
from ..listas.pizzas import Pizzas
from .menu_pizzas import MenuPizzas
from ..listas.ordenes import Ordenes
from .menu_ordenes import MenuOrdenes
from ..componentes.consola import Consola
from ..listas.ingredientes import Ingredientes
from .menu_ingredientes import MenuIngredientes
from ..enums.o_menu_principal import OMenuPrincipal
from ..componentes.valores_predeterminados import ValoresPredeterminados

class MenuPrincipal:
    __pizzas: Pizzas = None
    __ordenes: Ordenes = None
    __historico_ordenes: Ordenes = None
    __ingredientes: Ingredientes = None
        
    def __init__(self):
        self.__pizzas = Pizzas()
        self.__ordenes = Ordenes()
        self.__historico_ordenes = Ordenes()
        self.__ingredientes = Ingredientes()
        ValoresPredeterminados(self.__ingredientes, self.__pizzas)
    
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
            print('{0}. {1}'.format(OMenuPrincipal.Historico_Ordenes.value, OMenuPrincipal.Historico_Ordenes.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Desarrollador.value, OMenuPrincipal.Desarrollador.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPrincipal.Salir.value, OMenuPrincipal.Salir.name.replace('_', ' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuPrincipal.Ingredientes.value):
                    MenuIngredientes(self.__ingredientes).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Pizzas.value):
                    MenuPizzas(self.__pizzas, self.__ingredientes).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Ordenes.value):
                    MenuOrdenes(self.__ordenes, self.__pizzas, self.__historico_ordenes).mostrar_menu()
                elif int(opcion) == int(OMenuPrincipal.Historico_Ordenes.value):
                    self.__mostrar_historico()
                elif int(opcion) == int(OMenuPrincipal.Desarrollador.value):
                    mostar_desarrollador = True
                elif int(opcion) == int(OMenuPrincipal.Salir.value):
                    salir = True
                    
    def __mostrar_historico(self):
        Consola.limpiar_consola()
        print('-'*20 + 'HISTORICO DE ORDENES' + '-'*20)
        
        orden: Orden
        for orden in self.__historico_ordenes:
            delta_tiempo = (orden.get_hora_entrega() - orden.get_hora_pedido()) + datetime.timedelta(minutes = orden.get_tiempo_preparacion())
            print('-'*20 + 'Código {}'.format(orden.get_numero()) + '-'*20)
            
            print('Cliente: {}'.format(orden.get_cliente().get_nombre()))
            print('Pizzas: {}'.format(orden.get_total_pizzas()))
            for pizza in orden.get_pizzas():
                print('  Pizza: {} de {} - {} min'.format(pizza.get_cantidad() ,pizza.get_nombre(), pizza.get_tiempo_preparacion()))
                for ingrediente in pizza.get_ingredientes():
                    print('    Ingredinete: {} - {} min'.format(ingrediente.get_nombre(), ingrediente.get_tiempo_preparacion()))
            print('Pedido: {}'.format(orden.get_hora_pedido().strftime('%H:%M:%S')))
            print('Entregado: {}'.format(orden.get_hora_entrega().strftime('%H:%M:%S')))
            print('Tiempo preparación: {} minutos'.format(orden.get_tiempo_preparacion()))
            print('Tiempo total: {}'.format(delta_tiempo))
        
        print('\nPresione la tecla Enter para volver')
        input()