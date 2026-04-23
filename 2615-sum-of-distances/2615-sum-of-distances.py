from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        
        # group indices
        for i, v in enumerate(nums):
            groups[v].append(i)
        
        res = [0] * len(nums)
        
        # process each group
        for indices in groups.values():
            m = len(indices)
            
            # prefix sum
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + indices[i]
            
            for k in range(m):
                idx = indices[k]
                
                # left contribution
                left = k * idx - prefix[k]
                
                # right contribution
                right = (prefix[m] - prefix[k + 1]) - (m - k - 1) * idx
                
                res[idx] = left + right
        
        return res
        