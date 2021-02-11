#!/usr/bin/env python3
import unittest
import sys


from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Common")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"/Common")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Player")
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"/Player")
import game_tree as g
import State as s
import FishBoard as f
from strategy import BestStrategy
from player import Player
from referee import Referee

#this implementation of player is only for testing purposes
#   - it is intended to give an error to the referee to practice kicking players
class BadPlayer():
    def has_been_kicked(self, color):
        #this implementation of player does nothing special upon learning a player was kicked
        return

    def set_color(self, color):
        #this implementation of player does nothing special upon learning its color
        return

    def get_placement(self, state):
        return ("Placement", (-1,-2))

    def get_move(self, state):
        return 

    def end_game(self, state):
         #this implementation of player does nothing special upon learning a game has ended
        return

#this implementation of an observer is only for testing purposes
#   - it stores up the messages received except for the state part (not needed for testing)
class AccumulatingObserver():
    def __init__(self):
        self.messages_rec = []

    def update_observer(self, msg):
        if msg[0] == "End":
            self.messages_rec.append(msg)
        else:
            self.messages_rec.append(msg[0])

#Some of these tests may take a few seconds especially those that execute an entire game (this class usually takes around 70 seconds for us)
class TestReferee(unittest.TestCase):
    # Test to make sure referee.startGame executes the entire game
    # - a deeper testing breakdown for each phase of the game is done below
    def test_referee_complete_game(self):
        test_player_1 = Player()
        test_player_2 = Player()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        ex_referee.start_game()

        #check that the state in the referee is an state of a game that has ended
        self.assertEqual("End", ex_referee.get_game_info()[3].phase)
        #check no player has been kicked (assumes our player successfully sends valid moves/placements which is checked in test_player)
        self.assertEqual([], ex_referee.get_game_info()[2])

    # Test to make sure player is kicked by the referee if caught cheating
    def test_referee_error(self):
        test_player_1 = Player()
        # a bad player class is define at the top of the class - where the placement it returns is invalid
        test_player_2 = BadPlayer()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        ex_referee.start_game()

        #make sure that the bad player has been kicked
        self.assertEqual([test_player_2], ex_referee.get_game_info()[2])

    # Test to make setting up a game works properly
    def test_setup_game(self):
        test_player_1 = Player()
        test_player_2 = Player()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        
        ex_referee.setup_game()
        
        self.assertEqual(ex_referee.state.board.columns,4)
        self.assertEqual(ex_referee.state.board.rows,4)

        # count that there are at least than 8 non-zero squares - places to put the penguins
        counter = 0
        for row in range(len(ex_referee.state.board.tiles)):
            for column in range(len(ex_referee.state.board.tiles[0])):
                if ex_referee.state.board.tiles[row][column] != 0:
                    counter += 1
        
        self.assertGreaterEqual(counter, 8)

    # Test to make sure placement phase works correctly
    def test_run_placement_phase(self):
        test_player_1 = Player()
        test_player_2 = Player()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        
        ex_referee.setup_game()
        #check to make sure now in placement phase
        ex_referee.run_placement_phase()
        #Check to make sure penguin_map has been populated, meaning penguins have been placed
        ex_map = ex_referee.state.penguin_map
        for player_penguin_map in ex_map:
            self.assertEqual(len(ex_map[player_penguin_map]), 4)

    # Test for run_move_phase 
    def test_run_move_phase(self):
        test_player_1 = Player()
        test_player_2 = Player()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        
        ex_referee.setup_game()
        #check to make sure now in placement phase
        ex_referee.run_placement_phase()

        # Check scores to make sure they are all 0 before moving
        ex_score_map = ex_referee.state.score_map

        for player_score_map in ex_score_map:
            self.assertEqual(ex_score_map[player_score_map],0)
        
        # Run moving phase, check if scores are not 0
        #   for a 4x4 board with no holes, both players will have made at least one move

        ex_referee.run_move_phase()

        for player_score_map in ex_score_map:
            self.assertNotEqual(ex_score_map[player_score_map],0)

    # Test to make sure end_game function works properly
    # Uses an observer to verify that the end game function works
    def test_end_game(self):
        test_player_1 = Player()
        test_player_2 = Player()
        test_obs = AccumulatingObserver()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        ex_referee.add_observer(test_obs)
        
        ex_referee.setup_game()
        ex_referee.run_placement_phase()
        self.assertEqual(test_obs.messages_rec[-1][0],"Placement")

        ex_referee.run_move_phase()
        self.assertEqual(test_obs.messages_rec[-1][0],"Move")

        ex_referee.end_game()

        #test that the observer's received an end message
        self.assertEqual(test_obs.messages_rec[-1][0],"End")
        #list of kicked players is empty
        self.assertEqual(test_obs.messages_rec[-1][2],[])

    # Test to make sure game info works
    def test_game_info_1(self):
        test_player_1 = Player()
        test_player_2 = Player()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        # Make sure get game info returns not started if the game has not started with placement phase
        self.assertEqual(ex_referee.get_game_info(),"Not Started")

    # Test to make sure game info works for in-progress game
    def test_game_info_2(self):
        test_player_1 = Player()
        test_player_2 = Player()
        test_obs = AccumulatingObserver()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        ex_referee.add_observer(test_obs)
        
        ex_referee.setup_game()

        self.assertEqual(ex_referee.get_game_info()[0],"In Progress")

    # Test to make sure get_game_info returns the right message for game that has ended
    def test_end_game_info(self):
        test_player_1 = Player()
        test_player_2 = Player()
        test_obs = AccumulatingObserver()

        ex_referee = Referee([test_player_1, test_player_2],4,4)
        ex_referee.add_observer(test_obs)
        
        ex_referee.setup_game()
        ex_referee.run_placement_phase()
        ex_referee.run_move_phase()
        ex_referee.end_game()

        self.assertEqual(ex_referee.get_game_info()[0],"End")







    

        



                

