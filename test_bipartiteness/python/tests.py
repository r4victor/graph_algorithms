import unittest
import time

import test_bipartiteness as tb


class TestGraphForBibartite(unittest.TestCase):

    def base_adjacency_list_test(self, expected, rows):
        adjacency_list = tb.get_adjacency_list(rows)
        self.assertListEqual(expected, adjacency_list)

    def test_empty_adjacency_list(self):
        self.base_adjacency_list_test(
            [set(), set()],
            ['0 0', '0 0']
        )

    def test_common_adjacency_list(self):
        self.base_adjacency_list_test(
            [{1,2}, {0,2}, {0, 1}],
            ['0 1 1', '1 0 1', '1 1 0']
        )

    def base_bipartiteness_test(self, expected, adjacency_list):
        result = tb.test_bipartiteness(adjacency_list, 0)
        self.assertEqual(expected, (result))

    def test_bipartiteness_test_empty(self):
        self.base_bipartiteness_test((set(), set()), [])

    def test_bipartiteness_test_wrong(self):
        self.base_bipartiteness_test(False, [{1,2}, {0,2}, {0,1}])

    def test_bipartiteness_test_one_node(self):
        self.base_bipartiteness_test(({0}, set()), [set()])

    def test_bipartiteness_test_common(self):
        expected = {0,1,2,3}, {4,5,6,7}
        adjacency_list = []
        for i in [1,0]:
            adjacency_list.extend([expected[i] for j in range(4)])
        self.base_bipartiteness_test(expected, adjacency_list)

    def _test_bipartiteness_test_big(self):
        part1 = set(range(10000))
        part2 = set(range(10000, 20000))
        adjacency_list = []
        for part in [part2, part1]:
            adjacency_list.extend([part for j in range(10000)])
        start = time.time()
        self.base_bipartiteness_test((part1, part2), adjacency_list)
        print(time.time() - start)


if __name__ == '__main__':
    unittest.main()
