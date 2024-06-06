from functools import reduce

def multiply(numbers):

    return reduce(lambda x, y: x * y,numbers)

my_list = [8,3,7,-1,2]

multiply = multiply(my_list)

print(multiply)