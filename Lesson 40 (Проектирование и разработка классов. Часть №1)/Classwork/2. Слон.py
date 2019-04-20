class Bishop:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color
        
    def fix_coords(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8) 
    
    def set_position(self, row, col):
        self.row, self.col = row, col
        
    def char(self):
        return 'B'
    
    def get_color(self):
        return self.color
    
    def can_move(self, row, col):
        if not self.fix_coords(row, col):
            return False
        return abs(self.row - row) == abs(self.col - col)