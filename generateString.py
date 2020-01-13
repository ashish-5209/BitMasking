def generate(a):
    n = len(a)
    r = (1<<n)
    for i in range(r):
        filterChars(a, i)

def filterChars(a, n):
    i = 0
    while n > 0:
        print(a[i], end="") if (n&1) != 0 else print("",end="")
        i += 1
        n = n>>1
    print()

lis = ['a','b','c']
generate(lis)
