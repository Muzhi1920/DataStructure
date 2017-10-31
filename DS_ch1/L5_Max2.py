# 一般的，也是最坏的 2n-3
def max2(A, lo, hi):
    x1 = lo
    for i in range(lo + 1, hi):
        if A[x1] < A[i]:
            x1 = i
    x2 = lo
    for i in range(lo + 1, x1):
        if A[x2] < A[i]:
            x2 = i
    for i in range(x1 + 1, hi):
        if A[x2] < A[i]:
            x2 = i
    return x1, x2


# 递归分治----错误！
def max2_iter(A, lo, hi, x3=0, x4=0):
    mi = (lo + hi) / 2
    x1l = 0
    x2l = 0
    max2_iter(A, lo, mi, x1l, x2l)
    x1r = 0
    x2r = 0
    max2_iter(A, mi, hi, x1r, x2r)
    if A[x1l] > A[x1r]:
        x3 = x1l
        x4 = x2l if (A[x2l] > A[x1r]) else x1r
    else:
        x3 = x1r
        x4 = x1l if (A[x1l] > A[x2r]) else x2r
    return x3, x4


A = [3, 4, 2, 1, 8, 5, 6, 0, 9]
x1, x2 = max2(A, 0, 9)
print(x1, x2)

# x3, x4 = max2_iter(A, 0, 9)
# print(x3, x4)
