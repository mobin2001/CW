def three_top(d):
    lits_of_items = list(d.items())
    lits_of_items.sort(key= lambda x:x[1],reverse= True)
    dict_of_top_three = dict()
    for x in range(3):
        dict_of_top_three[lits_of_items[x][0]] = lits_of_items[x][1]
    return dict_of_top_three

my_dict = {'T-shirt': 45.50, 'Pants': 35, 'Sneakers': 41.30, 'Hat': 55, 'Backpack': 24}

dict_top_three = three_top(my_dict)

print(dict_top_three)