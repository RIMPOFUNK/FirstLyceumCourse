class Selector:
    def __init__(self, numbers):
        self.num = numbers[:]
    
    def get_odds(self):
        return list(filter(lambda x: x % 2 != 0, self.num))
    
    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.num))
        