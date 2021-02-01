# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return {""}

        if n == 1:
            return {"()"}

        if n == 2:
            return {"()()", "(())"}

        results = set()

        for N in range(n / 2 + 1):
            half = self.generateParenthesis(N)
            half2 = self.generateParenthesis(n - N - 1)
            for string in half:
                for string2 in half2:
                    results.add("(" + string2 + ")" + string)
                    results.add("(" + string + ")" + string2)

                    results.add(string2 + "(" + string + ")")
                    results.add(string + "(" + string2 + ")")

                    results.add("(" + string2 + string + ")")
                    results.add("(" + string + string2 + ")")

                    results.add("()" + string2 + string)
                    results.add("()" + string + string2)

                    results.add(string2 + string + "()")
                    results.add(string + string2 + "()")

        return results
        """
        :type n: int
        :rtype: List[str]
        """
