import random
import copy
from FishTile import *

#This class represents a board of tiles used to play the Fish game
#It stores a 2D array of Tiles that contain the information about the board
class FishBoard:
    def __init__(self, rows, columns):

        # Column and row validation
        if (rows > 0 and columns > 0):
            self.columns = columns
            self.rows = rows
        else:
            raise ValueError("Rows and columns need to be above 0")

        # store tiles and the number of fish on them
        # - 2D array of number of fish (depends on current known rules of game)
        self.tiles = []

    def makeGrid(self, rows, columns):
        grid = []
        for i in range(columns):
            grid.append([None] * rows)
        return grid

    def getBoardCopy(self):
        return copy.deepcopy(self.tiles)

    # Creates a board based on given specifications
    # Functionality includes giving rows, columns, randomizing holes, assigning holes
    # Using the exact option allows a user to ignore any randomization and give a board the exact Tiles specifications desired

    # for "creating a board that has holes in specific places and is set up with a minimum number of 1-fish tiles"
    # - createBoard(holes=[[1,2],[3,2]], minFish={1:7}, randomHoles = False) ---- creates board with holes in spots (1,2) and (3,2) with 7 1-fish tiles
    # for "creating a board that has the same number of fish on every tile and has no holes"
    # - createBoard(equal=True, randomHoles = False) ---- creates board with holes in spots (1,2) and (3,2) with 7 1-fish tiles

    def createBoard(self, exact = [], holes=[], minFish={}, equal=False, randomHoles=False):
        # create 2d array
        self.tiles = self.makeGrid(self.rows, self.columns)
        
        if len(exact) != 0:
            for x in range(self.columns):
                for y in range(self.rows): 
                    self.tiles[x][y] = FishTile(exact[y][x])
            return

        # set specific holes
        for coordinate in holes:
            # check valid spot
            self.tiles[coordinate[0]][coordinate[1]] = FishTile(0)

        toBeFilled = []
        indicesLeft = self.rows * self.columns - len(holes)
        for numPer, tileCount in minFish.items():
            for tile in range(tileCount):
                toBeFilled.append(FishTile(numPer))
            indicesLeft = indicesLeft - tileCount

        # fill in the rest of the tiles randomly
        # - or with a singular value if equal = True
        if equal:
            fish_equal = random.randint(1, 5)
            for index_left in range(indicesLeft):
                toBeFilled.append(FishTile(fish_equal))
        else:
            for emptyIndices in range(indicesLeft):
                if randomHoles:
                    toBeFilled.append(FishTile(random.randint(0, 5)))
                else:
                    toBeFilled.append(FishTile(random.randint(1, 5)))

        # insert tiles randomly into board
        random.shuffle(toBeFilled)
        fillIndex = 0
        for row in range(self.rows):
            for col in range(self.columns):
                if self.tiles[col][row] == None:
                    self.tiles[col][row] = toBeFilled[fillIndex]
                    fillIndex = fillIndex + 1
                    
    # "determining the positions reachable via straight lines from a given position"
    #  (Int) x, (Int) y, (Map(String -> [(Int,Int)]))  -> [(Int, Int)]
    def availibleMoves(self, x, y, penguin_position_map={}):
        #turn the map of penguin locations into a single list of all penguin locations
        penguin_position_list = []
        for penguin_list in penguin_position_map.values():
            penguin_position_list.extend(penguin_list)


        working_x = x
        working_y = y
        # check up
        while working_y - 2 >= 0 and self.tiles[working_x][working_y - 2].numFish > 0 and (working_x, working_y - 2) not in penguin_position_list:
            working_y = working_y - 2
            yield (x, working_y)

        working_x = x
        working_y = y
        # check down
        while working_y + 2 < len(self.tiles[0]) and self.tiles[working_x][working_y + 2].numFish > 0 and (working_x, working_y + 2) not in penguin_position_list:
            working_y = working_y + 2
            yield (x, working_y)

        # check up-left  [y][x]
        # -- even row  [0][1] --> [0][0]
        # -- odd row [1][2] --> [0][1]
        working_x = x
        working_y = y
        while True:
            if (working_y % 2 == 0):
                if (working_y - 1 >= 0 and working_x - 1 >= 0 and self.tiles[working_x - 1][working_y - 1].numFish > 0 and (working_x - 1, working_y - 1) not in penguin_position_list):
                    working_y = working_y - 1
                    working_x = working_x - 1
                    yield (working_x, working_y)
                else:
                    break
            else:
                if (working_y - 1 >= 0 and self.tiles[working_x][working_y - 1].numFish > 0 and (working_x, working_y - 1) not in penguin_position_list):
                    working_y = working_y - 1
                    yield (working_x, working_y)
                else:
                    break

        # check down-left
        # -- even row [0][1] --> [0][2]
        # -- odd row   [1][2] --> [0][3]
        working_x = x
        working_y = y
        while True:
            if (working_y % 2 == 0):
                if (working_y + 1 < len(self.tiles[0]) and working_x - 1 >= 0 and self.tiles[working_x - 1][working_y + 1].numFish > 0 and (working_x - 1, working_y + 1) not in penguin_position_list):
                    working_y = working_y + 1
                    working_x = working_x - 1
                    yield (working_x, working_y)
                else:
                    break
            else:
                if (working_y + 1 < len(self.tiles[0]) and self.tiles[working_x][working_y + 1].numFish > 0 and (working_x, working_y + 1) not in penguin_position_list):
                    working_y = working_y + 1
                    yield (working_x, working_y)
                else:
                    break

        # check up-right
        # -- even row [0][1] --> [1][0]
        # -- odd row  [1][2] --> [1][1]
        working_x = x
        working_y = y
        while True:
            if (working_y % 2 == 0):
                if (working_y - 1 >= 0 and self.tiles[working_x][working_y - 1].numFish > 0 and (working_x, working_y - 1) not in penguin_position_list):
                    working_y = working_y - 1
                    yield (working_x, working_y)
                else:
                    break
            else:
                if (working_y - 1 >= 0 and working_x + 1 < len(self.tiles) and self.tiles[working_x + 1][
                    working_y - 1].numFish > 0 and (working_x + 1, working_y - 1) not in penguin_position_list):
                    working_y = working_y - 1
                    working_x = working_x + 1
                    yield (working_x, working_y)
                else:
                    break

        # check down-right
        # -- even row [0][1] --> [1][2]
        # -- odd row [1][2] --> [1][3]
        working_x = x
        working_y = y
        while True:
            if (working_y % 2 == 0):
                if (working_y + 1 < len(self.tiles[0]) and self.tiles[working_x][working_y + 1].numFish > 0 and (working_x, working_y + 1) not in penguin_position_list):
                    working_y = working_y + 1
                    yield (working_x, working_y)
                else:
                    break
            else:
                if (working_y + 1 < len(self.tiles[0]) and working_x + 1 < len(self.tiles) and self.tiles[working_x + 1][
                    working_y + 1].numFish > 0 and (working_x + 1, working_y + 1) not in penguin_position_list):
                    working_y = working_y + 1
                    working_x = working_x + 1
                    yield (working_x, working_y)
                else:
                    break

    # remove tile from board

    def removeTile(self, row, column):
        self.tiles[row][column].numFish = 0

    # (int) (int) --> (int)
    # Takes in coordinates and returns the value of fish at coordinates
    def get_score(self,x,y):
        return self.tiles[x][y].numFish
