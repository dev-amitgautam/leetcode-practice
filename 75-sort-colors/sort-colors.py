class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start = 0
        mid = 0
        end = n-1

        while mid <= end:
            if nums[mid] == 1:
                mid += 1
            elif nums[mid] < 1:
                nums[start], nums[mid] = nums[mid], nums[start]
                mid += 1
                start += 1
            else:
                nums[end], nums[mid] = nums[mid], nums[end]
                end -= 1
