from collections import deque

class Graph(object):

    # Two methods of initializing graph. Either with dictionary style (or) with edges. 
    def __init__(self, graph=None, edges=None):
        if graph is None and edges is None:
            self.__graph = dict()
        elif not graph is None and edges is None:
            self.__graph = graph
        elif not edges is None:
            self.__graph = dict()
            for edge in edges:
                self.add_edge(edge)
        else:
            raise Exception("Don't set both graph and edges")

    def vertices(self):
        return self.__graph.keys()

    def add_edge(self, edge):
        (vertex1, vertex2, cost) = edge
        if vertex1 not in self.__graph:
            self.__graph[vertex1] = []
        if vertex2 not in self.__graph:
            self.__graph[vertex2] = []
        
        self.__graph[vertex1].append((vertex2, cost))

    def neighbours(self, vertex):
        return self.__graph[vertex]

    def __str__(self):
        pieces = []
        for vertex, adjacency_list in self.__graph.items():
            pieces.append(f"{vertex}-->{adjacency_list}")
        return "\n".join(pieces)

