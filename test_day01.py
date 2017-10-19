import day01


def test_tokenize():
    assert day01.tokenize('R1, R2, R3') == ['R1', 'R2', 'R3']


def test_parse_rotation():
    assert day01.parse_rotation('R') == day01.RIGHT
    assert day01.parse_rotation('L') == day01.LEFT


def test_rotate():
    assert day01.rotate(day01.NORTH, day01.RIGHT) == day01.EAST
    assert day01.rotate(day01.NORTH, day01.LEFT) == day01.WEST
    assert day01.rotate(day01.EAST, day01.RIGHT) == day01.SOUTH
    assert day01.rotate(day01.EAST, day01.LEFT) == day01.NORTH
    assert day01.rotate(day01.SOUTH, day01.RIGHT) == day01.WEST
    assert day01.rotate(day01.SOUTH, day01.LEFT) == day01.EAST
    assert day01.rotate(day01.WEST, day01.RIGHT) == day01.NORTH
    assert day01.rotate(day01.WEST, day01.LEFT) == day01.SOUTH


def test_move():
    assert day01.move((1, 1), day01.NORTH, 3) == (1, -2)
    assert day01.move((0, 0), day01.EAST, 1) == (1, 0)
    assert day01.move((-3, -3), day01.SOUTH, 2) == (-3, -1)
    assert day01.move((-4, 0), day01.WEST, 2) == (-6, 0)


def test_distance_calculation():
    assert day01.distance(5, 5) == 10
    assert day01.distance(2, -7) == 9


def test_first():
    assert day01.calculate_distance('R2, L3') == 5


def test_second():
    assert day01.calculate_distance('R2, R2, R2') == 2


def test_third():
    assert day01.calculate_distance('R5, L5, R5, R3') == 12


def test_puzzle1a():
    assert day01.calculate_distance('R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5') == 230


def test_location_visited_twice():
    assert day01.calculate_distance_to_first_revisited('R8, R4, R4, R8') == 4


def test_puzzle1b():
    assert day01.calculate_distance_to_first_revisited('R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5') == 154
