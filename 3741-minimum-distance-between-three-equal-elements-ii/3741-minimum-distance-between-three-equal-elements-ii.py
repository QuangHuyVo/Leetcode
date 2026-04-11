class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        
        # Step 1: collect indices
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = float('inf')
        
        # Step 2: check each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            # Step 3: sliding window of size 3
            for i in range(len(indices) - 2):
                dist = indices[i + 2] - indices[i]
                res = min(res, dist)
        
        return -1 if res == float('inf') else 2 * res
        