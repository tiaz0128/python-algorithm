from collections import deque


def bfs(start_pos, target, board, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_x, start_y = start_pos

    distance = [[-1] * m for _ in range(n)]
    distance[start_x][start_y] = 0

    search_queue = deque([start_pos])

    while search_queue:
        x, y = search_queue.popleft()

        if board[x][y] == target:
            return distance[x][y]

        for i in range(4):
            nx, ny = x, y  # 현재 위치에서 출발

            # [핵심 로직] 벽이나 끝에 닿을 때까지 계속 이동 (Sliding)
            while True:
                # 일단 한 칸 가봄
                nx += dx[i]
                ny += dy[i]

                # 1. 지도를 벗어나거나 OR 2. 장애물(D)을 만났다면?
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == "D":
                    # "어이쿠, 너무 갔네!" -> 한 칸 뒤로 후퇴하고 멈춤
                    nx -= dx[i]
                    ny -= dy[i]
                    break

            # 방문 안 한 곳이면 큐에 넣기
            if distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                search_queue.append((nx, ny))

    return -1


def find_start_and_goal_pos(board, n, m):
    start_pos = None
    goal_pos = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start_pos = (i, j)
            elif board[i][j] == "G":
                goal_pos = (i, j)

    return start_pos, goal_pos


def solution(board):
    n, m = len(board), len(board[0])

    start_pos, goal_pos = find_start_and_goal_pos(board, n, m)

    answer = bfs(start_pos, "G", board, n, m)

    return answer
