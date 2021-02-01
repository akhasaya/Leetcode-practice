# in an array arr[0] <= arr[1] >= arr[2] <= arr[3] >= arr[4] ....
class Solution(object):
    def wiggle(self, nums, l):
        for i in range(0, l, 2):
            if i + 1 < l and nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp

            if i + 2 < l and nums[i + 2] > nums[i + 1]:
                temp = nums[i + 2]
                nums[i + 2] = nums[i + 1]
                nums[i + 1] = temp

    def isWiggled(self, nums, l):
        print(nums)
        nums = list(nums)
        for i in range(1, l, 2):
            if nums[i] < nums[i - 1]:
                return False
            if i + 1 < l and nums[i] < nums[i + 1]:
                return False

        return True

    def wiggleSort(self, nums):
        l = len(nums)
        if l < 2:
            return

        print(nums)
        while not self.isWiggled(nums, l):
            self.wiggle(nums, l)
