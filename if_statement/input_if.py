age = int(input("Enter your age: "))
print("Your age is", age)
if age >=18 :
    print("your are eligible for vote")
else:
    print("not eligible")
# checking whether a value Is not in a list
banned_user = ['suraj', 'shyam', 'devang', 'anukalp']
username = input('username :')
if username not in banned_user:
    print(f"{username.title()}, you can join our club")
else:
    print(f"{username.title()}, you can't join our club")