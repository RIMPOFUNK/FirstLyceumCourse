class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.car = carbohydrates
        
    def __add__(self, other):
        return FoodInfo(self.proteins + other.proteins, 
                        self.fats + other.fats,
                        self.car + other.car)
    
    def get_proteins(self):
        return self.proteins
    
    def get_fats(self):
        return self.fats
    
    def get_carbohydrates(self):
        return self.car
    
    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.car