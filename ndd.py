#! /usr/bin/env python

from detector import Detector

if __name__ == "__main__":
    # run the program
    detector = Detector('./test')
    print "Checking for duplicates using NDD..."
    print detector.check_for_duplicates()
