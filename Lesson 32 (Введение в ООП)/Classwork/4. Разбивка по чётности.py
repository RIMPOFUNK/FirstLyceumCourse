class OddEvenSeparator:
    def __init__(self):
        self.two = []
        self.not_two = []
    
    def add_number(self, number):
        if number % 2:
            self.not_two.append(number)
        else:
            self.two.append(number)
            
    def even(self):
        return self.two
    
    def odd(self):
        return self.not_two
