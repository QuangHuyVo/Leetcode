from typing import List
from math import inf

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = 0
        row_sums = [0] * m
        col_sums = [0] * n

        first_row = {}
        last_row = {}
        first_col = {}
        last_col = {}

        # Precompute sums and boundary positions for each value
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                total += v
                row_sums[i] += v
                col_sums[j] += v

                if v not in first_row:
                    first_row[v] = i
                    first_col[v] = j
                else:
                    first_row[v] = min(first_row[v], i)
                    first_col[v] = min(first_col[v], j)

                last_row[v] = i
                last_col[v] = j

        # Check if a value can be removed from the top section
        def can_remove_top(diff: int, cut_row: int) -> bool:
            rows = cut_row + 1
            if rows == 1:
                return grid[0][0] == diff or grid[0][n - 1] == diff
            if n == 1:
                return grid[0][0] == diff or grid[cut_row][0] == diff
            return diff in first_row and first_row[diff] <= cut_row

        # Check if a value can be removed from the bottom section
        def can_remove_bottom(diff: int, cut_row: int) -> bool:
            start = cut_row + 1
            rows = m - start
            if rows == 1:
                return grid[start][0] == diff or grid[start][n - 1] == diff
            if n == 1:
                return grid[start][0] == diff or grid[m - 1][0] == diff
            return diff in last_row and last_row[diff] >= start

        # Check if a value can be removed from the left section
        def can_remove_left(diff: int, cut_col: int) -> bool:
            cols = cut_col + 1
            if cols == 1:
                return grid[0][0] == diff or grid[m - 1][0] == diff
            if m == 1:
                return grid[0][0] == diff or grid[0][cut_col] == diff
            return diff in first_col and first_col[diff] <= cut_col

        # Check if a value can be removed from the right section
        def can_remove_right(diff: int, cut_col: int) -> bool:
            start = cut_col + 1
            cols = n - start
            if cols == 1:
                return grid[0][start] == diff or grid[m - 1][start] == diff
            if m == 1:
                return grid[0][start] == diff or grid[0][n - 1] == diff
            return diff in last_col and last_col[diff] >= start

        # Try horizontal cuts
        top_sum = 0
        for cut_row in range(m - 1):
            top_sum += row_sums[cut_row]
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            if top_sum > bottom_sum:
                if can_remove_top(diff, cut_row):
                    return True
            else:
                if can_remove_bottom(diff, cut_row):
                    return True

        # Try vertical cuts
        left_sum = 0
        for cut_col in range(n - 1):
            left_sum += col_sums[cut_col]
            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if can_remove_left(diff, cut_col):
                    return True
            else:
                if can_remove_right(diff, cut_col):
                    return True

        return False