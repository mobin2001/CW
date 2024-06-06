def perfect_number(my_number):
    sum_divisor = 0
    for x in range(1,my_number):
        if my_number % x == 0:
            sum_divisor += x
    if sum_divisor == my_number:
        print("True")
    else:
        print('False')

perfect_number(int(input()))