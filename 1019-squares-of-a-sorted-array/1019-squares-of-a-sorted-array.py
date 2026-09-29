class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        start = 0
        end = idx = n - 1

        while start <= end:
            absStart = abs(nums[start])
            absEnd = abs(nums[end])

            if absStart > absEnd:
                res[idx] = absStart ** 2
                start += 1
            else:
                res[idx] = absEnd ** 2
                end -= 1
            idx -= 1
        return res
            

