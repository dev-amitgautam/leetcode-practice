class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            s = target - nums[i]

            if s in seen:
                return [seen[s], i]
            seen[nums[i]] = i
        return []