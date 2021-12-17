import re
from utils import *

with open("input.txt", "r") as file:
    data = file.read()


@test(45)
def part1(data):
    data = data.strip()
    minx, maxx, miny, maxy = map(int, re.findall(r"-?\d+", data))
    def compute(x, y):
        ycap = 0
        class X:
            x: int
            y: int
        start = X()
        start.x, start.y = 0, 0
        velocity = X()
        velocity.x, velocity.y = x, y
        while True:
            start.x += velocity.x
            start.y += velocity.y
            if start.y > ycap:
                ycap = start.y
            velocity.x -= 1 if velocity.x != 0 else 0
            velocity.y -= 1

            if minx <= start.x <= maxx and miny <= start.y <= maxy:
                return ycap
            if start.x > maxx or start.y < maxy:
                return

    results = []
    for y in range(abs(miny)//2, abs(miny)+1):
        for x in range(0, maxx+1):
            result = compute(x, y)
            if result is not None:
                results.append(result)
    return max(results)

@test()
def part2(data):
    data = data.strip()
    minx, maxx, miny, maxy = map(int, re.findall(r"-?\d+", data))
    def compute(x, y):
        ycap = 0
        class X:
            x: int
            y: int
        start = X()
        start.x, start.y = 0, 0
        velocity = X()
        velocity.x, velocity.y = x, y
        while True:
            start.x += velocity.x
            start.y += velocity.y
            if start.y > ycap:
                ycap = start.y
            velocity.x -= 1 if velocity.x != 0 else 0
            velocity.y -= 1

            if minx <= start.x <= maxx and miny <= start.y <= maxy:
                return ycap
            if start.x > maxx or start.y < maxy:
                return

    results = []
    for y in range(miny, abs(miny)+1):
        for x in range(0, maxx+1):
            result = compute(x, y)
            if result is not None:
                results.append(result)
    return len(results)


print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
