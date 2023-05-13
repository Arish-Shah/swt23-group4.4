from battleship.board import Board
from battleship.ships import Ship
from battleship.utils import IS_HIT, IS_NOT_HIT, IS_SUNK

def test_draw():
    board = Board((8, 8), (5, 4))
    assert board.draw() == None

def test_is_valid_choice():
    board = Board((8, 8), (5, 4))
    assert board.is_valid_choice("A1") == True
    assert board.is_valid_choice("Z9") == False

def test_choice_to_indices():
    board = Board((8, 8), (5, 4))
    assert board.choice_to_indices("A1") == (0, 0)
    assert board.choice_to_indices("D4") == (3, 3)

def test_bomb():
    board = Board((8, 8), (1, 4))
    coords = [(0, 0), (0, 1), (0, 2), (0, 3)]
    board.ships.ships[0] = Ship(coords, "h")
    assert board.bomb("A1") == IS_HIT
    assert board.bomb("B1") == IS_HIT
    assert board.bomb("C1") == IS_HIT
    assert board.bomb("D1") == IS_SUNK
    assert board.bomb("B3") == IS_NOT_HIT
