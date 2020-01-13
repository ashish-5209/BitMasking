def single(arr, n):

    s = arr[0]

    for i in range(1,n):
        s ^= arr[i]

    return s

lis = [-3,2,3,4,4,3,2]
n = len(lis)
print(single(lis, n))
