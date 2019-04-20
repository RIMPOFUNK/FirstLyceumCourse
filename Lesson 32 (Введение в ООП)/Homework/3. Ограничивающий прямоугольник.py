class BoundingRectangle:
    def __init__(self):
        self.x = []
        self.y = []

    def width(self):
        return max(self.x) - min(self.x)

    def height(self):
        return max(self.y) - min(self.y)

    def top_y(self):
        return max(self.y)

    def bottom_y(self):
        return min(self.y)

    def left_x(self):
        return min(self.x)

    def right_x(self):
        return max(self.x)

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)
