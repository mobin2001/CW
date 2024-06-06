def counter(my_string):
    
    counter_upper = 0
    counter_lower = 0

    for letter in my_string:
        if letter.isupper():
            counter_upper += 1

        elif letter.islower():
            counter_lower += 1

    return counter_upper,counter_lower
    

string = input()

upper , lower = counter(string)

print(f'No. of Lower case characters : {lower}\nNo. of upper case characters : {upper}')