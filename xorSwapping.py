def xor(a, b):

    a = a^b
    b = b^a
    a = a^b

    return(a, b)

print(*xor(12, 13))
