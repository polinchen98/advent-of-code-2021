# part one

measurements = open('input_1.txt', 'r')
measurements_list = measurements.read().splitlines()

increases_1 = 0
for i in range(len(measurements_list) - 1):
    if measurements_list[i + 1] > measurements_list[i]:
        increases_1 += 1

result = increases_1 + 1
print(result)  # 1676

# part two

increases_2 = 0
window = 3
measurements_list = [int(x) for x in measurements_list]
for i in range(len(measurements_list) - window):
    previous_sum = measurements_list[i] + measurements_list[i+1] + measurements_list[i+2]
    now_sum = measurements_list[i+1] + measurements_list[i+2] + measurements_list[i+3]
    if now_sum > previous_sum:
        increases_2 += 1

print(result)  # 1706
