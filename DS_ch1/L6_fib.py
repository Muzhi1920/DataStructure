# 前n-1项
def fib(n):
    return n if (n < 2) else (fib(n - 1) + fib(n - 2))


# 前 n项
def fib2(n):
    f = 0
    g = 1
    while (n > 0):
        g = g + f
        f = g - f
        n -= 1
    return g


def fib3(n):
    f1 = f2 = 1
    for k in range(1, n):
        f1, f2 = f2, f1 + f2
    return f2


print(fib(13))
print(fib2(13))
print(fib3(13))