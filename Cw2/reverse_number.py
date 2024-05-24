


for x in range(5,0,-1):
    string_num = ''

    for y in range(0,x):
        string_num += str(x) + ' '
        x -= 1

    print(string_num)