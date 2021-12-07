import os, sys

utils_text = r"""
import time

def test(solution=None):
    def wrapper(func):
        def inner(data):
            if solution is not None:
                with open("test_input.txt", "r") as file:
                    test_data = file.read()
                test_result = func(test_data)
                if test_result != solution:
                    raise ValueError(f"{func.__name__} fails test. Output {test_result} doesn't match solution {solution}!")
            start = time.time()
            ret = func(data)
            end = time.time()
            print("\u001b[38;5;244m", f"[{func.__name__} took {round(end-start, 5)}s]", "\u001b[0m")
            return ret
        return inner
    return wrapper
"""

text = r"""
from utils import *

with open("input.txt", "r") as file:
    data = file.read()


@test()
def part1(data):
    data = data.split("\n")
    # data = list(map(int, data))



@test()
def part2(data):
    data = data.split("\n")
    # data = list(map(int, data))



print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
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

    with open(f"{dir_name}/utils.py", "w") as file:
        file.write(utils_text)
    print(f'Created file "{dir_name}/utils.py"')

    with open(f"{dir_name}/input.txt", "w") as file:
        file.write("")
    print(f'Created file "{dir_name}/input.txt"')

    with open(f"{dir_name}/test_input.txt", "w") as file:
        file.write("")
    print(f'Created file "{dir_name}/test_input.txt"')

    print("Done!")


if __name__ == "__main__":
    main()