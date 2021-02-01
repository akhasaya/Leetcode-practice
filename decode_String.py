# my solution - in this i decode from outer scope to inner scope
# the more efficient way is to decode from inner to outer, which can be implemented with stack
class Solution(object):
    def decodeString(self, s):
        def expand(number, string):
            result = ""
            for i in range(number):
                result += string

            return result

        l = len(s)
        answer = ""
        index = 0
        while index < l and s[index].isalpha():
            answer += s[index]
            index += 1
        if index == l:
            return answer

        number = ""
        while index < l and s[index].isdigit():
            number += s[index]
            index += 1
        print(number)

        if len(number) > 0 and s[index] != "[":
            return "error"
        else:
            index += 1

        left = 1
        right = 0
        start = index
        itr = start
        for letter in s[index:]:
            if letter == "[":
                left += 1

            elif letter == "]":
                right += 1
                if left == right:
                    break
            itr += 1

        print(int(number))
        answer += expand(int(number), s[start:itr])
        if itr < l - 1:
            answer += s[itr + 1:]

        print(answer)

        return self.decodeString(answer)

        """
        :type s: str
        :rtype: str
        """
