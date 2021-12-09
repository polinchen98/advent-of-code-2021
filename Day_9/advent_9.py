# part one

with open('input_9.txt') as data:
    points = list(filter(lambda x: x != '', data.read().split('\n')))

count = 0
for i in range(len(points)):
    for j in range(len(points[i])):
        if not ((j + 1 < len(points[i]) and points[i][j] >= points[i][j + 1]) \
                or (j - 1 >= 0 and points[i][j] >= points[i][j - 1])\
                or (i - 1 >= 0 and points[i][j] >= points[i - 1][j])
                or (i + 1 < len(points) and points[i][j] >= points[i + 1][j])):

            count += int(points[i][j]) + 1
print(count)
