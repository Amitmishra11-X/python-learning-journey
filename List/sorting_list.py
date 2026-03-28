## sorting list technique
Cars=['BMW', 'honda', 'tata', 'mercedes', 'mahendira']
Cars.sort()
print(Cars)
##sorting reverse 
Cars=['BMW', 'honda', 'tata', 'mercedes', 'mahendira']
Cars.sort(reverse=True)
print(Cars)
## thats all are temporary sorted order 
print("\nHere is the original list: ")
print(Cars)
## Parmently changes in list 
# printing list in reverse oerder parmanet 
CarsNew=['bmw', 'audi', 'toyota', 'subaru']
CarsNew.reverse()
print(CarsNew)
#The reverse() method changes the order of a list paremanently, but you can revert to the original order anytime by applying reverse() to the same list a second
##-->>>> Notice that reverse() doesn't sort backward alphabatically; it simply revsrse the order of the list:

##Finding the length of a list 
Cars=['bmw', 'audi', 'toyota', 'subaru']
len(Cars)
