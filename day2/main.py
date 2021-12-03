data = None
with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")

def part1(data):
    depth = 0
    forward = 0

    for line in data:
        cmd, val = line.split(" ")
        if cmd == "forward":
            forward += int(val)
        elif cmd == "down":
            depth += int(val)
        elif cmd == "up":
            depth -= int(val)

    return depth * forward

def part2(data):
    depth = 0
    forward = 0
    aim = 0

    for line in data:
        cmd, val = line.split(" ")
        if cmd == "forward":
            forward += int(val)
            depth += aim * int(val)
        elif cmd == "down":
            aim += int(val)
        elif cmd == "up":
            aim -= int(val)

    return depth * forward

print(part1(data))
print(part2(data))