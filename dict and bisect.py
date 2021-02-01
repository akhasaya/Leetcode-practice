# https://leetcode.com/problems/avoid-flood-in-the-city/

from collections import defaultdict
class Solution(object):
    def avoidFlood(self, rains):

        position = defaultdict()
        answer = [-1 for i in range(len(rains))]
        dry_days = []

        for index, lake in enumerate(rains):
            if lake == 0:
                answer[index] = 0
                dry_days.append(index)
                continue
            if lake not in position:
                position[lake] = index
            else:
                last = position[lake]
                # find first elem in dry_days > last , < index
                j = bisect.bisect_left(dry_days, last)
                # returns a point to insert last in dry_days

                if j < len(dry_days):
                    pos = dry_days[j]
                    dry_days.pop(j)
                    answer[pos] = lake
                    position[lake] = index
                else:
                    return []

        for index, lake in enumerate(answer):
            if lake == 0:
                answer[index] = 1

        return answer

        """
        :type rains: List[int]
        :rtype: List[int]
        """
