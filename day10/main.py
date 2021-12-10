
from utils import *

with open("input.txt", "r") as file:
    data = file.read()

pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}
scores = {
    ")": 3,
    "]":  57,
    "}": 1197,
    ">": 25137
}

@test(26397)
def part1(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    summ = 0
    for line in data:
        chars_done = []
        for i, char in enumerate(list(line)):
            if i in chars_done:
                continue
            if char in pairs.values():
                print(scores[char], line.count(char))
                summ += scores[char] * line.count(char)
                break
            chars_done.append(i)
            
            closing = pairs[char]
            x = [(i, char) for i, char in enumerate(list(line)) if i not in chars_done and char == closing]
            if x:
                chars_done.append(x[0][0])
            else:
                break

    return summ

@test()
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
