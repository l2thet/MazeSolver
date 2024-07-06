from src.line import Line
from src.point import Point
from src.window import Window


def main():
    window = Window(1024, 768)
    line = Line(Point(0, 0), Point(1024, 768))
    window.draw_line(line, "green")
    window.wait_for_close()
        
if __name__ == "__main__":
    main()