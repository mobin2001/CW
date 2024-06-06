def outer_function(number_1,number_2):
    
    def inner_function(x,y):
        return x+y
    answer = inner_function(number_1,number_2)
    return answer + 5

print(outer_function(5,10))
