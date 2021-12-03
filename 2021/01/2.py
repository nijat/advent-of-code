list = [int(line) for line in open("input.txt").read().splitlines()]
print(sum(list[idx] + list[idx - 1] + list[idx - 2]> list[idx - 1] + list[idx - 2] + list[idx - 3]for idx, val in enumerate(list)))
