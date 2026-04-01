age =12
if age < 4:
    price = 0
elif age < 18 :
    price = 25
elif age < 65 :
    price = 40 
else :
    price = 20
print(f"your admission cost is ${price}")

#the if-elif-else appropriate to use when you just need one test to pass. As soon as python finds one test,
#it skips the rest of the test.This behviour is beneficial, because it's efficient and allows you to test for one specific condition. 
# ifff we need to check all conditions then apply if-if-if 
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 
