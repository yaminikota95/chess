from config import *
from piece import *
class Pawn(Piece):
    def find_next_moves(self):
        next_pos = []
        a,b = self.curr_pos
        if a<WIDTH-1:
            next_pos.append((a+1,b))
        if b<HEIGHT-1:
            next_pos.append((a+1,b-1))
            next_pos.append((a+1,b+1))
        return next_pos
