# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):
# my solution - not complete
# https://leetcode.com/explore/interview/card/google/59/array-and-strings/436
class Solution(object):
    def __init__(self):
        self.storage = []
    def read4(self,read4):
        # returns 4 chars from the file
        pass

    def read(self, buf, n):
        index = 0
        if n > len(self.storage):
            remaining = n - len(self.storage)
            for i in range(len(self.storage)):
                buf[index] = self.storage[index]
                index += 1
            self.storage = []
            while remaining > 0:
                buf4 = ["", "", "", ""]
                ans = self.read4(buf4)
                if ans > remaining:
                    for i in range(remaining):
                        buf[index] = buf4[index]
                        index += 1
                    self.storage = buf4[remaining:]
                    remaining = 0
                else:
                    for i in range(ans):
                        buf[index] = buf4[index]
                        index += 1
                    remaining -= ans
            return len(buf)
        else:
            for i in range(n):
                buf[index] = self.storage[index]
                index += 1
            self.storage = self.storage[n:]
            return len(buf), buf
