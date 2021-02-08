
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

    @property
    def get_board(self) -> str:
        """str: ASCII style representation of the board"""
        ret = ""
        first_line = "".join(list(map(lambda x: " " + str(x + 1), range(7)))) + "\n"
        for row in range(6):
            ret += "│"
            for col in range(7):
                item = self.__board[col][row]

                if row == 0 and item == "":
                    first_line += " V"

                ret += (item if item else " ") + "│"
            ret += "\n"
        return first_line + "\n" + ret + "└─────────────┘"

    def set_stone(self, slot: int) -> MoveResult:
        pass

    def get_move_instruction(self) -> MoveResult:
        pass

    def __set_slot(self, slot: int):
        pass

    def __check_status(self) -> str:
        pass

    def __check_slot(self, slot: int) -> bool:
        col = self.__board[slot - 1]
        return "" in col

    def __recommend_slot(self) -> int:
        pass


if __name__ == '__main__':
    game_1 = ConnectFour(True, "My Name")
    print(game_1.player_name_1)
    print(game_1.player_name_2)

    print(game_1.get_board)
