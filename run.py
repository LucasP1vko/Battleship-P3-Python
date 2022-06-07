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
        self.coordinates_list = [
            (col, row) for col in range(1, 6) for row in range(1, 6)
        ]
    def column_number(self, col):

        return self.board[0].index(col.upper())

    def display_board(self):

        print(f"\n   {self.name}'s board:\n")
        for row in self.board:
            joint_row = "   ".join(row)
            print(f"{joint_row}\n")

    def place_ships(self, col, row):

        if type(col) is str:
            col_num = self.column_number(col)
        else:
            col_num = col
        self.board[int(row)][col_num] = "S"

    def create_five_random_coordinates(self):

        col_list = ["A", "B", "C", "D", "E"]
        row_list = [1, 2, 3, 4, 5]
        coordinate_list = []
        x = 0
        while x < 5:
            col = random.choice(col_list)
            row = random.choice(row_list)
            col_num = self.column_number(col)
            rand_coordinates = [row, col_num]
            if rand_coordinates in coordinate_list:
                pass
            else:
                coordinate_list.append(rand_coordinates)
                x += 1
        return coordinate_list




def place_ships():        
    coordinates = player_board.create_five_random_coordinates()
    for coor in coordinates:
        a, b = coor
        player_board.place_ships(a, b)
    player_board.display_board()


play_game = True
while play_game:
        
    player_name = input("Please enter your name:\n")
    player_board = Board(player_name)
    place_ships()
    
    computer_board = Board("Computer")
    computer_coords = computer_board.create_five_random_coordinates()
    computer_board.display_board()





