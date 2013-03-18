#! /usr/bin/env python

import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from ngram import Ngram

print "Testing class Ngram..."

def test_hash_fn():
    ngram1 = Ngram(1, 'a-rose-is', './test/testfile1.txt')
    ngram2 = Ngram(2, 'rose-is-a', './test/testfile1.txt')
    assert ngram1.__hash__() != ngram2.__hash__(), 'the two hashes should not be the same'
    print 'Ngrams with different string values give different hashes... ok'
    
    ngram2.value = 'a-rose-is'
    assert ngram1.__hash__() == ngram2.__hash__(), 'the two hashes should not be the same'
    print 'Ngrams with the same string values give the same hash... ok'

if __name__ == "__main__":
    test_hash_fn()
    