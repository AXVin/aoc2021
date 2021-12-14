from collections import Counter, defaultdict
from utils import *
from copy import copy

with open("input.txt", "r") as file:
    data = file.read()


@test(1588)
def part1(data):
    template, instruction_lines = data.strip().split("\n\n")
    # data = list(map(int, data))
    instructions = {}
    for line in instruction_lines.strip().split('\n'):
        join, insert = line.strip().split(' -> ')
        instructions[join] = join[0] +insert

    template = template.strip()
    for _ in range(10):
        new_template = ''
        for i, char_a in enumerate(template):
            char_b = template[i+1] if len(template) > i+1 else None
            if char_b is None:
                new_template += char_a
                continue
            if char_a+char_b in instructions:
                new_template += instructions[char_a+char_b]
            else:
                new_template += char_a
        template = new_template

    count = {
        char: template.count(char)
        for char in template
    }
    return count[max(count, key=lambda x: count[x])] - count[min(count, key=lambda x: count[x])]


@test(2188189693529)
def part2(data):
    template_str, instruction_lines = data.strip().split("\n\n")
    # data = list(map(int, data))
    instructions = {}
    for line in instruction_lines.strip().split('\n'):
        join, insert = line.strip().split(' -> ')
        instructions[join] = (join[0] + insert, insert + join[1])

    print(instructions)
    template = defaultdict(int)
    for a, b in zip(template_str.strip(), template_str.strip()[1:]):
        template[a+b] += 1
    template = dict(template)
    for step in range(4):
        print(template)
        new_template = defaultdict(int)
        for key in template:
            if key in instructions:
                keys = instructions[key]
                for key in keys:
                    try:
                        value = template[key]
                    except KeyError:
                        value = 1
                    new_template[key] += value
            else:
                new_template[key] = template[key]
        template = dict(new_template)

    counts = defaultdict(int)
    for key, value in template.items():
        counts[key[0]] += value
        counts[key[1]] += 1

    sorts = sorted(counts, key=lambda x: counts[x])
    print(sorts[-1], counts[sorts[-1]], sorts[0], counts[sorts[0]])
    return counts[sorts[-1]] - counts[sorts[0]]



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
