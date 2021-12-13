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
        max_x = max(points, key=lambda x: x[0])[0]
        max_y = max(points, key=lambda x: x[1])[1]

        instruction = instruction.strip()
        axis, i = instruction[-3], instruction[-1]
        i = int(i)
        if axis == "x":
            for a, b in zip(range(i, 0, -1), range(i, max_x)):
                for y in range(max_y):
                    points[(a, y)] += points[(b, y)]
                    del points[(b, y)]
        else:
            for a, b in zip(range(i, 0, -1), range(i, max_y)):
                for x in range(max_x):
                    points[(x, a)] += points[(x, b)]
                    del points[(x, b)]
        break

    return(sum(1 for value in points.values() if value))



@test()
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
