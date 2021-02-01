class Solution(object):
    def maxSatisfaction(self, satisfaction):
        l = len(satisfaction)

        if l < 1:
            return 0

        # sort descending
        satisfaction.sort(reverse=True)
        print(satisfaction)

        # for each elemnt choose to pick it or not

        sum_array = []
        sum_i = 0
        for i in range(l):
            sum_array.append(sum_i)
            sum_i += satisfaction[i]

        print(sum_array)
        output = 0
        for i in range(l):
            if satisfaction[i] + sum_array[i] + output > output:
                output = satisfaction[i] + sum_array[i] + output
            else:
                return output
        return output

mysol = Solution()
optimal_satisfaction = mysol.maxSatisfaction([-1,5,0,3,-8,2])
print(optimal_satisfaction)