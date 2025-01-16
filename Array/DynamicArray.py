class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    def resize(self):
        print("resizing initiated")
        self.capacity *= 2
        tempArray = [0] * self.capacity

        for i, data in enumerate(self.arr):
            tempArray[i] = data

        self.arr = tempArray

    def pushback(self, data):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = data
        self.length += 1

    def popback(self):
        if self.length > 0:
            self.arr[self.length-1] = 0
            self.length -= 1


    def getvalue(self, idx):
        if 0 <= idx < self.length:
            return self.arr[idx]
        else:
            raise OverflowError

    def insertatIndex(self, idx, data):
        if self.length == self.capacity:
            self.resize()
        for i in range(self.length, idx-1, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[idx] = data
        self.length += 1

    def print(self):
        print("[", end=" ")
        for i in range(self.length):
            print(self.arr[i], end=", ")
        print("]")


arr = Array()
arr.pushback(20)
arr.pushback(30)
arr.pushback(60)
arr.pushback(40)
arr.pushback(50)
arr.print()
arr.popback()
arr.print()
arr.popback()
arr.print()
arr.insertatIndex(1,11)
arr.print()
