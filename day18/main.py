from __future__ import annotations
import itertools
import functools
import math
from typing import List, Optional, Union
from utils import *

with open("input.txt", "r") as file:
    data = file.read()

def split(number):
    if number > 9:
        half = int(number) / 2
        return ['[', math.floor(half), ',', math.ceil(half), ']']
    return [number]

Data = List[Union[int, str]]

def reduce(data: Data) -> Data:
    can_split = False
    while True:
        # time.sleep(1)
        # print("".join(map(str, data)))

        depth = 0
        previous_number: Optional[tuple[int, int]] = None
        new_data = []
        for i, char in enumerate(data):
            if isinstance(char, str):
                if char == '[':
                    depth += 1
                elif char == ']':
                    depth -= 1
                new_data.append(char)
            else:
                if depth > 4: # and isinstance(data[i+2], int):
                    # explode
                    # pop the previously appended [
                    new_data.pop()
                    # if prv exists:
                    #   mutate prv number (prv + current)
                    if previous_number:
                        new_data[previous_number[0]] = previous_number[1] + char
                    # get 2nd from current pair
                    num2 = data[i+2]
                    assert isinstance(num2, int)
                    # replace the current pair [x,y] with 0
                    new_data.append(0)
                    # find next most number and mutate (2nd + current)
                    already_added = False
                    for next_char in data[i+4:]:
                        if isinstance(next_char, int):
                            if not already_added:
                                next_char += num2
                                already_added = True
                                # new_data.extend(split(next_char))
                                # continue
                        new_data.append(next_char)
                    # while finding above, add all chars to new_data
                    data = new_data
                    break
                if char > 9 and can_split:
                    # split just in case
                    new_data.extend(split(char))
                    new_data.extend(data[i+1:])
                    data = new_data
                    can_split = False
                    break
                previous_number = (i, char)
                new_data.append(char)
        else:
            if can_split == False:
                can_split = True
            else:
                data = new_data
                break
    return eval("".join(map(str, data)))

filter_line = lambda x: list(
    filter(
        lambda x: x != ' ',
        map(
            lambda x: int(x) if x.isdigit() else x,
            str(x)
        )
    )
)
def magnitude(data):
    summ = 0
    if isinstance(data, list):
        if len(data) == 2:
            summ += (3 * magnitude(data[0])) + (2 * magnitude(data[1]))
        else:
            summ += magnitude(data[0])
    else:
        return data
    return summ

def add(a, b):
    return reduce(filter_line([a, b]))

@test(4140)
def part1(data):
    data = data.strip().split("\n")
    data = [eval(line) for line in data]
    return magnitude(functools.reduce(add, data))


@test(3993)
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    magnitudes = []
    data = [eval(line) for line in data]
    for a, b in itertools.permutations(data, 2):
        magnitudes.append(magnitude(reduce(filter_line([a, b]))))
    return max(magnitudes)



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
