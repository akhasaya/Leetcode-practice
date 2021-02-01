#https://leetcode.com/explore/interview/card/google/59/array-and-strings/3047/
# find longest substring that does not have a duplicate character

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 1
        l = len(s)
        if l < 1:
            return 0

        storage = {s[0]}
        answer = 1
        length = 1

        while right < l:
            while s[right] in storage:
                left += 1
                storage.remove(s[left - 1])
                length -= 1

            storage.add(s[right])
            right += 1
            length += 1
            answer = max(answer, length)

        return answer