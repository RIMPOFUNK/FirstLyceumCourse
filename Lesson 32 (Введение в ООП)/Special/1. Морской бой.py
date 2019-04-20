def is_valid(range, object):
    return object in range


class SeaMap:
    def __init__(self):
        self.field = [['.' for _ in range(10)] for _ in range(10)]

    def set_sink(self, row, col):
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < 10 and 0 <= j < 10:
                    if i == row and j == col or self.field[i][j] == 'x':
                        continue
                    self.field[i][j] = '*'

    def shoot(self, row, col, result):
        if result == "miss":
            self.field[row][col] = '*'
        elif result == "sink":
            rng = range(0, 10)
            self.set_sink(row, col)
            self.field[row][col] = 'x'

            for i in range(1, 4):
                if row - i in rng and self.field[row - i][col] == 'x':
                    self.set_sink(row - i, col)
                if row + i in rng and self.field[row + i][col] == 'x':
                    self.set_sink(row + i, col)

                if col - i in rng and self.field[row][col - i] == 'x':
                    self.set_sink(row, col - i)
                if col + i in rng and self.field[row][col + i] == 'x':
                    self.set_sink(row, col + i)

                if col - i in rng and row - i in rng and self.field[row - i][col - i] == 'x':
                    self.set_sink(row - i, col - i)
                if col + i in rng and row + i in rng and self.field[row + i][col + i] == 'x':
                    self.set_sink(row + i, col + i)
        elif result == "hit":
            self.field[row][col] = 'x'

    def cell(self, row, col):
        return self.field[row][col]
