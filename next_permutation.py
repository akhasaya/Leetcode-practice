# given a permutation of numbers, modify it in-place to change it into next permutation of the same numbers
class Solution(object):
    def nextPermutation(self, nums):
        N = len(nums)
        queue = [nums[N - 1]]

        index = N - 2
        while index > -1 and nums[index] > nums[index + 1]:
            queue.append[nums[index]]
            index -= 1

        if index > -1:
            small = nums[index]
            nums = nums[:index]
            for i in range(len(queue) - 1, -1, -1):
                if queue[i] > small:
                    nums.append(queue[i])
                    queue[i] = small
                    break
            print(nums)
            print(queue)
            queue.sort()
            nums.extend(queue)
            print(nums)
        else:
            nums.sort()
            print(nums)

        return nums

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
