# From
# https://www.youtube.com/watch?v=oLtvUWpAnTQ
# https://www.youtube.com/watch?v=bD8RT0ub--0&t=883s
# https://www.youtube.com/watch?v=9wV1VxlfBlI: Dijkstra algorithm
import heapq
import math


def bfs(graph, s):
    queue = [s]
    seen = set(s)
    parent = {s: None}  # To memorize the tree
    while len(queue) > 0:
        v = queue.pop(0)
        adjacents = graph[v]
        for w in adjacents:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = v
    print(parent)


def dfs(graph, s):
    stack = [s]
    seen = set(s)
    while len(stack) > 0:
        v = stack.pop()
        adjacents = graph[v]
        for w in adjacents:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(v)


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}  # To memorize the tree
    distance = {v: math.inf for v in graph.keys()}
    distance[s] = 0

    while len(pqueue) > 0:
        dist, v = heapq.heappop(pqueue)
        seen.add(v)

        adjacents = graph[v].keys()
        for w in adjacents:
            if w not in seen:
                if dist + graph[v][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[v][w], w))
                    parent[w] = v
                    distance[w] = dist + graph[v][w]
    print(parent)
    print(distance)


def test_bfs():
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'c', 'e', 'f'],
        'e': ['c', 'd'],
        'f': ['d']
    }

    bfs(graph, 'e')


def test_dijkstra():
    graph = {
        'a': {'b': 5, 'c': 1},
        'b': {'a': 5, 'c': 2, 'd': 1},
        'c': {'a': 1, 'b': 2, 'd': 4, 'e': 8},
        'd': {'b': 1, 'c': 4, 'e': 3, 'f': 6},
        'e': {'c': 8, 'd': 3},
        'f': {'d': 6}
    }

    dijkstra(graph, 'a')


if __name__ == '__main__':
    test_dijkstra()
