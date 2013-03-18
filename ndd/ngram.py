# Ngram class
#
# Written by Parker Moore (pjm336)
# http://www.parkermoore.de

class Ngram:
    
    def __init__(self, index, value, containing_file):
        self.indx = index
        self.value = value
        self.containing_files = [containing_file]
        self.ID = self.__hash__()
    
    def add_containing_file(self, containing_file):
        self.containing_files.append(containing_file)
    
    def __eq__(self, other):
        return self.value.__eq__(other.value)
    
    def __hash__(self):
        return self.value.__hash__()
    
    def __str__(self):
        return self.value.__str__()
    
    def __repr__(self):
        return self.value.__str__()

    def __hash__(self):
        return hash(self.value)
