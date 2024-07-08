from tkinter import Canvas

class Line():
    def __init__(self, p1, p2, color) -> None:
        self.p1 = p1
        self.p2 = p2
        self.color = color
        
    def draw(self, canvas: Canvas) -> None:
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=self.color)
        