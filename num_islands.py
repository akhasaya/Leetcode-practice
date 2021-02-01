class Solution(object):
    def change2(self, grid, m, n, i, j):
        grid[i][j] = "2"
        if i - 1 > -1 and grid[i - 1][j] == "1":
            self.change2(grid, m, n, i - 1, j)
        if i + 1 < m and grid[i + 1][j] == "1":
            self.change2(grid, m, n, i + 1, j)
        if j - 1 > -1 and grid[i][j - 1] == "1":
            self.change2(grid, m, n, i, j - 1)
        if j + 1 < n and grid[i][j + 1] == "1":
            self.change2(grid, m, n, i, j + 1)

    def numIslands(self, grid):
        islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    self.change2(grid, m, n, i, j)

        return islands
        """
        :type grid: List[List[str]]
        :rtype: int
        """
