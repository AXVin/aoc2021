from __future__ import annotations
from math import prod
from typing import NamedTuple, Union
from utils import *


with open("input.txt", "r") as file:
    data = file.read()

class Literal(NamedTuple):
    version: int
    value: int

class Operator(NamedTuple):
    version: int
    type: int
    subs: list[Union[Operator, Literal]]

    @property
    def value(self) -> int:
        value = 0
        if self.type == 0:
            value = sum(sub.value for sub in self.subs)
        elif self.type == 1:
            value = prod(sub.value for sub in self.subs)
        elif self.type == 2:
            value = min(sub.value for sub in self.subs)
        elif self.type == 3:
            value = max(sub.value for sub in self.subs)
        elif self.type == 5:
            value = bool(self.subs[0].value > self.subs[1].value)
        elif self.type == 6:
            value = bool(self.subs[0].value < self.subs[1].value)
        elif self.type == 7:
            value = bool(self.subs[0].value == self.subs[1].value)
        return value


def parse_literal(data):
    total_bits = ''
    i = 0
    while True:
        bits = data[i*5:(i*5)+5]
        total_bits += bits[1:]
        if bits[0] == '0':
            break
        i += 1
    return int(total_bits, 2), i

def parse(data):
    if len(data) < 8:
        return []
    parsed = []
    version = int(data[:3], 2)
    packet_type = int(data[3:6], 2)
    if packet_type == 4:
        literal, i = parse_literal(data[6:])
        parsed.append(Literal(version=version, value=literal))
        parsed.extend(parse(data[6+(i+1)*5:]))
    else:
        subs = []
        length_type = data[6]
        length_type = 15 if length_type == '0' else 11
        length = int(data[7:7+length_type], 2)
        if length_type == 15:
            subpackets = data[7+length_type:7+length_type+length]
            subs.extend(parse(subpackets))
            parsed.append(Operator(version=version, type=packet_type, subs=subs))
            parsed.extend(parse(data[7+length_type+length:]))
        else:
            stuff = parse(data[7+length_type:])
            subs.extend(stuff[:length])
            parsed.append(Operator(version=version, type=packet_type, subs=subs))
            parsed.extend(stuff[length:])
    return parsed

def version_sum(tokens):
    summ = 0
    for token in tokens:
        summ += token.version
        if isinstance(token, Operator):
            summ += version_sum(token.subs)
    return summ

@test()
def part1(data):
    data = ''.join([bin(int(x.strip(), 16))[2:].zfill(4) for x in data.strip()])
    tokens = parse(data)
    return version_sum(tokens)

@test()
def part2(data):
    data = ''.join([bin(int(x.strip(), 16))[2:].zfill(4) for x in data.strip()])
    tokens = parse(data)
    return tokens[0].value


print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
