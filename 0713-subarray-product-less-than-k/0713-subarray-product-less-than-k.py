class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        start = 0
        prod = 1
        count = 0

        for end in range(len(nums)):
            prod *= nums[end]

            while prod >= k:
                prod //= nums[start]
                start += 1

            count += end - start + 1

        return count