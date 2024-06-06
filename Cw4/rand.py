import random


range_numbers = int(input())
range_numbers_2 = int(input())
count_number = int(input())

print(random.sample(range(range_numbers,range_numbers_2),count_number))