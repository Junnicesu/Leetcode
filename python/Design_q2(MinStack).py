class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = 2**31-1

    def push(self, val: int) -> None:
        self.data.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        if len(self.data) == 1:
            self.min = 2**31-1
            self.data.pop()
            return
        if self.data[-1] == self.min:
            self.min = min(self.data[:-1])
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''
Your input

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Your answer

[null,null,null,null,-3,null,0,-2]

Expected answer

[null,null,null,null,-3,null,0,-2]
'''