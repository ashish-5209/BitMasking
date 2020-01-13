def unique(a, n):
    res = 0
    for i in a:
        res ^= i

    i = 0
    temp = res
    while temp > 0:
        if (temp&1):
            break
        i += 1
        temp >>= 1

    mask = (1<<i)
    firstNum = 0
    for i in a:
        if (mask&i) != 0:
            firstNum ^= i

    secondNum = res ^ firstNum

    return (firstNum, secondNum)

lis = [1, 2, 3, 4, 5, 4, 3, 1]
n = len(lis)
print(*unique(lis, n))
