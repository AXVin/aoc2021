from __future__ import annotations

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
    while True:
        # time.sleep(.5)
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
                if char > 9:
                    # split just in case
                    new_data.extend(split(char))
                    new_data.extend(data[i+1:])
                    data = new_data
                    break
                if depth > 4 and isinstance(data[i+2], int):
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
                                new_data.extend(split(next_char))
                                continue
                        new_data.append(next_char)
                    # while finding above, add all chars to new_data
                    data = new_data
                    break
                previous_number = (i, char)
                new_data.append(char)
        else:
            data = new_data
            break
    return eval("".join(map(str, data)))



@test(4140)
def part1(data):
    data = data.strip().split("\n")
    filter_line = lambda x: list(
        filter(
            lambda x: x != ' ',
            map(
                lambda x: int(x) if x.isdigit() else x,
                str(x)
            )
        )
    )
    data = [eval(line) for line in data]
    new_data = []
    for i, line in enumerate(data):
        print(str(new_data))
        if i in (0, 1):
            new_data.append(line)
            if i == 1:
                new_data = reduce(filter_line(new_data))
        else:
            new_data = [new_data]
            new_data.append(line)
            new_data = reduce(filter_line(new_data))
            if i == len(data) - 1:
                new_data = [new_data]

    print("".join(map(str, new_data)))


@test()
def part2(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
