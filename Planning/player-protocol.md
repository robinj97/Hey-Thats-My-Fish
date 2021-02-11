Player Protocol
===
Calling Sequence
-----
- set_color is called once to each player to set each individual players respective colors for the game.
- get_placement is called to each player (in move-order) until each player has placed their required amount of penguins
- get_move is called on each player (in move-order) until the game ends. No specific total number of calls
- end_game is called once at the end of the game to show that the game has ended.

- kick_player can be called at any time (when a player has cheated or failed)


------------------------
Dependencies
--------
- The order of which they can be called is the same as calling sequence. 
    - get_placement will never be called before set_color
    - All get_move calls will come after all get_placement calls
    - end_game will only be called last
- get_placement and get_move require a valid return value, otherwise kick_player will be used to kick the player

