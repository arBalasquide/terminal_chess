
class Piece:
    def move(self):
        raise NotImplementedError("Move must be implemented")

    def set_attacking_squares(self, attacking_squares):
        raise NotImplementedError("Move must be implemented")

    # Name is the character(s) that appears on the board
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
