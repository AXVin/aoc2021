from collections import defaultdict
from utils import *


with open("input.txt", "r") as file:
    data = file.read()


@test(19)
def part1(data):
    data = data.strip().split("\n")
    paths = defaultdict(list)
    for line in data:
        start, end = line.strip().split('-')
        if start != 'start' and end != 'end':
            paths[end].append(start)
        if end != 'start' and start != 'end':
            paths[start].append(end)

    def recur_paths(start, already_visited):
        if start == 'end':
            return 1
        else:
            total = 0
            if start.islower():
                already_visited.append(start)
            if already_visited.count(start) > 1:
                return 0
            for new_start in paths[start]:
                total += recur_paths(new_start, [x for x in already_visited])
            return total
    
    return recur_paths('start', [])


@test(103)
def part2(data):
    data = data.strip().split("\n")
    paths = defaultdict(list)
    for line in data:
        start, end = line.strip().split('-')
        if start != 'start' and end != 'end':
            paths[end].append(start)
        if end != 'start' and start != 'end':
            paths[start].append(end)

    def recur_paths(start, already_visited):
        if start == 'end':
            return 1
        else:
            total = 0
            if start == 'start' and start in already_visited:
                return 0
            if start.islower():
                already_visited.append(start)
            if already_visited.count(start) >= 2:
                if already_visited[0] == True:
                    return 0
                else:
                    already_visited[0] = True
            for new_start in paths[start]:
                total += recur_paths(new_start, [x for x in already_visited])
            return total
    # the first element in already_visited denotes whether a small cave
    # has already been visited twice in this path
    return recur_paths('start', [False])


print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
