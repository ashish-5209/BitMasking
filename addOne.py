def addOne1(n):

    m = 1
    while n & m:
        n ^= m
        m <<= 1

    n ^= m

    return n

def addOne2(n):
    return -(~n)

print(addOne1(11))
print(addOne2(11))
