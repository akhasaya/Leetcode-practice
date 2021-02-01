# i did binary search
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/


class Solution(object):
    def searchRange(self, nums, target):
        l = len(nums)
        if l < 1:
            return [-1, -1]
        if l == 1:
            if target == nums[0]:
                return [0, 0]
            else:
                return [-1, -1]

        left = 0
        right = l - 1
        mid = (left + right) / 2

        first = -1
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        while left <= right:
            if nums[mid] == target:
                first = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            mid = (left + right) / 2

        if first == -1:
            return [-1, -1]

        position = first
        while first > 0 and nums[first - 1] == target:
            first -= 1

        second = position
        while second < l - 1 and nums[second + 1] == target:
            second += 1

        return [first, second]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
