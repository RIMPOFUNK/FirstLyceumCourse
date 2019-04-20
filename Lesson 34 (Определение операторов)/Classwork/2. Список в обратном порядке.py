class ReversedList:
    def __init__(self, lst):
        self.lst = list(reversed(lst[:]))
        
    def __getitem__(self, key):
        return self.lst[key]
    
    def __len__(self):
        return len(self.lst)
