
with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
# data = [int(x) for x in data]

class Number:
    def __init__(self, number):
        self.number = number
        self.marked = False
    
    def __repr__(self):
        return str(self.number)

class Board:
    def __init__(self, board):
        self.won = False
        self.board = []
        for line in board.split("\n"):
            row = []
            for number in line.split(" "):
                if number.strip():
                    row.append(Number(int(number.strip())))
            self.board.append(row)
        if len(self.board) != 5:
            self.board.pop(0)

    def turn(self, number_played):
        for row in self.board:
            for number in row:
                if number.number == number_played:
                    number.marked = True
                    return

    def win(self):
        for row in self.board:
            marked_numbers = 0
            for number in row:
                if number.marked:
                    marked_numbers += 1
            if marked_numbers == 5:
                self.won = True
                return True

        for i in range(5):
            col_score = 0
            for row in self.board:
                if row[i].marked:
                    col_score += 1
            if col_score == 5:
                self.won = True
                return True
        return self.won
                


def part1(data):
    data = data[:]
    turns = data.pop(0)
    turns = [int(x) for x in turns.split(",")]
    data = "\n".join(data)
    board_data = data.split("\n\n")
    boards = [Board(board) for board in board_data]
    
    for turn in turns:
        for board in boards:
            board.turn(turn)
            if board.win():
                unmarked_number_sum = 0
                for row in board.board:
                    for number in row:
                        if not number.marked:
                            unmarked_number_sum += number.number
                return unmarked_number_sum * turn


def part2(data):
    data = data[:]
    turns = data.pop(0)
    turns = [int(x) for x in turns.split(",")]
    data = "\n".join(data)
    board_data = data.split("\n\n")
    boards = [Board(board) for board in board_data]
    last_turn = last_board_won = None
    for turn in turns:
        for board in boards:
            if board.won:
                continue
            board.turn(turn)
            if board.win():
                last_board_won = board
                last_turn = turn

    unmarked_number_sum = 0
    for row in last_board_won.board:
        for number in row:
            if not number.marked:
                unmarked_number_sum += number.number
    return unmarked_number_sum * last_turn


print("Part 1:", part1(data))
print("Part 2:", part2(data))