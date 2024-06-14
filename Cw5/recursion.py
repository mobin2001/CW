def fibonacci(number):
    if number == 0:
        return number + 0
    elif number == 1:
        return number + 
    return number + fibonacci(number -1)
n = 10


fib_number = fibonacci(n) 


print(f"The {n}th number of the Fibonacci sequence is: {fib_number}")