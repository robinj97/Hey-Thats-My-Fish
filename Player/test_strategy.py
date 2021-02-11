#!/usr/bin/env python3
import unittest
import sys
from strategy import BestStrategy

from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)]+"\\Common")

import game_tree as g
import State as s
import FishBoard as f

#method that returns if all the fields of 2 states are equal
def state_equal(state1,state2):
    if state1.turn == state2.turn:
        if state1.player_list == state2.player_list:
            if state1.penguin_map == state2.penguin_map:
                if state1.score_map == state2.score_map:
                    for x in range(len(state1.board.tiles)):
                        for y in range(len(state1.board.tiles[0])):
                            state1.board.tiles[x][y].numFish == state2.board.tiles[x][y].numFish
                    return True
    return False

class TestGame(unittest.TestCase):
    # Test to make sure nearest tile on row is populated
    def test_placement_1(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0)], "white":[(3,2),(3,1),(0,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        red_strat = BestStrategy()
        placement = red_strat.place_penguin(ex_state)
        self.assertEqual(placement, ("Placement", (3,0)))

    # Test to make sure None is returned if invalid player or action
    def test_placement_2(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        red_strat = BestStrategy()

        with self.assertRaises(ValueError):
            red_strat.place_penguin(ex_state)
      
    # Test to make sure placement is right when first row is filled.
    def test_placement_3(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "white", "Moving")

        red_strat = BestStrategy()
        placement = red_strat.place_penguin(ex_state)

        self.assertEqual(placement, ('Placement', (0, 1)))
    
    # Test to make sure move works for one step ahead
    def test_move_1(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(0,1)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        strat = BestStrategy()
        move = strat.move_penguin(ex_state,1)

        self.assertEqual(move, ('Move', (2, 0), (2, 1), 'red'))

    # Test to make sure move works when game ends before the look-ahead ends
    def test_move_2(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(0,1)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        strat = BestStrategy()
        move = strat.move_penguin(ex_state,4)

        self.assertEqual(move, ('Move', (2, 0), (2, 1), 'red'))

    # Test to make sure move works when looking ahead multiple moves
    def test_move_3(self):
        player_list = ["red","white"]
        b = [[1,2,3,2,4],[4,0,2,1,3],[1,1,0,4,2],[2,3,1,4,1]]

        ex_board = f.FishBoard(4,5)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(4,1),(3,0)], "white":[(3,2),(3,1),(0,2),(0,1)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        strat = BestStrategy()
        move = strat.move_penguin(ex_state,1)

        self.assertEqual(move, ('Move', (4, 1), (4, 0), 'red'))

    # Test to make sure move works when planning_player runs out of moves
    def test_move_4(self):
        player_list = ["red","white"]
        b = [[1,2,3,2,0],[0,0,0,0,0],[1,0,0,0,0],[0,3,1,4,1],[2,3,1,4,1]]

        ex_board = f.FishBoard(5,5)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,0),(3,1),(3,2),(3,3)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")

        strat = BestStrategy()
        move = strat.move_penguin(ex_state,1)

        self.assertEqual(move, ('Move', (0, 0), (0, 2), 'red'))
 