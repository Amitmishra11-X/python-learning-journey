current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "\nplese enter the nsme of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt).strip().lower()
    if city == 'quit':
        break
    else:
        print(f"I'd love to go {city.title()}")


## continue keyword used as skip
current_count = 0 
while current_count < 10:
    current_count += 1
    if current_count % 2 == 0:
        continue
    else:
        print(current_count)
    