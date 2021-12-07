import math
from collections import Counter

# part one

with open('input_7.txt') as data:
    positions = data.read().split(',')
    positions = [int(x) for x in positions]

counter_positions = {}
for i in range(len(positions)):
    counter_positions = Counter([position for position in positions])

print(counter_positions)

min_count = math.inf
for i in range(len(positions)):
    n = 0
    for key in counter_positions.keys():
        n += abs(key - i) * counter_positions[key]
    if n < min_count:
        min_count = n

print(min_count)  # 342534

# part two

min_count = math.inf
for i in range(len(positions)):
    n = 0
    for key in counter_positions.keys():
        plain_distance = abs(key - i)
        real_distance = int((plain_distance + 1) * plain_distance / 2)
        n += real_distance * counter_positions[key]
    if n < min_count:
        min_count = n

print(min_count)  # 94004208
