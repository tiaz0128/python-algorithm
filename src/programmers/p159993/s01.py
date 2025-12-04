from collections import deque


# S와 L의 위치를 미리 찾아둡니다.
def find_start_and_lever_pos(maps, n, m):
    start_pos = None
    lever_pos = None

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start_pos = (i, j)
            elif maps[i][j] == "L":
                lever_pos = (i, j)

    return start_pos, lever_pos


def bfs(start, target, maps, n, m):
    start_x, start_y = start

    distance = [[-1] * m for _ in range(n)]
    distance[start_x][start_y] = 0

    search_queue = deque([start])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while search_queue:
        x, y = search_queue.popleft()

        if maps[x][y] == target:
            return distance[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] != "X" and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    search_queue.append((nx, ny))
    return -1


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    start_pos, lever_pos = find_start_and_lever_pos(maps, n, m)

    one_time = bfs(start_pos, "L", maps, n, m)

    if one_time == -1:
        return -1

    two_time = bfs(lever_pos, "E", maps, n, m)

    if two_time == -1:
        return -1

    return one_time + two_time
