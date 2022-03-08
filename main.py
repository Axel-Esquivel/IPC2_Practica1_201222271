from paquetes.modelos.ingrediente import Ingrediente
from paquetes.listas.ingredientes import Ingredientes

def main():
    ingredientes = Ingredientes()
    ingredientes.agregar(Ingrediente('Pepperoni', 3))
    ingredientes.agregar(Ingrediente('Salchicha', 4))
    ingredientes.agregar(Ingrediente('Carne', 10))
    ingredientes.agregar(Ingrediente('Queso', 5))
    ingredientes.agregar(Ingrediente('Piña', 2))
    
    for ingrediente in ingredientes:
        print(ingrediente.get_nombre(), ingrediente.get_tiempo())
    print(ingredientes.elementos())
    
    ingredientes.eliminar_indice(1)
    
    for ingrediente in ingredientes:
        print(ingrediente.get_nombre(), ingrediente.get_tiempo())
    print(ingredientes.elementos())

if __name__ == '__main__':
    main()