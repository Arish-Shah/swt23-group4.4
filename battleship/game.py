from board import Board
import os

class Game:
    def __init__(self) -> None:
        self.board = Board((8, 8), (5, 4))

    def play(self) -> None:
        over = False
        message = "Find 5 ships."
        choices = []

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
            message = "Hit/Miss."
            self.board.bomb(choice)
            choices.append(choice)
