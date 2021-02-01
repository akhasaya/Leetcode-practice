# https://leetcode.com/problems/string-to-integer-atoi/submissions/
class Solution(object):
    def myAtoi(self, s):
        l = len(s)

        if l < 1:
            return 0

        i = 0
        while i < l and s[i] == ' ':
            i += 1

        if i == l:
            return 0

        j = i
        sighns = ["+", "-"]
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        if (s[j] in sighns and j + 1 < l and s[j + 1] in digits) or (s[j] in digits):
            if s[j] in sighns:
                j += 2
            else:
                j += 1

            while j < l and s[j] in digits:
                j += 1
            print("i is: " + str(i))
            print("j is: " + str(j))
            first_num = s[i:j]
            first_num = int(first_num)

            if first_num < -2147483648:
                return -2147483648
            elif first_num > 2147483647:
                return 2147483647
            return first_num

        return 0
        """
        :type s: str
        :rtype: int
        """

mysol = Solution()
print(mysol.myAtoi("   +-42"))