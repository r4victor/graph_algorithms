#!/usr/bin/env python3


KNIGHT_MOVES = [
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, 2),
]

PAWN_ATTACK_MOVES = [
        (1, -1),
        (-1, -1)
]


def find_knight_path(knight_square, pawn_square):
    def get_path(parent):
        path = []
        square = pawn_square
        while True:
            path.append(square)
            if square == knight_square:
                break
            square = parent[square]
        return path[::-1]

    squares_under_attack = [get_square(pawn_square, move) for move in PAWN_ATTACK_MOVES]
    visited = set()
    parent = {}
    stack = [knight_square]
    while stack:
        square = stack.pop()
        visited.add(square)
        if square == pawn_square:
            return get_path(parent)
        for s in get_legal_squares(square):
            if s not in visited and s not in squares_under_attack:
                parent[s] = square
                stack.append(s)


def get_legal_squares(square):
    def is_legal(square):
        if 0 <= square[0] <= 7 and 0 <= square[1] <= 7:
            return True
        return False

    squares = []
    for move in KNIGHT_MOVES:
        next_square = get_square(square, move)
        if is_legal(next_square):
            squares.append(next_square)
    return squares


def get_square(square, move):
    return square[0] + move[0], square[1] + move[1]


def parse_input(lines):
    knight_square = lines[0]
    pawn_square = lines[1]
    return (
        parse_algebraic_notation(knight_square),
        parse_algebraic_notation(pawn_square)
    )


def parse_algebraic_notation(square):
    return ord(square[0]) - ord('a'), int(square[1]) - 1


def to_algebraic_notation(square):
    return chr(square[0] + ord('a')) + str(square[1] + 1)


def read_file(filename):
    with open(filename) as f:
        return f.readlines()


def write_to_file(filename, output):
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    path = find_knight_path(*parse_input(read_file('in.txt')))
    output = '\n'.join(to_algebraic_notation(square) for square in path)
    write_to_file('out.txt', output)
