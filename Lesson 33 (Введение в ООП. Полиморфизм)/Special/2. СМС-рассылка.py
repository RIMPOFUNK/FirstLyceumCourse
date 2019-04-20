class Person:
    def __init__(self, name, fath, surname, phones):
        self.name = name
        self.f = fath
        self.surname = surname
        self.phones = phones
        
    def get_phone(self):
        if 'private' in self.phones:
            return self.phones['private']
        return None
    
    def get_name(self):
        return f"{self.surname} {self.name} {self.f}"
    
    def get_work_phone(self):
        if 'work' in self.phones:
            return self.phones
        return None   
    
    def get_sms_text(self):
        return f"Уважаемый {self.name} {self.f}! " + \
               "Примите участие в нашем беспроигрышном конкурсе для физических лиц"
    

class Company:
    def __init__(self, name, tp, phones, *stuff):
        self.name = name
        self.tp = tp
        self.phones = phones
        self.st = stuff
        
    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for i in self.st:
            if 'work' in i.phones:
                return i.phones['work']
        return None
    
    def get_name(self):
        return self.name
    
    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! " + \
               f"Примите участие в нашем беспроигрышном конкурсе для {self.tp}"
    
            
def send_sms(*vals):
    company, stuff = [], []
    
    for i in vals:
        if isinstance(i, Company):
            company.append(i)
        else:
            stuff.append(i)
            
    for i in stuff:
        if i.get_phone():
            print(f"Отправлено СМС на номер {i.get_phone()} c текстом: {i.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {i.get_name()}")
    
    for i in company:
        if i.get_phone():
            print(f"Отправлено СМС на номер {i.get_phone()} c текстом: {i.get_sms_text()}")
        else:
            print(f"Не удалось отправить сообщение абоненту: {i.get_name()}")