class Balance:
    def __init__(self):
        self.L = 0
        self.R = 0
    
    def add_right(self, val):
        self.R = self.R + val
            
    def add_left(self, val):
        self.L = self.L + val
        
    def result(self):
        if self.L > self.R:
            return "L"
        if self.L < self.R:
            return "R"
        return "="

    