from collections import defaultdict
from utils import *

with open("input.txt", "r") as file:
    data = file.read()


@test(17)
def part1(data):
    point_lines, instructions = data.strip().split("\n\n")
    # data = list(map(int, data))
    points = defaultdict(int)
    for line in point_lines.split("\n"):
        x, y = line.strip().split(",")
        points[(int(x), int(y))] = 1

    for instruction in instructions.split("\n"):
        max_x = max(points, key=lambda x: x[0])[0] + 1
        max_y = max(points, key=lambda x: x[1])[1] + 1

        instruction = instruction.strip().split(' ')[-1]
        axis, i = instruction.split('=')
        i = int(i)
        # print(axis, i)
        if axis == "x":
            for a, b in zip(range(i, -1, -1), range(i, max_x)):
                for y in range(max_y):
                    points[(a, y)] += points[(b, y)]
                    del points[(b, y)]
        else:
            for a, b in zip(range(i, -1, -1), range(i, max_y)):
                for x in range(max_x):
                    points[(x, a)] += points[(x, b)]
                    del points[(x, b)]
        break
    return sum(1 for value in points.values() if value)



@test()
def part2(data):
    point_lines, instructions = data.strip().split("\n\n")
    # data = list(map(int, data))
    points = defaultdict(int)
    for line in point_lines.split("\n"):
        x, y = line.strip().split(",")
        points[(int(x), int(y))] = 1

    for instruction in instructions.split("\n"):
        max_x = max(points, key=lambda x: x[0])[0] + 1
        max_y = max(points, key=lambda x: x[1])[1] + 1

        instruction = instruction.strip().split(' ')[-1]
        axis, i = instruction.split('=')
        i = int(i)
        # print(axis, i)
        if axis == "x":
            for a, b in zip(range(i, -1, -1), range(i, max_x)):
                for y in range(max_y):
                    points[(a, y)] += points[(b, y)]
                    del points[(b, y)]
        else:
            for a, b in zip(range(i, -1, -1), range(i, max_y)):
                for x in range(max_x):
                    points[(x, a)] += points[(x, b)]
                    del points[(x, b)]

    ret = ""
    max_x = max(points, key=lambda x: x[0])[0] + 1
    max_y = max(points, key=lambda x: x[1])[1] + 1
    for y in range(max_y):
        for x in range(max_x):
            ret += '#' if points[(x, y)] else ' '
        ret += "\n"
    print(ret)
    return sum(1 for value in points.values() if value)




print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
