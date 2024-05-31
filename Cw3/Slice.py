sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

n = int(input())

chunk = int(len(sample_list) / n)

list_of_reversed = list()

new_list = list()

for i in range(0,len(sample_list),chunk):
    
    list_of_reversed = sample_list[i:i+chunk]
    list_of_reversed.reverse()
    print(list_of_reversed)
    