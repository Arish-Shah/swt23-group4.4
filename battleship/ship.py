import random

class Ship:
    @staticmethod
    def get_starting_index(size: tuple[int, int]):
        col = random.randint(0, size[0] - 1)
        row = random.randint(0, size[1] - 1)
        return (row, col)

    @staticmethod
    def get_orientation() -> str:
        return random.choice(["h", "v"])
