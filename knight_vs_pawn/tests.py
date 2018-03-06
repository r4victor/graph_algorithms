#!/usr/bin/env python3

import unittest

import knight_path as kp

class TestKnightPath(unittest.TestCase):
    def test_parser(self):
        self.assertTupleEqual(
            ((1, 1), (4, 5)),
            kp.parse_input(['b2', 'e6'])
        )

    def base_path_test(self, knight_square, pawn_square, expected):
        self.assertListEqual(
            kp.find_knight_path(knight_square, pawn_square),
            expected
        )

    def test_no_moves(self):
        self.base_path_test((1, 1), (1, 1), [(1, 1)])

    def test_one_move_path(self):
        self.base_path_test((1, 1), (2, 3), [(1, 1), (2, 3)])

    def test_common_case(self):
        expected = [
            (6, 0),
            (7, 2),
            (6, 4),
            (7, 6),
            (5, 7)
        ]
        self.base_path_test((6, 0), (5, 7), expected)

    def test_under_pawn_attack(self):
        path = kp.find_knight_path((1, 1), (3, 4))
        self.assertNotEqual(path[0], (2, 3))



if __name__ == '__main__':
    unittest.main()