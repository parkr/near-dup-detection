# NearDuplicatesIndex class
#
# Generates an entry for each appended document, that allows for estimating
# the Jaccard Coefficient between documents.

import math, random, sys
from ngram import Ngram

class NearDuplicatesIndex:
    def __init__(self):
        self.ngrams = [] # all ngrams
        self.ngrams_to_objs = {} # all ngrams
        self.docs_to_ngrams = {} # maps filenames to Ngram objects
        self.p = 24107.0 # a prime larger than the number of 3-grams we'll have
        self.n = 25 # the number of samples for the sketches
        self.pairs_of_randoms = []
        self.generate_random_pairs_of_numbers()
        self.sketches = {} # maps filename to sketch

    # A document is an array of terms (e.g., ['a','this','where','pretzel']).
    # Every document must have a unique name.
    def append(self, doc, docname):
        if docname in self.sketches:
            raise Exception

        p = self.p
        self.calculate_ngrams(doc, 3, docname)
        self.calculate_sketch(docname)

    # Public: creates n-grams for a specified document
    #
    # doc - document (array of terms) to be n-grammed
    # length - value of 'n' in 'n-grams'; default=3
    # docname - document name
    #
    # Returns the n-grams for the document
    def calculate_ngrams(self, doc, length=3, docname=None):
        num_terms = len(doc)
        ngrams = []
        for t in xrange(num_terms):
            if num_terms <= t+length-1:
                break # n-2 ngrams!
            ngram_tokens = doc[t:t+length]
            ngram_value = "-".join(ngram_tokens)
            ngram = Ngram(len(self.ngrams)+1, ngram_value, docname)
            if ngram_value in self.ngrams:
                self.ngrams_to_objs[ngram_value].add_containing_file(docname)
            else:
                self.ngrams_to_objs[ngram_value] = ngram
                self.ngrams.append(ngram_value)
            ngrams.append(ngram)
        self.docs_to_ngrams[docname] = ngrams

    # Public: calculates the sketches for a document based on the random
    #         numbers which were generated beforehand
    #
    # Returns nothing
    def calculate_sketch(self, docname):
        p = self.p
        sketch = [0] * self.n
        for s in xrange(self.n):
            f_min = sys.float_info.max
            a_s = self.pairs_of_randoms[s][0]
            b_s = self.pairs_of_randoms[s][1]
            for obj in self.docs_to_ngrams[docname]:
                fsx = (a_s*float(obj.ID) + b_s) % p
                if fsx < f_min:
                    f_min = fsx
            sketch[s] = f_min
        self.sketches[docname] = sketch

    # Public: generates 25 random pairs of numbers
    #
    # Returns nothing
    def generate_random_pairs_of_numbers(self):
        for i in xrange(25):
            a = random.randint(1, self.p-1)
            b = random.randint(0, self.p-1)
            self.pairs_of_randoms.append((a,b))

    # Public: Estimates the jaccard coefficient
    #
    # m - the number of sketches (in the same index) of the same value
    #
    # Returns the estimated jaccard coefficient
    def jaccard(self, m):
        return (m/float(self.n))

    # Public: calculates the estimated jaccard coefficient between two documents
    #
    # docname1 - first document's name
    # docname2 - second document's name
    #
    # Returns the estimated jaccard coefficient between both documents
    def get_jaccard(self, docname1, docname2):
        if not (self.sketches[docname1] or self.sketches[docname2]):
            raise Exception

        # get num of same sketch values
        k = 0.0
        for index in xrange(self.n):
            if self.sketches[docname1][index] == self.sketches[docname2][index]:
                k += 1
        return self.jaccard(k)

    def __len__(self):
        return len(self.sketches)
