def PrintNonConsecutive1(n):
    result = []

    def Recursion(idx, current):
        if idx == n:
            result.append(current)
            return
        if current[-1] == "1":
            Recursion(idx + 1, current + "0")
        else:
            Recursion(idx + 1, current + "1")
            Recursion(idx + 1, current + "0")

    Recursion(1, "0")
    Recursion(1, "1")
    return result


print(PrintNonConsecutive1(4))
