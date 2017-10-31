# 冒泡排序  type为小于时，递减；type为大于时，递增
def bubbleSort(A, type='>'):
    n = len(A)
    while n > 0:
        for i in range(1, n):
            if type == '<':
                if A[i - 1] < A[i]:
                    A[i - 1], A[i] = A[i], A[i - 1]
            if type == '>':
                if A[i - 1] > A[i]:
                    A[i - 1], A[i] = A[i], A[i - 1]
        n -= 1
    return A


A = [2, 1, 4, 3, 7, 5, 9, 6, 8, 0]
B = bubbleSort(A, '<')
print(B)
