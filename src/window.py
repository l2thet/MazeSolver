from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.widget = Tk()
        self.widget.title("Maze Solver")
        self.widget.geometry(f"{self.width}x{self.height}")
        self.widget.resizable(False, False)
        self.canvas = Canvas(self.widget, bg="black")
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False
        self.widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()
        
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
        
    def close(self):
        self.is_running = False
        self.widget.destroy()
        
    
