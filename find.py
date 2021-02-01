# find elements that add up to a given sum and return it's indices
from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        record = defaultdict()

        for index, element in enumerate(nums):
            if target - element in record:
                return [record[target - element], index]
            else:
                record[element] = index

        return [-1, -1]

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
