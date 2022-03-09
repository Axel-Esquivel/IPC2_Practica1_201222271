from ..componentes.consola import Consola
from ..modelos.ingrediente import Ingrediente
from ..listas.ingredientes import Ingredientes
from ..enums.o_menu_ingredientes import OMenuIngredientes
from ..enums.o_menu_ingredientes_crear import OMenuIngredientesCrear

class MenuIngredientes:
    __ingredientes: Ingredientes = None
    
    def __init__(self, ingredientes: Ingredientes):
        self.__ingredientes = ingredientes
    
    def mostrar_menu(self):
        volver = False
        
        while volver == False:
            Consola.limpiar_consola()
            print('-'*20 + 'INGREDIENTES ACTUALES' + '-'*20)
            contador = 0
            for ingrediente in self.__ingredientes:
                contador += 1
                print('{0}. {1}'.format(contador, ingrediente.get_nombre()))
                
            print('-'*20 + 'MENU INGREDIENTES' + '-'*20)
            print('{0}. {1}'.format(OMenuIngredientes.Crear_Ingrediente.value, OMenuIngredientes.Crear_Ingrediente.name.replace('_',' ')))
            print('{0}. {1}'.format(OMenuIngredientes.Eliminar_Ingrediente.value, OMenuIngredientes.Eliminar_Ingrediente.name.replace('_',' ')))
            print('{0}. {1}'.format(OMenuIngredientes.Volver.value, OMenuIngredientes.Volver.name.replace('_',' ')))
            
            print('Ingrese el número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuIngredientes.Crear_Ingrediente.value):
                    self.__crear_ingrediente()
                elif int(opcion) == int(OMenuIngredientes.Eliminar_Ingrediente.value):
                    self.__eliminar_ingrediente()
                elif int(opcion) == int(OMenuIngredientes.Volver.value):
                    volver = True
                    
    def __crear_ingrediente(self):
        salir = False
        ingrediente = Ingrediente()
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'INGREDIENTE' + '-'*20)
            print('Nombre: {}'.format(ingrediente.get_nombre()))
            print('Tiempo preparación: {} minutos'.format(ingrediente.get_tiempo_preparacion()))
            
            print('-'*20 + 'CREAR INGREDIENTE' + '-'*20)
            print('{0}. {1}'.format(OMenuIngredientesCrear.Nombre.value, OMenuIngredientesCrear.Nombre.name.replace('_',' ')))
            print('{0}. {1}'.format(OMenuIngredientesCrear.Tiempo_Preparacion.value, OMenuIngredientesCrear.Tiempo_Preparacion.name.replace('_',' ')))
            print('{0}. {1}'.format(OMenuIngredientesCrear.Guardar.value, OMenuIngredientesCrear.Guardar.name.replace('_',' ')))
            print('{0}. {1}'.format(OMenuIngredientesCrear.Cancelar.value, OMenuIngredientesCrear.Cancelar.name.replace('_',' ')))
            
            print('Ingrese en número de la opción que desea seleccionar:')
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) == int(OMenuIngredientesCrear.Nombre.value):
                    Consola.limpiar_consola()
                    print('Ingrese el nombre del ingrediente:')
                    nombre = input()
                    
                    if nombre != '': ingrediente.set_nombre(nombre)
                if int(opcion) == int(OMenuIngredientesCrear.Tiempo_Preparacion.value):
                    Consola.limpiar_consola()
                    print('Ingrese el tiempo de preparación en minutos:')
                    tiempo_preparacion = input()
                    
                    if tiempo_preparacion != '' and tiempo_preparacion.isnumeric(): ingrediente.set_tiempo_preparacion(tiempo_preparacion)
                elif int(opcion) == int(OMenuIngredientesCrear.Guardar.value):
                    if ingrediente.get_nombre() != None and ingrediente.get_tiempo_preparacion() != None:
                        salir = True
                        self.__ingredientes.agregar(ingrediente)
                elif int(opcion) == int(OMenuIngredientesCrear.Cancelar.value):
                    salir = True
                
    def __eliminar_ingrediente(self):
        salir = False
        
        while salir == False:
            Consola.limpiar_consola()
            print('-'*20 + 'INGREDIENTES ACTUALES' + '-'*20)
            contador = 0
            for ingrediente in self.__ingredientes:
                contador += 1
                print('{0}. {1}'.format(contador, ingrediente.get_nombre()))
                
            print('\n{}. Cancelar'.format(contador + 1))
            
            print('Ingrese el número del ingrediente que desea eliminar o {0} para Cancelar:'.format(contador + 1))
            opcion = input()
            
            if opcion.isnumeric():
                if int(opcion) >= 1 and int(opcion) <= self.__ingredientes.contar():
                    salir = True
                    self.__ingredientes.eliminar_indice(int(opcion) - 1)
                if int(opcion) == contador + 1:
                    salir = True