import piece
class King(piece.Piece):
    def move(self,new_pos):
        self.curr_pos = new_pos
