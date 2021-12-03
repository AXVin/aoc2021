
with open("input.txt", "r") as file:
    data = file.read()
data = data.split("\n")

def part1(data):
    gamma_rate = ""
    epsilon_rate = ""
    data2 = [[] for i in range(len(data[0]))]

    for line in data:
        for i, char in enumerate(list(line)):
            data2[i].append(char)

    for binlist in data2:
        zeroes = 0
        ones = 0
        for char in binlist:
            if char == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data):
    oxygen_data = data[:]
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for line in oxygen_data:
            chars = list(line)
            if chars[i] == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            oxygen_data = [line for line in oxygen_data if line[i] == "0"]
        else:
            oxygen_data = [line for line in oxygen_data if line[i] == "1"]
        if len(oxygen_data) == 1:
            break
    oxygen = int(oxygen_data[0], 2)


    co2_data = data[:]
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for line in co2_data:
            chars = list(line)
            if chars[i] == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            co2_data = [line for line in co2_data if line[i] == "1"]
        else:
            co2_data = [line for line in co2_data if line[i] == "0"]
        if len(co2_data) == 1:
            break

    co2 = int(co2_data[0], 2)

    return oxygen * co2

print(part1(data))
print(part2(data))