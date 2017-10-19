import day03


def test_invalid_triangle():
    assert day03.is_valid_triangle(5, 10, 25) == False


def test_puzzla3a():
    valid_count = 0

    with open('day03.txt', 'rb') as f:
        for line in f.readlines():
            candidate_triangle = [int(s) for s in line.split()]
            if day03.is_valid_triangle(*candidate_triangle):
                valid_count += 1


    assert valid_count == 1050
