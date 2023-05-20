from cell import *
from grid import *
import random

class Maze():
    def __init__(self, grid) -> None:
        self.grid_class = grid
        self.grid = grid.get_grid()
        self.stack = []
        self.neighbors = grid.get_neighbors()

    def generate(self):
        temp = [0, 1, 2, 3]
        random.shuffle(temp)
        self.stack.append(START_GEN_CELL)
        self.grid[START_GEN_CELL[0]][START_GEN_CELL[1]].set_visited()
        while len(self.stack) != 0:
            current_cell = self.stack.pop()
            n_list = []
            for temp_n in temp:
                i = self.neighbors[current_cell][temp_n]
                if i != None:
                    if not self.grid[i[0]][i[1]].get_visited():
                        n_list.append(temp_n)
            if len(n_list) != 0:
                self.stack.append(current_cell)
                n = random.choice(n_list)
                i = self.neighbors[current_cell][n]
                if i != None:
                    match n:
                        case 0:
                            self.grid[current_cell[0]][current_cell[1]].remove_wall(n)
                            self.grid[i[0]][i[1]].remove_wall(2)
                        case 1:
                            self.grid[current_cell[0]][current_cell[1]].remove_wall(n)
                            self.grid[i[0]][i[1]].remove_wall(3)
                        case 2:
                            self.grid[current_cell[0]][current_cell[1]].remove_wall(n)
                            self.grid[i[0]][i[1]].remove_wall(0)
                        case 3:
                            self.grid[current_cell[0]][current_cell[1]].remove_wall(n)
                            self.grid[i[0]][i[1]].remove_wall(1)
                    self.grid[i[0]][i[1]].set_visited()         
                    self.stack.append(i)
        self.grid_class.set_grid(self.grid)
        return self.grid_class
            





        