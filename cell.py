import pygame
from config import *

class Cell():
    def __init__(self, x, y, width):
        self.visited = False
        self.current = False

        self.x = x
        self.y = y
        self.width = width

        self.TL = (x, y)
        self.TR = (x+width, y)
        self.BL = (x, y+width)
        self.BR = (x+width, y+width)

        self.walls = [True, True, True, True]
        self.walls_coord = [(self.BL, self.TL),
                            (self.TL, self.TR),
                            (self.TR, self.BR),
                            (self.BR, self.BL)]
        
        self.start = False
        self.end = False

    def draw(self, canvas):
        if self.start:
            pygame.draw.rect(canvas, START, (self.x+1, self.y+1, self.width-1, self.width-1))
        elif self.end:
            pygame.draw.rect(canvas, END, (self.x+1, self.y+1, self.width-1, self.width-1))
        else:
            pygame.draw.rect(canvas, CELL, (self.x, self.y, self.width, self.width))
        

        if not self.start and not self.end:
            for i in range(len(self.walls)):
                if self.walls[i]:
                    pygame.draw.line(canvas, WALL, self.walls_coord[i][0], self.walls_coord[i][1], width=WALL_WIDTH)
    
    def is_clicked(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.width:
            return True
        return False
    
    def set_start(self):
        self.start = True
        return
    
    def set_end(self):
        self.end = True
        return
        
