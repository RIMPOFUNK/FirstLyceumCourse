class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h

    def get_top_x(self):
        return self.x + self.w

    def get_top_y(self):
        return self.y + self.h

    def get(self):
        return [self.x, self.y, self.w, self.h]

    def intersection(self, val):
        ret_x, ret_y = val.x - self.x, val.y - self.y
        ret_h, ret_w = self.get_top_y() - val.y, self.get_top_x() - val.x

        ret = Rectangle(ret_x, ret_y, ret_w, ret_h)

        if not all(map(lambda x: bool(x), ret.get())):
            return None
        if val.x < self.x and val.get_top_x() > self.get_top_x() and \
                val.y < self.y and val.get_top_y() > self.get_top_y():
            return self
        if self.x < val.x and self.get_top_x() > val.get_top_x() and \
                self.y < val.y and self.get_top_y() > val.get_top_y():
            return val
        return ret

