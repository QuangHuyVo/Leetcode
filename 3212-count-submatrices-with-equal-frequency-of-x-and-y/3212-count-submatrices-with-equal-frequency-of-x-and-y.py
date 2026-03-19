from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        col_x = [0] * cols
        col_y = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'X':
                    col_x[j] += 1
                elif grid[i][j] == 'Y':
                    col_y[j] += 1

            x_total = 0
            y_total = 0

            for j in range(cols):
                x_total += col_x[j]
                y_total += col_y[j]

                if x_total == y_total and x_total > 0:
                    count += 1

        return count
        