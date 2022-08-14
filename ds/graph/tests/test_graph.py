from algorithms import graph


def test_graph():
    graph_structure = {
        's': {'u': 10, 'x': 5},
        'u': {'v': 1, 'x': 2},
        'v': {'y': 4},
        'x': {'u': 3, 'v': 9, 'y': 2},
        'y': {'s': 7, 'v': 6}
    }

    g = graph.Graph(graph_structure)

    assert len(g.vertices()) == 5

    edge = ('y', 'z', 4)
    g.add_edge(edge)

    assert len(g.edges()) == 11


def test_cyclic():
    g2 = {
        "1": {"2": 0},
        "2": {"3": 0},
        "3": {"1": 0}
    }
    assert graph.Graph(g2).cyclic()

    g3 = {"1": {"2": 0},
          "2": {"3": 0},
          "3": {"4": 0},
          "4": {}
          }
    assert not graph.Graph(g3).cyclic()


def test_dfs_bfs():
    g = {
        'A': {'B': 1, 'C': 4, 'D': 2},
        'B': {'A': 9, 'E': 5},
        'C': {'A': 4, 'F': 15},
        'D': {'A': 10, 'F': 7},
        'E': {'B': 3, 'J': 7},
        'F': {'C': 11, 'D': 14, 'K': 3, 'G': 9},
        'G': {'F': 12, 'I': 4},
        'H': {'J': 13},
        'I': {'G': 6, 'J': 7},
        'J': {'H': 2, 'I': 4},
        'K': {'F': 6}
    }
    print("DFS: ", graph.Graph(g).dfs('A'))
    print("BFS: ", graph.Graph(g).bfs('A'))


def test_find_shortest_path():
    g = {
        'A': {'B': 1, 'C': 4, 'D': 2},
        'B': {'A': 9, 'E': 5},
        'C': {'A': 4, 'F': 15},
        'D': {'A': 10, 'F': 7},
        'E': {'B': 3, 'J': 7},
        'F': {'C': 11, 'D': 14, 'K': 3, 'G': 9},
        'G': {'F': 12, 'I': 4},
        'H': {'J': 13},
        'I': {'G': 6, 'J': 7},
        'J': {'H': 2, 'I': 4},
        'K': {'F': 6}
    }
    graph.Graph(g).find_shortest_path('A', 'J')


def test_connected():
    g = {
        'A': {'B': 1, 'C': 4, 'D': 2},
        'B': {'A': 9, 'E': 5},
        'C': {'A': 4, 'F': 15},
        'D': {'A': 10, 'F': 7},
        'E': {'B': 3, 'J': 7},
        'F': {'C': 11, 'D': 14, 'K': 3, 'G': 9},
        'G': {'F': 12, 'I': 4},
        'H': {'J': 13},
        'I': {'G': 6, 'J': 7},
        'J': {'H': 2, 'I': 4},
        'K': {'F': 6}
    }
    assert graph.Graph(g).is_connected()


def test_not_connected():
    g = {
        'A': {'B': 1, 'C': 4},
        'B': {},
        'C': {},
        'D': {'E': 10},
        'E': {},
        'F': {}
    }
    assert not graph.Graph(g).is_connected()
