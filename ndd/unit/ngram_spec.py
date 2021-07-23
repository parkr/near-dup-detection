#! /usr/bin/env python

import sys
from os.path import dirname, abspath

from ..ngram import Ngram

print("Testing class Ngram...")


def test_hash_fn():
  ngram1 = Ngram("a-rose-is")
  ngram2 = Ngram("rose-is-a")
  assert (
      ngram1.__hash__() != ngram2.__hash__()
  ), "the two hashes should not be the same"
  print("Ngrams with different string values give different hashes... ok")

  ngram2.value = "a-rose-is"
  assert (
      ngram1.__hash__() == ngram2.__hash__()
  ), "the two hashes should not be the same"
  print("Ngrams with the same string values give the same hash... ok")


if __name__ == "__main__":
  test_hash_fn()
