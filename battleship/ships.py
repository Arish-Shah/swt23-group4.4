from random import choice, randint

class Ship:
    def __init__(self, coords, orient):
        self.coords = coords
        self.orient = orient
        self.hits = []
        self.sunk = False

    def is_hit(self, coord):
        if coord in self.coords:
            self.hits.append(coord)
            # say that ship sinks as soon as hit coords == coords
            if len(self.hits) == len(self.coords):
                self.sunk = True
            return True
        return False

    def is_sunk(self):
        # return True just once, so user is reported as soon as it sinks
        if self.sunk:
            self.sunk = False
            return True
        return False

class Ships:
    # Note: ships: [count, size]
    def __init__(self, ships, limits):
        self.count, self.size = ships
        self.limits = limits
        self.ships = []
        
        for _ in range(self.count):
            ship = self.get_ship()
            while self.is_overlapping(ship):
                ship = self.get_ship()
            self.ships.append(ship)

    def is_overlapping(self, new_ship):
        for ship in self.ships:
            if len(set(ship.coords).intersection(new_ship.coords)) > 0:
                return True
        return False

    def get_ship(self):
        orient = choice(["h", "v"])
        coords = []
        row, col = randint(0, self.limits[0] - 1), randint(0, self.limits[1] - 1)

        # decrease if starting index makes ship go outside board
        if orient == "v" and row > self.limits[0] - self.size:
            row = self.limits[0] - self.size
        elif orient == "h" and col > self.limits[1] - self.size:
            col = self.limits[1] - self.size
        coords.append((row, col))

        for _ in range(self.size - 1):
            if orient == "h":
                col += 1
            elif orient == "v":
                row += 1
            coords.append((row, col))

        return Ship(coords, orient)

    def is_hit(self, coord):
        for ship in self.ships:
            if ship.is_hit(coord):
                return ship
        return None

    def is_sunk(self, ship):
        return ship.is_sunk()
