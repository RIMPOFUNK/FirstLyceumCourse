class Knight:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color
        
    def correct_coords(self, row, col):
        return (0 <= row < 8) and (0 <= col < 8)   
    
    def set_position(self, row, col):
        self.row, self.col = row, col
        
    def char(self):
        return 'N'
    
    def get_color(self):
        return self.color
    
    def can_move(self, row, col):
        if not self.correct_coords(row, col):
            return False
        return (abs(self.row - row) == 2 and abs(self.col - col) == 1) or \
               (abs(self.row - row) == 1 and abs(self.col - col) == 2)