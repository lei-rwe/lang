# https://docs.python.org/3.5/library/stdtypes.html#typesseq
# There are three basic sequence types: lists, tuples, and range objects.
# Additional sequence types tailored for processing of binary data and text
# strings are described in dedicated sections
import unittest

class TestSequenceTypes(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_range(self):
        for i in range(10):
            print(i)
        print( range(20).__contains__(11) )        

if __name__ == '__main__':
    unittest.main()
