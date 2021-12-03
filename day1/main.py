with open("data.txt", "r") as file:
    data = file.read()
data = data.split("\n")
data = [int(x) for x in data]

def part1(data):
    solution = 0
    for i, x in enumerate(data[1:]):
        xminus1 = data[i-1]
        if x > xminus1:
            solution += 1
    return solution


def part2(data):
    new_data = []
    for i, x in enumerate(data[:-2]):
        new_data.append(x + data[i+1] + data[i+2])


    solution = 0
    for i, x in enumerate(new_data[1:]):
        xminus1 = new_data[i-1]
        if x > xminus1:
            solution += 1
    return solution

print(part1(data))
print(part2(data))
