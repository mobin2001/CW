str1 = "PYnative"

my_str = ""

for x in range(len(str1)-1,-1,-1):

    my_str += str1[x]
    print(x,str1[x])

print(my_str)