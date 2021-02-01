# https://leetcode.com/problems/meeting-rooms-ii/
class Solution(object):
    def minMeetingRooms(self, intervals):
        record = []

        l = len(intervals)
        if l < 2:
            return l
        rooms = 1

        intervals.sort()

        for start, end in intervals:
            clash = 0
            for s, e in record:
                if start < e:
                    clash += 1
            if clash + 1 > rooms:
                rooms = clash + 1
            record.append([start, end])

        return rooms

        """
        :type intervals: List[List[int]]
        :rtype: int
        """
