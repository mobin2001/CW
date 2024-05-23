string_1 = input()
string_2 = input()

string = string_2[0:2] + string_1[-1] + " " +  string_1[0:2] + string_2[-1]

print(string)