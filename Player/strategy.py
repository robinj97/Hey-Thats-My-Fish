
import copy
import sys

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"/Common")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Common")
import game_tree as g 
import State as s
import FishBoard as f

# Data Def:
# A move is a = ("Move", (Int,Int), (Int,Int), String)
#   where the first (Int,Int) is the starting position (x,y)
#   where the second (Int,Int) is the ending position (x,y)
#   where the string is the color of the player making the move

#A placement is a = ("Placement", (Int,Int))
#  where the pair of integers is the position (x,y) to place the penguin


#This class represents an implementation of a strategy component to be used by a Player to help decide placements and moves
# - The place_penguin method decides on a placement (a position (x,y)) 
#   - This implementation picks the position in the upper most availible row, and the left most column in that row

# - The move_penguin method decides on a move (a starting position (x,y) and an ending position (x,y))
#   - This implementation picks the move that provides the highest score according to a minimax algorithm
#       (planner tries to maximize score and other players try to minimize the planner's score)

class BestStrategy():
    
    # game_state -> placement
    # where a placement = ("Placement", (Int,Int)) 
    #   -- the tuple of integers is the desired placement position in (x,y) 
    # Given a game state, returns the placement that places the next penguin in the uppermost row and the left-most column in that row
    def place_penguin(self,state):
        player_color = state.player_list[state.turn]
        working_state = copy.deepcopy(state)
        #Iterate through row and check nearest unpopulated tile
        # Return ("placement",(int)(int))
        for y in range(len(state.board.tiles[0])):
            for x in range(len(state.board.tiles)):
                try:
                    working_state.place_penguin(x,y,player_color)
                    return ("Placement",(x,y)) 
                except ValueError:
                    #signals an invalid move was given, try more moves
                    continue
        raise ValueError("Player cannot place a penguin currently")
        
    # (list of actions) --> (list of actions)
    # Sorts the list of actions based on top-left most location 
    # Determines placement of penguin based on tie breaker
    def _action_list_tiebreaker(self, action_list):
        #lowest row starting -> lowest column starting -> lowest row ending -> lowest column starting
        sorted_actions = sorted(action_list, key = lambda a : (a[1][1], a[1][0], a[2][1], a[2][0]))
        return sorted_actions[0]

    # (game_tree) (int) (Action) --> (int)
    # Returns the 'best' value of doing the singular action onto the given tree
    # - either returns just the score (if not looking-ahead more or game is over) or recurses if not done looking-ahead 
    def _get_action_value(self, tree, turns_ahead, action, planning_color):
        #if the player doing the planning cannnot move anymore
        if tree.state.player_list[tree.state.turn] == planning_color and turns_ahead <= 0:
            return tree.state.score_map[planning_color]

        tree.moveForwardTree(action)

        if tree.is_stuck(planning_color) or not tree.state.any_moves():
            score = tree.state.score_map[planning_color]
        elif tree.state.player_list[tree.state.turn] == planning_color:
            score = self._get_best_action(tree, turns_ahead - 1, planning_color)[1]
        else:
            score = self._get_best_action(tree, turns_ahead, planning_color)[1]

        tree.moveBackTree()

        return score

    # (game_tree) (int) --> (Action,int)
    # Returns the 'best' action and score after looking ahead a given amount of turns
    def _get_best_action(self, tree, turns_ahead,planning_color):
        #gets one-layer of action:state pairs
        action_state_pairs = tree.get_child_nodes()
        #for array of scores
        score_action_map = {}

        for action, state in action_state_pairs:
            score = self._get_action_value(tree,turns_ahead,action,planning_color)
            if score in score_action_map:
                score_action_map[score].append(action)
            else:
                score_action_map[score] = [action]

        return self._min_or_max(tree, score_action_map, planning_color)

    # game_tree (Map of Integer:Move)
    # either returns the action that gives the maximum score or minimum score in the given score:action map
    # - if multiple actions satisfy the maximum score a tiebreaker is done to determine which to return
    def _min_or_max(self, tree, score_action_map, planning_color):
        if tree.state.player_list[tree.state.turn] == planning_color:
            max_score = max(score_action_map.keys())
            action_list = score_action_map[max_score]
            action_picked = self._action_list_tiebreaker(action_list) 
            return (action_picked,max_score)
        else:
            min_score = min(score_action_map.keys())
            action_list = score_action_map[min_score]
            return (action_list[0],min_score)

    # game_state Integer -> move
    # where move = ("Move", (Int,Int), (Int,Int)) 
    #   -- the first tuple of integers is the starting position in (x,y) and the second tuple is the ending position in (x,y)
    # Given a GameState and an integer ( greater than zero) for the amount of turns to look ahead, 
    #   returns the 'best' move where the color in focus tries to maximize their score and the other
    #   players try to minimize the score of the player in-focus (in-focus player is the player that moves next in the given state)
    # Because the strategy works for whoever has the current turn:
    #   - Either the current player will be able to return a move
    #   - Or the ValueError for game ended will be raised
    #       (this happens because our state auto-skips players so either a current player will have a move or the game will be over)
    def move_penguin(self,state,turns_ahead):
        if turns_ahead <= 0:
            raise ValueError("The amount of turns to look ahead must be at least 1")
        
        if not state.any_moves:
            raise ValueError("The game was already ended")
    
        planning_color = state.player_list[state.turn]
        tree = g.GameTree(state)
        action,score = self._get_best_action(tree,turns_ahead,planning_color)
        return action
