"""the value the function returns is called return value"""
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
professor = get_formatted_name('Dr.Arjun', 'rai')
print(professor)
professor = get_formatted_name('Dr.Arjun', 'rai', 'patel')
print(professor)

""" RETURNING A DICTIONARY"""
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}    
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

"""Using a Function with a while loop """ """ infinite loop"""
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name
while True:
    print('\nplease tell me your name : ')
    f_name = input("First name:")
    l_name = input("last name:")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nhello {formatted_name}")
