from math import dist
from itertools import product

a_range = 5000
house_gap = 10

num = 0
loop_range = range(-(a_range + house_gap), a_range + house_gap, house_gap)

for position in product(loop_range, loop_range):
    if dist(position, (0, 0)) <= a_range:
        num += 1

print(num)
