# part one

positions = open('input2.txt', 'r')
positions_list = positions.read().splitlines()
position_dict = {'forward': 0, 'down': 0, 'up': 0}
for position in positions_list:
    for i in position.split():
        if i == 'forward':
            position_dict['forward'] += int(position.split()[1])
        elif i == 'down':
            position_dict['down'] += int(position.split()[1])
        elif i == 'up':
            position_dict['up'] += int(position.split()[1])

for key, value in position_dict.items():
    print(key, value)

depth = position_dict['down'] - position_dict['up']
answer = depth * position_dict['forward']

print(answer)  # 2091984

# part two

position_dict = {'forward': 0, 'down': 0, 'up': 0, 'aim': 0, 'depth': 0}
for position in positions_list:
    for i in position.split():
        if i == 'forward':
            position_dict['forward'] += int(position.split()[1])
            position_dict['depth'] += (int(position.split()[1]) * position_dict['aim'])
        elif i == 'down':
            position_dict['down'] += int(position.split()[1])
            position_dict['aim'] += int(position.split()[1])
        elif i == 'up':
            position_dict['up'] += int(position.split()[1])
            position_dict['aim'] -= int(position.split()[1])

for key, value in position_dict.items():
    print(key, value)

answer = position_dict['depth'] * position_dict['forward']
print(answer)  # 2086261056

