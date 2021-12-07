with open('input_4.txt') as data:
    content = data.read().split("\n\n")[:~0]
    numbers = [int(x) for x in content[0].split(",")]
    array_with_numbers = list(map(lambda x: [list(map(int, m.strip(",").split(","))) for m in x],
                                  [x.replace("  "," 0").replace(' ',',').split("\n") for x in content[1:]]))


def full_string(array):
    for i in range(len(array)):
        count = 0
        for j in array[i]:
            if j != 0:
                count += 1
        if count == len(array[i]):
            return True
    return False


def full_col(array):
    for j in range(len(array[0])):
        count = 0
        for i in range(len(array)):
            if array[i][j] != 0:
                count += 1
        if count == len(array):
            return True
        return False


def summary_check(array):
    return full_col(array) or full_string(array)


def solve():
    zeros_array = [[[0 for k in range(len(array_with_numbers[0]))]
                    for j in range(len(array_with_numbers[0]))]
                   for i in range(len(array_with_numbers))]
    for num in numbers:
        for index_array, array in enumerate(array_with_numbers):
            for index_row, row in enumerate(array):
                for index_col, col in enumerate(row):
                    if num == col:
                        zeros_array[index_array][index_row][index_col] = col
                if summary_check(zeros_array[index_array]):
                    return num, zeros_array[index_array], array_with_numbers[index_array]

    return zeros_array


num, zeros_array, full_array = solve()
for i in range(len(zeros_array)):
    print(zeros_array[i])

summa = 0
for i in range(len(full_array)):
    for j in range(len(full_array[i])):
        if zeros_array[i][j] == 0:
            summa += full_array[i][j]
answer = summa * num
print(answer)  # 28082
