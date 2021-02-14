# Game design

## Design principle
This game is build with the _YAGNI_ software design principle. YAGNI stands for _"You aren't gonna need it"_
and signals that you probably need the program only once. YAGNI is a extension to the _KISS_ principle with stands for 
_"Keep it simple and Stupid"_.  
Therefore the program will be easy to understand but is not intended to have a lot of changes over its lifetime.

## Implementation
The main class only has two readonly properties for the names and everything else is handled with three public methods and
private methods as helper methods. One extra class (_MoveResult_) is used to inform the player about the current state.

### get_board()
This method is used to see the board in its current state. It's only a ASCII representation and not intended to 
transmit information to other classes or methods.

### set_stone(slot: int)
The _set_stone_ method has the main logic for the game and provides interaction with the game.
With the _slot_ parameter you tell the game logic where you want to place the next stone. The result, after a player 
sets a stone, is a _MoveResult_ and only transmits information about the current state of the game to the player.  
The Method will check and do a view things:

 * If it's possible to place the stone in the slot
 * Actually places the stone
 * Check if the current player has won the game with the last move
 * Check if the game board is full
 * Plays as the bot

### get_move_instruction()
This method will provide information for the first turn of the game and is used to provide a default message for the
_set_stone_ method.  

## Game design choices

The game is desinged to be simple and therefore doesn't allow you to save/load a game, manipulate the state other then
to set a stone, change the board ouput style or get specific information about the board and the state. Therefore the
implementaion is really easy.

### The game board
The state of the game is stored in a list of lists of strings. The hole board is initialized with empty strings.
The first list in this hierarchy represents the columns and there are a total of seven sublists. 
Within the seven sublists are the strings which represent the actual stones and there are 6 entries for each sublist 
which represent the rows of the specific column.
The first entry of a sublist is top of the game board.

&nbsp;&nbsp;----> X direction  
&nbsp;|  
&nbsp;|&nbsp;&nbsp; _game board_  
&nbsp;|  
&nbsp;|  
&nbsp;| O X X  
&nbsp;| X O X O  
V  
Y direction

```python
    board = [
        ["", "", "", "", "O", "X"],  # Column 1
        ["", "", "", "", "X", "O"],  # Column 2
        ["", "", "", "", "X", "X"],  # Column 3
        ["", "", "", "", "", "O"],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""]
        # Row 1, Row 2, Row 3...
    ]
    left_bottom_stone = boar[0][5]  # left_bottom_stone = "X"
```

It is easy to check if the a specific slot is full, the game board is full and to output the game board to the console.

### The current player / Player names
Player 1 will always place "X" as a stone and player 2 an "O". The current player name is stored in 
_"\_\_current\_player"_ and based on this private property the logic knows whos turn it is. It's important to 
change the current player only if it is neceserry and the two player names need to be different.

### Move instruction
A extra class called _MoveResult_ will transmit information about the state of the game to the player. One could
use a tuple with the three needed values but we decided aginst the tuple because it is not apparent which tuple item
holdes the wanted information.

### Set stone
After each stone is set into a slot, the game will first check if the slot can hold the stone or a _MoveResult_ with 
_failed_move_ = True is returned and the current player needs to chose a difrent slot.
  
After each placed stone the method _\_\_check\_status_ checks if there are in fact 4 stones of the same type in a row 
(horizontal, vertical, diagonals) and return a _MoveResult_ with _game\_won_ = True is returned.
The logic only needs to check around the last stone placed, because nothing else is changing the state of the game
other then the last placed stone. The Methon cannot check the complete board at once but was simple to implement.

### Check game won
The private method _\_\_check\_status_ checks if the last placed stone turns out to be a winnig game.
It does this by generating coordinates around the coordinate of the stone by selecting 3 more coordinates in each
direction and putting the cooridnates in seperatet list depending on the direction (horizontal, vertical, diagonals).
```python
vertical = list(map(lambda x: (index_last_stone[0], x + index_last_stone[1] - 3), range(7)))
horizontal = list(map(lambda x: (x + index_last_stone[0] - 3, index_last_stone[1]), range(7)))

# The diagonals are the product of the horizontal and vertical lines
# On diagonal which is from a reversed vertical line
diagonal_1 = list(map(lambda x, y: (y[0], x[1]), vertical, horizontal))
diagonal_2 = list(map(lambda x, y: (y[0], x[1]), vertical[::-1], horizontal))
```

The cooridinates of the lists will be filtered to remove coordinates out of bound and then maped to the real values.

```python
check_placed_stone = [vertical, horizontal, diagonal_1, diagonal_2]

# Filters out unwanted coordinates and maps the coordinates to the real values
for i in range(len(check_placed_stone)):
    check_placed_stone[i] = list(map_values(filter_list(check_placed_stone[i])))
```

After these steps, the logic only needs to count if there are four stones of the same type from the current player
and return true.