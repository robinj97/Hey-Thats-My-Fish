Hey Thats My Fish!
==================
Welcome to a fully functional version of Hey Thats my Fish! This game has minimal GUI implimentation as it only renders a single state at a time. The game is fully functional using the command line and implements AI player strategies one can use to compete against or use in a tournament to be implemented in the future.



- Common: Contains all the code for required assingments. This includes the visual and the logistics part.
- Planning: Contains all documents pertaining to planning ahead. Including planning of how to represent a game state, as well as how to represent games for an external interface to see. This folder also includes self-eval forms.a

- RoadMap
    - Game tree (game_tree.py) deals with constructing a game tree from a given state
    - Game state (State.py) deals with penguins and player as well as moving and placing penguins (game state contains a board)
    - Game board (FishBoard.py) deals with the storing and changing of tiles (contains a 2D array of FishTile objects) as well as determining if a move is possible 
    - Tile (FishTile.py) deals with storing how many fish are on a tile
    - View is the class that contains the graphical elements. These methods take in the game state or board to draw
    - Strategy (strategy.py) is the class that contains the algorithm for choosing which move to make in order to get adjacent to previous players penguin that was moved
    - Referee (Referee.py) is the class that contains the logic for the referee interactions 
    - Player (Player.py) is an implementation of a Player that can return placements and moves upon being prompted

- How to run test harness (from the folder named 6)

    - ./xstrtegy

- How to run unit tests (TEST ME)

    - ./xtest 

    - This will automatically run all tests. The individual test files are in Common folder and are named:
        
        - test_game.py
        - test_state.py
        - test_board.py
        - test_strategy
        - test_referee 
        - test_player
