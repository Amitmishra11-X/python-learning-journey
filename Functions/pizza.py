def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepproni')
make_pizza('mushroom', 'green peppers', 'extra chesse')

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza('pepproni')
make_pizza('mushroom', 'green peppers', 'extra chesse')

"""Mixing postional and Arbitrary Arguments"""

def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
    
make_pizza(16, 'pepproni')
make_pizza(12, 'mushroom', 'green peppers', 'extra chesse')