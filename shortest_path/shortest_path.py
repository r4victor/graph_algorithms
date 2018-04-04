
def parse_input(filename):
    with open(filename) as f:
        n = int(f.readline())
        graph= parse_weighted_adjacency_matrix(
            [f.readline() for i in range(n)]
        )
        start_node = int(f.readline()) - 1
        stop_node = int(f.readline()) - 1
        return graph, start_node, stop_node


def parse_weighted_adjacency_matrix(matrix_rows):
    graph = {}
    for i, row in enumerate(matrix_rows):
        graph[i] = {}
        for j, weight in enumerate(row.split()):
            if weight != '32767':
                graph[i][j] = int(weight)
    return graph


def find_shortest_path(graph, start_node, stop_node):
    def traverse():
        path = []
        node = stop_node
        while node != None:
            path.append(node)
            node = prev[node]
        return reversed(path)

    sorted_nodes = topological_sort(graph)
    distance = [None]*len(graph)
    distance[start_node] = 0
    prev = [None]*len(graph)
    for node in sorted_nodes:
        if distance[node] is not None:
            for adjacent in graph[node]:
                if (distance[adjacent] is None or
                     distance[adjacent] > distance[node] + graph[node][adjacent]):
                    distance[adjacent] = distance[node] + graph[node][adjacent]
                    prev[adjacent] = node

    return traverse(), distance[stop_node]



def topological_sort(graph):
    def visit(node):
        if node in visited:
            return
        if node in temp:
            raise ValueError('Graph is not acyclic.')
        temp.add(node)
        for adjacent in graph[node]:
            visit(adjacent)
        visited.add(node)
        ordered_nodes.append(node)

    ordered_nodes = []
    visited = set()
    temp = set()
    for node in graph.keys():
        if node not in visited:
            visit(node)
    return reversed(ordered_nodes)


def get_output(path, distance):
    if distance is None:
        return 'N'
    return 'Y\n{}\n{}'.format(
        ' '.join(str(i + 1) for i in path),
        distance
    )


def write_to_file(filename, output):
    with open(filename, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    write_to_file(
        'out.txt',
        get_output(*find_shortest_path(*parse_input('in.txt')))
    )
