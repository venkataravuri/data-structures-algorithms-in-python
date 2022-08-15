from graph1 import Graph
import collections

#https://en.wikipedia.org/wiki/Shortest_path_problem

def bfs(graph, start):
    seen = [start]
    q = collections.deque(start)

    while q:
        vertex = q.popleft()
        for neighbour, _ in graph.neighbours(vertex):
            if neighbour not in seen:
                seen.append(neighbour)
                q.append(neighbour)

    return seen

if __name__ == '__main__':

    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 10),
             ('B', 'C', 5), ('C', 'E', 3), ('E', 'D', 4), ('D', 'F', 11)]

    graph = Graph(edges=edges)
    print(graph)
    seen = bfs(graph, 'A')
    print(seen)

