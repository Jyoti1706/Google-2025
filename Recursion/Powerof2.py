def power(num):
    if num == 0:
        return False
    if num == 1:
        return True
    if num % 2 == 1:
        return False

    return power(num // 2)

def SumofDigit(num):
    if num == 0:
        return 0
    return SumofDigit(num // 10)+num%10


print(power(16))
print(power(17))
print(SumofDigit(731))