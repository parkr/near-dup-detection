class Ngram:
    
    def __init__(self, index, value, containing_file):
        self.index = index
        self.value = value
        self.containing_file = containing_file
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __hash__(self):
        return self.value.__hash__()