# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# first hard problem i have solved in <1 hour

class Solution(object):
    def neighbours(self, row, col):
        answer = []
        if row - 1 > -1:
            answer.append([row - 1, col])
        if col - 1 > -1:
            answer.append([row, col - 1])

        if row + 1 < self.m:
            answer.append([row + 1, col])

        if col + 1 < self.n:
            answer.append([row, col + 1])

        return answer

    def longFromindex(self, i, j):
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        val = 1  # sequence of only 1
        for x, y in self.neighbours(i, j):
            # print("[{},{}] neighbour [{},{}]".format(i,j,x,y))
            if self.matrix[x][y] > self.matrix[i][j]:
                val = max(val, self.longFromindex(x, y) + 1)

        self.dp[i][j] = val
        return val

    def longestIncreasingPath(self, matrix):
        self.matrix = matrix
        # start - 12th dec, 9:10 pm
        self.m = len(matrix)
        if self.m < 1:
            return 0
        self.n = len(matrix[0])
        self.dp = [[0 for i in range(self.n)] for j in range(self.m)]

        val = 1
        for row_index in range(self.m):
            for col_index in range(self.n):
                val = max(val, self.longFromindex(row_index, col_index))

        return val
