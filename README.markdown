# Near-Duplicate Detection

This program identifies near-duplicates in a corpus using techniques described
by Professor William Arms of Cornell University in his lectures to the students
of INFO 4300, Information Retrieval, Fall 2012.

This program was written by Parker Moore (pjm336), Fall 2012.

It is hosten on GitHub at https://github.com/parkr/near-dup-detection

[![Build Status](https://travis-ci.org/parkr/near-dup-detection.svg?branch=master)](https://travis-ci.org/parkr/near-dup-detection?branch=master)

## Install

```
pip install git://github.com/parkr/near-dup-detection.git#egg=NearDuplicatesDetection
```

## Usage

    python ndd.py

## Explanation of Methodology

All of the logic for the program is built into the Detector class
(`detector.py`). This class contains the methods and instance variables needed
to detect near-duplicates, such as the `get_jaccard(file1, file2)` method, the
`calculate_sketches()` method and the fundamental `create_3grams()` method.

This program implements the standard procedure for detecting near-duplicates:

1. Generate n-grams (3-grams in this case) for each document. Assign these
    n-grams a unique ID based on a 64-bit hash.
2. Create 25 sketches for document based on 50 randomly selected
    numbers and some stuff we generated earlier:
    - `p` is the closest prime number to the # of n-grams
    - `a_s` random, in the range [1, p-1]
    - `b_s` random, in the range [0, p-1]
    - `x` is the n-gram ID (the hash generated in step 1)
    - using the equation: `f_s(x) = (a_s*x + b_s) % p`
    - note: this equation is calculated 25 times per document (one time per
            random pair `a_s` and `b_s`), but only the minimum result of
            `f_s(x)` for each of the 25 pairs is saved. Thus, at the end of
            the calculation, each document has 25 `f_min`'s, one for each
            pair of random numbers.
3. Go through each document and compare it to all the other documents using the
    Jaccard coefficient estimation equation : `J(d1, d2) = m/n`, where:
    - `m` = number of sketch values (must be at the same index in respective
        lists) which are the same between the two documents
    - `n` = number of samples (# of sketches)
4. Having defined an arbitrary Jaccard coefficient threshold of `0.5`, the
    program prints out the names of the documents whose Jaccard coefficient
    is greater than the threshold previously defined, as well as the corresponding
    Jaccard coefficient.

As an addendum to the project, the three "nearest neighbors" to the first ten
documents is calculated at the end using the same method (and the data from
before).

## License

Standard GPLv2 license applies. Copyright (2012) Parker Moore.
