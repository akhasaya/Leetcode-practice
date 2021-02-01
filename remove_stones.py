# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# I coded this after reading the answer provided in leetcode
# this code looks much cleaner than any code i have written before

class Solution(object):
    def removeStones(self, stones):
        ls = len(stones)
        adj_list = [[] for i in range(ls)]

        for i1 in range(ls):
            for i2 in range(i1):
                if stones[i1][0] == stones[i2][0] or stones[i1][1] == stones[i2][1]:
                    adj_list[i1].append(i2)
                    adj_list[i2].append(i1)

        seen = [False] * ls
        ans = 0
        for i in range(ls):
            if seen[i] == False:
                stack = [i]
                seen[i] = True
                while stack:
                    elem = stack.pop()
                    for nei in adj_list[elem]:
                        if seen[nei] == False:
                            stack.append(nei)
                            seen[nei] = True
                            ans += 1

        return ans

        """
        :type stones: List[List[int]]
        :rtype: int
        """
