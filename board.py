import sys
from config import BOARD_WIDTH, BOARD_LENGTH
from string import ascii_uppercase as alphabet

class Square:
    def is_valid(self, position):
        x, y = position
        return x <= Board.WIDTH and y <= Board.LENGTH

    # Names are, for example, A1, B7, D3, etc.
    def _get_name(self):
        letter = alphabet[self.x - 1]  # Numbers greater than 26 not supported (yet)
        number = self.y
        return letter + str(number)

    def _get_color(self):
        is_even = lambda n: n % 2 == 0

        if is_even(self.y):
            return 'black' if is_even(self.x) else 'white'
        else:
            return 'white' if is_even(self.x) else 'black'

    def __init__(self, position: tuple, name=None, color=None):
        assert self.is_valid(position), "{} is not a valid position!".format(position)

        self.position = position
        self.x, self.y = position

        if name is None:
            name = self._get_name()

        if color is None:
            color = self._get_color()

        self.name = name
        self.color = color

class Board:
    WIDTH = BOARD_WIDTH
    LENGTH = BOARD_LENGTH

    def __init__(self):
        # TODO: Change to list comprehension
        self.board = []
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_LENGTH):
                self.board.append(Square((x, y)))

def main():
    sys.path.insert(1, 'tests/') # Add 'tests/' directory to the import path
    import testBoard
    
    testBoard.main()


if __name__ == '__main__':
    main()
