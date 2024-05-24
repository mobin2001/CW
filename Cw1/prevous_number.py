previous_number = 0

for x in range(0,10):
    print('Current Number %i Previous Number %i Sum: %i' %(x,previous_number,x+previous_number))
    previous_number = x