from graph1 import Graph
import queue

def dijkstra(graph, start):
    distance = {vertex: float("inf") for vertex in graph.vertices()}
    distance[start] = 0
    visited = {vertex: False for vertex in graph.vertices()}
    prev = {vertex: None for vertex in graph.vertices()}
    
    pq = queue.PriorityQueue()
    pq.put((start, 0))

    while not pq.empty():
        vertex, min_value = pq.get()
        visited[vertex] = True
        if distance[vertex] < min_value:
            continue

        for neighbour, cost in graph.neighbours(vertex):
            if visited[neighbour]:
                continue
            new_distance = distance[vertex] + cost

            if new_distance < distance[neighbour]:
                prev[neighbour] = vertex
                distance[neighbour] = new_distance
                pq.put((neighbour, new_distance))
    
    return distance, prev

if __name__ == '__main__':

    start = 'A'
    end = 'F'

    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 10),
             ('B', 'C', 5), ('C', 'E', 3), ('E', 'D', 4), ('D', 'F', 11)]

    graph = Graph(edges=edges)
    distance, prev = dijkstra(graph, start)
    print("distance: ", distance)
    print("prev: ", prev)

    path = []
    at = end
    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()
    print(f"Shortest path: {path}")


