Game states
------------------
 Creation of game
 
    There will need to be some initial game state for when the game is being initialized, this will be the game
    state that is called when the board is being initalized but not populated. This will just be represented by 
    initalizing classes.
    
 Game playing
 
    This is the main game state for the game. This occurs as soon as the board is populated with tiles,
    as soon as players place their penguins and start playing. This game state is the same for before players place
    all penguins, and after. 
    
    There are several data representations that need to be tracked in the playing game state. Firstly, the array
    of the tiles need to be returned in this game state. This is so that the referee knows the locations of tiles
    in order to then further use that knowledge to evaluate legal moves and such.
    In addition to this, the playing game state need to be tracking the coordinates of players and the coordinates
    they wish to move to. Using this information, it will be sent to the external referee and validate. 
    This data representation will be an array of coordinates.
    
    The available moves array will also need to be tracked and sent to the referee, it will be used to validate each
    move to be made against this array.
    
 End of game state
 
    This will be the end of the game. This is how the external interface determines if the game is over. This means
    that this game state need to contain the array of possible moves and array of players. Once a player has 0 possible
    moves, it will be removed from this array until one player remains. Once this happens, the game determines that
    this player is the winner.
    
 
 External Interface
 ------------------
 The external interface is some server sided piece of code that sends and recieves player data. This includes
 a single player's penguin coordinates, as well as a single players available moves. The interface will use this
 information to determine if a player is making a valid move, by cross referencing the move with the list of
 available moves supplied to the interface. 
 
 The interface also needs to be supplied information about the board, meaning the coordinates of tiles that will serve
 as the reference point for the availableMoves() function. 
 
 To summarize, the external interface needs to be supplied data about the locations of tiles, as well as the locations
 of each individual penguin and its player. The final two pieces of information requires will be the move a single player
 will make, this will be sent to the external referee, as well as a list of possible moves this player can make, to cross
 check if this move is valid.