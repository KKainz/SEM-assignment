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
    def __init__(self, vs_bot: bool, player_name_1: str, player_name_2: str = None):
        self.__vs_bot = vs_bot
        self.__player_name_1 = player_name_1 if player_name_1 else "Player" if vs_bot else "Player 1"
        if vs_bot:
            self.__player_name_2 = "Bot"
        else:
            self.__player_name_2 = player_name_2 if player_name_2 else "Player 2"

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
        return self.__player_name_1

    @property
    def player_name_2(self) -> str:
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

        Attributes:
        -------------
        slot: int
            Slot Player wants to place the stone in

        Returns:
        ----------
        MoveResult
            Information about the current game
        """
        if self.__check_slot(slot):
            self.__set_slot(slot)

            if self.__check_status(slot):
                self.__last_move_instruction = MoveResult(f'{self.__current_player} wins!', False, True)
            elif "" not in map(lambda x: x[0], self.__board):
                return MoveResult(f'Board is full - Game Over', False, True)
            else:
                self.__current_player = self.__player_name_1 if self.__current_player != self.__player_name_1 else self.__player_name_2
                self.__last_move_instruction = None
                self.__last_move_instruction = self.get_move_instruction()

            if self.__vs_bot and not self.__last_move_instruction.game_won:
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
        return MoveResult(f"It is {name} turn. Place a stone into a marked column", False, False)

    def __set_slot(self, slot: int):
        if 1 > slot > 7:
            return

        col = self.__board[slot - 1]
        last_open_index = len(col) - 1 - col[::-1].index("")
        place = "X" if self.__current_player == self.__player_name_1 else "O"
        col[last_open_index] = place

    def __check_status(self, slot: int) -> bool:
        """checks if current player has won with placing the stone in slot"""

        slot = slot - 1
        stone_type = "X" if self.__current_player == self.__player_name_1 else "O"
        index_last_stone = (slot, self.__board[slot].index(stone_type))

        def filter_list(lst):
            """removes out of bound coordinates"""
            return [t for t in lst if -1 < t[0] < 7 and -1 < t[1] < 6]

        def map_values(lst):
            """replaces coordinates with current vaules"""
            return map(lambda x: self.__board[x[0]][x[1]], lst)

        vertical = list(map(lambda x: (index_last_stone[0], x + index_last_stone[1] - 3), range(7)))
        horizontal = list(map(lambda x: (x + index_last_stone[0] - 3, index_last_stone[1]), range(7)))
        diagonal_1 = list(map(lambda x, y: (y[0], x[1]), vertical, horizontal))
        diagonal_2 = list(map(lambda x, y: (y[0], x[1]), vertical[::-1], horizontal))

        check_placed_stone = [vertical, horizontal, diagonal_1, diagonal_2]

        for i in range(len(check_placed_stone)):
            check_placed_stone[i] = list(map_values(filter_list(check_placed_stone[i])))

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
        col = self.__board[slot - 1]
        return "" in col

    def __recommend_slot(self) -> int:
        open_slots = list([i for i, x in enumerate(map(lambda x: x[0], self.__board)) if x == ""])
        return open_slots[random.randint(0, len(open_slots) - 1)] + 1


if __name__ == '__main__':
    game_1 = ConnectFour(True, "Hans")
    print(game_1.player_name_1)
    print(game_1.player_name_2)

    print(game_1.get_board)

    print(game_1.get_move_instruction().message)

    exit(0)
    # for later testing place some stones and print board
    slots = [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7]

    for slt in slots:
        print("#######################")
        print("Place stone in: " + str(slt))
        game_1.set_stone(slt)
        print(game_1.get_board)
