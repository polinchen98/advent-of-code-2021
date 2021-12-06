# part one

from collections import Counter
import numpy as np

binary_numbers = open('Day_3/input_3.txt', 'r')
binary_numbers_list = binary_numbers.read().splitlines()

matrix = []
for line in binary_numbers_list:
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

# # part two

gamma = binary_numbers_list[::]
for i in range(len(binary_numbers_list[0])):
    most = Counter([r[i] for r in gamma])
    most = '1' if most['1'] >= most['0'] else '0'
    gamma = list(filter(lambda x: x[i] == most, gamma))
    if len(gamma) == 1:
        break

epsilon = binary_numbers_list[::]
for i in range(len(binary_numbers_list[0])):
    least = Counter([r[i] for r in epsilon])
    least = '0' if least['1'] >= least['0'] else '1'
    epsilon = list(filter(lambda x: x[i] == least, epsilon))
    if len(epsilon) == 1:
        break

epsilon_rate = int(epsilon[0], 2)
gamma_rate = int(gamma[0], 2)
print(gamma_rate * epsilon_rate)  # 4267809
