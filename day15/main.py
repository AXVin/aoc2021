
from utils import *
import grid

with open("input.txt", "r") as file:
    data = file.read()


@test(40)
def part1(data):
    board = grid.Grid.from_text(data.strip())
    path = board.dijkstra(board.nodes[0], board.nodes[-1])
    # path = board.astar(board.nodes[0], board.nodes[-1])
    return sum(x.value for x in path if x != board.nodes[0])
    # data = list(map(int, data))


@test(315)
def part2(data):
    board_list = []
    for line in data.strip().split("\n"):
        row = []
        for val in line.strip():
             row.append(int(val))
        board_list.append(row)

    new_board = []
    for row in board_list:
        new_row = []
        for i in range(5):
            for val in row:
                new_val = val + i
                if new_val > 9:
                    new_val = new_val % 9
                new_row.append(new_val)
        new_board.append(new_row)

    newest_board = []
    for i in range(5):
        for row in new_board:
            new_row = []
            for val in row:
                new_val = val + i
                if new_val > 9:
                    new_val = new_val % 9
                new_row.append(new_val)
            newest_board.append(new_row)

    ret = ""
    for row in newest_board:
        for val in row:
            ret += str(val)
        ret += "\n"
    board = grid.Grid.from_text(ret.strip())
    path = board.dijkstra(board.nodes[0], board.nodes[-1])
    return sum(x.value for x in path if x != board.nodes[0])
 


print("Part 1:", "\u001b[36;1m", part1(data), "\u001b[0m")
print("Part 2:", "\u001b[36;1m", part2(data), "\u001b[0m")
