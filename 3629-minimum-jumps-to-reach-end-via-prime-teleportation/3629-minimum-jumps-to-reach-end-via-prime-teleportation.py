from collections import defaultdict, deque
from math import isqrt
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        # Prime check
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            
            for d in range(3, isqrt(x) + 1, 2):
                if x % d == 0:
                    return False
            return True

        # Get unique prime factors
        def prime_factors(x):
            factors = set()

            while x % 2 == 0:
                factors.add(2)
                x //= 2

            d = 3
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 2

            if x > 1:
                factors.add(x)

            return factors

        # Map: prime factor -> indices divisible by it
        factor_to_indices = defaultdict(list)

        for i, val in enumerate(nums):
            for f in prime_factors(abs(val)):
                factor_to_indices[f].append(i)

        q = deque([(0, 0)])  # (index, steps)
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:
            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # Adjacent moves
            for ni in (i - 1, i + 1):
                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))

            # Prime teleportation
            p = nums[i]

            if is_prime(p) and p not in used_prime:
                used_prime.add(p)

                for ni in factor_to_indices[p]:
                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, steps + 1))

        return -1
        