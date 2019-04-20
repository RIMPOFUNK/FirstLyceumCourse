class Profile:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        return ''
    
    def describe(self):
        print(self.__class__.__name__)
        print(self.info())

        
class Vacancy(Profile):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def info(self):
        return f"Предлагаемая зарплата: {self.salary}"
    
    
class Resume(Profile):
    def __init__(self, name, time):
        self.name = name
        self.time = time
        
    def info(self):
        return f"Стаж работы: {self.time}"
