from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read()

data = data.split(",")
data = list(map(int, data))


def part1(data):
    new_data = []
    for i in range(80):
        print(i)
        new_data = []
        for fish in data:
            if fish == 0:
                fish = 6
                new_data.append(8)
            else:
                fish -= 1
            new_data.append(fish)
        data = new_data
    return len(data)


def part2(data):
    fishies = defaultdict(int)
    
    for i in range(9):
        count = data.count(i)
        fishies[i] = count
    for _ in range(256):
        new_fishies = defaultdict(int)
        for days_left, count in fishies.items():
            if days_left == 0:
                new_fishies[6] += count
                new_fishies[8] += count
            else:
                new_fishies[days_left-1] += count
        fishies = new_fishies
            
    return sum(fishies.values())
    


print("Part 1:", part1(data))
print("Part 2:", part2(data))
