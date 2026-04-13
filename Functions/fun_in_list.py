def greet_users(names):
    for name in names:
        msg = f"hello my friend {name.title()}"
        print(msg)
        
usernames = ['marie', 'sambinvi', 'kulwati' ]
greet_users(usernames)

"""MODIFYING A LIST IN FUNCTION"""

unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model : {current_design}")
    completed_models.append(current_design)
print(f"\nthe following models have been printed : ")
for completed_model in completed_models:
    print(completed_model)
