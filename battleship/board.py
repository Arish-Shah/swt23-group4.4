from .ships import Ships
from .util import IS_NOT_HIT, IS_HIT, IS_SUNK

class Board:
    # NOTE: size: [row, col]
    def __init__(self, size, ships):
        self.size = size
        self.board = [["-"] * size[1] for _ in range(size[0])]
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ships = Ships(ships, size)

    def draw(self):
        print("  ", " ".join(self.alpha[:self.size[1]]))
        for i, row in enumerate(self.board):
            print("{:2d}".format(i + 1), " ".join(row))
    
    def is_valid_choice(self, choice):
        # NOTE: might need to change if grid goes beyond 9x9
        if len(choice) != 2: return False
        
        col, row = choice[0], choice[1]
        
        # check if col is alphabet and falls under board size
        if not col.isalpha(): return False
        else:
            col = col.upper()
            if col not in self.alpha[:self.size[1]]: return False
        
        # check if row is digit and falls under board size
        if not row.isdigit(): return False
        else:
            row = int(row)
            if row < 1 or row > self.size[0]: return False
        return True

    def choice_to_indices(self, choice):
        col, row = choice[0].upper(), int(choice[1])
        col = self.alpha.index(col)
        return (row - 1, col)

    def bomb(self, choice):
        row, col = self.choice_to_indices(choice)
        ship = self.ships.is_hit((row, col))
        if ship is None:
            self.board[row][col] = "O"
            return IS_NOT_HIT
        else:
            self.board[row][col] = "X"
            if self.ships.is_sunk(ship):
                return IS_SUNK
            return IS_HIT
