import operator
import functools

def multiply(numbers):

    print(functools.reduce(operator.mul,numbers))

list1 = [8,2,3,-1,7]

multiply(list1)