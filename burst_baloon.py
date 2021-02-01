# https://leetcode.com/problems/burst-balloons/ - didn't solve it yet

class Solution(object):
    def calcLR(self, bits):
        l = 0
        left = [0]
        for i in range(1, self.N):
            if bits[i - 1] == "1":
                l = i - 1
            left.append(l)

        r = self.N - 1
        right = [self.N - 1 for i in range(self.N)]
        for i in range(self.N - 2, -1, -1):
            if bits[i + 1] == "1":
                r = i + 1
            right[i] = r

        return left, right

    def dp(self, available):
        if available in self.store:
            return self.store[available]

        coins = 0

        left, right = self.calcLR(available)
        for i in range(1, self.N - 1):
            if available[i] == "1":
                new_avail = available[:i] + "0" + available[i + 1:]
                coins = max(coins, self.nums[i] * self.nums[left[i]] * self.nums[right[i]] + self.dp(new_avail))

        self.store[available] = coins
        return coins

    def maxCoins(self, nums):
        self.N = len(nums)
        if self.N == 1:
            return nums[0]
        self.nums = [1] + nums + [1]
        self.N += 2
        self.store = defaultdict()

        return self.dp(str("{0:0b}".format(2 ** (self.N + 2) - 1)))
        """
        :type nums: List[int]
        :rtype: int
        """
