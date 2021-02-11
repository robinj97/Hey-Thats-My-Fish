#!/usr/bin/env python3
import unittest
import sys


import FishBoard as f
import State as s
#from FishBoard import FishBoard
#from State import State
#from Player import Player

class TestState(unittest.TestCase):
    #place avatar
    # - errors: Avatar is being placed on already occupied tile
    #           Avatars are being placed on empty tile
    # - behavior: Test if map is populated with designated coordinate given by place_penguin function

    def test_place_avatar(self):
        player_list = ["red","white"]
        
        ex_board = f.FishBoard(4,3)
        ex_board.createBoard(equal=True, randomHoles=False)
        
        ex_state = s.State(ex_board,player_list)

        # Place youngest players penguins at 0,0
        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,1,"white")

        self.assertEqual(ex_state.penguin_map["red"][0],(0,0))
        self.assertEqual(ex_state.penguin_map["white"][0],(1,1))

    # Test to make sure error is thrown to place avatar on occupied tile
    def test_place_wrong_avatar_tile(self):
        player_list = ["red","white"]
        
        ex_board = f.FishBoard(4,3)
        ex_board.createBoard(equal=True, randomHoles=False)
        
        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        
        with self.assertRaises(ValueError):
            ex_state.place_penguin(0,0,"white")


    
    # Test to make sure avatar cannot be placed on hole, in order
    def test_place_avatar_empty_tile(self):
        hole_locations = [[0,0]]
        player_list = ["red","white"]

        ex_board = f.FishBoard(4,3)

        ex_board.createBoard(holes=hole_locations,equal=True, randomHoles=False)

        ex_state = s.State(ex_board,player_list)

        with self.assertRaises(ValueError):
            ex_state.place_penguin(0,0,"red")

    
    # Test to make sure white cannot place before red
    def test_place_in_order(self):
        player_list = ["red","white"]

        ex_board = f.FishBoard(4,3)

        ex_board.createBoard(equal=True, randomHoles=False)

        ex_state = s.State(ex_board,player_list)

        with self.assertRaises(ValueError):
            ex_state.place_penguin(0,0,"white")



    #move avatar
    # - errors: wrong turn, not correct player, invalid move
    # - behavior: move single penguin (square left behind is empty), move multiple penguins, check score

    # Test to make sure you cannot move before all penguins have been placed
    def test_move_before_all_placed(self):
        player_list = ["red","white"]

        ex_board = f.FishBoard(4,3)

        ex_board.createBoard(equal=True, randomHoles=False)

        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,0,"white")

        with self.assertRaises(ValueError):
            ex_state.move_penguin(0,0,1,0,"red")

    # Test to make sure regular placing penguin works
    def test_move_penguin(self):
        player_list = ["red","white"]

        ex_board = f.FishBoard(4,3)

        ex_board.createBoard(equal=True, randomHoles=False)

        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,0,"white")

        ex_state.place_penguin(0,2,"red")
        ex_state.place_penguin(1,2,"white")

        ex_state.place_penguin(2,0,"red")
        ex_state.place_penguin(1,3,"white")

        ex_state.place_penguin(2,1,"red")
        ex_state.place_penguin(0,1,"white")

        fish_on_tile = ex_board.tiles[2][1].numFish

        ex_state.move_penguin(2,1,2,2,"red")

        #Assert previous tile is empty
        self.assertEqual(ex_board.tiles[2][1].numFish,0)

        #Assert penguin got moved
        self.assertEqual(ex_state.penguin_map["red"][3],(2,2))

        #Assert that points got updated
        self.assertEqual(ex_state.score_map["red"],fish_on_tile)

    # Test to make sure error if all penguins are placed but white makes first move instead of red
    def test_move_wrong_penguin(self):
        player_list = ["red","white"]

        ex_board = f.FishBoard(4,3)

        ex_board.createBoard(equal=True, randomHoles=False)

        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,0,"white")

        ex_state.place_penguin(0,2,"red")
        ex_state.place_penguin(1,2,"white")

        ex_state.place_penguin(2,0,"red")
        ex_state.place_penguin(1,3,"white")

        ex_state.place_penguin(2,1,"red")
        ex_state.place_penguin(0,1,"white")

        fish_on_tile = ex_board.tiles[2][1].numFish

        with self.assertRaises(ValueError):
            ex_state.move_penguin(2,1,2,2,"white")

        

    #determine if player can move avatar
    # - behavior: states where no one can move, states where person whose turn it is can move, states where only person whose turn it is not can move
    def test_board_move_availible(self):
        player_list = ["red","white"]
        
        ex_board = f.FishBoard(4,3)
        ex_board.createBoard(equal=True, randomHoles=False)
        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,0,"white")

        ex_state.place_penguin(0,2,"red")
        ex_state.place_penguin(1,2,"white")

        ex_state.place_penguin(2,0,"red")
        ex_state.place_penguin(1,3,"white")

        ex_state.place_penguin(2,1,"red")
        ex_state.place_penguin(0,1,"white")

        self.assertEqual(ex_state.any_moves(), True)

    def test_board_move_unavailible(self):
        player_list = ["red","white"]
        
        ex_board = f.FishBoard(4,2)
        ex_board.createBoard(equal=True, randomHoles=False)
        ex_state = s.State(ex_board,player_list)

        ex_state.place_penguin(0,0,"red")
        ex_state.place_penguin(1,0,"white")

        ex_state.place_penguin(0,1,"red")
        ex_state.place_penguin(1,1,"white")

        ex_state.place_penguin(0,2,"red")
        ex_state.place_penguin(1,2,"white")

        ex_state.place_penguin(0,3,"red")
        ex_state.place_penguin(1,3,"white")

        self.assertEqual(ex_state.any_moves(), False)
    
