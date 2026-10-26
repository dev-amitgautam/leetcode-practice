class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        seen = []

        for ch in s:
            seen.append(ch)

            if len(seen) >= k:
                isDuplicate = False
                temp = seen[-k:]
                for i, c in enumerate(temp):
                    if temp[i] != temp[i-1]:
                        break
                    if i == len(temp) - 1: 
                        isDuplicate = True

                if isDuplicate:
                    del seen[-k:]

        return ''.join(seen)