# c# colution, (not mine) Problem: there are some workers and bikes in a 2d map.
# assign bike to ech worker based on manhattan distance
# this is not done to reduce overall distance for all workers together - distances are all sorted and pickup from least distance
# https://leetcode.com/problems/campus-bikes/

# the datastructure used is a map and a sortedDictionary

# public class Solution {
# / // study  C# code
# // / time complexity - calculate all possible pairs
# public int[] AssignBikes(int[][] workers, int[][] bikes)
# {
# var map = new SortedDictionary < int, List < int[] >> ();
#
# for (int i = 0; i < workers.Length; i++)
# {
# for (int j = 0; j < bikes.Length; j++)
# {
# var worker = workers[i];
# var bike = bikes[j];
#
# var distance =  Math.Abs(worker[0] - bike[0]) + Math.Abs(worker[1] - bike[1]);
#
# if (!map.ContainsKey(distance))
# {
# map.Add(distance, new List < int[] > ());
# }
#
# map[distance].Add(new int[] {i, j});
# }
# }
#
# var result = new int[workers.Length];
#
# var workerTaken = new HashSet < int > ();
# var bikeTaken = new HashSet < int > ();
#
# foreach(var d in map)
# {
# var value = d.Value;
#
# for (int i = 0; i < value.Count; i++)
# {
# var worker = value[i][0];
# var bike   = value[i][1];
#
# if (!workerTaken.Contains(worker) & & !bikeTaken.Contains(bike))
# {
# result[worker] = bike;
#
# workerTaken.Add(worker);
# bikeTaken.Add(bike);
# }
# }
# }
#
#
# return result;
# }
# }

# python solution with heap

def assignBikes(self, workers, bikes):
    distances = []  # distances[worker] is tuple of (distance, worker, bike) for each bike
    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
    heapq.heapify(queue)

    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike

    return result