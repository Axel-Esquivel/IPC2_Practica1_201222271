from paquetes.modelos.pizza import Pizza
from paquetes.listas.pizzas import Pizzas
from paquetes.modelos.ingrediente import Ingrediente
from paquetes.listas.ingredientes import Ingredientes

def main():
    ingredientes = Ingredientes()
    ingredientes.agregar(Ingrediente('Pepperoni', 3))
    ingredientes.agregar(Ingrediente('Salchicha', 4))
    ingredientes.agregar(Ingrediente('Carne', 10))
    ingredientes.agregar(Ingrediente('Queso', 5))
    ingredientes.agregar(Ingrediente('Piña', 2))
    
    pizzas = Pizzas()
    pizzas.agregar(Pizza('Mixta pequeña', 45, 4, ingredientes))
    pizzas.agregar(Pizza('Mixta mediana', 90, 5, ingredientes))
    pizzas.agregar(Pizza('Mixta grande', 120, 2, ingredientes))
    print(pizzas.contar())
    
    for pizza in pizzas:
        print(pizza.get_nombre(), pizza.get_cantidad() * pizza.get_precio(), pizza.get_ingredientes())
    

if __name__ == '__main__':
    main()