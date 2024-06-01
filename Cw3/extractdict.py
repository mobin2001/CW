sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"} 

keys = ["name", "salary"]

my_dict = {}

for item in keys:
    my_dict[item] = sample_dict[item]

print(my_dict)
