class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        res = float('inf')
        s = 0

        for high in range(len(nums)):
            s = s + nums[high]

            while s >= target:
                res = min(res, high - low + 1)
                s = s - nums[low]
                low += 1
            
        return res if res != float('inf') else 0
