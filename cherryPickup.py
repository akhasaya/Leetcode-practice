# https://leetcode.com/problems/cherry-pickup-ii/
# my solution - does not produce correct result - why?? - i still dont know

class Solution(object):
    def cherryPickup(self, grid):
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])

        dp = [[[-1 for i in range(n)] for j in range(n)] for k in range(m)]

        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        for row in range(1, m):
            for i in range(0, min(row + 1, n)):
                for j in range(max(n - row - 1, 0), n):
                    value = -1
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if 0 <= k < n and 0 <= l < n and k <= row and l >= n - row:
                                value = max(value, dp[m - 1][k][l])

                    dp[row][i][j] = value + grid[row][i] + (grid[row][j] if i != j else 0)

        value = 0

        for i in range(n):
            for j in range(n):
                value = max(value, dp[m - 1][i][j])

        return value
        """
        :type grid: List[List[int]]
        :rtype: int
        """


