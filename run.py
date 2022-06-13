import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# importing modules:
# random - for generating random coordinates and
# colorama - for displaying colors in terminal


class Board:
    # contain board matrix, ship count and coordinates list

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
        # list of column indexes

        return self.board[0].index(col.upper())

    def display_board(self):
        print(
            Fore.CYAN +
            "------------------------------------\n"
            f"          {self.name}'s board:\n"
            "------------------------------------")
        for row in self.board:
            joint_row = "  ||  ".join(row)
            print(
                f"{joint_row}")

    def place_ships(self, col, row):
        # displaying player ships on board

        if type(col) is str:
            col_num = self.column_number(col)
        else:
            col_num = col
        self.board[int(row)][col_num] = "S"

    def create_five_random_coordinates(self):
        # create 5 random coordinates

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
        # removing coords from list if hit
        # marking board hit or miss
        # updating computer ship count if hit
        # displaying messages
        col_num = self.column_number(col)
        coords = [int(row), col_num]
        if coords in coor_list:
            self.board[int(row)][col_num] = "X"
            coor_list.remove(coords)
            self.ship_count -= 1
            if self.ship_count > 1:
                print(
                    Fore.YELLOW +
                    f"\nYour shot at {col.upper()} {row} was a hit. "
                    f"Computer still have {self.ship_count} ships left ")
        else:
            print(
                Fore.YELLOW +
                f"\nYour shot at {col.upper()} {row} was missed.. "
                f"Computer still have {self.ship_count} ships left ")
            self.board[int(row)][col_num] = "O"

    def guess_player_ships(self, player_name):
        # create random coordinates
        # update coord list if hit
        # Marking board if hit / miss
        # Updating player ship count if hit
        # Display messages
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
                    Fore.YELLOW +
                    f"\nComputer shot your ship at "
                    f"{self.board[0][col].upper()} {row}! "
                    f"You have {self.ship_count} ships left..")
            elif self.ship_count == 1:
                print(
                    Fore.YELLOW +
                    f"\nComputer shot your ship at "
                    f"{self.board[0][col].upper()} {row}! "
                    f"You have last ship left..")
            else:
                print(
                    Fore.YELLOW +
                    f"\nComputer shot your last ship at "
                    f"{self.board[0][col].upper()} {row}!")
        else:
            print(
                Fore.YELLOW +
                "\nComputer shot at "
                f"{self.board[0][col].upper()} {row} was missed.. "
                f"You have {self.ship_count} ships left..")
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
        # Coordinations entry
        # Entry format validation
        coordinates = input(
            Fore.GREEN +
            "To make shot type coordinates: "
            "Column(A-E) + "
            "SPACE + "
            "Row(1-5)\n"
            "Example: A 1 . "
            "Please type here:\n")
        if len(coordinates) > 3:
            print(
                Fore.RED +
                "\n#########\n"
                "Wrong input.\n"
                "Your input should look like this --> A 1\n"
                "Column letter, space and a row number.\n"
                "Please try again..\n\n")
            continue
        elif len(coordinates) < 3:
            print(
                Fore.RED +
                "\n#########\n"
                "Wrong input.\n"
                "Your input should look like this --> A 1\n"
                "Column letter, space and a row number.\n"
                "Please try again..\n\n")
            continue
        else:
            try:
                # split entry and use as row and column
                # validate if row is in range
                a, b = coordinates.split()
                a_num = computer_board.column_number(a)
                if (int(b) > 5):
                    print(
                        Fore.RED +
                        "\n\n#########\nWrong input..\n"
                        f"Your typed row coordinate is > {int(b)} <."
                        "\nThere is only 5 rows."
                        "\nPlease try again:\n")
                elif (int(b) < 1):
                    print(
                        Fore.RED +
                        "\n#########\nWrong input..\n"
                        f"Row number {int(b)} doesn't exist on board."
                        "\nPlease try again:\n")
                elif (
                    # Check if coordinates are already marked
                    # Display error if yes
                    computer_board.board[int(b)][a_num] == "X" or
                    computer_board.board[int(b)][a_num] == "O"
                ):
                    print(
                        Fore.RED +
                        f"\n!!! You already shot {a.upper()} {b}! "
                        "Please choose another coordinate !!!\n")
                else:
                    computer_board.guess_computer_ships(a, b, computer_coords)
                    shot = False
            except ValueError:
                # handle column incorrect format error
                print(
                    Fore.RED +
                    "\n#########\n"
                    "Wrong input.\n"
                    "Your input should look like this --> A 1\n"
                    "Letter, space and a number.\n"
                    "Please try again..\n\n")


def computer_turn():
    player_board.guess_player_ships(player_name)


