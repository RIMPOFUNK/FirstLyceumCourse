class Date:
    def __init__(self, mm, dd):
        self.mm = mm
        self.dd = dd
        self.mounth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __sub__(self, val):
        return (sum(self.mounth[:self.mm - 1]) + self.dd) - (sum(val.mounth[:val.mm - 1]) + val.dd)
