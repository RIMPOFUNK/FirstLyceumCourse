class Queue:
    def __init__(self, *vals):
        if isinstance(vals, tuple):
            self.val = list(vals[:])
        else:
            self.val = vals[:]
        
    def append(self, *vals):
        self.val.extend(vals[:])
    
    def copy(self):
        return Queue(*self.val)
    
    def pop(self):
        if len(self.val) == 0:
            return
        tmp = self.val[0]
        del self.val[0]
        return tmp
    
    def extend(self, val):
        self.val.extend(val.val[:])
        
    def __next__(val):
        return Queue(*val.val[1:])

    def next(self):
        return Queue(*self.val[1:])
    
    def __add__(self, other):
        return Queue(*(self.val + other.val))
    
    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def __eq__(self, other):
        return self.val == other
    
    def __str__(self):
        return "[{}]".format(' -> '.join(map(lambda x: str(x), self.val)))
    
    def __rshift__(self, n):
        return Queue(*self.val[n:])
