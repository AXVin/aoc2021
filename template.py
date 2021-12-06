import os, sys

text = """
with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\\n")
# data = list(map(int, data))


def part1(data):
    pass


def part2(data):
    pass


print("Part 1:", part1(data))
print("Part 2:", part2(data))
"""

def main():
    try:
        day = int(sys.argv[1])
    except IndexError:
        print("Please provide the day for the challenge!")
        return
    except ValueError:
        print("Day must be an integer. Aborting!")
        return
    
    dir_name = f"day{day}"
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print(f"A directory with name {dir_name} already exists. Aborting!")
        return
    else:
        print(f"Created directory {dir_name}")

    with open(f"{dir_name}/main.py", "w") as file:
        file.write(text)
    print(f'Created file "{dir_name}/main.py"')

    with open(f"{dir_name}/input.txt", "w") as file:
        file.write("")
    print(f'Created file "{dir_name}/input.txt"')

    print("Done!")


if __name__ == "__main__":
    main()