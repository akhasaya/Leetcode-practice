# i solved, it was asked in plivo interview
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []
        """
        initialize your data structure here.
        """

    def push(self, x):
        self.stack.append(x)
        if len(self.stack) == 1 or x <= self.getMin():
            self.min_stack.append(x)

        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        if self.top() == self.getMin():
            self.min_stack.pop()
        self.stack.pop()

        """
        :rtype: None
        """

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        return self.min_stack[-1]
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()