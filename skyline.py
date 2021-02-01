# skyline problem - https://leetcode.com/problems/the-skyline-problem/
# my own solution - faster than 96.76 % solutions - unbelievable
class Solution(object):
    def getSkyline(self, buildings):
        l = len(buildings)
        if l < 1:
            return []
        skyline = []
        b1 = buildings[0]
        skyline.append([b1[0], b1[2]])
        skyline.append([b1[1], 0])

        for b in buildings[1:]:
            # new building is after all previous buildings
            if b[0] > skyline[-1][0]:
                skyline.append([b[0], b[2]])
                skyline.append([b[1], 0])
            elif b[0] == skyline[-1][0]:
                if b[2] == skyline[-2][1]:
                    skyline[-1][0] = b[1]
                else:
                    skyline[-1][1] = b[2]
                    skyline.append([b[1], 0])

            # in the array of skyline find the first interval that has start <= b[0] and next elem > b[0]
            left = 0
            right = len(skyline)
            mid = left + (right - left) / 2
            while not (skyline[mid][0] <= b[0] and skyline[mid + 1][0] > b[0]):
                if skyline[mid][0] > b[0]:
                    right = mid
                elif skyline[mid + 1][0] <= b[0]:
                    left = mid + 1

                mid = left + (right - left) / 2

            index = mid
            start2 = b[0]
            end2 = b[1]
            height2 = b[2]

            while index < len(skyline) - 1 and skyline[index][0] < end2:
                start1 = skyline[index][0]
                end1 = skyline[index + 1][0]
                height1 = skyline[index][1]

                if height2 > height1:
                    if end2 >= end1:
                        if start1 == start2:
                            # print("change ht from "+str(skyline[index][1])+" to "+str(height2))
                            skyline[index][1] = height2
                        else:
                            # print("start.is not equal")
                            skyline.insert(index + 1, [start2, height2])
                    else:
                        if start1 == start2:
                            skyline[index][1] = height2
                            skyline.insert(index + 1, [end2, height1])

                        else:
                            skyline.insert(index + 1, [start2, height2])
                            skyline.insert(index + 2, [end2, height1])

                start2 = skyline[index + 1][0]
                if index - 1 > -1 and skyline[index][1] == skyline[index - 1][1]:
                    skyline.pop(index)
                    index -= 1

                index += 1
            if skyline[-1][0] < end2:
                if skyline[-2][1] == height2:
                    skyline[-1][0] = end2
                else:
                    skyline[-1][1] = height2
                    skyline.append([end2, 0])
            # print(skyline)

        return skyline

        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
