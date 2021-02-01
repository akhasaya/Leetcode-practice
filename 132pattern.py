from collections import defaultdict
class Solution(object):
    def find132pattern(self, nums):
        NINF = -10 ** 7
        N = len(nums)
        if N < 3:
            return False

        intervals = defaultdict()

        intervals[nums[0]] = NINF

        for i in nums[1:]:
            for key in intervals.keys():
                if i > intervals[key] and i > key:
                    intervals[key] = i
                    if i not in intervals.keys():
                        intervals[i] = NINF
                elif key < i < intervals[key]:
                    return True
                elif i < key and i not in intervals.keys():
                    intervals[i] = NINF
        return False

# ascii values in python
print(chr(ord('1')+1))
