## Self-Evaluation Form for Milestone 5

Under each of the following elements below, indicate below where your
TAs can find:

- the data definition, including interpretation, of penguin placements for setups 
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/9d0cd19f196f9f1803fc4729e42e1c6e61df078a/Fish/Player/strategy.py#L20-L21
    - This same definition is listed in all of the classes that use placements (so it would be clear for any new maintainer)
    - A data representation and an interpretation of each piece of the data is given

- the data definition, including interpretation, of penguin movements for turns
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/9d0cd19f196f9f1803fc4729e42e1c6e61df078a/Fish/Player/strategy.py#L15-L18
    - This same definition is listed in all of the classes that use placements (so it would be clear for any new maintainer)
    - A data representation and an interpretation of each piece of the data is given

- the unit tests for the penguin placement strategy 
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/9d0cd19f196f9f1803fc4729e42e1c6e61df078a/Fish/Player/test_strategy.py#L29-L73
    - Different valid test cases are done as well as another test case that tests an invalid state
  
- the unit tests for the penguin movement strategy; 
  given that the exploration depth is a parameter `N`, there should be at least two unit tests for different depths 
  - https://github.ccs.neu.edu/CS4500-F20/warrencity/blob/9d0cd19f196f9f1803fc4729e42e1c6e61df078a/Fish/Player/test_strategy.py#L76-L137
    - Test cases of different values of N are done, as well as test cases for if the game ends or the given player runs out of moves before the end of plannning
  
- any game-tree functionality you had to add to create the `xtest` test harness:
  - no new functionality had to be added to the game-tree for the xtree to work.
    - the only functionality in xtree is for converting between the common ontology and our ontology, for checking if the valid moves are 1 tile away from the desired tile, and for doing the tie breaker between potential moves
    - the only functionality added to game-tree that did not already exist was for checking if a player is stuck which was missing from our original game-tree assignment and was used in the strategy assignment
    
    
  - where the functionality is defined in `game-tree.PP`
  - where the functionality is used in `xtree`
  - you may wish to submit a `git-diff` for `game-tree` and any auxiliary modules 
   

**Please use GitHub perma-links to the range of lines in specific
file or a collection of files for each of the above bullet points.**

  WARNING: all perma-links must point to your commit "9d0cd19f196f9f1803fc4729e42e1c6e61df078a".
  Any bad links will result in a zero score for this self-evaluation.
  Here is an example link:
    <https://github.ccs.neu.edu/CS4500-F20/warrencity/tree/9d0cd19f196f9f1803fc4729e42e1c6e61df078a/Fish>

