def make_graph(n, node):
    graph = [[] for _ in range(n + 1)]

    for a, b in node:
        graph[a].append(b)
        graph[b].append(a)

    return graph


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

graph = make_graph(n, vertex)
print(graph)
