my_list = [120, 230, 30, 40, 45, 75, 93, 100]

for item in my_list:
    if item <= 100 and item % 2 == 0:
        print(f'there is a {item} at index no: {my_list.index(item)}')