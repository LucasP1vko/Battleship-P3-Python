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

    
    def guess_computer_ships(self, col, row, coor_list):

        col_num = self.column_number(col)
        coords = [int(row), col_num]
        if coords in coor_list:
            self.board[int(row)][col_num] = "X"
            coor_list.remove(coords)
            self.ship_count -= 1
            if self.ship_count > 1:
                print(
                    f"\n Your shot at {col.upper()} {row} was a hit."
                    f"Computer still have {self.ship_count} ships left "

                )
        else:
            print(f"\n Your shot at {col.upper()} {row} was missed")
            self.board[int(row)][col_num] = "O"
    


    def guess_player_ships(self, player_name):

        i = len(self.coordinates_list)
        rand_index = random.randrange(i)
        rand_coordinate = self.coordinates_list[rand_index]
        col, row = rand_coordinate
        coordinate = self.board[row][col]
        self.coordinates_list.remove(rand_coordinate)
        if coordinate == "S":
            self.board[row][col] = "X"
            self.ship_count -= 1
            if self.ship_count > 1:
                print(
                    f"\nComputer shot your ship at "
                    f"{self.board[0][col].upper()} {row}!\n"
                    f"You have {self.ship_count} ships left.."
                )

            else:
                print(
                    f"\nComputer shot your last ship at "
                    f"{self.board[0][col].upper()} {row}!\n"
                )
        else:
            print(
                "\n Computer shot at "
                f"{self.board[0][col].upper()} {row} was missed.."
            )
            self.board[row][col] = "O"




def place_ships():        
    coordinates = player_board.create_five_random_coordinates()
    for coor in coordinates:
        a, b = coor
        player_board.place_ships(a, b)
    player_board.display_board()



def player_turn():
    shot = True
    while shot:
        coordinates = input(
            "To make shot type: \n"
            "letter for column (A-E) and number for row (1-5) divided by a space\n"
            "Example: A 1\n"
            "Please type here: "
        )
        if len(coordinates) > 3:
            print(
                "\n#########\n"
                "Wrong input.\n"
                "Your input should look like this --> A 1\n"
                "Letter, space and a number.\n"
                "Please try again..\n\n"
            )
            continue
        elif len(coordinates) < 3:
            print(
                "\n#########\n"
                "Wrong input.\n"
                "Your input should look like this --> A 1\n"
                "Letter, space and a number.\n"
                "Please try again..\n\n"
            )
            continue
        else:
            try:
                a, b = coordinates.split()
                a_num = computer_board.column_number(a)
                if (
                    computer_board.board[int(b)][a_num] == "X" or
                    computer_board.board[int(b)][a_num] == "O"
                ):
                    print(
                        f"\n!!! You already shot {a.upper()} {b}! "
                        "Please choose another coordinate !!!\n"
                    )
                else:
                    computer_board.guess_computer_ships(a, b, computer_coords)
                    shot = False
            except ValueError:
                print("\n#########\n"
                "Wrong input.\n"
                "Your input should look like this --> A 1\n"
                "Letter, space and a number.\n"
                "Please try again..\n\n"
                )


def computer_turn():
    player_board.guess_player_ships(player_name)


def start_game():
    while computer_board.ship_count > 0 and player_board.ship_count > 0:
        player_turn()
        if computer_board.ship_count == 0 or player_board.ship_count == 0:
            player_board.display_board()
            computer_board.display_board()
            break
        computer_turn()
        player_board.display_board()
        computer_board.display_board()


def game_over():
    if computer_board.ship_count == 0:
        print("\n__     _____ ____ _____ ___  ______   __\n"
        "\ \   / /_ _/ ___|_   _/ _ \|  _ \ \ / /\n"
        " \ \ / / | | |     | || | | | |_) \ V / \n"
        "  \ V /  | | |___  | || |_| |  _ < | |  \n"
        "   \_/  |___\____| |_| \___/|_| \_\|_|  \n \n"
        "You won the game! Well done!\n")

    elif player_board.ship_count == 0:
        print(" ____  _____ _____ _____    _  _____ \n"
        "|  _ \| ____|  ___| ____|  / \|_   _|\n"
        "| | | |  _| | |_  |  _|   / _ \ | |  \n"
        "| |_| | |___|  _| | |___ / ___ \| |  \n"
        "|____/|_____|_|   |_____/_/   \_\_|  )\n"
        "\nGame lost.. Computer shot all of your ships.\n")


game_on = True
while game_on:
        
    player_name = input(
        " ____    _  _____ _____ _     _____ ____  _   _ ___ ____  \n"
        "| __ )  / \|_   _|_   _| |   | ____/ ___|| | | |_ _|  _ \ \n"
        "|  _ \ / _ \ | |   | | | |   |  _| \___ \| |_| || || |_) |\n"
        "| |_) / ___ \| |   | | | |___| |___ ___) |  _  || ||  __/ \n"
        "|____/_/   \_\_|   |_| |_____|_____|____/|_| |_|___|_|    \n \n"
        "Welcome in Battleship game!\n\nWhat is your name?\nPlease type here:\n\n")
    player_board = Board(player_name)
    place_ships()
    
    computer_board = Board("Computer")
    computer_coords = computer_board.create_five_random_coordinates()
    computer_board.display_board()

    start_game()
    game_over()

    game_on = False

