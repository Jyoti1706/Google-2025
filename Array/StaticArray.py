class StaticArray:
    def __init__(self, arrSize):
        self.size = arrSize
        self.arr = [0 for _ in range(arrSize)]
        self.currentSize = 0

    def insertEnd(self, data):
        if self.currentSize < self.size:
            self.arr[self.currentSize] = data
            self.currentSize += 1
        else:
            raise ValueError

    def removeEnd(self):
        if self.currentSize > 0:
            self.arr[self.currentSize] = 0
            self.currentSize -= 1
        else:
            raise ValueError

    def insertMiddle(self, pos, data):
        if self.currentSize < self.size and pos-2 >= 0:
            for i in range(self.currentSize, pos-2, -1):
                self.arr[i + 1] = self.arr[i]
            self.currentSize += 1
            self.arr[pos - 1] = data
        else:
            raise ValueError

    def removeMiddle(self, pos):
        if pos <= self.currentSize:
            for i in range(pos-1, self.currentSize):
                self.arr[i] = self.arr[i + 1]
            self.arr[self.currentSize] = 0
            self.currentSize -= 1
        else:
            raise ValueError

    def PrintArray(self):
        print("[", end=" ")
        for i in range(0, self.currentSize):
            print(self.arr[i], end=",")
        print("]")


arr = StaticArray(5)
arr.insertEnd(20)
arr.insertEnd(25)
arr.insertEnd(30)
arr.insertEnd(10)
arr.PrintArray()
arr.removeEnd()
arr.PrintArray()
arr.insertMiddle(2,11)
arr.PrintArray()
arr.removeMiddle(3)
arr.PrintArray()
