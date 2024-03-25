import pygame
from config import *

class Cell():
    def __init__(self, x, y, width):
        self.visited = False  # Maze gen
        self.found = False

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
        self.path = False

    def draw(self, canvas):
        # rect = (self.x+WALL_WIDTH, self.y+WALL_WIDTH, self.width-WALL_WIDTH, self.width-WALL_WIDTH)
        rect = (self.x, self.y, self.width, self.width)
        if self.start:
            pygame.draw.rect(canvas, START, rect)
        elif self.end:
            pygame.draw.rect(canvas, END, rect)
        elif self.path:
            pygame.draw.rect(canvas, PATH, rect)
        elif self.found:
            pygame.draw.rect(canvas, FOUND, rect)
        else:
            pygame.draw.rect(canvas, CELL, rect)
        

        for i in range(4):
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

    def set_visited(self):
        self.visited = True
        return
    
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def get_visited(self):
        return self.visited
    
    def remove_wall(self, index):
        self.walls[index] = False
        return
    
    def set_found(self):
        self.found = True
        return
    
    def get_found(self):
        return self.found
    
    def get_wall(self):
        return self.walls
    
    def set_path(self):
        self.path = True
        return
    
    def remove_found(self):
        self.found = False
        return
    def remove_start(self):
        self.start = False
        return
    def remove_end(self):
        self.end = False
        return
    def remove_path(self):
        self.path = False
        return