def start_game():
    # Checking score
    # Running turns for player and computer
    # Displaying boards
    # If ship_count = 0 break to skip to game_over
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
    # Checks for ship_count status for player and cpu.
    # After veryfing score displaying game result.
    if computer_board.ship_count == 0:
        print(
            Fore.GREEN + Style.BRIGHT +
            "\n__     _____ ____ _____ ___  ______   __\n"
            "\ \   / /_ _/ ___|_   _/ _ \|  _ \ \ / /\n"
            " \ \ / / | | |     | || | | | |_) \ V / \n"
            "  \ V /  | | |___  | || |_| |  _ < | |  \n"
            "   \_/  |___\____| |_| \___/|_| \_\|_|  \n \n"
            "     You won the game! Well done!\n")

    elif player_board.ship_count == 0:
        print(
            Fore.RED + Style.BRIGHT +
            " ____  _____ _____ _____    _  _____ \n"
            "|  _ \| ____|  ___| ____|  / \|_   _|\n"
            "| | | |  _| | |_  |  _|   / _ \ | |  \n"
            "| |_| | |___|  _| | |___ / ___ \| |  \n"
            "|____/|_____|_|   |_____/_/   \_\_|  \n\n"
            "Game lost.. Computer shot all of your ships.\n")


def instructions():
    instructions_prompt = True
    while instructions_prompt is True:
        instructions_yn = input(
            Fore.GREEN +
            "\nWelcome in Battleship Game.\n"
            "To read game instructions press: 1.\n"
            "To play game press: 2.\n")
        if instructions_yn == "1":
            print(
                Back.YELLOW + Fore.BLACK +
                "Battleship game goal is to defeat all enemy\n"
                "ships before enemy will shot yours.\n"
                "Both: player and computer (enemy) ships\n"
                "are allocated randomly around the board.\n"
                "To guess enemy ships position player needs to:\n"
                "type coordinates in specific format:\n"
                "Letter for Column and numer for Row divided by space.\n"
                "Example: A 1.\n"
                "Board contains columns A,B,C,D,E and rows 1,2,3,4,5.\n"
                "First one to shot 5 of enemy ships wins the game!"
                "Good Luck!"
            )
        elif instructions_yn == "2":
            print(
                Back.YELLOW + Fore.BLACK +
                ">>>>>>>>>>>>>>> Let's Go! <<<<<<<<<<<<<<<<<"

            )
            instructions_prompt = False
        elif len(instructions_yn) > 1:
            print(
                Fore.RED + Style.BRIGHT +
                "\n#########\n"
                "Wrong input.\n"
                "Please answer 1 or 2.\n")
            continue
        else:
            print(
                Fore.RED + Style.BRIGHT +
                "##########\n" +
                "Wrong input.\n" +
                "Please answer 1 or 2.\n")

game_on = True
while game_on:
    # Player name input
    # Running all game functions and loop for game retry
    # Keeps game function together
    print(
        Fore.WHITE + Back.RED + Style.BRIGHT +
        " ____    _  _____ _____ _     _____ ____  _   _ ___ ____  \n"
        "| __ )  / \|_   _|_   _| |   | ____/ ___|| | | |_ _|  _ \ \n"
        "|  _ \ / _ \ | |   | | | |   |  _| \___ \| |_| || || |_) |\n"
        "| |_) / ___ \| |   | | | |___| |___ ___) |  _  || ||  __/ \n"
        "|____/_/   \_\_|   |_| |_____|_____|____/|_| |_|___|_|    \n"
        "==========================================================")
    print(
        Fore.WHITE + Back.BLUE + Style.BRIGHT +
        "         [|    [|                                         \n"
        "    __|__ |___| |\                       v    |]         v\n"
        "    |o__| |___| | \          v               /|           \n"
        "    |___| |___| |o \             v          /o|       v   \n"
        "   _|___| |___| |_o_\                      /  |           \n"
        "  /...\_____|___|____\_/     o--- - - =D _/___|__         \n"
        "  \   / * o * * o o  /  - - ---o        \--O--O--/        \n"
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    instructions()
    player_name = input(
        Fore.GREEN +
        "\nWelcome in Battleship game!\n\n"
        "What is your name?\n"
        "Please type here:\n\n")
    player_board = Board(player_name)
    place_ships()

    computer_board = Board("Computer")
    computer_coords = computer_board.create_five_random_coordinates()
    computer_board.display_board()

    start_game()
    game_over()
    ###
    # Prompt for game retry
    ###
    retry_yn = False
    while retry_yn is False:
        y_n = input(
            Fore.GREEN +
            "\nWould you like to play another game? "
            "Please answer Yes or No:\n")
        if y_n.lower().strip() == "y":
            print(
                Back.YELLOW + Fore.BLACK +
                "              ---------------------               \n"
                "                    GET READY!                    \n"
                "             MORE SHIPS IS INCOMING!              \n"
                "              ---------------------               "
            )
            retry_yn = True
        elif y_n.lower().strip() == "n":
            print(
                Back.YELLOW + Fore.BLACK +
                "      ---------------------------------      \n"
                "      THANK YOU FOR PLAYING BATTLESHIP!      \n"
                "              COME BACK SOON                 \n"
                "      ---------------------------------      "
            )
            game_on = False
            retry_yn = True
        else:
            print(
                Fore.RED + Style.BRIGHT +
                "##########\n" +
                "Wrong input.\n" +
                "Please answer YES or NO.\n")
