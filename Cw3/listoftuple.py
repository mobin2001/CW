def list_of_tuple(list_1,list_2):
    list_1.sort()
    list_2.sort(reverse = True)
    list_of_tupels = list()


    for x in range(len(list_2)):
        list_of_tupels.append((list_1[x],list_2[x]))
    return list_of_tupels


lst1 = ["Mike", "Danny", "Jim", "Annie"]
lst2 = [4, 12, 7, 19]

print(list_of_tuple(lst1,lst2))