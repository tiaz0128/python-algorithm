from collections import deque


def dfs(graph, n, start_node):
    distance = [-1 for _ in range(n + 1)]

    distance[start_node] = 0
    search_queue = deque([start_node])

    while search_queue:
        node = search_queue.popleft()

        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                search_queue.append(neighbor)

    max_num = max(distance)
    return distance.count(max_num)


def make_graph(n, edge):
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    return graph


def solution(n, edge):
    start_node = 1

    graph = make_graph(n, edge)
    answer = dfs(graph, n, start_node)

    return answer
