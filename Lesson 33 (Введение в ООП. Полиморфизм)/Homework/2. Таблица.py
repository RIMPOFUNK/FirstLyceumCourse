class Table:
    def __init__(self, row, col):
        self.data = [[0 for _ in range(col)] for _ in range(row)]
        
    def get_value(self, row, col):
        if row >= len(self.data) or row < 0 or col >= len(self.data[0]) or col < 0:
            return None
        return self.data[row][col]
    
    def set_value(self, row, col, value):
        self.data[row][col] = value
        
    def n_rows(self):
        return len(self.data)
    
    def n_cols(self):
        return len(self.data[0]) if self.data else 0