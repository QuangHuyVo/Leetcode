from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x: int) -> int:
            return int(str(x)[::-1])
        
        last_seen = {}
        ans = float('inf')
        
        for i, x in enumerate(nums):
            # check if current matches reverse of previous
            if x in last_seen:
                ans = min(ans, i - last_seen[x])
            
            r = reverse(x)
            last_seen[r] = i
        
        return ans if ans != float('inf') else -1