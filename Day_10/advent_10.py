# part one

with open('input_10.txt') as data:
    navigation_subsystem = data.read().split('\n')


def find_not_match(text):
    dict_matches = {')': '(',
                    ']': '[',
                    '}': '{',
                    '>': '<'}
    stack = []
    not_match = ''
    for letter in text:
        if letter in dict_matches:
            if dict_matches[letter] != stack.pop():
                not_match += letter
        else:
            stack.append(letter)
    return not_match


def scoring_1(array):
    points = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}
    sum_score = 0
    for letter in array:
        sum_score += points[letter]
    return sum_score


result = []
[result.append(find_not_match(navigation_subsystem[i])) for i in range(len(navigation_subsystem))]

result = list(filter(lambda x: x != '', result))
print(scoring_1(result))  # 193275


# part two


def find_closed(text):
    dict_matches = {')': '(',
                    ']': '[',
                    '}': '{',
                    '>': '<'}
    stack = []
    for letter in text:
        if letter in dict_matches:
            if dict_matches[letter] != stack.pop():
                return False, letter
        else:
            stack.append(letter)
    return True, stack


for string in navigation_subsystem:
    points = {')': 1,
              ']': 2,
              '}': 3,
              '>': 4}
    scores = []
    valid, remaining = find_closed(string)
    if valid:
        scores.append(0)
        while remaining:
            scores[-1] = scores[-1] * 5 + points[remaining.pop()]
    print(sorted(scores)[len(scores) // 2])
