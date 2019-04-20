class Queen:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color

    def fix_coords(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8)
    
    def set_position(self, row, col):
        self.row, self.col = row, col
        
    def char(self):
        return 'Q'
    
    def get_color(self):
        return self.color
    
    def can_move(self, row, col):
        if not self.fix_coords(row, col):
            return False
        return not (abs(self.row - row) != abs(self.col - col) and self.row != row and self.col != col)