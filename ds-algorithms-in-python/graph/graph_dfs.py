from graph1 import Graph
import collections

#https://en.wikipedia.org/wiki/Shortest_path_problem

def dfs(graph, start):

    def visit(vertex, seen=None):
        if seen is None:
            seen = []
        seen.append(vertex)

        for neighbour, _ in graph.neighbours(vertex):
            if neighbour not in seen:
                visit(neighbour, seen)
        return seen

    return visit(start)

if __name__ == '__main__':

    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 10),
             ('B', 'C', 5), ('C', 'E', 3), ('E', 'D', 4), ('D', 'F', 11)]

    graph = Graph(edges=edges)
    print(graph)
    seen = dfs(graph, 'A')
    print(seen)

