command_list = map(lambda val: val.split(" "), open("input.txt").read().splitlines())
pos = [0, 0, 0]
for command, instruction in command_list:
    pos[len(command) / 2 - 1] += int(instruction)
print((pos[1] - pos[0]) * pos[2])