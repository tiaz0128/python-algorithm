def solution(grid: list[list[int]]) -> list[list[int]]:
    n, m = len(grid), len(grid[0])

    def is_valid_cell(y, x):
        return 0 <= y < n and 0 <= x < m

    def update_adjacent_cells(i, j):
        range_xy = [-1, 0, 1]
        for y in range_xy:
            for x in range_xy:
                if not (x == 0 and y == 0):
                    target_y, target_x = i + y, j + x
                    if (
                        is_valid_cell(target_y, target_x)
                        and grid[target_y][target_x] != -1
                    ):
                        grid[target_y][target_x] += 1

    for i in range(n):
        for j in range(m):
            cell = grid[i][j]

            if cell == -1:
                update_adjacent_cells(i, j)

    return grid
