def is_valid_triangle(a, b, c):
    return ((a + b) > c) and ((b + c) > a) and ((a + c) > b)
