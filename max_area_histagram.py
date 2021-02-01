# https://leetcode.com/problems/largest-rectangle-in-histogram/ - my solution - yet to be verified
class Solution(object):
    def largestRectangleArea(self, heights):
        N = len(heights)
        if N < 1:
            return 0
        min_after = [0 for i in range(N)]
        m = heights[N - 1]
        m_i = N - 1
        for index in range(N - 1, -1, -1):
            if heights[index] <= m:
                m = heights[index]
                m_i = index
            min_after[index] = m_i

        # print(min_after)
        max_area = 0
        for index in range(N):
            m = 10 ** 9
            area = 0
            for j in range(index, min_after[index] + 1):
                if index == min_after[index]:
                    area = heights[j] * (N - index)
                elif j == index:
                    area = heights[j]
                    m = heights[j]
                elif j == min_after[index]:
                    area = heights[j] * (N - index)
                else:
                    m = min(m, heights[j])
                    area = (j - index + 1) * m
                # print(area)
                if area > max_area:
                    max_area = area

        return max_area
        """
        :type heights: List[int]
        :rtype: int
        """
