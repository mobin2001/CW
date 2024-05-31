def tuple_to_dict (t):

    dictionary_of_tuple = dict()

    if len(t) % 2 == 0:

        for x in range(len(t)):

            if x % 2 == 0:
                dictionary_of_tuple[t[x]] = t[x+1]

    else:

        for x in range(len(t)-1):

            if x % 2 == 0:
                dictionary_of_tuple[t[x]] = t[x+1]

    return dictionary_of_tuple

my_tuple = (2, "Python", (3, 5), [2, "Python", (3, 5)],2,"Maktab")

test = tuple_to_dict(my_tuple)

print(test)