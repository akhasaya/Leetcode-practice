# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3057/

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        l = len(indexes)

        order = sorted(range(l), key=lambda i: indexes[i])

        if order != range(l):
            s = []
            t = []
            j = []
            for i in order:
                j.append(indexes[i])
                s.append(sources[i])
                t.append(targets[i])
            indexes = j
            sources = s
            targets = t

        diff = 0
        for i in range(l):
            sub = len(sources[i])
            j = indexes[i] + diff
            if S[j:j + sub] == sources[i]:
                S = S[:j] + targets[i] + S[j + sub:]

                diff += len(targets[i]) - sub

        print(S)
        return S

        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """

