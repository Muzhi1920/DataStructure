# 递归迭代求和
def sumIt(A, n):
    return 0 if n < 1 else sumIt(A, n - 1) + A[n - 1]


# 二分递归
def sum(A, lo, hi):
    if lo == hi:
        return A[lo]
    mi = (lo + hi) >> 1
    return sum(A, lo, mi) + sum(A, mi + 1, hi)


A = [0, 1, 2, 3, 4, 5, 6]
print(sumIt(A, len(A)))
print(sum(A, 0, len(A) - 1))
