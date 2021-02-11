#!/usr/bin/env python3
import unittest
import sys

import game_tree as t
import FishBoard as f
import State as s

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



    #Test to make sure you are able to traverse forwards in the tree
    def test_forwards_in_tree(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)
        nodes = ex_tree.get_child_nodes()

        action = ('Move', (0, 0), (0, 1), "red")
        
        ex_tree.moveForwardTree(action)

        b1 = [[0,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board1 = f.FishBoard(3,4)
        ex_board1.createBoard(exact=b)

        ex_peng_map1 = {"red":[(0,1),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state1 = s.State(ex_board1,player_list, ex_peng_map1, {"red":1,"white":0}, "white")
        #assert that the tree's root state is now the 2nd example state that is post-move
        self.assertTrue(state_equal(ex_tree.state,ex_state1))
        #assert that the old root state is now the last element in the path
        self.assertTrue(state_equal(ex_tree.path[-1],ex_state))



    #back
    def test_back_in_tree(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)
        nodes = ex_tree.get_child_nodes()

        action = ('Move', (0, 0), (0, 1), "red")
        
        #perform the move forward
        ex_tree.moveForwardTree(action)

        b1 = [[0,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board1 = f.FishBoard(3,4)
        ex_board1.createBoard(exact=b)

        ex_peng_map1 = {"red":[(0,1),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state1 = s.State(ex_board1,player_list, ex_peng_map1, {"red":1,"white":0}, "white")
        #assert that the tree's root state is now the 2nd example state that is post-move
        self.assertTrue(state_equal(ex_tree.state,ex_state1))
        #assert that the old root state is now the last element in the path
        self.assertTrue(state_equal(ex_tree.path[-1],ex_state))

        old_path_len = len(ex_tree.path)
        #perform the move back
        ex_tree.moveBackTree()

        #assert that the tree's root state is now the original state
        self.assertTrue(state_equal(ex_tree.state,ex_state))
        #assert that the path is shorter by 1 element
        self.assertEqual(len(ex_tree.path),old_path_len - 1)        

    #Test to make sure the creation of child nodes work. 
    def test_get_children(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)
        nodes = ex_tree.get_child_nodes()
        
        expected_moves =  [('Move', (0, 0), (0, 1), "red"), ('Move', (1, 0), (0, 1), "red"), 
        ('Move', (2, 0), (2, 1), "red"), ('Move', (3, 0), (2, 1), "red")]
        self.assertEqual(len(nodes), 4)
        for action,move in nodes:
            self.assertEqual(expected_moves.count(action),1)
    
    # Test to make sure that given an action query that a new state is produced
    def test_action_query_valid(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)

        action = ('Move', (0, 0), (0, 1), "red")

        new_state = ex_tree.action_query(action)

        #create expected state
        b1 = [[0,2,3,2],[4,0,5,1],[1,1,0,4]]
        ex_board1 = f.FishBoard(3,4)
        ex_board1.createBoard(exact=b)
        ex_peng_map1 = {"red":[(0,1),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state1 = s.State(ex_board1,player_list, ex_peng_map1, {"red":1,"white":0}, "white")
        # Make sure new state is not the same as old state
        self.assertTrue(state_equal(ex_state1,new_state))

    # Test to make sure that given an action query that a new state is produced
    def test_action_query_invalid(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)

        action = ('Move', (0, 0), (0, 3), "red")

        new_state = ex_tree.action_query(action)

        self.assertEqual(new_state,False)

    # Test to make sure the function query on game tree works properly
    def test_function_query_2(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)

        func = lambda st : st.turn

        
        res = ex_tree.apply_function_query(func)
        expected_result = [(('Move', (0, 0), (0, 1), 'red'), 1), (('Move', (1, 0), (0, 1), 'red'), 1), (('Move', (2, 0), (2, 1), 'red'), 1), (('Move', (3, 0), (2, 1), 'red'), 1)]
        self.assertEqual(res,expected_result)

    def test_function_query_1(self):
        player_list = ["red","white"]
        b = [[1,2,3,2],[4,0,5,1],[1,1,0,4]]

        ex_board = f.FishBoard(3,4)
        ex_board.createBoard(exact=b)

        ex_peng_map = {"red":[(0,0),(1,0),(2,0),(3,0)], "white":[(3,2),(3,1),(0,2),(1,2)]}
        ex_state = s.State(ex_board,player_list, ex_peng_map, {"red":0,"white":0}, "red", "Moving")
        ex_tree = t.GameTree(ex_state)

        func = lambda st : st.score_map['red']

        res = ex_tree.apply_function_query(func)
        expected_result = [(('Move', (0, 0), (0, 1), 'red'), 1), (('Move', (1, 0), (0, 1), 'red'), 2), (('Move', (2, 0), (2, 1), 'red'), 3), (('Move', (3, 0), (2, 1), 'red'), 2)]
        self.assertEqual(res,expected_result)

