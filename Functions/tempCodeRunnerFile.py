
unprinted_designs = ['phone case', 'robot pendent', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model : {current_design}")
    completed_models.append(current_design)
print(f"\nthe following models have been printed : ")
for completed_model in completed_models:
    print(completed_model)
