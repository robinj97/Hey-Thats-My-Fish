import FishBoard
import copy

POSSIBLE_COLORS = ["red", "white", "brown", "black"]

#this class represents a game state of the Fish game
# Fields:
# board = an instance of a Fishboard which stores the state of the board
# penguin_map = a map of color (as a string) to a list of points (ex: [(x1,y1),(x2,y2),...])
#       - the list of points represents the locations of the penguins for the player whose color is the key of the map
# player_list = a list of Player, Color pairs where Player is an object that stores information about the player
#       - the list also represents the move order where the 1st player is in index 0 and 2nd player is in index 1 and onward
# score_map = a map of player's color to an integer representing the amount of points they have scored in the game
# phase = phase that the game is currently in (one of: "placing", "moving", "end")
class State:
    def __init__(self, fishboard, list_of_players, penguin_map = {},score_map = {}, turn = "", phase = "Placing"):
        self.board = fishboard
        self.phase = phase

        #Validation to make sure player count is in desired range
        if (len(list_of_players) >= 5) or (len(list_of_players) < 0):
            raise ValueError("Number of players should be between 0 and 4")

        #Order of players 
        #stored as a list of color (where color is represented by a string)
        # - for now we just assign color in the order of "red", "white", "brown", "black"
        for player_color in list_of_players:
            if player_color not in POSSIBLE_COLORS:
                raise ValueError("Invalid color given: " + player_color)
            if list_of_players.count(player_color) > 1:
                raise ValueError("Two players cannot share the same color: " + player_color)
        self.player_list = list_of_players

        # Storing the value of the amount of penguins each player gets in this game
        self.num_penguins_per_player = 6 - len(self.player_list)
        
        #List of kicked players
        #Stored as List of String (where the string represents the player's color)
        self.kicked_players = []

        # Represents which player's turn it is currently
        # stored as the index in the player list
        self.turn = 0
        if len(turn) > 0:
            self.turn = list_of_players.index(turn)
        

        # store penguin locations and player's color
        # - "Player Color" : [[x1,y1],[x2,y2],...]
        # - "red", "white", "brown", "black
        # in this map a player is simply represented by their color (in string format)
        self.penguin_map = {}
        if len(penguin_map) > 0:
            self.penguin_map = penguin_map
        else:    
            for player in self.player_list:
                self.penguin_map[player] = []

        # Store each colors points as a list of points
        #  - :Player Color" : int
        # - "red", "white", "brown", "black
        # in this map a player is simply represented by their color (in string format)
        self.score_map = {}
        if len(score_map) > 0:
            self.score_map = score_map
        else:    
            for player in self.player_list:
                self.score_map[player] = 0

    def done_placing(self):
        return self.done_placing    
    
    #List of Points -> Boolean
    # - Points is a tuple (2 values) of integers = (x,y)
    #takes in a list of positions and checks if any moves are valid starting from those poitions
    #  -True if any position's move is valid, False if no position's move is valid
    def pos_list_contains_valid_move(self, pos_list):
        for pos in pos_list:
                if len(list(self.board.availibleMoves(pos[0],pos[1],self.penguin_map))) > 0:
                    return True
        return False
        
        
    #Void -> Boolean
    #Determines if any player can make a move (returns true if any player can or false if no player can)
    def any_moves(self):
        #gather all penguin positions
        cumulative_positions = []
        for penguin_pos_list in self.penguin_map.values():
            cumulative_positions.extend(penguin_pos_list)
            
        #see if any penguin can move
        return self.pos_list_contains_valid_move(cumulative_positions)
        
    #Void -> Boolean
    #Check to see if the current board and penguin map imply that the next turn should be skipped 
    def should_skip_next(self):
        return not self.pos_list_contains_valid_move(self.penguin_map[self.player_list[self.turn]])
        
    #Void -> Void
    #skips the turn - meaning it changes who has the next move but does not edit the board or penguins 
    def skip_next(self):
        if self.turn == len(self.player_list) - 1:
            self.turn = 0
        else:
            self.turn += 1
            
    # (Int) xpos, (Int) ypos, (String) current_player --> (Void)
    # Places a certain players penguin at x,y positions unless tile is empty or occupied
    def place_penguin(self,x_pos,y_pos,player_color):
        # Check if it is player's turn?
        if player_color != self.player_list[self.turn]:
            raise ValueError("It is not the" + player_color + " player's turn")

        #Make sure the color is valid
        if player_color not in self.penguin_map:
            raise ValueError("Not a valid color")

        # Check if the player has maximum number of penguins
        if len(self.penguin_map[player_color]) >= self.num_penguins_per_player:
            raise ValueError("The player has placed the maximum number of penguins")

        # Check if tile value is above 0
        tiles = self.board.getBoardCopy()
        if tiles[x_pos][y_pos].numFish == 0:
            raise ValueError("Cannot place on empty tile")


        # Check if tile has other player
        for position_list in self.penguin_map.values():
            if (x_pos,y_pos) in position_list:
                raise ValueError("Cannot place on tile that already contains a penguin")

        # Place penguin
        self.penguin_map[player_color].append((x_pos,y_pos))

        # Move to next turn
        if self.turn == len(self.player_list) - 1:
            self.turn = 0
        else:
            self.turn += 1
            
        #if the last penguin was placed, check to see if any turns should be skipped
        if len(self.penguin_map[self.player_list[len(self.player_list) - 1]]) == self.num_penguins_per_player:
            # Sets the game to moving phase since all penguins have been placed
            self.phase = "Moving"
            
            while self.any_moves():
                if self.should_skip_next():
                    self.skip_next()
                else:
                    break
            # No more avaialble moves means game is over, sets phase to End        
            if not self.any_moves():
                self.phase = "End"

    # (Int) starting x, (Int) starting_y, (Int) ending x, (Int) ending y, (String) Player_color --> void
    # Moves the penguin of a player if it is that players turn and the move is valid. Void method just changes coordinates of penguin
    def move_penguin(self,x_start,y_start,x_end,y_end,player_color):
        # Check if it is player's turn?
        if player_color != self.player_list[self.turn]:
            raise ValueError("It is not the" + player_color + " player's turn")
        # Does this penguin belong to this player
        if (x_start,y_start) not in self.penguin_map[player_color]:
            raise ValueError(player_color + " does not have a penguin in the given position: " + str(x_start) + ", " + str(y_start))

        # If not all are placed then no move
        # If length of values =! 6 - len(player_list)

        if self.phase == "Placing":
            raise ValueError("Not all penguins have been placed, cannot move")

        # Check if valid move straight line
        valid_moves = list(self.board.availibleMoves(x_start,y_start,self.penguin_map))
        if (x_end, y_end) not in valid_moves:
            raise ValueError("Given starting and ending coordinates do not define a valid move")

        #move penguin (change tuple)
        index =  self.penguin_map[player_color].index((x_start,y_start))
        self.penguin_map[player_color][index] = (x_end,y_end)
        #remove tile
        score_number = self.board.get_score(x_start,y_start)
        self.board.removeTile(x_start,y_start)

        self.score_map[player_color] += score_number

        if self.turn == len(self.player_list) - 1:
            self.turn = 0
        else:
            self.turn += 1  
            
        #if some player has a move, skip turns that need to be skipped until it is the turn of a player with a possible move 
        while self.any_moves():
            if self.should_skip_next():
                self.skip_next()
            else:
                break
        if not self.any_moves():
            self.phase = "End"

    # (string) --> void
    # Kicks a player out of the game
    def kick_player(self,player_color):
        #check to make sure player exists
        if not player_color in self.player_list:
            raise ValueError("Player does not exist")
        
        # Remove player's penguins
        del self.penguin_map[player_color]
        # Remove player's score
        del self.score_map[player_color]
        # Remove player from playerlist
        self.player_list.remove(player_color)
        # Add player to kicked list
        self.kicked_players.append(player_color)
        # Makes sure there is no index out of bounds if a player is kicked
        if self.turn == len(self.player_list):
            self.turn = 0

        



        


    

        
