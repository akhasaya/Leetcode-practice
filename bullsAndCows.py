# bulls and games - https://leetcode.com/problems/bulls-and-cows/
from collections import Counter
class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        l = len(secret)
        for i in range(l):
            if secret[i] == guess[i]:
                bulls += 1

        sec = Counter(secret)
        gss = Counter(guess)
        cows = 0
        for i in sec.keys():
            cows += min(sec[i], gss[i])

        cows = cows - bulls

        s = str(bulls) + "A" + str(cows) + "B"
        return s
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
