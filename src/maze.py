import random
from time import sleep
from src.cell import Cell
from src.point import Point


class Maze:
    def __init__(
      self,
      x1,
      y1,
      num_rows,
      num_cols,
      cell_size_x,
      cell_size_y,
      win = None,
      color = "green",
      seed = None  
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.color = color
        if seed is not None:
            random.seed(seed)
        self._cells: Cell = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        
    def _break_entrance_and_exit(self):
        if self._cells:
            self._cells[0][0].has_top_wall = False
            self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
            self._draw_cell(self._cells[0][0], self.color)
            self._draw_cell(self._cells[self.num_rows - 1][self.num_cols - 1], self.color)
        
    def _break_walls_r(self, i, j):
        adjacent_cells = {}
        start_cell = self._cells[i][j]
        start_cell.visited = True
        
        adjacent_cells = self._select_adjacent_cells(i, j)

        if len(adjacent_cells) == 0:
            return#No available moves

        direction_to_take = random.choice(adjacent_cells)
        print(f"Direction to take: {direction_to_take}")
        direction_to_take["cell"].visited = True
        start_cell.draw_move(direction_to_take["cell"], self.win)
        
        if direction_to_take["direction"] == "down":
            start_cell.has_bottom_wall = False
            direction_to_take["cell"].has_top_wall = False
        elif direction_to_take["direction"] == "up":
            start_cell.has_top_wall = False
            direction_to_take["cell"].has_bottom_wall = False
        elif direction_to_take["direction"] == "right":
            start_cell.has_right_wall = False
            direction_to_take["cell"].has_left_wall = False
        elif direction_to_take["direction"] == "left":
            start_cell.has_left_wall = False
            direction_to_take["cell"].has_right_wall = False
        
        self._draw_cell(start_cell, self.color)
        self._draw_cell(direction_to_take["cell"], self.color)
        self._break_walls_r(direction_to_take["i"], direction_to_take["j"])
        
        
        
    def _select_adjacent_cells(self, i, j):
        adjacent_cells = []
        rows = len(self._cells)
        cols = len(self._cells[0]) if self._cells else 0
        
        if i + 1 < rows and self._cells[i+1][j] and not self._cells[i+1][j].visited:
            adjacent_cells.append({"cell": self._cells[i+1][j], "i": i+1, "j": j, "direction": "down"})
        if i - 1 >= 0 and self._cells[i-1][j] and not self._cells[i-1][j].visited:
            adjacent_cells.append({"cell": self._cells[i-1][j], "i": i-1, "j": j, "direction": "up"})
        if j + 1 < cols and self._cells[i][j+1] and not self._cells[i][j+1].visited:
            adjacent_cells.append({"cell": self._cells[i][j+1], "i": i, "j": j+1, "direction": "right"})
        if j - 1 >= 0 and self._cells[i][j-1] and not self._cells[i][j-1].visited:
            adjacent_cells.append({"cell": self._cells[i][j-1], "i": i, "j": j-1, "direction": "left"})
        return adjacent_cells
    
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                top_left = Point(self.x1 + j * self.cell_size_x, self.y1 + i * self.cell_size_y)
                bottom_right = Point(self.x1 + (j + 1) * self.cell_size_x, self.y1 + (i + 1) * self.cell_size_y)
                cell = Cell(top_left, bottom_right, True, True, True, True, self.win)
                row.append(cell)
                self._draw_cell(cell, self.color)
            self._cells.append(row)       
    
    def _draw_cell(self, cell, color):
        cell.draw(color)
        self._animate()
        
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)