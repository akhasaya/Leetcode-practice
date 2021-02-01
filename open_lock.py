# https://leetcode.com/problems/open-the-lock/

# my solution but not right
class Solution(object):
    def toStr(self, numbers):
        return str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[3])

    def change1(self, target, index):
        if target[index] > 5:
            target[index] = (target[index] + 1) % 10
        else:
            target[index] = (target[index] - 1) % 10

    def oppositeChange(self, target, index):
        if target[index] > 5:
            target[index] = (target[index] - 1) % 10
        else:
            target[index] = (target[index] + 1) % 10

    def open(self, deadends, target):
        if target == [0, 0, 0, 0]:
            return 0
        print("target now:", target)
        distance = map(lambda i: min(i, 10 - i), target)

        for i in range(4):
            if target[i] != 0:
                print("chnaging index: " + str(i))
                self.change1(target, i)
                if self.toStr(target) not in deadends:
                    return 1 + self.open(deadends, target)

        for i in range(4):
            if distance[i] == 0:
                self.change1(target, i)
                if self.toStr(target) not in deadends:
                    return 1 + self.open(deadends, target)

                temp = self.oppositeChange(target, i)
                if self.toStr(target) not in deadends:
                    return 1 + self.open(deadends, target)

        for i in range(4):
            if distance[i] > 0:
                temp = self.oppositeChange(target, i)
                if self.toStr(target) not in deadends:
                    return 1 + self.open(deadends, target)

        return -1

    def openLock(self, deadends, target):
        if "0000" in deadends or target in deadends:
            return -1

        target = list(target)
        numbers = map(int, target)
        print(numbers)
        return self.open(deadends, numbers)

# right solution

class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1