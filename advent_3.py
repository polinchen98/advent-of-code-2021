# part one

from collections import Counter
import numpy as np

binary_numbers = open('input_3.txt', 'r')
binary_numbers_list = binary_numbers.read().splitlines()


matrix = []
for line in binary_numbers_list:
    length = len(binary_numbers_list)
    matrix.append([int(x) for x in line])

gamma_rate = []
epsilon_rate = []
matrix = np.array(matrix)
matrix = matrix.swapaxes(0, 1)
for i in matrix:
    counter = Counter(i)
    values = list(counter.values())
    keys = list(counter.keys())
    if counter[0] > counter[1]:
        gamma_rate.append(0)
        epsilon_rate.append(1)
    else:
        gamma_rate.append(1)
        epsilon_rate.append(0)

gamma_rate = [str(x) for x in gamma_rate]
gamma_rate = ''.join(gamma_rate)
gamma_rate_binary = 0
for i, bit in enumerate(gamma_rate[::-1]):
    n = 2 ** i * int(bit)
    gamma_rate_binary += n

print(gamma_rate_binary)  # 2520

epsilon_rate = [str(x) for x in epsilon_rate]
epsilon_rate = ''.join(epsilon_rate)
epsilon_rate_binary = 0
for i, bit in enumerate(epsilon_rate[::-1]):
    n = 2 ** i * int(bit)
    epsilon_rate_binary += n

print(epsilon_rate_binary)  # 1575

power_consumption = gamma_rate_binary * epsilon_rate_binary
print(power_consumption)  # 3969000


# part two

counter_1 = {}
rev_matrix = matrix.swapaxes(1, 0)
count = []
for array in rev_matrix:
    count.append(array[0])
    counter_1 = Counter(count)


