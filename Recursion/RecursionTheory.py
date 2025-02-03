def recursion(num):
    if num == 0:
        return
    recursion(num-1)
    print(num, end=" ")

def recursionTail(num):
    if num == 0:
        return
    print(num, end=" ")
    recursion(num - 1)


recursion(10)
print()
recursionTail(10)