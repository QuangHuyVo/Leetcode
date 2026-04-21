from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # build components
        for a, b in allowedSwaps:
            union(a, b)
        
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)
        
        mismatch = 0
        
        for indices in groups.values():
            count = Counter()
            
            # count source values
            for i in indices:
                count[source[i]] += 1
            
            # try match target values
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    mismatch += 1
        
        return mismatch