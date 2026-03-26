from collections import Counter
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        # ---------- Helper for horizontal cuts ----------
        def can_remove_from_top(diff: int, cut_row: int, top_count: Counter) -> bool:
            rows = cut_row + 1
            area = rows * n

            if area <= 1:
                return False

            # A line: only endpoint cells can be removed
            if n == 1:
                return grid[0][0] == diff or grid[cut_row][0] == diff

            if rows == 1:
                return grid[0][0] == diff or grid[0][n - 1] == diff

            # Real rectangle: removing any one cell keeps it connected
            return top_count[diff] > 0

        def can_remove_from_bottom(diff: int, cut_row: int, bottom_count: Counter) -> bool:
            start = cut_row + 1
            rows = m - start
            area = rows * n

            if area <= 1:
                return False

            if n == 1:
                return grid[start][0] == diff or grid[m - 1][0] == diff

            if rows == 1:
                return grid[start][0] == diff or grid[start][n - 1] == diff

            return bottom_count[diff] > 0

        # ---------- Check all horizontal cuts ----------
        top_sum = 0
        top_count = Counter()
        bottom_count = Counter()

        for row in grid:
            bottom_count.update(row)

        for i in range(m - 1):
            row_sum = sum(grid[i])
            top_sum += row_sum

            for val in grid[i]:
                top_count[val] += 1
                bottom_count[val] -= 1
                if bottom_count[val] == 0:
                    del bottom_count[val]

            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                if can_remove_from_top(diff, i, top_count):
                    return True
            else:
                if can_remove_from_bottom(diff, i, bottom_count):
                    return True

        # ---------- Helper for vertical cuts ----------
        def can_remove_from_left(diff: int, cut_col: int, left_count: Counter) -> bool:
            cols = cut_col + 1
            area = m * cols

            if area <= 1:
                return False

            if m == 1:
                return grid[0][0] == diff or grid[0][cut_col] == diff

            if cols == 1:
                return grid[0][0] == diff or grid[m - 1][0] == diff

            return left_count[diff] > 0

        def can_remove_from_right(diff: int, cut_col: int, right_count: Counter) -> bool:
            start = cut_col + 1
            cols = n - start
            area = m * cols

            if area <= 1:
                return False

            if m == 1:
                return grid[0][start] == diff or grid[0][n - 1] == diff

            if cols == 1:
                return grid[0][start] == diff or grid[m - 1][start] == diff

            return right_count[diff] > 0

        # ---------- Check all vertical cuts ----------
        left_sum = 0
        left_count = Counter()
        right_count = Counter()

        for r in range(m):
            for c in range(n):
                right_count[grid[r][c]] += 1

        col_sums = [0] * n
        for c in range(n):
            for r in range(m):
                col_sums[c] += grid[r][c]

        for j in range(n - 1):
            left_sum += col_sums[j]

            for r in range(m):
                val = grid[r][j]
                left_count[val] += 1
                right_count[val] -= 1
                if right_count[val] == 0:
                    del right_count[val]

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if can_remove_from_left(diff, j, left_count):
                    return True
            else:
                if can_remove_from_right(diff, j, right_count):
                    return True

        return False