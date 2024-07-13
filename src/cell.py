from src.point import Point
from src.window import Window


class Cell():
    def __init__(self, top_left: Point, bottom_right: Point, has_left_wall=False, has_right_wall=False, has_top_wall=False, has_bottom_wall=False, window : Window=None):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._top_left = Point(top_left.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_right = Point(bottom_right.x, bottom_right.y)
        self._center_point = Point((top_left.x + bottom_right.x) // 2, (top_left.y + bottom_right.y) // 2)
        self._window = window
        self.visited = False
        

    def draw(self, color):
        if self.has_left_wall:
            self._window.canvas.create_line(self._top_left.x, self._top_left.y, self._bottom_left.x, self._bottom_left.y, fill=color)
        else:
            self._window.canvas.create_line(self._top_left.x, self._top_left.y, self._bottom_left.x, self._bottom_left.y, fill="black")
        if self.has_right_wall:
            self._window.canvas.create_line(self._top_right.x, self._top_right.y, self._bottom_right.x, self._bottom_right.y, fill=color)
        else:
            self._window.canvas.create_line(self._top_right.x, self._top_right.y, self._bottom_right.x, self._bottom_right.y, fill="black")
        if self.has_top_wall:
            self._window.canvas.create_line(self._top_left.x, self._top_left.y, self._top_right.x, self._top_right.y, fill=color)
        else:
            self._window.canvas.create_line(self._top_left.x, self._top_left.y, self._top_right.x, self._top_right.y, fill="black")
        if self.has_bottom_wall:
            self._window.canvas.create_line(self._bottom_left.x, self._bottom_left.y, self._bottom_right.x, self._bottom_right.y, fill=color)
        else:
            self._window.canvas.create_line(self._bottom_left.x, self._bottom_left.y, self._bottom_right.x, self._bottom_right.y, fill="black")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        self._window.canvas.create_line(self._center_point.x, self._center_point.y, to_cell._center_point.x, to_cell._center_point.y, fill=color)

    def __str__(self):
        return f'Cell( {self.has_left_wall}, {self.has_right_wall}, {self.has_top_wall}, {self.has_bottom_wall}, {self._window})'

    def __repr__(self):
        return str(self)