# https://leetcode.com/problems/search-insert-position/
# accepted solution - 60%, 70% better than other sols in python
class Solution(object):
    def searchInsert(self, nums, target):
        l = len(nums)
        if l < 1:
            return 0

        if target in nums:
            return nums.index(target)

        if target < nums[0]:
            return 0
        if target > nums[l - 1]:
            return l

        low = 0
        high = l - 1
        index = l / 2

        while (True):
            if high - low < 3:
                for i in range(low, high + 1):
                    if nums[i] < target and nums[i + 1] > target:
                        return i + 1

            if target < nums[index]:
                if index - 1 > 0 and nums[index - 1] < target:
                    return index
                else:
                    high = index - 1
                    index = low + (high - low) / 2

            if nums[index] < target:
                if index + 1 < l and nums[index + 1] > target:
                    return index + 1
                else:
                    low = index + 1
                    index = low + (high - low) / 2

mysol = Solution()
print(mysol.searchInsert([1,3,5,7,11, 34, 43, 55, 56, 57, 89], 8))