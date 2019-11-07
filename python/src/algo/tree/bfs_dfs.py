# From https://www.youtube.com/watch?v=oLtvUWpAnTQ


def bfs(graph, s):
    queue = [s]
    seen = set(s)
    while len(queue) > 0:
        v = queue.pop(0)
        adjacents = graph[v]
        for w in adjacents:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(v)


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


if __name__ == '__main__':
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['b', 'c', 'e', 'f'],
        'e': ['c', 'd'],
        'f': ['d']
    }

    bfs(graph, 'e')