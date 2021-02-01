# slpit array into m continous subarrays such that maximum of subarray sums is minimum
# https://leetcode.com/problems/split-array-largest-sum/
# my solution - solved it on my own - but took 2 hours or so

class Solution(object):
    def splitArray(self, nums, m):
        N = len(nums)
        print("N=", str(N))
        inf = 10 ** 9
        dp = [[inf] * N] * m

        dp[0][0] = nums[0]
        for i in range(1, N):
            # splitting into 1 subarray
            dp[0][i] = dp[0][i - 1] + nums[i]

        if m == 1:
            return dp[0][N - 1]

        ans = 0
        for i in range(1, m):
            sum_array = list(dp[i - 1])
            for j in range(i, N):
                s = 0
                minimised = 0
                for k in range(j - 1, i - 2, -1):
                    s += nums[k + 1]
                    m = sum_array[k]
                    max_sub_sum = max(s, m)

                    if k == j - 1:
                        minimised = max_sub_sum
                    else:
                        minimised = min(minimised, max_sub_sum)

                    if m < s:
                        break
                dp[i][j] = minimised
                ans = minimised
        return ans

        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
