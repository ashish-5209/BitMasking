def countingSlow(n):
    count = 0

    while n > 0:
        count += (n&1)
        n >>= 1

    return count

def countingFast(n):
    count = 0
    while n:
        count += 1
        n &= (n-1)

    return count

print(countingSlow(3))
print(countingFast(3))
