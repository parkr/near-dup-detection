import unittest
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from ndindex import NearDuplicatesIndex

class TestNearDuplicatesIndex(unittest.TestCase):
    def setUp(self):
        self.docs = []
        self.docs.append(['this','is','a','document'])
        self.docs.append(['this','is','b','document'])
        self.index = NearDuplicatesIndex()

    def test_should_allow_to_append_documents(self):
        self.index.append(self.docs[0], 'doc1')
        self.index.append(self.docs[1], 'doc2')
        self.assertEqual(len(self.index), 2)

    def test_should_raise_an_error_when_docname_is_duplicated(self):
        self.index.append(self.docs[0], 'doc1')
        with self.assertRaises(Exception):
            self.index.append(self.docs[1], 'doc1')

    def test_should_calculate_jaccard_coefficient(self):
        self.index.append(self.docs[0], 'doc1')
        self.index.append(self.docs[0], 'doc2')
        self.assertEqual(self.index.get_jaccard('doc1', 'doc2'), 1.0)

    def test_should_raise_an_error_if_document_does_not_exist(self):
        with self.assertRaises(Exception):
            self.index.get_jaccard('doc1', 'doc3')

    def test_should_append_a_document_if_its_not_duplicated(self):
        self.index.append(self.docs[0], 'doc1')
        self.index.appendif(self.docs[1], 'doc2', 1.0)
        self.assertEqual(len(self.index), 2)

    def test_should_not_append_a_document_if_its_duplicated(self):
        self.index.append(self.docs[0], 'doc1')
        self.index.appendif(self.docs[1], 'doc2', -1.0)
        self.assertEqual(len(self.index), 1)

if __name__ == '__main__':
    unittest.main()
