import sys
import copy

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Common")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"/Common")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Player")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"/Player")
from State import State
from FishBoard import FishBoard
from strategy import BestStrategy
from player import Player

# Data Defs:

# #   A Game Message is one of:
#   - ("Not started")
#   - ("In Progress", game_state)
#   - ("End", winners, kicked, game_state) 
#       - a tuple of the string "End", a list of Players who won, a list of Players who were kicked, and a game_state)

# Observer is an object that implements the method update_observer(update) 
# update_observer(update) takes in an Update 
# An Update is one of:
#   - (Move, game_state)
#   - (Placement, game_state)  
#   - ("End", winners, kicked, state) 
#       - a tuple of the string "End", a list of Players who won, a list of Players who were kicked, and a game_state)


#This class represents an implementation of a referee component to be used in order to make sure the game is ran smoothly and to retrieve information about the game. 
#   - The referee takes in a list of players (in ascending order of age) to play the game 
#   - The referee, when told to, runs an entire game which consists of prompting players for placements or moves
#       - A player may send back a response that is abnormal (wrong structure/type or the returned placement/move may not be valid in the current state)
#           - If this happens when asking for a move or placement the referee kicks the player and alerts all players that the specific player has been kicked (and the game continues)
#   - Referees can also be given observers who will be updated as game actions occur
#       - or the get_game_info method can be used to retrieve information about the current game

class Referee:

    # Players is a list of Players (given to us in the order of youngest to oldest)
    # (int),(int)  row,col are dimensions for the board that the referee will create
    # This initalizes a referee, this is the constructor for the referee. 
    # To initialize: Referee([Players],(int),(int))
    def __init__(self, players, row, col):
        self.color_player_map = {}
        color_list = ["red","white","brown","black"][0:len(players)]
        for i in range(len(players)):
            self.color_player_map[color_list[i]] = players[i]

        self.row = row
        self.col = col
        #observers is a list of Observers - can be added to with the add_observer method
        self.observers = []
        #state is the current state of the game (a game_state) that starts out with no value (the state, along with its board, are created when start_game is called)
        self.state = None 

    # Observer --> void
    # Adds a given observer to the list of observers who will be updated when the game state changes (movements or placements) or the game ends
    def add_observer(self,observer):
        self.observers.append(observer)
    


# void --> Game Message
# This function returns info about the game, wether it has started, in progress or if it has ended
#   A Game Message is one of:
#   - ("Not started")
#   - ("In Progress", game_state)
#   - ("End", winners, kicked, game_state) 
#       - a tuple of the string "End", a list of Players who won, a list of Players who were kicked, and a game_state)
    def get_game_info(self):
        if self.state == None:
            return ("Not Started")

        if self.state.phase == "Placing" or self.state.phase == "Moving":
            return ("In Progress", copy.deepcopy(self.state))

        if self.state.phase == "End":
            # Get player(s) with highest score
            max_score = max(self.state.score_map.values())
            winning_players = []

            for color,player in self.color_player_map.items():
                if color in self.state.score_map and self.state.score_map[color] == max_score:
                    winning_players.append(player)

            kicked_players = []
            for color,player in self.color_player_map.items():
                if color in self.state.kicked_players:
                    kicked_players.append(player)
                    
            return ("End", winning_players, kicked_players, copy.deepcopy(self.state))

    # void --> void
    # Method to run a whole game from start to finish
    # This method will call the helpers and set up the board, run all the moves according to player strategy and end the game once no more moves are available. 
    def start_game(self):
        self.setup_game()
      
        self.run_placement_phase()
       
        self.run_move_phase()
       
        self.end_game()
       
    # void --> void
    # Sets up the initial state and board for the game 
    def setup_game(self):
        #creating board
        board = FishBoard(self.row,self.col)
        board.createBoard()
        #creating game_state
        self.state = State(board,list(self.color_player_map))

        for color,player in self.color_player_map.items():
            try:
                player.set_color(color)
            except:
                #player's failing set_color or end_game are not integral to the running of a game so they are ignored
                pass

    # void --> void   
    # Runs the placement phase of the game
    # This method will try to place penguins according to the strategy of placing penguins for Player, zig zag start at top-left
    # If there is any illegal placement or cheating detected, that player will be kicked, observers will be notified
    def run_placement_phase(self):
        while self.state.phase == 'Placing':
            current_color = self.state.player_list[self.state.turn]
            current_player = self.color_player_map[current_color]

            try:
                potential_placement = current_player.get_placement(copy.deepcopy(self.state))
                self.state.place_penguin(potential_placement[1][0],potential_placement[1][1], current_color)
            except ValueError:
                #kick player
                self.state.kick_player(current_color)
                #alert players a player has been kicked
                for color,player in self.color_player_map.items():
                    player.has_been_kicked(current_color)
                #continue with the next move
                continue

            for observer in self.observers:
                try:
                    observer.update_observer((potential_placement, copy.deepcopy(self.state)))
                except:
                    #observers failing can be ignored, but a failing observer should not stop the game from continuing
                    pass

    # void --> void
    # Function in charge of running the move phase of a game. This is until the game ends, once players cannot make more moves
    # If during the move phase an illegal move is made, the player making illegal moves/cheats will be kicked
    # If such cheating or illegal actions occur, the observers will also be notified
    def run_move_phase(self):
        while self.state.phase == 'Moving':
            current_color = self.state.player_list[self.state.turn]
            current_player = self.color_player_map[current_color]

            try:
                potential_move = current_player.get_move(copy.deepcopy(self.state)) 
                self.state.move_penguin(potential_move[1][0],potential_move[1][1],potential_move[2][0],potential_move[2][1],current_color)
            except ValueError:
                #kick player
                self.state.kick_player(current_color)
                #alert players a player has been kicked
                for color,player in self.color_player_map:
                    player.has_been_kicked(current_color)
                #continue with the next move
                continue

            for observer in self.observers:
                try:
                    observer.update_observer((potential_move, copy.deepcopy(self.state)))
                except:
                    #observers failing can be ignored, but a failing observer should not stop the game from continuing
                    pass


    # void --> void
    # This function is used to inform observers once a game has ended about who won, who got kicked, and the final state of the game
    # This function is also used to alert players that the game has ended
    def end_game(self):
        message = self.get_game_info()

        # Alert observer
        for observer in self.observers:
            try:
                observer.update_observer(message)   
            except:
                #observers failing can be ignored, but a failing observer should not stop the game from continuing
                pass

        for player in self.color_player_map.values():     
            try:
                player.end_game(copy.deepcopy(state))   
            except:
                #player's failing set_color or end_game are not integral to the running of a game so they are ignored
                pass     
        