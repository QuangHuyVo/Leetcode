from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            rotated = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = matrix[i][j]
            
            return rotated

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False
        