def signed(x, y):

    return (x^y) < 0

def unsigned(x, y):

    return (False if (x^y)>>31 == 0 else True)

print(signed(-1, 100))
print(unsigned(1, 100))
