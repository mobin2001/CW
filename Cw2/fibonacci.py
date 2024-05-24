first_number = 0
seccond_number = 1

number = int(input('please enter number: '))

fibo_list = [0, 1]

for i in range(number-2):
    
    new_number = first_number + seccond_number
    first_number = seccond_number
    seccond_number = new_number
    fibo_list.append(new_number)

print(fibo_list)
