#Data Def:
#Move = ("move", (Int,Int), (Int,Int)) 
#   where the first tuple of integers is the starting position in (x,y) and the second tuple is the ending position in (x,y)
#Placement = ("placement", (Int,Int)) 
#   where the tuple of integers is the desired placement position in (x,y) 

# String --> Void
# Alerts a player that the given player (represented as the string of their color) has been kicked from the game
# Can be called at any time (as a player may fail or cheat at any time)
def kick_player(color):

# String -> Void
# Takes in a string representing the color of this player
# Called once at the beginning of each game 
# Represents the start of a game
def set_color(color):

# state --> placement
# - where a placement is a tuple of the string "placement" and a tuple of 2 integers representing position (x,y)
# - example: ("placement", (1,2))
# Takes in a game state and uses it to return a placement action (represented by a tuple of "placement" and a pair of integers for the position)
# Called once for the individual player's turn. Expects a placement given back(as a return value) based off the given state
def get_placement(state):

# state --> move
# - where a move is tuple of of the string "placement", a tuple of 2 integers representing starting position (x,y), and a tuple of 2 integers representing ending position (x,y)
# - example: ("move", (1,2), (0,1)) 
# Takes in a game state and uses it to return a move action (represented by a tuple of "move", a pair of integers for the starting position, and a pair of integers for the ending position)
# Called once for the individual player's turn. Expects a move given back(as a return value) based off the given state
def get_move(state):

# state --> void
# Takes in a ending game state that has final scores for players. This function will be used to communicate game winner(s) and scores. 
# Called once at the end of the game
# Represents the end of a game
def end_game(state):






