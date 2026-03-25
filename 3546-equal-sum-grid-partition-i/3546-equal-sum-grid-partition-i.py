from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total = sum(sum(row) for row in grid)

        # Check horizontal cuts
        top_sum = 0
        for i in range(m - 1):  
            top_sum += sum(grid[i])
            if top_sum * 2 == total:
                return True

        # Check vertical cuts
        col_sums = [0] * n
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]

        left_sum = 0
        for j in range(n - 1):  
            left_sum += col_sums[j]
            if left_sum * 2 == total:
                return True

        return False