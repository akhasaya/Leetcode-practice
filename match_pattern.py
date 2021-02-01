# hard problem - given an array of words
# [abb, drr, tkf, dnd, ccc]
# pattern "mee"
# find words in the array that match this patter
# result is to have two hashtables - one that maps a -> m, b -> e
# one more that maps m -> a and e -> b
# https://leetcode.com/problems/find-and-replace-pattern/submissions/

from _collections import defaultdict

class Solution(object):
    def hasMap(self, word, pattern):
        l = len(pattern)
        if len(word) != l:
            return False

        matching = defaultdict()
        rev_matching = defaultdict()

        for index in range(l):
            if pattern[index] in matching.keys():
                if word[index] != matching[pattern[index]]:
                    return False

            if word[index] in rev_matching.keys():
                if pattern[index] != rev_matching[word[index]]:
                    return False
            else:
                matching[pattern[index]] = word[index]
                rev_matching[word[index]] = pattern[index]

        return True

    def findAndReplacePattern(self, words, pattern):
        output = []
        for word in words:
            if self.hasMap(word, pattern):
                output.append(word)
        return output
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

mysol = Solution()
ans = mysol.findAndReplacePattern(["abb", "bdd", "ccc"], "mee")
print("\n".join(str(x) for x in ans))