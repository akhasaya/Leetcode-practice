# given a bunch of points, return K closest neighbours to origin
# my solution
from heapq import heapify, heappush, heappop
from collections import defaultdict

class Solution(object):
    def kClosest(self, points, K):
        heap = []
        heapify(heap)
        record = defaultdict(list)

        for point in points:
            dis = point[0] ** 2 + point[1] ** 2
            heappush(heap, [dis, point[0], point[1]])
            record[dis].append(point)

        result = []
        for i in range(K):
            dis = heappop(heap)
            result.append([dis[1], dis[2]])

        return result
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

# given solution
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
