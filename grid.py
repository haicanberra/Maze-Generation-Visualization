from cell import *
from config import *

class Grid():
    def __init__(self):
        self.grid = None
        self.neighbors = {}
        self.num_rows = None
        self.num_cellprows = None

        self.start_pos = None
        self.end_pos = None

    def create(self):
        grids = []
        x, y = X_DEFAULT, Y_DEFAULT
        for j in range(TOP_MARGIN+BOTTOM_MARGIN, HEIGHT//CELL_WIDTH):
            x = X_DEFAULT
            row = []
            for i in range(SIDE_MARGIN*2, WIDTH//CELL_WIDTH):
                row.append(Cell(x, y, CELL_WIDTH))
                x = x + CELL_WIDTH
            grids.append(row)
            y = y + CELL_WIDTH
        self.grid = grids
        self.num_rows = len(self.grid)
        self.num_cellprows = len(self.grid[0])
        self.set_neighbors()

    def draw(self, canvas):
        for row in self.grid:
            for cell in row:
                cell.draw(canvas)

    def cell_clicked(self, event, choose_start, choose_end):
        for i in range(self.num_rows):
            for j in range(self.num_cellprows):
                if self.grid[i][j].is_clicked(event.pos):
                    if choose_start:
                        self.grid[i][j].set_start()
                        self.start_pos = (i, j)
                        choose_start = False
                    elif choose_end:
                        self.grid[i][j].set_end()
                        self.end_pos = (i, j)
                        choose_end = False
                    # else:
                    #     for n in self.neighbors[(i, j)]:
                    #         if n != None:
                    #             self.grid[n[0]][n[1]].set_start()
        return choose_start, choose_end

    def set_neighbors(self):
        for i in range(self.num_rows):
            for j in range(self.num_cellprows):
                if i == 0:
                    # Top row
                    if j == 0:
                        self.neighbors[(i, j)] = [None,None,(i,j+1),(i+1,j)]
                    elif j == len(self.grid[i])-1:
                        self.neighbors[(i, j)] = [(i,j-1),None,None,(i+1,j)]
                    else:
                        self.neighbors[(i, j)] = [(i,j-1),None,(i,j+1),(i+1,j)]
                    # Bottom row
                elif i == self.num_rows-1:
                    if j == 0:
                        self.neighbors[(i, j)] = [None,(i-1,j),(i,j+1), None]
                    elif j == self.num_cellprows-1:
                        self.neighbors[(i, j)] = [(i,j-1),(i-1,j), None, None]
                    else:
                        self.neighbors[(i, j)] = [(i,j-1),(i-1,j),(i,j+1), None]
                else:
                    if j == 0:
                        self.neighbors[(i, j)] = [None,(i-1,j),(i,j+1),(i+1,j)]
                    elif j == self.num_cellprows-1:
                        self.neighbors[(i, j)] = [(i,j-1),(i-1,j),None,(i+1,j)]
                    else:
                         self.neighbors[(i, j)] = [(i,j-1),(i-1,j),(i,j+1),(i+1,j)]
                    
    def get_neighbors(self):
        return self.neighbors
    
    def get_grid(self):
        return self.grid
    
    def set_grid(self, grid):
        self.grid = grid
        return
    
    def get_start(self):
        return self.start_pos

    def get_end(self):
        return self.end_pos
    
    def clear(self):
        for i in range(self.num_rows):
            for j in range(self.num_cellprows):
                self.grid[i][j].remove_found()
                self.grid[i][j].remove_path()
                self.grid[i][j].remove_start()
                self.grid[i][j].remove_end()
        self.start_pos = None
        self.end_pos = None
        return
    