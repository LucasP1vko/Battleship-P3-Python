import random


class Board:

    def __init__(self, name):
        self.name = name
        self.board = [
            [" ", "A", "B", "C", "D", "E"],
            ["1", "~", "~", "~", "~", "~"],
            ["2", "~", "~", "~", "~", "~"],
            ["3", "~", "~", "~", "~", "~"],
            ["4", "~", "~", "~", "~", "~"],
            ["5", "~", "~", "~", "~", "~"],
        ]
        self.ship_count = 5
        self.turn_count = 0
        self.win = 0
        self.num_of_getting_hit = 0
        self.coordinates_list = [
            (col, row) for col in range(1, 6) for row in range(1, 6)
        ]
playersBoard = Board('player')
print(playersBoard.board)