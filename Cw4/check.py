import string
import sys

def ispangram(my_str, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)

    str_set = set(my_str.lower())

    return alphaset <= str_set

my_string = input("please enter the string: ")

print(ispangram(my_string))