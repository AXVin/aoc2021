from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")


def part1(data):
    points = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, line.replace(" -> ", ",").split(","))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, i)] += 1

        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                points[(i, y1)] += 1

    return sum(count >= 2 for count in points.values())


def part2(data):
    points = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = map(int, line.replace(" -> ", ",").split(","))
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, i)] += 1
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                points[(i, y1)] += 1
        else:
            x = 1 if x2 > x1 else -1
            y = 1 if y2 > y1 else -1
            point = (x1, y1)
            while True:
                points[point] += 1
                point = (point[0]+x, point[1]+y)
                if point == (x2, y2):
                    points[point] += 1
                    break

    return sum(count >= 2 for count in points.values())


print("Part 1:", part1(data))
print("Part 2:", part2(data))
