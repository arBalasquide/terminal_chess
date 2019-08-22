
class Piece:
    def move(self):
        raise NotImplementedError("move must be implemented")

    def set_attacking_squares(self, attacking_squares):
        raise NotImplementedError("set_attacking_squares must be implemented")

    # Name is the character(s) that appears on the board, on top of the corresponding square
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
