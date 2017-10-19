NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


RIGHT = 0
LEFT = 1


# Start facing north
INITIAL_DIRECTION = NORTH


def calculate_distance(sequence):
    current_direction = INITIAL_DIRECTION
    current_location = (0, 0)

    for token in tokenize(sequence):
        direction_to_face = parse_rotation(token[0])
        distance_to_walk = int(token[1:])

        current_direction = rotate(current_direction, direction_to_face)
        current_location = move(current_location,
                                current_direction,
                                distance_to_walk)

    return distance(*current_location)


def calculate_distance_to_first_revisited(sequence):
    current_direction = INITIAL_DIRECTION
    current_location = (0, 0)
    visited = set()

    for token in tokenize(sequence):
        direction_to_face = parse_rotation(token[0])
        current_direction = rotate(current_direction, direction_to_face)

        for intermediate_location in range(int(token[1:])):
            distance_to_walk = 1

            current_location = move(current_location,
                                    current_direction,
                                    distance_to_walk)

            if current_location in visited:
                print(f'Revisited {current_location}')
                return distance(*current_location)
            else:
                # print(f'Visited {current_location}')
                visited.add(current_location)

    raise ValueError('Never visited the same location twice')


def distance(*position):
    return abs(position[0]) + abs(position[1])


def move(current_location, direction, distance_to_walk):
    if direction == NORTH:
        return current_location[0], current_location[1] - distance_to_walk
    elif direction == EAST:
        return current_location[0] + distance_to_walk, current_location[1]
    elif direction == SOUTH:
        return current_location[0], current_location[1] + distance_to_walk
    elif direction == WEST:
        return current_location[0] - distance_to_walk, current_location[1]


def parse_rotation(rotation):
    if rotation == 'R':
        return RIGHT
    elif rotation == 'L':
        return LEFT


def rotate(current_direction, rotation):
    if current_direction == NORTH:
        return EAST if rotation == RIGHT else WEST
    elif current_direction == EAST:
        return SOUTH if rotation == RIGHT else NORTH
    elif current_direction == SOUTH:
        return WEST if rotation == RIGHT else EAST
    elif current_direction == WEST:
        return NORTH if rotation == RIGHT else SOUTH


def tokenize(string):
    return string.split(', ')
