class MinStack:
    def __init__(self):
        self.arr = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minStack or self.minStack[-1] >= val:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.arr[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minStack[-1]