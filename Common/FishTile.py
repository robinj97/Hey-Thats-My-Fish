#!/usr/bin/env python
import argparse

MAX_FISH = 5
TILE_SIZE = 50

#this class represents a tile in the fish board
# - it contains a single field for the number of fish on a tile
# - empty tiles are represented by having a "numFish" of 0
class FishTile():
    def __init__(self, numFish):
        self.numFish = numFish
