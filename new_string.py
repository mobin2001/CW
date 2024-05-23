string_1 = input()
string_2 = input()

string = string_2[0:2] + string_1[2:] + " " +  string_1[0:2] + string_2[2:]

print(string)