=Referee component
==================

## Relevant Information
A referee must record:
- a game state for a Fish game, which contains:
    - information about the board (tiles), locations of penguins, order of turns, score of players
- a list of Players of the game 
    - for asking each player for a placement/move on their turn and alerting them to start/end of game
- a list of Observers of the game
    - for updating the observers about the game

A referee does the following internal operations:

- Sets up a board
- Checks validity of a move
- Checks if player is cheating
    - Remove player from game
- Inform game observers about ongoing actions
- When GameOver, reports the scores and reports cheaters
 
## Use Cases

A tournament manager can use the referee to:
- coordinate the running of a game of players (starting and ending the game)
- gain information on who won this single game.
- gain information on which players cheated 

## External Interface
The interface of a referee must accommodate a Tournament Manager

create-referee

    Create an initial Referee for a game with a given list of Players

 add-observer

    Adds an observer to receive updates about the game

 start-game

    Tells the referee to start the game

 
 get-game-info (communicating with tournament manager regarding winners and cheaters)

    Retrieves info about the current game: who won and who cheated. 
 
