#!/usr/bin/env python3
import unittest
import sys
from FishBoard import FishBoard
import State


class TestBoard(unittest.TestCase):
# Test to make sure all tiles on a board are the same, with same number of fish
    def test_create_even_board(self):
        ex_board_one = FishBoard(4, 3)
        ex_board_one.createBoard(equal=True, randomHoles=False)
        fish_per = ex_board_one.tiles[0][0].numFish
        for r in range(4):
            for c in range(3):
                self.assertEqual(ex_board_one.tiles[c][r].numFish, fish_per)

    # Test to make sure all tiles are the same, and that values of fish is also the same -- Different variable for grid given
    def test_create_even_board_3players(self):
        ex_board_one = FishBoard(6, 6)
        ex_board_one.createBoard(equal=True, randomHoles=False)
        self.assertEqual(ex_board_one.tiles[3][1].numFish, ex_board_one.tiles[1][1].numFish)
        self.assertNotEqual(ex_board_one.tiles[0][0], None)
        fish_per = ex_board_one.tiles[0][0].numFish
        for r in range(6):
            for c in range(6):
                self.assertEqual(ex_board_one.tiles[r][c].numFish, fish_per)

    # Test to make sure holes are in correct spot
    def test_create_random_board_holes(self):
        hole_locations = [[0,0],[1,3],[2,0]]
        ex_board_one = FishBoard(4, 3)
        ex_board_one.createBoard(minFish={1:6},holes = hole_locations,equal=False, randomHoles=False)
        one_count = 0
        for r in range(4):
            for c in range(3):
                if [c,r] in hole_locations:
                    self.assertEqual(ex_board_one.tiles[c][r].numFish, 0)
                else:
                    self.assertNotEqual(ex_board_one.tiles[c][r].numFish, 0)
                    if ex_board_one.tiles[c][r].numFish == 1:
                        one_count = one_count + 1
        self.assertGreaterEqual(one_count, 6)


    # Test to make sure given grid inputs are valid
    def test_valid_dimensions(self):
        with self.assertRaises(ValueError):
            ex_board = FishBoard(0, 10)

        with self.assertRaises(ValueError):
            ex_board = FishBoard(10, 0)

        with self.assertRaises(ValueError):
            ex_board = FishBoard(-1, 10)

        with self.assertRaises(ValueError):
            ex_board = FishBoard(10, -2)

    def test_remove_tile(self):
        ex_board = FishBoard(4,3)
        ex_board.createBoard(equal=True, randomHoles=False)
        self.assertNotEqual(ex_board.tiles[0][0].numFish, 0)
        ex_board.removeTile(0,0)
        self.assertEqual(ex_board.tiles[0][0].numFish, 0)

        self.assertNotEqual(ex_board.tiles[1][2].numFish, 0)
        ex_board.removeTile(1,2)
        self.assertEqual(ex_board.tiles[1][2].numFish, 0)

    def test_moves(self):
        ex_board = FishBoard(4,3)
        ex_board.createBoard(equal=True, randomHoles=False)

        self.assertEqual(set(ex_board.availibleMoves(0,2)),set([(0, 0), (0, 1), (1, 0), (0, 3)]))
        self.assertEqual(set(ex_board.availibleMoves(1,2)),set([(0, 0), (0, 1), (1, 0), (0, 3), (1, 1), (1, 3), (2, 0)]))
        self.assertEqual(set(ex_board.availibleMoves(0,0)),set([(0, 2), (0, 1), (1, 2), (1, 3)]))
