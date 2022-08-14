from graph1 import Graph

def detect_cycle(graph):
    path = set()
    visited = set()

    def visit(vertex):
        if vertex in visited:
            return False
        visited.add(vertex)
        path.add(vertex)

        for neighbour, _ in graph.neighbours(vertex):
            if neighbour in path or visit(neighbour):
                return True

        path.remove(vertex)
        return False

    return any(visit(v) for v in graph.vertices())

if __name__ == '__main__':

    edges = [('A', 'B', 5), ('A', 'C', 9), ('B', 'D', 2),
             ('B', 'E', 7), ('C', 'D', 3), ('D', 'A', 1), ('D', 'E', 13)]

    graph = Graph(edges=edges)
    print(graph)
    path = detect_cycle(graph)
    print(path)

