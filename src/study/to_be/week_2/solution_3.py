def solution(grid):
    # 행 row
    n = len(grid)

    # 열 col
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            cell = grid[i][j]
            print(i, j, cell)

            if cell == -1:
                wave_plus_one(grid, n, m, i, j)

    return grid


def wave_plus_one(grid, n, m, i, j):
    # 범위
    range_xy = [-1, 0, 1]

    for y in range_xy:
        for x in range_xy:
            if not (x == 0 and y == 0):
                target_y = i + y
                target_x = j + x
                if target_y >= 0 and target_y < n and target_x >= 0 and target_x < m:
                    if grid[target_y][target_x] != -1:
                        grid[target_y][target_x] += 1
