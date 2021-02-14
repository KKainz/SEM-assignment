import random


class MoveResult:
    """ Provides instruction/information after move:
    Instructions for the Next move and if the move failed or the game is won.

    Attributes
    ----------
    message: str
        Contains human readable instructions for the next move.
    failed_move: bool
        If true, then the last move was not expected to be mad.
        Message will contain error message.
    game_won:
        True when the game is won. The message will contain winner.
    """
    def __init__(self, message: str, failed_move: bool, game_won: bool):
        self.message = message
        self.failed_move = failed_move
        self.game_won = game_won


class ConnectFour:
    """ A class witch allows you to play connect four.\n
    \n
    You can see the game board with the method get_board()\n
    Set a stone with the method set_stone(slot: int)
    With the get_move_instruction method, you get instruction
    on whose turn it is.\n
    \n
    You provide player names and whether you want to play against a bot.

    Parameters
    ----------
    vs_bot: bool
        Specifies if the second player is a bot.
    player_name_1: str
        The name of player 1.
    player_name_2: str
        The name of player 2, if player 2 is not a bot.
    """
    def __init__(self, vs_bot: bool, player_name_1: str, player_name_2: str = None):
        self.__vs_bot = vs_bot
        self.__player_name_1 = player_name_1 if player_name_1 else "Player" if vs_bot else "Player 1"
        if vs_bot:
            self.__player_name_2 = "Bot"
        else:
            self.__player_name_2 = player_name_2 if player_name_2 else "Player 2"
            
        if self.__player_name_1 == self.__player_name_2:
            self.__player_name_1 += "_1"
            self.__player_name_2 += "_2"

        self.__current_player = self.__player_name_1
        self.__last_move_instruction = None

        # Init empty board
        # The first depth of the array represents the columns,
        # the array within are the rows.
        self.__board = [
            ["", "", "", "", "", ""],  # Column 1
            ["", "", "", "", "", ""],  # Column 2
            ["", "", "", "", "", ""],  # Column 3
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""],
            ["", "", "", "", "", ""]
            # Row 1, Row 2, Row 3...
        ]

    @property
    def player_name_1(self) -> str:
        """The name of player 1"""
        return self.__player_name_1

    @property
    def player_name_2(self) -> str:
        """The name of player 2, if you play vs bot, then the name is 'Bot'"""
        return self.__player_name_2

    def get_board(self) -> str:
        """str: ASCII style representation of the board"""
        ret = ""
        first_line = "".join(list(map(lambda x: " " + str(x + 1), range(7)))) + "\n"
        for row in range(6):
            ret += "│"
            for col in range(7):
                item = self.__board[col][row]

                if row == 0:
                    first_line += " V" if item == "" else "  "

                ret += (item if item else " ") + "│"
            ret += "\n"
        return first_line + "\n" + ret + "└─────────────┘"

    def set_stone(self, slot: int) -> MoveResult:
        """ Checks if the selected slot for the stone is possible and then places the stone

        Parameters
        ----------
        slot: int
            Slot in which the current player wants to place the stone in

        Returns
        -------
        MoveResult
            Information about the current game
        """
        if self.__check_slot(slot):
            self.__set_slot(slot)

            if self.__check_status(slot):
                self.__last_move_instruction = MoveResult(f'{self.__current_player} wins!', False, True)
            elif "" not in map(lambda x: x[0], self.__board):
                # Checks if board is full
                return MoveResult(f'Board is full - Game Over', False, True)
            else:
                self.__current_player = self.__player_name_1 if self.__current_player != self.__player_name_1 else self.__player_name_2
                self.__last_move_instruction = None  # need to be None that self.get_move_instruction() return defaut message.
                self.__last_move_instruction = self.get_move_instruction()

            if self.__vs_bot and not self.__last_move_instruction.game_won and self.__current_player == self.__player_name_2:
                slot_bot = self.__recommend_slot()
                self.__last_move_instruction = self.set_stone(slot_bot)

        else:
            self.__last_move_instruction = MoveResult(f'Please choose a different slot, {self.__current_player}', True, False)

        return self.__last_move_instruction

    def get_move_instruction(self) -> MoveResult:
        """ Returns the move instructions for the current state
        Returns
        -------
        MoveResult
            Information about the current game
        """
        if self.__last_move_instruction:
            return self.__last_move_instruction
        name = self.__current_player + ("'" if self.__current_player[-1].lower() == 's' else '\'s')
        return MoveResult(f"It is {name} turn. Place a stone into a marked column.", False, False)

    def __set_slot(self, slot: int):
        """Sets the stone in the provided slot for the current player"""
        col = self.__board[slot - 1]  # selects to correct slot where the stone should be placed in

        # Calculates the last open index, for how far the stone will fall down
        last_open_index = len(col) - 1 - col[::-1].index("")  
        stone = "X" if self.__current_player == self.__player_name_1 else "O" 
        col[last_open_index] = stone

    def __check_status(self, slot: int) -> bool:
        """checks if current player has won with placing the stone in slot"""

        slot = slot - 1  # slot is 0-index rather than 1 of the normal game.
        stone_type = "X" if self.__current_player == self.__player_name_1 else "O"

        # index_last_stone is a coordinate of the last placed stone from the last player
        index_last_stone = (slot, self.__board[slot].index(stone_type))

        def filter_list(lst):
            """removes out of bound coordinates"""
            return [t for t in lst if -1 < t[0] < 7 and -1 < t[1] < 6]

        def map_values(lst):
            """replaces coordinates with current values"""
            return map(lambda x: self.__board[x[0]][x[1]], lst)

        # Four list with coordinates of the board are generated. 
        # They are around the coordinate index_last_stone and reach out 3 extra coordinates in each direction
        vertical = list(map(lambda x: (index_last_stone[0], x + index_last_stone[1] - 3), range(7)))
        horizontal = list(map(lambda x: (x + index_last_stone[0] - 3, index_last_stone[1]), range(7)))

        # The diagonals are the product of the horizontal and vertical lines
        # On diagonal which is from a reversed vertical line
        diagonal_1 = list(map(lambda x, y: (y[0], x[1]), vertical, horizontal))
        diagonal_2 = list(map(lambda x, y: (y[0], x[1]), vertical[::-1], horizontal))

        check_placed_stone = [vertical, horizontal, diagonal_1, diagonal_2]

        # Filters out unwanted coordinates and maps the coordinates to the real values
        for i in range(len(check_placed_stone)):
            check_placed_stone[i] = list(map_values(filter_list(check_placed_stone[i])))

        # Checks if four stones of the same type are in fact together without space
        for stones in check_placed_stone:
            count_in_row = 0
            for stone in stones:
                if stone == stone_type:
                    count_in_row += 1
                else:
                    count_in_row = 0
                if count_in_row == 4:
                    return True

    def __check_slot(self, slot: int) -> bool:
        """Checks if a stone can be placed within the slot"""
        col = self.__board[slot - 1]
        return "" in col  # Will be true if that slot has an empty space 

    def __recommend_slot(self) -> int:
        """Selects a random and valid slot for the bot"""
        # map(lambda x: x[0], self.__board) => will create a list with stones from the first row

        # [i for i, x in enumerate(...) if x == ""] => will remove all the slot which has a stone
        # in the top row, removes all full columns
        # The generated list has numbers corresponding to the slot indexs, which are not full and are suitable
        # for the bot to place a stone
        open_slots = list([i for i, x in enumerate(map(lambda x: x[0], self.__board)) if x == ""])
        return open_slots[random.randint(0, len(open_slots) - 1)] + 1


if __name__ == '__main__':
    game_1 = ConnectFour(True, "Hans")
    print(game_1.player_name_1)
    print(game_1.player_name_2)

    print(game_1.get_board)

    print(game_1.get_move_instruction().message)

    slots = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7]

    for slt in slots:
        print("#######################")
        print("Place stone in: " + str(slt))
        game_1.set_stone(slt)
        print(game_1.get_board())
