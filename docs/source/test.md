# Tests

Due to the game design we approached, we only tested the initializer method of the two classes 
_ConnectFour_ and _MoveResult_. The reason is that most of the class methods cannot be tested on their own, either 
they are dependent on game state or they are private methods. Therefore we decided to test the gameplay which should
cover most of the methods.

ConnectFour:
 * Names need to be different
 * Player name 2 ignored when playing vs. bot
 * set_stone method (gameplay):
   * Move not possible when slot is full
   * Check if game is won for all directions