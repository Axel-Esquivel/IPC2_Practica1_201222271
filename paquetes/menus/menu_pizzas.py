from ..modelos.pizza import Pizza
from ..listas.pizzas import Pizzas
from ..componentes.consola import Consola
from ..enums.o_menu_pizzas import OMenuPizzas
from ..listas.ingredientes import Ingredientes
from ..enums.o_menu_pizzas_crear import OMenuPizzasCrear
from ..enums.o_menu_pizzas_datos import OMenuPizzasDatos

class MenuPizzas:
    __pizzas: Pizzas = None
    __ingredientes: Ingredientes = None
    
    def __init__(self, pizzas: Pizzas, ingredientes: Ingredientes):
        self.__pizzas = pizzas
        self.__ingredientes = ingredientes
    
    def mostrar_menu(self):
        volver = False
        
        while volver == False:
            Consola.limpiar_consola()
            print('-'*20 + 'PIZZAS ACTUALES' + '-'*20)
            contador = 0
            for pizza in self.__pizzas:
                contador += 1
                print('{0}. {1}'.format(contador, pizza.get_nombre()))
            
            print('-'*20 + 'PIZZAS' + '-'*20)
            print('{0}. {1}'.format(OMenuPizzas.Crear_Pizza.value, OMenuPizzas.Crear_Pizza.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzas.Modificar_Pizza.value, OMenuPizzas.Modificar_Pizza.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzas.Eliminar_Pizza.value, OMenuPizzas.Eliminar_Pizza.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzas.Volver.value, OMenuPizzas.Volver.name.replace('_', ' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuPizzas.Crear_Pizza.value):
                    self.__crear_pizza()
                elif int(opcion) == int(OMenuPizzas.Eliminar_Pizza.value):
                    self.__eliminar_pizza()
                elif int(opcion) == int(OMenuPizzas.Modificar_Pizza.value):
                    self.__modificar_pizza()
                elif int(opcion) == int(OMenuPizzas.Volver.value):
                    volver = True
    
    def __crear_pizza(self):
        salir = False
        pizza = Pizza()
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'PIZZA' + '-'*20)
            print('Nombre: {0}'.format(pizza.get_nombre()))
            print('Precio: {0}'.format(pizza.get_precio()))
            
            print('-'*20 + 'CREAR PIZZA' + '-'*20)
            print('{0}. {1}'.format(OMenuPizzasCrear.Nombre.value, OMenuPizzasCrear.Nombre.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzasCrear.Precio.value, OMenuPizzasCrear.Precio.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzasCrear.Guardar.value, OMenuPizzasCrear.Guardar.name.replace('_', ' ')))
            print('{0}. {1}'.format(OMenuPizzasCrear.Cancelar.value, OMenuPizzasCrear.Cancelar.name.replace('_', ' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuPizzasCrear.Nombre.value):
                    Consola.limpiar_consola()
                    print('Ingrese el nombre de la pizza:')
                    nombre = input()
                    
                    if nombre != '': pizza.set_nombre(nombre)
                elif int(opcion) == int(OMenuPizzasCrear.Precio.value):
                    Consola.limpiar_consola()
                    print('Ingrese el precio de la pizza:')
                    precio = input()
                    
                    if precio != '' and precio.isnumeric(): pizza.set_precio(precio)
                elif int(opcion) == int(OMenuPizzasCrear.Guardar.value):
                    if pizza.get_nombre() != None and pizza.get_precio() != None:
                        salir = True
                        self.__pizzas.agregar(pizza)
                elif int(opcion) == int(OMenuPizzasCrear.Cancelar.value):
                    salir = True
        
    def __eliminar_pizza(self):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'ELIMINAR PIZZA' + '-'*20)
            contador = 0
            for pizza in self.__pizzas:
                contador +=1
                print('{0}. {1}'.format(contador, pizza.get_nombre()))
                
            print('{0}. Cancelar'.format(contador + 1))
            
            print('Ingrese el numero de la pizza que desea eliminar o {0} para Cancelar'.format(contador + 1))
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) >= 1 and int(opcion) <= self.__pizzas.contar():
                    salir = True
                    self.__pizzas.eliminar_indice(int(opcion) - 1)
                elif int(opcion) == int(contador + 1):
                    salir = True
        
    def __modificar_pizza(self):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'MODIFICAR PIZZA' + '-'*20)
            contador = 0
            for pizza in self.__pizzas:
                contador += 1
                print('{}. {}'.format(contador, pizza.get_nombre()))
                
            print('{0}. Cancelar'.format(contador + 1))
            
            print('Ingrese el numero de la pizza que desea modificar o {0} para Cancelar'.format(contador + 1))
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) >= 1 and int(opcion) <= self.__pizzas.contar():
                    self.__cambiar_datos_pizza(int(opcion))
                elif int(opcion) == contador + 1:
                    salir = True
                    
    def __cambiar_datos_pizza(self, indice_pizza: int):
        salir = False
        pizza = self.__pizzas.elemento(indice_pizza - 1)
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'PIZZA' + '-'*20)
            print('Nombre: {}'.format(pizza.get_nombre()))
            print('Precio: {}'.format(pizza.get_precio()))
            
            print('-'*20 + 'DATOS PIZZA' + '-'*20)
            print('{}. {}'.format(OMenuPizzasDatos.Nombre.value, OMenuPizzasDatos.Nombre.name))
            print('{}. {}'.format(OMenuPizzasDatos.Precio.value, OMenuPizzasDatos.Precio.name))
            print('{}. {}'.format(OMenuPizzasDatos.Agregar_Ingrediente.value, OMenuPizzasDatos.Agregar_Ingrediente.name))
            print('{}. {}'.format(OMenuPizzasDatos.Eliminar_Ingrediente.value, OMenuPizzasDatos.Eliminar_Ingrediente.name))
            print('{}. {}'.format(OMenuPizzasDatos.Cancelar.value, OMenuPizzasDatos.Cancelar.name))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuPizzasDatos.Nombre.value):
                    Consola.limpiar_consola()
                    print('Ingrese el nuevo nombre de la pizza:')
                    nombre = input()
                    
                    if nombre != '': pizza.set_nombre(nombre)
                elif int(opcion) == int(OMenuPizzasDatos.Precio.value):
                    Consola.limpiar_consola()
                    print('Ingrese el nuevo precio de la pizza:')
                    precio = input()
                    
                    if precio != '' and precio.isnumeric(): pizza.set_precio(precio)
                elif int(opcion) == int(OMenuPizzasDatos.Agregar_Ingrediente.value):
                    self.__agregar_ingrediente_pizza(indice_pizza)
                elif int(opcion) == int(OMenuPizzasDatos.Eliminar_Ingrediente.value):
                    self.__eliminar_ingrediente_pizza(indice_pizza)
                elif int(opcion) == int(OMenuPizzasDatos.Cancelar.value):
                    salir = True
                    
    def __agregar_ingrediente_pizza(self, indice_pizza: int):
        salir = False
        pizza = self.__pizzas.elemento(indice_pizza - 1)
        ingredientes_pizza = pizza.get_ingredientes()
        
        while salir == False:
            print('-'*20 + 'AGREGAR INGREDIENTE A PIZZA' + '-'*20)
            contador = 0
            for ingrediente in self.__ingredientes:
                contador += 1
                if not ingredientes_pizza.existe(ingrediente):
                    print('{}. {}'.format(contador, ingrediente.get_nombre()))
            
            print('{}. Cancelar'.format(contador + 1))
            
            print('Ingrese el número del ingrediente que desea agregar a la pizza o {} para cancelar:'.format(contador + 1))
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) >= 1 and int(opcion) <= contador:
                    pizza.get_ingredientes().agregar(self.__ingredientes.elemento(int(opcion) - 1))
                elif int(opcion) == contador + 1:
                    salir = True
        
    def __eliminar_ingrediente_pizza(self, indice_pizza: int):
        salir = False
        pizza = self.__pizzas.elemento(indice_pizza - 1)
        
        while salir == False:
            print('-'*20 + 'ELIMINAR INGREDIENTE A PIZZA' + '-'*20)
            contador = 0
            for ingrediente in pizza.get_ingredientes():
                contador += 1
                print('{}. {}'.format(contador, ingrediente.get_nombre()))
                
            print('{}. Cancelar'.format(contador + 1))
            
            print('Ingrese el número del ingrediente que desea eliminar de la pizza o {} para cancelar:'.format(contador + 1))
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) >= 1 and int(opcion) <= contador:
                    pizza.get_ingredientes().eliminar_indice(int(opcion) - 1)
                elif int(opcion) == contador + 1:
                    salir = True