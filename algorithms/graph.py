""" A Python Graph Class with weights. """
import collections
import queue


class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    # https://realpython.com/instance-class-and-static-methods-demystified/
    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (vertex, neighbour, self.__graph_dict[vertex][neighbour]) not in edges:
                    edges.append((vertex, neighbour, self.__graph_dict[vertex][neighbour]))
        return edges

    def add_vertex(self, vertex):
        self.__graph_dict[vertex] = {}

    def add_edge(self, edge):
        (vertex1, vertex2, distance) = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1][vertex2] = distance
        else:
            self.__graph_dict[vertex1] = {vertex2: distance}

    def __str__(self):
        output = "Vertices: " + str(self.vertices()) + "\nEdges: " + str(self.__generate_edges())
        print(output)

    def cyclic(self):
        path = set()
        visited = set()

        def visit(vertex):
            if vertex in visited:
                return False
            visited.add(vertex)
            path.add(vertex)

            for neighbour in self.__graph_dict[vertex]:
                if neighbour in path or visit(neighbour):
                    return True

            path.remove(vertex)
            return False

        return any(visit(v) for v in self.__graph_dict.keys())

    # https://www.programiz.com/dsa/graph-dfs
    def dfs(self, start):

        def visit(vertex, visited=None):
            if visited is None:
                visited = []
            visited.append(vertex)

            for next_vertex in self.__graph_dict[vertex]:
                if next_vertex not in visited:
                    visit(next_vertex, visited)

            return visited

        return visit(start)

    # Breadth first search - https://codereview.stackexchange.com/questions/135156/bfs-implementation-in-python-3
    def bfs(self, start):
        seen = set(start)
        q = collections.deque(start)

        while q:
            vertex = q.popleft()
            for neighbour in self.__graph_dict[vertex]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)
        return seen

    # https://www.youtube.com/watch?v=pSqmAO-m7Lk
    def dijkstra(self, start):

        distance = {vertex: float("inf") for vertex in self.vertices()}
        distance[start] = 0
        visited = {vertex: False for vertex in self.vertices()}
        prev = {vertex: None for vertex in self.vertices()}

        pq = queue.PriorityQueue()
        pq.put((start, 0))

        print(pq.empty())

        while not pq.empty():
            vertex, min_value = pq.get()
            visited[vertex] = True
            if distance[vertex] < min_value:
                continue

            for neighbour in self.__graph_dict[vertex]:
                print('\nvertex: ', vertex)
                print('neighbour: ', neighbour)
                if visited[neighbour]:
                    continue
                new_distance = distance[vertex] + self.__graph_dict[vertex][neighbour]
                print('new_distance: ', new_distance)
                print('distance[neighbour]: ', distance[neighbour])
                print(new_distance < distance[neighbour])
                if new_distance < distance[neighbour]:
                    prev[neighbour] = vertex
                    distance[neighbour] = new_distance
                    print('(neighbour, new_distance): ', (neighbour, new_distance))
                    pq.put((neighbour, new_distance))
        return distance, prev

    def find_shortest_path(self, start, end):
        distance, prev = self.dijkstra(start)
        print("distance: ", distance)
        print("prev: ", prev)

        path = []
        if distance[end] == float("inf"):
            return path
        at = end
        while at is not None:
            path.append(at)
            at = prev[at]

        path.reverse()
        print("Shortest path: ", path)

    def is_connected(self):

        visited = {vertex: False for vertex in self.vertices()}

        for vertex in self.vertices():
            if not visited[vertex]:
                results = self.dfs(vertex)
                if len(results) > 1:
                    for result in results:
                        visited[result] = True

        is_connected = True
        for vertex in visited:
            if not visited[vertex]:
                is_connected = False

        return is_connected
