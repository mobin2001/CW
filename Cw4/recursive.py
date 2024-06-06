def recursive_function(count_number):
    if (count_number > 0):
        result = count_number + recursive_function(count_number - 1)
    else:
        result = 0
    return result

print(recursive_function(int(input())))