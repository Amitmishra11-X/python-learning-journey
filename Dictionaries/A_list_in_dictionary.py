pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"Your ordered {pizza['crust']}-crust pizza with following toppings:")

for topping in pizza['toppings']:
    print(topping)

