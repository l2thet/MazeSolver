from src.cell import Cell
from src.line import Line
from src.point import Point
from src.window import Window


def main():
    window = Window(1024, 768)
    
    #line = Line(Point(0, 0), Point(1024, 768), "green")
    #window.draw_line(line)
    
    cell_one = Cell(Point(100, 100), Point(200, 200), True, True, True, True)
    cell_two = Cell(Point(200, 100), Point(300, 200), True, True, True, True)
    window.draw_cell(cell_one, "green")
    window.draw_cell(cell_two, "blue")
    
    cell_one.draw_move(window.canvas, cell_two, True)
    
    
    window.wait_for_close()
        
if __name__ == "__main__":
    main()