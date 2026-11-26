class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        prod = 1
        start = 0
        count = 0

        for i in range(len(nums)):
            prod = prod * nums[i]

            while prod >= k:
                prod //= nums[start]
                start += 1

            count += (i - start + 1)
        return count
