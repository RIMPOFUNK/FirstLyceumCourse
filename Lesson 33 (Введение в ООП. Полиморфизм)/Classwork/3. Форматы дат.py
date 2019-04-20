class AmericanDate:
    def __init__(self, year, month, day):
        self.y = str(year)
        self.m = str(month)
        self.d = str(day)
        
    def set_year(self, val):
        self.y = str(val)
    
    def set_month(self, val):
        self.m = str(val)
    
    def set_day(self, val):
        self.d = str(val)
    
    def get_year(self):
        return self.y
    
    def get_month(self):
        return self.m
    
    def get_day(self):
        return self.d
    
    def format(self):
        return f"{self.m.rjust(2, '0')}.{self.d.rjust(2, '0')}.{self.y}"
    
    
class EuropeanDate:
    def __init__(self, year, month, day):
        self.y = str(year)
        self.m = str(month)
        self.d = str(day)
        
    def set_year(self, val):
        self.y = str(val)
    
    def set_month(self, val):
        self.m = str(val)
    
    def set_day(self, val):
        self.d = str(val)
    
    def get_year(self):
        return self.y
    
    def get_month(self):
        return self.m
    
    def get_day(self):
        return self.d
    
    def format(self):
        return f"{self.d.rjust(2, '0')}.{self.m.rjust(2, '0')}.{self.y}"