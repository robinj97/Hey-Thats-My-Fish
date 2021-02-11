## Self-Evaluation Form for Milestone 6

Indicate below where your TAs can find the following elements in your strategy and/or player-interface modules:

The implementation of the "steady state" phase of a board game
typically calls for several different pieces: playing a *complete
game*, the *start up* phase, playing one *round* of the game, playing a *turn*, 
each with different demands. The design recipe from the prerequisite courses call
for at least three pieces of functionality implemented as separate
functions or methods:

- the functionality for "place all penguins"
  
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L129-L151
  - In the overall running of the game, the run_placement_phase deals with players placing their penguins

- a unit test for the "place all penguins" funtionality 

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L103-L115
  - tests that all penguins have been placed after the run_placement_phase has been executed

- the "loop till final game state"  function

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L157-L179
  - The run_move_phase loops through asking for moves until the game ends
    - the overall start_game (line 100) runs the entire game (setup -> placing -> moving -> end)

- this function must initialize the game tree for the players that survived the start-up phase

  - We store the data in our referee as a game_state and it is initilized in the setup_game method
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L116

- a unit test for the "loop till final game state"  function

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L57-L67
  - a full game is ran and then it is checked to make sure the game successfully ended
    - the moving phase specifically is test on line 118:
    - - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L118-L140

- the "one-round loop" function

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L157
  - We do not have a helper method for this as it is 2 lines of code within a try-except. We did not see it necessary to use a helper method for this part as the code does not look complicated within the try-except format. 


- a unit test for the "one-round loop" function

  - We do not have a unit test for this function since we do not have a function that separately deals with this. It was within the 2 lines of code we needed. We only created unit tests for the public facing methods (and the 4 main helpers that correspond to each setup, placing, moving,and ending a game).
  - We only have unit tests for the whole move phase:
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L118

- the "one-turn" per player function

  - We do not have a individual function for this. We have different phases of the game where either a placement is tried or a move. This is done in the link below and the turn is kept track of in our state. 
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L157 


- a unit test for the "one-turn per player" function with a well-behaved player 

  - We do not have a helper method for this as it is 2 lines of code within a try-except. We did not see it necessary to use a helper method for this part as the code does not look complicated within the try-except format. 
  - We only have unit tests for the whole move phase:
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L118

- a unit test for the "one-turn" function with a cheating player

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L70-L79
  - Although we don't have a unit test for one-turn and a player failing, we have a unit test for a game where the player cheats on their first turn

- a unit test for the "one-turn" function with an failing player 

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/test_referee.py#L70-L79
  - Although we don't have a unit test for one-turn and a player failing, we have a unit test for a game where the player cheats on their first turn (our code deals with cheating and failing in the same way: by calling the move method and both will return an error since it is either structured wrong or is an invalid move)

- for documenting which abnormal conditions the referee addresses 

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L36-L37
  - Failing  (wrong structure returned) and cheating (invalid moves give) are both defined as abnormal behaviors that will cause a player to be kicked during the placement or movement phases


- the place where the referee re-initializes the game tree when a player is kicked out for cheating and/or failing 

  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish/Admin/referee.py#L139
  - The data that we kept in our referee is stored as a game_state and the state is updated on line 139 when a player is kicked

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "4b53136eed0be40fa9b7aa03f725ed21f4aafa96".
  Any bad links will be penalized.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/warrencity/tree/4b53136eed0be40fa9b7aa03f725ed21f4aafa96/Fish>

