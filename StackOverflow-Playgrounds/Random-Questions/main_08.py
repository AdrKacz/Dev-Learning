from math import log

n = 6
swap_list = list()
for i in range(0, n + 1, 2): #Walk two by two, only even number can be power of 2
    power = 0
    if i == 0: #Handle particular case
        power = 0.5
    else:
        power = log(i) / log(2) # Calculate exponent
    if int(power) == power:
        swap_list.append(i + 1)
        swap_list.append(i)
    else:
        swap_list.append(i)
        swap_list.append(i + 1)

swap_list = swap_list[1:] #Remove 0
if swap_list[-1] == n + 1:
    swap_list = swap_list[:-1] # Remove the last odd number

print(swap_list)
