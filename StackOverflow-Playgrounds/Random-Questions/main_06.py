# Find the greatest product on a list: SPOIL => DOESN'T WORK ...

from random import random

my_list = [random() * 10 - 5] * 4

my_list_sorted = sorted(my_list)

my_product = list()

# Take the number greater than 1
i = 0
while i < len(my_list_sorted) and my_list_sorted[i] >= 1:
	my_product.append(my_list_sorted[i])
	i += 1

# Take the number smaller than -1
i = len(my_list_sorted)
while i > 0 and my_list_sorted[i - 1] <= -1:
	i -= 1
	my_product.append(my_list_sorted[i])

# Remove the last one (i.e the smaller) if the number of negative one is odd
if len(my_list_sorted) - i % 2 == 1:
	my_product.pop()

product = 1
for item in my_product:
	product *= item

print(product)

