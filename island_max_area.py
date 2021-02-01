#https://leetcode.com/problems/max-area-of-island/
# faster than 100% submissions

class Solution(object):
    def calculate(self, grid, i, j):
        count = 0
        if grid[i][j] == 1:
            grid[i][j] = 2
            count += 1
        else:
            return count

        if i > 0 and grid[i - 1][j] == 1:
            count += self.calculate(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == 1:
            count += self.calculate(grid, i, j - 1)
        if i < self.rows - 1 and grid[i + 1][j] == 1:
            count += self.calculate(grid, i + 1, j)
        if j < self.cols - 1 and grid[i][j + 1] == 1:
            count += self.calculate(grid, i, j + 1)

        return count

    def maxAreaOfIsland(self, grid):
        self.rows = len(grid)
        self.cols = len(grid[0])

        max_area = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    area = self.calculate(grid, i, j)
                    if area > max_area:
                        max_area = area

        return max_area
        """
        :type grid: List[List[int]]
        :rtype: int
        """
