def greet_users(names):
    for name in names:
        msg = f"hello my friend {name.title()}"
        print(msg)
        
usernames = ['marie', 'sambinvi', 'kulwati' ]
greet_users(usernames)