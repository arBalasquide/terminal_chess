import sys
import unittest

sys.path.insert(1, '..')  # Add the above directory to the import path
from board import Square
from config import BOARD_WIDTH, BOARD_LENGTH

class SquareTest(unittest.TestCase):
    def test_create_square(self):
        position = (1, 2)
        square = Square(position)

    def test_invalid_square(self):
        position = (BOARD_WIDTH+1, BOARD_LENGTH+1)
        with self.assertRaises(

'''
class BoardTest(unittest.TestCase):
    # TODO: create setUp method to run before each test
    # TODO: remember to use subtests...
    def setUp(self):
        raise NotImplementedError("Set up method not implemented!")

    # TODO: add tests
'''

def main():
    unittest.main()

if __name__ == '__main__':
    main()
