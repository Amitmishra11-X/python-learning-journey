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

    
