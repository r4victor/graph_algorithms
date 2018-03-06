#!/usr/bin/env python3

import sys


def get_adjacency_matrix_rows(filename):
    with open(filename) as f:
        n = int(f.readline())
        return [f.readline() for i in range(n)]


def get_adjacency_list(adjacency_matrix_rows):
    adjacency_list = [None]*len(adjacency_matrix_rows)
    for i, row in enumerate(adjacency_matrix_rows):
        adjacency_list[i] = set(
                                j for j, value in enumerate(row.split())
                                if int(value)
                            )
    return adjacency_list


def test_bipartiteness(adjacency_list, start_node):
    def put(node, parent):
        if parent in part1:
            part2.add(node)
        else:
            part1.add(node)

    if not adjacency_list:
        return set(), set()

    queue = [start_node]
    part1 = {start_node}
    part2 = set()

    parent = [None]*len(adjacency_list)
    while queue:
        node = queue.pop()
        for adjacent in adjacency_list[node]:
            if parent[node] == adjacent:
                continue
            if adjacent in part1:
                if node in part1:
                    return False
            elif adjacent in part2:
                if node in part2:
                    return False
            else:
                parent[adjacent] = node
                put(adjacent, node)
                queue.append(adjacent)

    return part1, part2


def get_output(result):
    if not result:
        output = 'N'
    else:
        part1, part2 = [sorted(map(lambda x: x+1, list(part))) for part in result]
        output = 'Y\n'
        output += ' '.join(str(node) for node in part1)
        output += '\n0\n'
        output += ' '.join(str(node) for node in part2)
    return output


def write_to_file(filename, output):
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help':
            print('usage: $./test_bipartiteness.py input.txt')
        else:
            output = get_output(
                test_bipartiteness(
                    get_adjacency_list(
                        get_adjacency_matrix_rows(sys.argv[1])
                    ), 0
                )
            )
            write_to_file('output.txt', output)
