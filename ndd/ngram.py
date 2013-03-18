# Ngram class
#
# Written by Parker Moore (pjm336)
# http://www.parkermoore.de

class Ngram:

    def __init__(self, value):
        self.value = value
        self.ID = self.__hash__()

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
