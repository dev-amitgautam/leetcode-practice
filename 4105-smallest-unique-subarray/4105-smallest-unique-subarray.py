import random
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = (1 << 61) - 1
        BASE = random.randrange(10**6, MOD - 1)

        # prefix hashes and powers
        h = [0] * (n + 1)
        pw = [1] * (n + 1)
        for i, x in enumerate(nums):
            h[i + 1] = (h[i] * BASE + x) % MOD
            pw[i + 1] = pw[i] * BASE % MOD

        def has_unique(L):
            cnt = Counter()
            for i in range(n - L + 1):
                cnt[(h[i + L] - h[i] * pw[L]) % MOD] += 1
            return any(v == 1 for v in cnt.values())

        lo, hi = 1, n          # hi = n is always valid
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo