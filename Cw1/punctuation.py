import string
 
my_string = input()
 
test_str = my_string.translate(str.maketrans('', '', string.punctuation))
print(test_str)