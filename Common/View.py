from tkinter import *
from Fish.Common.FishTile import *
from Fish.Common.State import *

class View :
    
    # render tile graphically
    # Draws a single tile
    def drawTile(self, canvas_given, offset_x, offset_y, sizeGiven, numFish):
        points = [sizeGiven + offset_x, 2 * sizeGiven + offset_y, 
                  0 + offset_x, sizeGiven + offset_y, 
                  sizeGiven + offset_x, 0 + offset_y,
                  2 * sizeGiven + offset_x, 0 + offset_y, 
                  3 * sizeGiven + offset_x, sizeGiven + offset_y,
                  2 * sizeGiven + offset_x, 2 * sizeGiven + offset_y]
        if numFish > 0:
            canvas_given.create_polygon(points, outline="blue",
                                   fill="orange", width=2, tags="close")
        else:
            canvas_given.create_polygon(points, outline="black",
                                   fill="#6E6968" , width=2, tags="close")
                                   
        # Draws fish image
        for i in range(numFish):
            canvas_given.create_polygon([sizeGiven * 2 - sizeGiven * .25 + offset_x, ((sizeGiven * 2) / (numFish + 3)) * (i+2.5) + offset_y,
                                          sizeGiven * 2.25 + offset_x, ((sizeGiven * 2) / (numFish + 3)) * (i+2) + offset_y,
                                          sizeGiven * 2.25 + offset_x, ((sizeGiven * 2) / (numFish + 3)) * (i+3) + offset_y], fill='blue')
            canvas_given.create_oval(sizeGiven + offset_x, ((sizeGiven * 2) / (numFish + 3)) * (i+2) + offset_y,
                                    (sizeGiven * 2) + offset_x, ((sizeGiven * 2) / (numFish + 3)) * (i+3) + offset_y, fill='blue')

        return canvas_given

    # Draws what a penguin
    def drawPenguin(self, canvas_given, offset_x, offset_y, sizeGiven, color):
        #body
        canvas_given.create_oval(offset_x + sizeGiven / 1.8, offset_y + + sizeGiven / 1.8, 
                                        offset_x + sizeGiven / 1.3, offset_y + + sizeGiven * 1.4,
                                        fill=color)

        #head
        canvas_given.create_oval(offset_x + sizeGiven / 1.8, offset_y + + sizeGiven / 2.1, 
                                        offset_x + sizeGiven / 1.3, offset_y + + sizeGiven / 1.5,
                                        fill=color)


		#foot left
        canvas_given.create_oval(offset_x + sizeGiven / 1.85, offset_y + + sizeGiven * 1.3, 
										offset_x + sizeGiven / 1.6, offset_y + + sizeGiven * 1.5,
										fill=color)

		#foot left
        canvas_given.create_oval(offset_x + sizeGiven / 1.5, offset_y + + sizeGiven * 1.3, 
										offset_x + sizeGiven / 1.3, offset_y + + sizeGiven * 1.5,
										fill=color)

        return canvas_given

    def drawBoard(self, x_off, y_off, canvas_given, tiles, penguins):

        num_rows = len(tiles)
        num_columns = len(tiles[0])

        unit = TILE_SIZE
        x_offset = x_off
        y_offset = y_off
        for r in range(num_rows):
            x_offset = x_off
            for c in range(num_columns):
                if r % 2 == 0:
                    extra_offset = 0
                else:
                    extra_offset = 2 * unit
                self.drawTile(canvas_given, x_offset + extra_offset,y_offset,unit,tiles[r][c].numFish)
                for penguin_color in penguins:
                    if ([c,r] in penguins[penguin_color]):
                        self.drawPenguin(canvas_given, x_offset + extra_offset, y_offset, unit, penguin_color)
                x_offset = x_offset + 4 * unit
            y_offset = y_offset + unit
        return canvas_given
           
    def drawState(self, canvas_given, game_state):
        self.drawBoard(0,0,canvas_given,game_state.board.get_tile_copy(),game_state.penguin_map)
