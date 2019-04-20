class BigBell:
    def __init__(self):
        self.ding = "ding"
      
    def sound(self):
        print(self.ding)
        self.ding = "dong" if self.ding == "ding" else "ding"
