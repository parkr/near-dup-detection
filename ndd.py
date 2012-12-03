#! /usr/bin/env python
# Main near-duplicate detection "runner"
#
# Written by Parker Moore (pjm336)
# http://www.parkermoore.de

import operator, copy
from detector import Detector

if __name__ == "__main__":
    # run the program
    detector = Detector('./test')
    print "Checking for duplicates using NDD..."
    duplicates = detector.check_for_duplicates()
    if duplicates:
        print "Duplicates found (Jaccard coefficient > 0.5):"
        print duplicates
    
    print "Printing three nearest neighbors of the first 10 files..."
    filenames_of_first_ten = [detector.filename("file%02d.txt") % (f,) for f in xrange(10)]
    filenames_of_first_one_hundred = [detector.filename("file%02d.txt") % (f,) for f in xrange(100)]
    for index1, j in enumerate(filenames_of_first_ten):
        jaccard_coefficients = [0] * 100
        for index2, d in enumerate(filenames_of_first_one_hundred):
            if index1 != index2:
                jaccard_coefficients[index2] = detector.get_jaccard(j, d)
        three_nearest = []
        nearest_count = -1
        jcos = copy.deepcopy(jaccard_coefficients)
        while len(three_nearest) < 3:
            index,coefficient = max(enumerate(jcos), key=operator.itemgetter(1))
            del jcos[index]
            # put the index back where it was in the original jaccard_coefficients
            if nearest_count == 0 and index >= three_nearest[0][0]:
                index += 1
            if nearest_count == 1:
                if index >= three_nearest[0][0]:
                    index += 1
                if index >= three_nearest[1][0]:
                    index += 1
            three_nearest.append((index,coefficient))
            nearest_count += 1
        print "Three nearest neighbors to %s:" % ("file%02d.txt" % index1)
        for near in sorted(three_nearest, key=operator.itemgetter(1), reverse=True):
            print "\t%s with Jaccard coefficient of %0.3f" % ("file%02d.txt" % near[0], near[1])
