# How AI is behaving in our game of Connect Four

Since developing a bot that makes valid moves was our main priority, the AI of our Connect Four game 
is far from acting intelligent.

## Behavior
The computer opponent searches for an open slot on the board and then selects a random slot to place 
a stone.

## Method used
1. A list containing all still available open slots of the board is created. 
2. The bot chooses a one of these open slots using the 'random.randint'-function. To do so, all slots 
that still have an open space left are determined with a lambda function and then transferred into a 
list. From this list the bot chooses a slot for his play move.
 