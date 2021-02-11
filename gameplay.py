from connectfour import connectfour as cf
from os import system, name

def clear_screen():
    if name == 'nt':
        _ = system('cls')  # windows
    else:
        _ = system('clear')  # others

if __name__ == '__main__':
    print("You can exit the game with \"0\", you place stones with number 1 to 7")

    print("Please enter name for player 1:")
    player1 = input()

    print("Please enter name for player 2 (leave empty to play against bot):")
    player2 = input()

    vs_bot = False if player2 else True

    game = cf.ConnectFour(vs_bot, player1, player2)

    clear_screen()

    print(game.get_board())
    print(game.get_move_instruction().message)

    while True:
        inp = input()

        if not inp.isnumeric() or len(inp) != 1:
            print("Please type in number")
            continue

        inp = int(inp)

        if inp == 0:
            break  # Exit the game

        game.set_stone(inp)

        move_instructions = game.get_move_instruction()
        if move_instructions.game_won:
            clear_screen()
            print(game.get_board())
            print(move_instructions.message)
            break

        if move_instructions.failed_move:
            print(move_instructions.message)
            continue

        clear_screen()

        print(game.get_board())
        print(move_instructions.message)

