from src.maze import Maze
from src.window import Window


def main():
    window = Window(1024, 768)
    
    #line = Line(Point(0, 0), Point(1024, 768), "green")
    #window.draw_line(line)
    
    # cell_one = Cell(Point(100, 100), Point(200, 200), True, True, True, True)
    # cell_two = Cell(Point(200, 100), Point(500, 200), True, True, True, True)
    # window.draw_cell(cell_one, "green")
    # window.draw_cell(cell_two, "blue")
    
    # cell_one.draw_move(window.canvas, cell_two)
    
    maze = Maze(0, 0, 10, 10, 50, 50, window)
    
    window.wait_for_close()
        
if __name__ == "__main__":
    main()