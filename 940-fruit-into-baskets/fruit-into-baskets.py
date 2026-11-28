class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        low = 0
        seen = {}
        res = 0

        for high in range(len(fruits)):
            seen[fruits[high]] = seen.get(fruits[high], 0) + 1

            while len(seen) > 2:
                seen[fruits[low]] = seen[fruits[low]] - 1

                if seen[fruits[low]] == 0:
                    del seen[fruits[low]]
                low += 1

            res = max(res, high - low + 1) 
        return res