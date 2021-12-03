command_list = map(lambda val: val.split(" "), open("input.txt").read().splitlines())
horizontal = depth = aim = 0
for command, instruction in command_list:
    if command == "down":
        aim += int(instruction)
    elif command == "up":
        aim -= int(instruction)
    else:
        horizontal += int(instruction)
        depth += aim * int(instruction)
print(horizontal * depth)
