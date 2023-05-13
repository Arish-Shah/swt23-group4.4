from itertools import product
from battleship.game import Game

def test_play():
    game = Game((8, 8), (5, 4))
    choices = [f"{c1}{c2}" for c1, c2 in product("ABCDEFGH", "12345678")]
    choices.insert(0, "I9")
    choices.insert(0, "A1")
    
    def mock_input(_: object=""):
        return choices.pop(0)

    assert game.play(choice_input=mock_input) == None
