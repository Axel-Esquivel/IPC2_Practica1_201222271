from ..enums.opciones_menu_principal import OpcionesMenuPrincipal

class MenuPrincipal:
    def mostrar_menu(self):
        salir = False
        
        while salir == False:
            print('-'*20 + 'MENU PRINCIPAL' + '-'*20)
            print('{0}. {1}'.format(OpcionesMenuPrincipal.Crear_Ingrediente.value, OpcionesMenuPrincipal.Crear_Ingrediente.name))