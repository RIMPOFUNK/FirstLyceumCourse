class MinStat:
    def __init__(self):
        self.data = []
        
    def add_number(self, number):
        self.data.append(number)
        
    def result(self):
        return min(self.data) if self.data else None
    
    
class MaxStat:
    def __init__(self):
        self.data = []
        
    def add_number(self, number):
        self.data.append(number)
        
    def result(self):
        return max(self.data) if self.data else None
    
    
class AverageStat:
    def __init__(self):
        self.data = []
        
    def add_number(self, number):
        self.data.append(number)
        
    def result(self):
        return sum(self.data) / len(self.data) if self.data else None