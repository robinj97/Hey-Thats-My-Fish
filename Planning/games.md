Data Representation - Gamestate and Tree layout
=========
 - Structure
    - Gamestate given in constructor
    - Tree of possible move sequences generated off the given gamestate


- Initial position given in form of a gamestate
- Run available moves on initial position
- Create nodes from initial position to each final position
- Run recursively

This can be represented by a nested map where each key is a move (starting and ending point). 
All keys inside of a move's map are the list of valid moves that are availible after the move. 
If a move ends the game, that move is mapped to None (Null value) instead of another move-map.



External interface  
======
- This external interface would need to be able to perform the following functions:

    - Check validity of a move

        - Takes a move which is a starting and ending point and returns if the move is valid
    - Given a set of moves, use the final positions of all penguins to THEN determine the remainder of available moves

        - Takes in a list of moves, which is a list of pairs of starting/ending points and provides a list of the moves which are availible after the other moves have been applied
        
- Given the starting gamestate, referees and player AI could apply the moves to the starting gamestate to find what tiles would then be availible and what the score would be
