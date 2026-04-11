#shifting things from ine list to another
unregesterd = ['rahul', 'karthik', 'rj']
registered = []
while unregesterd :
    reg = unregesterd.pop()
    print(f"verfied : {reg.title()}")
    registered.append(reg)
print("following : ")
for st in registered: 
    print(st)
