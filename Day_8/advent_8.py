# part one

with open('input_8.txt') as data:
    strings = data.read().split('\n')
    entry = [i.split(' | ') for i in strings]


letters = []
for i in range(len(entry)):
    for j in entry[i]:
        letters.append(j.split(' '))

count = 0
for word_list in letters:
    if len(word_list) == 4:
        for word in word_list:
            if len(word) == 7 or len(word) == 4 or len(word) == 3 or len(word) == 2:
                count += 1

print(count)  # 554

# part two

digits = {
    1: "cf",
    7: "acf",
    4: "bcdf",
    2: "acdeg",
    3: "acdfg",
    5: "abdfg",
    6: "abdefg",
    9: "abcdfg",
    0: "abcefg",
    8: "abcdefg",
}
