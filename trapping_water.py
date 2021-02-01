# https://leetcode.com/problems/trapping-rain-water/
# hard problem

class Solution(object):
    def waterInOneV(self, nums):
        print("oneV:", nums)
        m = min(nums[0], nums[-1])
        print("min:", str(m))
        water = 0
        for i in range(len(nums)):
            if m > nums[i]:
                water += m - nums[i]

        return water

    def findLocalMaximas(self, nums):
        l = len(nums)

        order = sorted(range(l), key=lambda i: -nums[i])
        maximum = order[0]

        left = [maximum]
        for i in order:
            if i < left[-1]:
                left.append(i)

        right = [maximum]
        for i in order:
            if i > right[-1]:
                right.append(i)

        left = left[::-1]
        if len(right) > 1:
            left += right[1:]

        return left

    def trap(self, height):
        if len(height) < 3:
            return 0
        borders = self.findLocalMaximas(height)
        print(borders)
        water = 0
        b = len(borders)
        for i in range(b - 1):
            water += self.waterInOneV(height[borders[i]:borders[i + 1] + 1])

        return water

        """
        :type height: List[int]
        :rtype: int
        """
