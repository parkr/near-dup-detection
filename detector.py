import os

class Detector:
    
    def __init__(self, test_docs_dir="./test"):
        self.files = [d for d in os.listdir(test_docs_dir) if os.path.isfile(os.path.join(test_docs_dir, d)) and d[0] != "." ]
        print self.files
    
    def jaccard(self, set1, set2):
        pass
