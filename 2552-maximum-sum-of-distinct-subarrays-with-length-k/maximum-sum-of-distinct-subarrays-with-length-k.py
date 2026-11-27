class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        window_sum = 0
        res = 0
        freq = {}

        for i in range(len(nums)):
            # Add incoming element
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

            # Maintain window size k
            if i - low + 1 > k:
                outgoing = nums[low]
                window_sum -= outgoing

                freq[outgoing] -= 1

                if freq[outgoing] == 0:
                    del freq[outgoing]

                low += 1

            # Check window validity
            if i - low + 1 == k and len(freq) == k:
                res = max(res, window_sum)

        return res