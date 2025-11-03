from point import Point

class Pen:
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = Point(100, 100)

    def move_to(self, p):
        self.position = p

    def line_to(self, p):
        self.canvas.add_line(Point(self.position.x, self.position.y), Point(p.x, p.y))
        self.position = p

    def get_position(self):
        return self.position

    def display(self):
        self.canvas.print_lines()
