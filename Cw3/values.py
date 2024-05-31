speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

set_of_speed_values = set(speed.values())

print(list(set_of_speed_values))

for key,value in speed.items():
    print("{}\"***\"{}".format(key,value))

