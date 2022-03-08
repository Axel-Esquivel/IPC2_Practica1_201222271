from ..enums.opciones_menu_principal import OpcionesMenuPrincipal

class MenuPrincipal:
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
                if int(opcion) == int(OpcionesMenuPrincipal.Salir.value):
                    salir = True