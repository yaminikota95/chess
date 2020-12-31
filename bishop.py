from config import *
from piece import *
class Bishop(Piece):
    def find_next_moves(self):
        next_pos = []
        a,b = self.curr_pos
        while a>=0 and b>=0:
            if a!= self.curr_pos[0] and b!=self.curr_pos[1]:
                next_pos.append((a,b))
            a = a-1
            b = b-1
        a,b = self.curr_pos
        while a>=0 and b<HEIGHT:
            if a!= self.curr_pos[0] and b!=self.curr_pos[1]:
                next_pos.append((a,b))
            a = a-1
            b = b+1
        a,b = self.curr_pos
        while a<WIDTH and b>=0:
            if a!= self.curr_pos[0] and b!=self.curr_pos[1]:
                next_pos.append((a,b))
            a = a+1
            b = b-1
        a,b = self.curr_pos
        while a<WIDTH and b<HEIGHT:
            if a!= self.curr_pos[0] and b!=self.curr_pos[1]:
                next_pos.append((a,b))
            a = a+1
            b = b+1
        return next_pos
