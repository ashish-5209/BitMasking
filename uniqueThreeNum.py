def unique(lis, n):

    arr = [0]*64

    for j in range(n):

        i = 0
        no = lis[j]
        while no > 0:
            arr[i] += (no&1)
            i += 1
            no >>= 1

    p = 1
    ans = 0
    for k in range(64):
        arr[k] = arr[k] % 3

        ans += arr[k]*p
        p <<= 1

    return ans


lis = [7,7,3,4,12,6,6,6,3,3,4,4,7]
n = len(lis)
print(unique(lis, n))
