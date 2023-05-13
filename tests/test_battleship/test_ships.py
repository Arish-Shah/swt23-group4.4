from battleship.ships import Ship, Ships

def test_ship_is_hit():
    ship = Ship([(0, 1), (0, 2), (0, 3), (0, 4)], "h")
    assert ship.is_hit((0, 2)) == True
    assert ship.is_hit((1, 2)) == False

def test_ship_is_sunk():
    coords = [(0, 1), (0, 2), (0, 3), (0, 4)]
    ship = Ship(coords, "h")
    assert ship.is_sunk() == False
    
    for coord in coords:
        ship.is_hit(coord)
    assert ship.is_sunk() == True

def test_ships_is_hit():
    ships = Ships((5, 4), (8, 8))
    coord = ships.ships[0].coords[0]
    assert ships.is_hit(coord) == ships.ships[0]
    assert ships.is_hit((9, 9)) == None

def test_ships_is_sunk():
    ships = Ships((5, 4), (8, 8))
    assert ships.is_sunk(ships.ships[0]) == False

    for coord in ships.ships[0].coords:
        ships.is_hit(coord)
    assert ships.is_sunk(ships.ships[0]) == True
