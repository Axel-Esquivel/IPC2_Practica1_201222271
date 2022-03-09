from ..listas.pizzas import Pizzas
from ..listas.ordenes import Ordenes
from ..componentes.consola import Consola
from ..listas.ingredientes import Ingredientes
from ..enums.o_menu_ordenes import OMenuOrdenes

class MenuOrdenes:
    __pizzas: Pizzas = None
    __ordenes: Ordenes = None
    
    def __init__(self, ordenes: Ordenes, pizzas: Pizzas):
        self.__pizzas = pizzas
        self.__ordenes = ordenes
    
    def mostrar_menu(self):
        volver = False
        
        while volver == False:
            Consola.limpiar_consola()
            print('-'*20 + 'MENU ORDENES'  + '-'*20)
            for orden in self.__ordenes:
                print('{}. {}'.format(orden.get_numero(), orden.get_cliente().get_nombre()))
            
            print('{}. {}'.format(OMenuOrdenes.Orden_Completa.value, OMenuOrdenes.Orden_Completa.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenes.CrearOrden.value, OMenuOrdenes.CrearOrden.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenes.Volver.value, OMenuOrdenes.Volver.name.replace('_', ' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuOrdenes.Orden_Completa.value):
                    self.__ordenes.desencolar()
                if int(opcion) == int(OMenuOrdenes.CrearOrden.value):
                    self.__crear_orden()
                elif int(opcion) == int(OMenuOrdenes.Volver.value):
                    volver = True
    
    def __crear_orden(self):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            