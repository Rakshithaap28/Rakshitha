numbers = [1,2,3,4,5,6,7]
def triple(number):
    return number*3
tripled_numbers = list(map(triple,numbers))
print("Original list of numbers:", numbers)
print("Triple of list of numbers:", tripled_numbers)
