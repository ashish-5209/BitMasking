def setBit(n, i):

    n = n | (1 << i)
    return n

print(setBit(13, 1))
