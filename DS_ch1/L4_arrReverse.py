# 递归倒置列表元素，lo下界，hi上界  均对应于下标
def reverse(arr, lo, hi):
    if lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        reverse(arr, lo + 1, hi - 1)
    return arr


# 非递归
def reverse1(arr, lo, hi):
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1
    return arr


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(A)
    B = reverse(A, 0, 8)
    print(B)
