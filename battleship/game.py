import os
from .board import Board
from .util import IS_NOT_HIT, IS_HIT

class Game:
    def __init__(self) -> None:
        self.board_size = (8, 8)
        self.ship_size = (5, 4)
        self.board = Board(self.board_size, self.ship_size)

    def play(self) -> None:
        over = False
        message = "Find 5 ships."
        choices = []
        sunked = 0
        score = 0

        while not over:
            os.system("clear")
            self.board.draw()
            
            print(f"\n{message}\n")
            
            choice = input("Enter choice (like A3 or B4): ")
            if not self.board.is_valid_choice(choice):
                message = "Incorrect input!"
                continue
            if choice in choices:
                message = "You've guessed that already!"
                continue
            status = self.board.bomb(choice)
            
            if status == IS_NOT_HIT:
                message = "Bomb fell in the water!"
                score += 1
            elif status == IS_HIT:
                message = "You hit a ship!"
            else:
                message = "Ship is sunk!"
                sunked += 1
            if sunked == self.ship_size[0]:
                over = True
            choices.append(choice)

        os.system("clear")
        self.board.draw()
        print("\nGAME OVER\n")
        print("Score:", score)
