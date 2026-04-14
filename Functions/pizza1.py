def pizza_make(size, *toppings):
    print(f"{size}'s pizza with toppings : ")
    for topping in toppings:
        print(f"-{topping}")