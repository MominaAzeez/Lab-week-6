import math
from point import Point
from pen import Pen

class Turtle:
    def __init__(self, canvas, step_size=20):
        self.pen = Pen(canvas)
        self.direction = 0.0  # Facing right
        self.step_size = step_size

    def set_pen_position(self, p):
        self.pen.move_to(p)

    def move_forward(self):
        current = self.pen.get_position()
        dx = int(self.step_size * math.cos(math.radians(self.direction)))
        dy = int(self.step_size * math.sin(math.radians(self.direction)))
        next_point = Point(current.getX() + dx, current.getY() + dy)
        self.pen.line_to(next_point)

    def turn_right(self):
        self.direction -= 90
        if self.direction < 0:
            self.direction += 360

    def turn_left(self):
        self.direction += 90
        if self.direction >= 360:
            self.direction -= 360

    def process_commands(self, commands):
        for ch in commands:
            if ch == 'F':
                self.move_forward()
            elif ch == '+':
                self.turn_right()
            elif ch == '-':
                self.turn_left()
            else:
                print(f"Unknown command: {ch}")
        self.pen.display()
