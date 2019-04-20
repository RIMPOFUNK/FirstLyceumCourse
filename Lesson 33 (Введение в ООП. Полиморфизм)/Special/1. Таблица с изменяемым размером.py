class Table:
    def __init__(self, row, col):
        self.data = [[0 for _ in range(col)] for _ in range(row)]

    def get_value(self, row, col):
        if len(self.data) == 0:
            return None
        if row >= len(self.data) or col >= len(self.data[0]) or row < 0 or col < 0:
            return None
        return self.data[row][col]

    def set_value(self, row, col, value):
        self.data[row][col] = value

    def n_rows(self):
        return len(self.data)

    def n_cols(self):
        return len(self.data[0]) if self.data else 0

    def delete_row(self, row):
        if len(self.data) <= row:
            return
        del self.data[row]

    def delete_col(self, col):
        for i in range(len(self.data)):
            if len(self.data[i]) <= col:
                return
            del self.data[i][col]

    def add_row(self, row):
        self.data.insert(row, [0 for _ in
                               (range(len(self.data[0])) if len(self.data) != 0 else range(1))])

    def add_col(self, col):
        for i in range(len(self.data)):
            self.data[i].insert(col, 0)
