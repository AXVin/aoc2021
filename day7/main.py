
from utils import *

with open("input.txt", "r") as file:
    data = file.read()


@test(37)
def part1(data):
    data = data.split(",")
    data = list(map(int, data))
    fuels = []
    for i in range(min(data), max(data)):
        fuel_used = sum(abs(crab - i) for crab in data)
        fuels.append(fuel_used)
    return min(fuels)
    



@test(168)
def part2(data):
    data = data.split(",")
    data = list(map(int, data))
    fuels = []
    for i in range(min(data), max(data)):
        #fuel_used = sum(sum(range(abs(crab - i) + 1)) for crab in data)
        fuel_used = sum((abs(crab - i) * (abs(crab - i) + 1)) / 2 for crab in data)
        fuels.append(fuel_used)
    return min(fuels)



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
