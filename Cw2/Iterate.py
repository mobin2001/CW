list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
my_list = zip(list1, list2)

a = zip(list1, list2)

for items in my_list:
    print(items[0], items[1])