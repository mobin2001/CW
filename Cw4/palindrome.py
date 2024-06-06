def palindrome(my_string):

    palindrom_string = string.replace(" ", "")[::-1]
    
    return palindrom_string

string = input().lower()

palindrom_string = palindrome(string)

if palindrom_string == string:
    print('Yes')
else:
    print('No')