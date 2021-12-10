
from utils import *

with open("input.txt", "r") as file:
    data = file.read()


@test(15)
def part1(data):
    data = data.strip().split("\n")
    # data = list(map(list, data))
    summ = 0
    for i, row in enumerate(data):
        for j, point in enumerate(row):
            points = [
                point < data[i-1][j] if i > 0 else 9999,
                point < row[j-1] if j > 0 else 9999,
                point < row[j+1] if j < len(row)-1 else 9999,
                point < data[i+1][j] if i < len(data)-1 else 9999
            ]

            if all(points):
                summ += int(point)+1
    return summ

def nearby_low_points(data, i, j, points_done):
    row = data[i]
    points = [
        data[i-1][j] != "9" and (i-1, j) not in points_done if i > 0 else False,
        row[j-1] != "9" and (i, j-1) not in points_done if j > 0 else False,
        row[j+1] != "9" and (i, j+1) not in points_done if j < len(row)-1 else False,
        data[i+1][j] != "9" and (i+1, j) not in points_done if i < len(data)-1 else False
    ]
    return sum(points)


@test(1134)
def part2(data):
    data = data.strip().split("\n")
    basins = []
    points_done = []
    for i, row in enumerate(data):
        for j, point in enumerate(row):
            points = [
                point < data[i-1][j] if i > 0 else 9999,
                point < row[j-1] if j > 0 else 9999,
                point < row[j+1] if j < len(row)-1 else 9999,
                point < data[i+1][j] if i < len(data)-1 else 9999
            ]

            if all(points):
                points_to_be_done = [(i, j)]
                basin = 0
                while points_to_be_done:
                    i, j = points_to_be_done.pop()
                    if data[i][j] == "9":
                        continue
                    if i > 0:
                        if data[i-1][j] != "9" and (i-1, j) not in points_done:
                            basin += 1
                            points_to_be_done.append((i-1, j))
                            points_done.append((i-1, j))
                    if j > 0:
                        if data[i][j-1] != "9" and (i, j-1) not in points_done:
                            basin += 1
                            points_to_be_done.append((i, j-1))
                            points_done.append((i, j-1))
                    if j < len(data[i]) - 1:
                        if data[i][j+1] != "9" and (i, j+1) not in points_done:
                            basin += 1
                            points_to_be_done.append((i, j+1))
                            points_done.append((i, j+1))
                    if i < len(data) - 1:
                        if data[i+1][j] != "9" and (i+1, j) not in points_done:
                            basin += 1
                            points_to_be_done.append((i+1, j))
                            points_done.append((i+1, j))
                basins.append(basin)

    basins = sorted(basins, reverse=True)
    print(basins)
    return basins[0]*basins[1]*basins[2]



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
