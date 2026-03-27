from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            if i % 2 == 0:
                shifted = mat[i][k:] + mat[i][:k]
            else:
                shifted = mat[i][-k:] + mat[i][:-k]

            if shifted != mat[i]:
                return False

        return True