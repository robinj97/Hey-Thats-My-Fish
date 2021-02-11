
#Data Def:
#Move = ("Move", (Int,Int), (Int,Int)) 
#   where the first tuple of integers is the starting position in (x,y) and the second tuple is the ending position in (x,y)
#Placement = ("Placement", (Int,Int)) 
#   where the tuple of integers is the desired placement position in (x,y) 
from strategy import BestStrategy

# This class represents an implemenation of a Player using the 'BestStrategy' from Strategy.py
class Player:
    def __init__(self):
        self.strategy = BestStrategy()
    #set_color means starting
    #get_placement's next
    #get_move's next
    #end_game means final


    # String --> Void
    # Alerts a player that the given player (represented as the string of their color) has been kicked from the game
    # Can be called at any time (as a player may fail or cheat at any time)
    def has_been_kicked(self, color):
        #this implementation of player does nothing special upon learning a player was kicked
        return

    # String -> Void
    # Takes in a string representing the color of this player
    # Called once at the beginning of each game
    def set_color(self, color):
        #this implementation of player does nothing special upon learning its color
        return

    # state --> placement
    # - where a placement is a tuple of the string "placement" and a tuple of 2 integers representing position (x,y)
    # - example: ("Placement", (1,2))
    # Takes in a game state and uses it to return a placement action (represented by a tuple of "placement" and a pair of integers for the position)
    # Called once for the individual player's turn. Expects a placement given back(as a return value) based off the given state
    # Note: based off of referee specifications, this method will only be called when a player has a valid move to be made
    def get_placement(self, state):
        return self.strategy.place_penguin(state)

    # state --> move
    # - where a move is tuple of of the string "placement", a tuple of 2 integers representing starting position (x,y), and a tuple of 2 integers representing ending position (x,y)
    # - example: ("
    # Move", (1,2), (0,1)) 
    # Takes in a game state and uses it to return a move action (represented by a tuple of "move", a pair of integers for the starting position, and a pair of integers for the ending position)
    # Called once for the individual player's turn. Expects a move given back(as a return value) based off the given state
    # Note: - based off of referee specifications, this method will only be called when a player has a valid move to be made
    #       - By default our Player implementation uses a depth of 2 to plan moves
    def get_move(self, state):
        return self.strategy.move_penguin(state,2)

    # state --> void
    # Takes in a ending game state that has final scores for players. This function will be used to communicate game winner(s) and scores. 
    # Called once at the end of the game
    def end_game(self, state):
         #this implementation of player does nothing special upon learning a game has ended
        return