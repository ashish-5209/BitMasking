def getBit(n, i):

    return 1 if (n & (1 << i)) != 0 else 0

print(getBit(13, 2))
