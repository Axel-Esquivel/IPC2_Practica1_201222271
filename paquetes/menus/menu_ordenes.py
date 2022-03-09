import random
from ..modelos.orden import Orden
from ..listas.pizzas import Pizzas
from ..listas.ordenes import Ordenes
from ..modelos.cliente import Cliente
from ..componentes.consola import Consola
from ..enums.o_menu_ordenes import OMenuOrdenes
from ..enums.o_menu_orden_crear import OMenuOrdenCrear

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
            
            if self.__ordenes.contar() > 0:
                for orden in self.__ordenes:
                    print('{}. \t{} {} minutos'.format(orden.get_numero(), orden.get_cliente().get_nombre()))
            else:
                print('No hay pedidos.')
            
            print('\n{}. {}'.format(OMenuOrdenes.Orden_Completa.value, OMenuOrdenes.Orden_Completa.name.replace('_', ' ')))
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
        orden = Orden()
        cliente = Cliente()
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'DATOS ORDEN' + '-'*20)
            print('Cliente: {}'.format(cliente.get_nombre()))
            print('Dirección: {}'.format(cliente.get_direccion()))
            print('NIT: {}'.format(cliente.get_NIT()))
            print('Pizzas: {}'.format(orden.get_pizzas().contar()))
            
            print('-'*20 + 'CREAR ORDEN' + '-'*20)
            print('{}. {}'.format(OMenuOrdenCrear.Nombre.value, OMenuOrdenCrear.Nombre.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.Direccion.value, OMenuOrdenCrear.Direccion.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.NIT.value, OMenuOrdenCrear.NIT.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.Agregar_Pizzas.value, OMenuOrdenCrear.Agregar_Pizzas.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.Eliminar_Pizzas.value, OMenuOrdenCrear.Eliminar_Pizzas.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.Guardar.value, OMenuOrdenCrear.Guardar.name.replace('_', ' ')))
            print('{}. {}'.format(OMenuOrdenCrear.Cancelar.value, OMenuOrdenCrear.Cancelar.name.replace('_', ' ')))
            
            print('Ingrese en número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuOrdenCrear.Nombre.value):
                    Consola.limpiar_consola()
                    print('Ingrese el nombre del cliente:')
                    nombre = input()
                    
                    if nombre != '': cliente.set_nombre(nombre)
                elif int(opcion) == int(OMenuOrdenCrear.Direccion.value):
                    Consola.limpiar_consola()
                    print('Ingrese la direccion del cliente:')
                    direccion = input()
                    
                    if direccion != '': cliente.set_direccion(direccion)
                elif int(opcion) == int(OMenuOrdenCrear.NIT.value):
                    Consola.limpiar_consola()
                    print('Ingrese el NIT del cliente:')
                    NIT = input()
                    
                    if NIT != '': cliente.set_NIT(NIT)
                elif int(opcion) == int(OMenuOrdenCrear.Agregar_Pizzas.value):
                    self.__agregar_pizza_orden(orden)
                elif int(opcion) == int(OMenuOrdenCrear.Eliminar_Pizzas.value):
                    self.__eliminar_pizza_orden(orden)
                elif int(opcion) == int(OMenuOrdenCrear.Guardar.value):
                    if cliente.get_nombre() != None and cliente.get_NIT() != None: orden.set_cliente(cliente)
                    
                    if orden.get_cliente() != None and orden.get_pizzas().contar() > 0:
                        salir = True
                        orden.set_numero(random.randint(1, 1000))
                        self.__ordenes.encolar(orden)
                    
                elif int(opcion) == int(OMenuOrdenCrear.Cancelar.value):
                    salir = True

    def __agregar_pizza_orden(self, orden: Orden):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            contador = 0
            for pizza in self.__pizzas:
                contador += 1
                if not orden.get_pizzas().existe(pizza):
                    print('{}. {}'.format(contador, pizza.get_nombre()))
                    
            print('{}. Cancelar'.format(contador + 1))
            
            print('Ingrese el número de la pizza que desea agregar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion)>=1 and int(opcion)<= contador:
                    orden.get_pizzas().agregar(self.__pizzas.elemento(int(opcion) - 1))
                elif int(opcion) == contador + 1:
                    salir = True
        
    def __eliminar_pizza_orden(self, orden: Orden):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'ELIMINAR PIZZA DE ORDEN' + '-'*20)
            contador = 0
            for pizza in orden.get_pizzas():
                contador += 1
                print('{}. {}'.format(contador, pizza.get_nombre()))
                
            print('{}. Volver'.format(contador + 1))
            
            print('Ingrese el número de la pizza que desea eliminar de la orden:')
            opcion = input()
            
            if opcion.isnumeric():
                if orden.get_pizzas().contar() > 0 and int(opcion) >= 1 and int(opcion) <= contador:
                    orden.get_pizzas().eliminar_indice(int(opcion) - 1)
                elif int(opcion) == contador + 1:
                    salir = True