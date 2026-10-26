class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        seen = []

        for i in range(n):
            while seen and temperatures[i] > temperatures[seen[-1]]:
                last = seen.pop()
                res[last] = i - last

            seen.append(i)
            
        return res