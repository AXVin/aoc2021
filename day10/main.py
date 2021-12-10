
from utils import *

with open("input.txt", "r") as file:
    data = file.read()

pairs = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}
pairs_rev =  {v:k for k, v in pairs.items()}
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
        openings = []
        for char in line:
            if char in pairs:
                openings.append(char)
            else:
                if openings.pop() != pairs_rev[char]:
                    summ += scores[char]
                    break
    return summ

scores_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


@test(288957)
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    scores = []
    for line in data:
        openings = []
        for char in line:
            if char in pairs:
                openings.append(char)
            else:
                if openings.pop() != pairs_rev[char]:
                    break
        else:
            summ = 0
            for opening in openings:
                summ *= 5
                summ += scores_map[pairs[opening]]
            scores.append(summ)

    import statistics
    return statistics.median(scores)




# print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
