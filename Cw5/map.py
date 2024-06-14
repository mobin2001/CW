def map_tuple(my_list):
    return my_list[0] + ' ' + my_list[1]








tuples_list = [('Hello', 'World'), ('Open', 'AI'), ('GPT', '3')]

maptuple = map(map_tuple,tuples_list)

print(list(maptuple))