list_of_ages = []

for x in range(0,3):
    age = int(input())
    list_of_ages.append(age)
list_of_ages.sort()
print(list_of_ages[0],list_of_ages[-1])
