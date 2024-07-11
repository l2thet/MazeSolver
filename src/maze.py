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
      win = None  
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        
        
    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                top_left = Point(self.x1 + j * self.cell_size_x, self.y1 + i * self.cell_size_y)
                bottom_right = Point(self.x1 + (j + 1) * self.cell_size_x, self.y1 + (i + 1) * self.cell_size_y)
                cell = Cell(top_left, bottom_right, True, True, True, True, self.win)
                row.append(cell)
                self._draw_cell(cell, "white")
            self._cells.append(row)
            
    
    def _draw_cell(self, cell, color):
        
        cell.draw(color)
        self._animate()
        
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0.05)