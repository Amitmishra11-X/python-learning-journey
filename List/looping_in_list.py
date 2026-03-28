magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#doing more work within a for a loop 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(f"{magician.title()}, thats was a great trick")

## Using the range() Function 
for value in range(1, 5):
    print(value)

## using range() make a list of a numbers
numbers = list(range(1, 6))
print(numbers)

## even numbers in list
for numbers in range(2, 11, 2):
    print(numbers)

## ----> Squares 
squares = []
for value in range(1, 10):
    square=value**2
    squares.append(square)
print(squares)

## list comperhensions 
sqaures =  [value**2 for value in range(1, 10)]
print(sqaures)
