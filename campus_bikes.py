# bikes and workers are located in a map
# passes 22/44 test cases - leads to TLE for large test cases
# maybe try with selective bikes instead of trying with all bikes for each worker

class Solution(object):
    def min_manhattan(self, distance, workers, bikes):
        if len(workers) < 1:
            return 0
        worker_no = workers[0]
        inf = 10 ** 7
        total_dis = inf
        for b in range(len(bikes)):
            total_dis = min(total_dis, distance[worker_no][bikes[b]] + self.min_manhattan(distance, workers[1:],
                                                                                          bikes[:b] + bikes[b + 1:]))
        return total_dis

    def assignBikes(self, workers, bikes):
        nw = len(workers)
        nb = len(bikes)

        dis_array = []
        distance = [[None for i in range(nb)] for j in range(nw)]
        for i in range(nw):
            for j in range(nb):
                d = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
                dis_array.append(d)

        index = 0
        for i in range(nw):
            for j in range(nb):
                distance[i][j] = dis_array[index]
                index += 1
        dis = self.min_manhattan(distance, range(nw), range(nb))

        return dis

        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
