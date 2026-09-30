class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        s = 0
        res = 0
        prefix = {0: 1}

        for right in range(len(nums)):
            s += nums[right]

            needed = s - k

            if needed in prefix:
                res += prefix[needed]

            prefix[s] = prefix.get(s, 0) + 1

        return res

