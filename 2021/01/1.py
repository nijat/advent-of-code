list_command = [int(line) for line in open("input.txt").read().splitlines()]
print(sum(val > list_command[idx-1] for idx, val in enumerate(list_command)))
