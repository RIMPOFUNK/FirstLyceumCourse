class MinMaxWordFinder:
    def __init__(self):
        self.sentence = []
      
    def shortest_words(self):
        if not self.sentence:
            return []
        
        mmin = min([len(i) for i in self.sentence])
        return sorted([i for i in self.sentence if len(i) <= mmin])
        
    def longest_words(self):
        if not self.sentence:
            return []        
        
        mmax = max([len(i) for i in self.sentence])
        return sorted(set([i for i in self.sentence if len(i) >= mmax]))
        
    def add_sentence(self, val):
        self.sentence += val.split()