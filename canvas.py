from line import Line

class Canvas:
    def __init__(self):
        self.lines = []

    def add_line(self, p1, p2):
        self.lines.append(Line(p1, p2))

    def print_lines(self):
        for line in self.lines:
            print(f"→ Line from {line.get_start()} to {line.get_end()
