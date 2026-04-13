def greet_user():
    """simple greet message."""
    print("hello")
greet_user()

def greet_user(username):
    print(f"hello, {username.title()}")
greet_user('jullia')

"""Positional Arguments"""

def describe_pet(animal_type, pet_name):
    print(f"\nI have {animal_type.title()}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('german shephard', 'tommy')
describe_pet('dog', 'tommy')