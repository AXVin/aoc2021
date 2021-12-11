
from utils import *

with open("input.txt", "r") as file:
    data = file.read()

adjacent = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1,0),
    (-1, 1), (0, 1), (1, 1)
]

@test(1656)
def part1(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    octopuses = {
        (i, j): int(point)
        for i, line in enumerate(data)
        for j, point in enumerate(line.strip())
    }
    count = 0
    for _ in range(100):
        for coords in octopuses:
            octopuses[coords] += 1
        for coords, octopus in octopuses.items():
            if octopus > 9:
                to_do = [coords]
                while to_do:
                    coords = to_do.pop()
                    try:
                        octopus = octopuses[coords]
                    except KeyError:
                        continue
                    if octopus != 0:
                        octopuses[coords] += 1
                    octopus = octopuses[coords]
                    if octopus > 9:
                        count += 1
                        octopuses[coords] = 0
                        to_do.extend([(coords[0]+point[0], coords[1]+point[1]) for point in adjacent])

        board = ""
        for i in range(10):
            for j in range(10):
                board += str(octopuses[(i, j)])
            board += "\n"
        #print(board)
        #print()

    return count



@test(195)
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    octopuses = {
        (i, j): int(point)
        for i, line in enumerate(data)
        for j, point in enumerate(line.strip())
    }
    count = 0
    for day in range(1000):
        for coords in octopuses:
            octopuses[coords] += 1
        for coords, octopus in octopuses.items():
            if octopus > 9:
                to_do = [coords]
                while to_do:
                    coords = to_do.pop()
                    try:
                        octopus = octopuses[coords]
                    except KeyError:
                        continue
                    if octopus != 0:
                        octopuses[coords] += 1
                    octopus = octopuses[coords]
                    if octopus > 9:
                        count += 1
                        octopuses[coords] = 0
                        to_do.extend([(coords[0]+point[0], coords[1]+point[1]) for point in adjacent])

        board = 0
        for i in range(10):
            for j in range(10):
                board += octopuses[(i, j)]
        if board == 0:
            return day+1
        #if day == 195:
        #    print(board)
        #print(board)
        #print()





print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
