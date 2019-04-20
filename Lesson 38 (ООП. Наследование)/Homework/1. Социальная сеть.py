class User:
    def __init__(self, name):
        self.name = name
        
    def send_message(self, user, message):
        pass
    
    def post(self, message):
        pass
    
    def info(self):
        return ""
    
    def describe(self):
        print(f"{self.name} {self.info()}")
    

class Person(User):
    def __init__(self, name, bth):
        self.name = name
        self.date = bth
    
    def info(self):
        return f"Дата рождения: {self.date}"
    
    def subscribe(self, user):
        pass
        
        
class Community(User):
    def __init__(self, name, discription):
        self.name, self.desc = name, discription
        
    def info(self):
        return f"Описание: {self.desc}"