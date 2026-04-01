banned_user = ['suraj', 'shyam', 'devang', 'anukalp']
username = input()
if username not in banned_user:
    print(f"{username.title()}, you can join our club")
else:
    print(f"{username.title()}, you can't join our club")