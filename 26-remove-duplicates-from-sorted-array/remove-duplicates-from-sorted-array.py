class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return l

        start = 1

        for i in range(1, l):
            if nums[i] != nums[i-1]:
                nums[start] = nums[i]
                start += 1

        return start

        
