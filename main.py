from canvas import Canvas
from point import Point
from turtle import Turtle

def main():
    canvas = Canvas()
    turtle = Turtle(canvas, step_size=20)
    turtle.set_pen_position(Point(100, 100))

    # Try: "F+F+F+F" for a square
    # Try: "F-F+F-F" for a zigzag
    command_string = "F+F+F+F"
    turtle.process_commands(command_string)

if __name__ == "__main__":
    main()
