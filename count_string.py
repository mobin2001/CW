def find_digits_chars_symbols(a):
    letters = 0
    digits = 0
    symbols = 0
    for i in a:
        if "A"<=i <= "z" :
            letters += 1

        elif "0"<=i <= "9":
            digits +=1

        else:
            symbols += 1
            
    print("Letters=",letters)
    print("Digits=",digits)
    print("Symbols=",symbols)

s1 = 'p@#yn26at^&i5ve'
find_digits_chars_symbols(s1)