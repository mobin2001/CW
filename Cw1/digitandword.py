l=[i for i in input().split()]

a=[]

for i in l:

    if(any(c.isalpha() for c in i) and any(c.isdigit() for c in i)):

        a.append(i)

for item in a:
    print(item)