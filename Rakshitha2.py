numbers = [4,5,2,9]
def square(number):
    return number**2
squared_numbers = list(map(square,numbers))
print("Original list of numbers:", numbers)
print("Square of list of numbers:", squared_numbers)
