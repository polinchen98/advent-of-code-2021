with open('input_11.txt') as data:
    energy_levels = list(filter(lambda x: x != '', data.read().split('\n')))

energy_levels_str = []
for i in energy_levels:
    energy_levels_str.append(list(i))

energy_levels_int = []
for i in energy_levels_str:
    energy_levels_int.append([int(x) for x in i])

count = 0


def blast(blasted, array, i, j):
    global count
    if blasted[i][j]:
        return

    blasted[i][j] = True
    count += 1

    if j + 1 < len(array[i]):
        if not blasted[i][j + 1]:
            array[i][j + 1] += 1
            if array[i][j + 1] > 9:
                blast(blasted, array, i, j + 1)

    if j - 1 >= 0 and i - 1 >= 0:
        if not blasted[i - 1][j - 1]:
            array[i - 1][j - 1] += 1
            if array[i - 1][j - 1] > 9:
                blast(blasted, array, i-1, j-1)

    if i - 1 >= 0:
        if not blasted[i - 1][j]:
            array[i - 1][j] += 1
            if array[i - 1][j] > 9:
                blast(blasted, array, i-1, j)

    if i + 1 < len(array) and j + 1 < len(array[i]):
        if not blasted[i + 1][j + 1]:
            array[i + 1][j + 1] += 1
            if array[i + 1][j + 1] > 9:
                blast(blasted, array, i+1, j+1)

    if i - 1 >= 0 and j + 1 < len(array[i]):
        if not blasted[i - 1][j + 1]:
            array[i - 1][j + 1] += 1
            if array[i - 1][j + 1] > 9:
                blast(blasted, array, i-1, j+1)

    if i + 1 < len(array) and j - 1 >= 0:
        if not blasted[i + 1][j - 1]:
            array[i + 1][j - 1] += 1
            if array[i + 1][j - 1] > 9:
                blast(blasted, array, i+1, j - 1)

    if i + 1 < len(array):
        if not blasted[i + 1][j]:
            array[i + 1][j] += 1
            if array[i + 1][j] > 9:
                blast(blasted, array, i+1, j)

    if j - 1 >= 0:
        if not blasted[i][j - 1]:
            array[i][j - 1] += 1
            if array[i][j - 1] > 9:
                blast(blasted, array, i, j-1)


def all_blasted(blasted):
    for i in range(len(blasted)):
        for j in range(len(blasted)):
            if not blasted[i][j]:
                return False
    return True


blasted_times = 0
for a in range(300):
    blasted = [[False]*10 for i in range(10)]

    for i in range(len(energy_levels_int)):
        for j in range(len(energy_levels_int[i])):
            energy_levels_int[i][j] += 1

    for i in range(len(energy_levels_int)):
        for j in range(len(energy_levels_int[i])):
            if energy_levels_int[i][j] > 9:
                blast(blasted, energy_levels_int, i, j)

    for i in range(len(energy_levels_int)):
        for j in range(len(energy_levels_int[i])):
            if blasted[i][j]:
                energy_levels_int[i][j] = 0

    if all_blasted(blasted):
        print(a + 1)  # 256 - part two

print(count)  # 1649 - part one


