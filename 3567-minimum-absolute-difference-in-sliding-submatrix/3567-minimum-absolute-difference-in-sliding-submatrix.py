class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range (m - k + 1)]

        for i in range(m - k + 1):
            for j in range (n - k + 1):
                values =[]

                for r in range (i, i + k):
                    for e in range (j, j + k):
                        values.append(grid[r][e])
                        
                distinct_vals = sorted(set(values))

                if len(distinct_vals) <= 1:
                    ans[i][j] = 0
                else:
                    best = float("inf")
                    for t in range(1, len(distinct_vals)):
                        best = min(best, distinct_vals[t] - distinct_vals[t - 1])
                    ans[i][j] = best

        return ans