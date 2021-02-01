#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3055/
# given a row of sorted numbers and a range, return the array of missing ranges
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        ranges = []

        if len(nums) == 0:
            if lower == upper:
                ranges.append(str(lower))
            else:
                ranges.append(str(lower) + "->" + str(upper))

            return ranges

        if len(nums) == 1:
            if lower == upper == nums[0]:
                return []
            if lower == nums[0]:
                if upper > lower + 1:
                    ranges.append(str(lower + 1) + "->" + str(upper))
                else:
                    ranges.append(str(upper))
                return ranges
            elif upper == nums[0]:
                if lower < upper - 1:
                    ranges.append(str(lower) + "->" + str(upper - 1))
                else:
                    ranges.append(str(lower))
                return ranges
            else:
                if lower < nums[0] - 1:
                    ranges.append(str(lower) + "->" + str(nums[0] - 1))
                else:
                    ranges.append(str(lower))
                if upper > nums[0] + 1:
                    ranges.append(str(nums[0] + 1) + "->" + str(upper))
                else:
                    ranges.append(str(upper))
                return ranges

        if lower == nums[0] - 1:
            ranges.append(str(lower))
        elif lower < nums[0] - 1:
            ranges.append(str(lower) + "->" + str(nums[0] - 1))

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1] - 2:
                ranges.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
            elif nums[i] == nums[i + 1] - 2:
                ranges.append(str(nums[i] + 1))

        if upper == nums[-1] + 1:
            ranges.append(str(upper))
        elif upper > nums[-1] + 1:
            ranges.append(str(nums[-1] + 1) + "->" + str(upper))

        return ranges
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
