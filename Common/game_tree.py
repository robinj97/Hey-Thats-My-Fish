import copy
import State

# Data Def:
# AN ACTION IS ONE OF:
# -- ("Move", (Int,Int), (Int,Int), String)
#   where the first (Int,Int) is the starting position (x,y)
#   where the second (Int,Int) is the ending position (x,y)
#   where the string is the color of the player making the move


# A game tree represents an entire game starting from the given state
# Each state is connected to its legal successor states through the get_child_nodes method
# Each individual connection between a state and a successor is traversed/represented by the Action it takes to go from state to successor
class GameTree():

    # state -> tree
    # The constructor takes in a state and constructs a game tree with the state as the root node
    # The created tree represents an entire game starting from the given state
    # Fields:
    # - state = represents the state that is in 'focus' (the state that getChildNodes, actionQuery, and functionQuery are called on)
    # - path = represents the path from the root state to the state that is currently in 'focus'
    #  -- used for being able to traverse the tree and get information out of anywhere in the tree
    # - end = boolean representing if the game is over
    def __init__(self,state):
        # Make sure state is valid by number of penguins = 6-p  - for each player
        if state.phase == "Placing":
            raise ValueError("Not all penguins are placed")
        
        self.state = state 
        self.path = []

        self.end = not self.state.any_moves()
            
    # String -> Boolean
    # Determines if the given player (string representing their color) is stuck (can make no more moves/ is being skipped)
    def is_stuck(self, player):
        return not self.state.pos_list_contains_valid_move(self.state.penguin_map[player])
    

    # Action --> void
    # Throws an error if the action is not a valid action (this is exceptional behavior because the validity can be checked in action_query)
    # Moves forward a layer in the tree to the child that results from the given action
    # used to traverse the tree
    def moveForwardTree(self, action):
        next_state = self.action_query(action)
        if next_state == False:
            raise ValueError("Not a valid action")
        else:
            self.path.append(self.state)
            self.state = next_state
            self.end = not self.state.any_moves()

    # void --> void
    # Throws an error if the state in 'focus' is already the root node of the tree
    # Moves back a layer in the tree to the parent node of the state in 'focus'
    # used to traverse the tree
    def moveBackTree(self):
        if len(self.path) <= 0:
            raise ValueError("Already at root node")
        else:
            self.state = self.path[-1]
            self.end = False
            del self.path[-1]

    #Void -> List of (Pair of (action, state))
    #returns a list of pair of Action and State representing the child nodes of the tree and the action required to reach them
    def get_child_nodes(self):
        #current turn
        current_turn = self.state.player_list[self.state.turn]
        #look at penguins of current turn
        movable_penguins = self.state.penguin_map[current_turn]
        #get availible moves for those penguins
        possible_moves = []
        for penguin in movable_penguins:
            for availible_move in self.state.board.availibleMoves(penguin[0],penguin[1], self.state.penguin_map):
                possible_moves.append(((penguin[0],penguin[1]),(availible_move[0],availible_move[1])))
                
        #pair the moves with the state that results from them
        action_state_pairs = []
        for move in possible_moves:
            next_state = copy.deepcopy(self.state)
            next_state.move_penguin(move[0][0],move[0][1],move[1][0],move[1][1],current_turn)
            action = ("Move", (move[0][0],move[0][1]),(move[1][0],move[1][1]),current_turn)
            action_state_pairs.append((action,next_state))
        return action_state_pairs

    #Void -> List of (Pair of (action, tree))
    #returns a list of pair of Action and Tree representing the child nodes of the tree and the action required to reach them
    def get_child_trees(self):
        child_nodes = self.get_child_nodes()
        action_tree_pair = []
        for action,state in child_nodes:
            action_tree_pair.append((action,GameTree(state)))
        return action_tree_pair

    # (action) --> (state)
    # Takes in an action, and checks if the action can be performed on the root state
    # Returns the resulting state of applying the action or false if the action can't be applied
    # False is returned over throwing an error since it may be that the user will test many actions,
    #       so receiving an action that does not work is not "exceptional" behavior
    def action_query(self, action):
        if action[0] == "Move":
            # Make a copy of the state so original state does not get mutated
            copy_state = copy.deepcopy(self.state)
            
            #Call move function on copied state and retun this new state
            try:
                copy_state.move_penguin(action[1][0],action[1][1],action[2][0],action[2][1],action[3])
            except ValueError:
                return False
                
            return copy_state


    # (state -> x) --> List of (Pair of (action, x))
    # Takes in a function and applies the function to all direct child nodes in the tree
    # Returns a pair of action (required to get to the child node) to the result of applying the function
    def apply_function_query(self,func):
        # get list of child states and actions it takes to get there
        action_state_pairs = self.get_child_nodes()
        # apply the function to the states
        action_func_pair = []
        for action, state in action_state_pairs:
            action_func_pair.append((action, func(state)))
        return action_func_pair
