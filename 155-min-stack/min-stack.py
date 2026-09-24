class MinStack(object):
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value < self.min:
            self.min = value
        self.stack.append((value, self.min))

    def pop(self):
        """
        :rtype: None
        """
        # tricky because need to remove from one stack and potentially update min in constant time
        # guarentee that the current minimum is the minimum in a stack
        value, currentMin = self.stack.pop()
        if not self.stack:
            self.min = float('inf')
        elif currentMin == value:
            _, self.min = self.stack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        val, _ = self.stack[-1]
        return val
        

    def getMin(self):
        """
        :rtype: int
        """

        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()