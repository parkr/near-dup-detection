import os, math, random
from ngram import Ngram

class Detector:
    
    def __init__(self, test_docs_dir="./test"):
        self.test_docs_dir = test_docs_dir
        self.files = [d for d in os.listdir(test_docs_dir) if os.path.isfile(os.path.join(test_docs_dir, d)) and d[0] != "." ]
        self.ngrams = [] # all ngrams
        self.ngrams_to_objs = {} # all ngrams
        self.docs_to_ngrams = {} # maps filenames to Ngram objects
        self.p = 24107
        self.pairs_of_randoms = []
        self.generate_random_pairs_of_numbers()
        self.create_3grams()
        self.calculate_sketches()
    
    def calculate_sketches(self):
        pass
    
    def generate_random_pairs_of_numbers(self):
        for i in xrange(25):
            a = random.randint(1, self.p-1)
            b = random.randint(0, self.p-1)
            self.pairs_of_randoms.append((a,b))
    
    def f(self, s, x):
        return (self.pairs_of_randoms[s][0]*x + self.pairs_of_randoms[s][1]) % p
    
    def filename(self, filename):
        return "%s/%s" % (self.test_docs_dir, filename)
    
    def create_3grams(self):
        for file in self.files:
            filename = self.filename(file)
            with open(filename) as f:
                ngrams_for_file = self.ngram(f.read().strip().strip(",.!|&-_()[]<>{}/\"'").strip(), 3, filename)
                self.docs_to_ngrams[filename] = ngrams_for_file
    
    def ngram(self, file_contents, length=3, filename=None):
        tokens = file_contents.split(" ")
        num_tokens = len(tokens)
        ngrams = []
        for t in xrange(num_tokens):
            if num_tokens <= t+length-1:
                break # n-2 ngrams!
            ngram_tokens = tokens[t:t+length]
            ngram_value = "-".join(ngram_tokens)
            ngram = Ngram(len(self.ngrams)+1, ngram_value, filename)
            if ngram_value in self.ngrams:
                self.ngrams_to_objs[ngram_value].add_containing_file(filename)
            else:
                self.ngrams_to_objs[ngram_value] = ngram
                self.ngrams.append(ngram_value)
            ngrams.append(ngram)
        return ngrams
        
    def jaccard(self, set1, set2):
        set1 = set(set1)
        set2 = set(set2)
        union = set1.union(set2)
        intersection = set1.intersection(set2)
        return math.fabs(len(intersection))/math.fabs(len(union))
        
    def is_duplicate(self, set1, set2):
        return self.jaccard(set1, set2) >= 0.9
    
    def check_for_duplicates(self):
        return self.is_duplicate(self.docs_to_ngrams[self.filename('file00.txt')], self.docs_to_ngrams[self.filename('file01.txt')])
