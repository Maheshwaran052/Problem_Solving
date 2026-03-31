""" class MinStack:

    def __init__(self):
        self.Stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)

        if not self.MinStack:
            self.MinStack.append(val)
        else:
            self.MinStack.append(min(val,self.MinStack[-1]))

    def pop(self) -> None:
        self.MinStack.pop()
        self.Stack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]
     """

class MinStack:

    def __init__(self):
        self.MinStack = []

    def push(self, val: int) -> None:
        if not self.MinStack:
            minSoFar = val
        else:
            currentMin = self.getMin()
            minSoFar = min(val, currentMin)

        self.MinStack.append((val, minSoFar))

    def pop(self) -> None:
        self.MinStack.pop()

    def top(self) -> int:
        return self.MinStack[-1][0]

    def getMin(self) -> int:
        return self.MinStack[-1][1]