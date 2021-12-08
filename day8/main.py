
from utils import *

with open("input.txt", "r") as file:
    data = file.read()

uniques = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

@test(26)
def part1(data):
    data = data.strip().split("\n")
    # data = list(map(int, data))
    sum_ = 0
    for line in data:
        try:
            _, right = line.split(" | ")
        except:
            print(line)
            raise
        digits = right.split(" ")
        sum_ += sum(1 for digit in  digits if len(digit) in uniques.values())
    return sum_


segments = {
    0: [0,1,2,4,5,6],
    1: [2, 5],
    2: [0,2,3,4,6],
    3: [0,2,3,5,6],
    4: [1,2,3,5],
    5: [0,1,3,5,6],
    6: [0,1,3,4,5,6],
    7: [0,2,5],
    8: [0,1,2,3,4,5,6],
    9: [0,1,2,3,5,6]
}


@test(61229)
def part2(data):
    data = data.strip().split("\n")
    sum_ = 0
    # data = list(map(int, data))
    for line in  data:
        left, right = line.split(" | ")
        left_digits, right_digits = left.split(" "), right.split(" ")
        config = list(range(7))
        one = [digit for digit in left_digits if len(digit) == 2][0]
        seven = [digit for digit in left_digits if len(digit) == 3][0]
        config[0] = (set(seven)-set(one)).pop()
        four = [digit for digit in left_digits if len(digit) == 4][0]
        one_three_digits = set(four) - set(one)
        two_three_five = [digit for digit in left_digits if len(digit) == 5]
        three = [number for number in two_three_five if len(set(number)-set(seven))==2][0]
        three_six_digits = set(three)-set(seven)
        config[3] = [char for char in three_six_digits if char in one_three_digits][0] 
        config[6] = (three_six_digits-set(config[3])).pop()
        config[1] = (one_three_digits-set(config[3])).pop()
        zero_one_three_six_digits = {config[0], config[1], config[3], config[6]}
        five = [number for number in two_three_five if len(set(number)-zero_one_three_six_digits) == 1][0]
        config[5] = (set(five)-zero_one_three_six_digits).pop()
        config[2] = (set(one)-set(config[5])).pop()
        zero_one_three_six_digits.update({config[5], config[2]})
        eight = [digit for digit in left_digits if len(digit) == 7][0]
        config[4] = (set(eight)-zero_one_three_six_digits).pop()
        matchings = []
        for segment in segments.values():
            matchings.append({config[i] for i in segment})

        number = ""
        for digit in right_digits:
            digit = set(digit)
            for i, matching in enumerate(matchings):
                if len(digit) > len(matching):
                    if len(digit-matching) == 0:
                        number += str(i)
                        break
                else:
                    if len(matching-digit) == 0:
                        number += str(i)
                        break
        sum_ += int(number)

    return sum_


print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
