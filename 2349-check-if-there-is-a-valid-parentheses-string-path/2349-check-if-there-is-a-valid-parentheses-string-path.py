class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):

                new_dp = set()

                if i == 0 and j == 0:
                    new_dp.add(1)

                else:
                    if i > 0:
                        new_dp.update(dp[j])

                    if j > 0:
                        new_dp.update(dp[j - 1])

                    change = 1 if grid[i][j] == '(' else -1

                    new_dp = {
                        balance + change
                        for balance in new_dp
                        if balance + change >= 0
                    }

                dp[j] = new_dp

        return 0 in dp[n - 1]