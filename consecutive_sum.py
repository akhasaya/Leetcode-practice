# given a number N, find the number of ways in which it can be written as a sum of consecutive numbers
# https://leetcode.com/problems/consecutive-numbers-sum/
class Solution(object):
    def consecutiveNumbersSum(self, N):
        ways = 1
        i = 2
        while (N / i) > ((i - 1) / 2): # there should be i-1 / 2 numbers before N/i to compute sum of those numbers
            if i % 2 == 1:
                if int(N / i) * i == N :
                    print(i)
                    ways += 1

            else:
                if (2 * int(N / i) + 1) * int(i / 2) == N:
                    print(i)
                    ways += 1

            i += 1

        return ways
