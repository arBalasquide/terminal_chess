class ChessBoard:
    def __init__(self):
        self.board = [[1] * 8 for i in range(8)]
        rook = Rook("R", [])
        self.board.insert(rook, [0][0])
    def show():
        print(self.board)

class Piece:
    # TODO: Most likely create a class for each different piece inheriting Piece class
    #       Then define their own validMove method since some pieces vary upon different scenarions i.e king cant castle through check
    #       Move pattern, we have to define most likely a 2D array of possible coordinates to move at with the Piece being the origin (0,0)
    #       This will define how far it can go, but its validMove method will consider if that piece can take over a piece, move to that, or if its an illegal move etc

    def __init__(self, symbol="P", move_pattern): # default value will be P for pawn 
        self.symbol = symbol
        self.move_pattern = move_pattern

    def illegalMove(move):

    def promote(): # if pawn ask what unit to promote to and change its symbol and move pattern accordingly

class Rook(Piece):

    
    


