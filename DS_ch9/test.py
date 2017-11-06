class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum


# 请填写插入排序代码:后取往前插 ①取值前溯；②小于前，则后赋值留空；③否则换值
def insert_sort(lst):
    pass


# 请填写选择排序代码:①取最小；②非首则交换
def select_sort(lst):
    pass


# 请填写冒泡(起泡)排序代码: ①遍历，②长度-i，③与前比较，小则换
def bubble_sort(lst):
    pass


# 快速排序
def quick_sort(lst):
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin].key
        i = begin
        for j in range(begin + 1, end + 1):
            if lst[j].key < pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i - 1)
        qsort(lst, i + 1, end)

    qsort(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    myData = [3, 5, 2, 4, 6, 1, 9, 8, 0, 7]
    # 构造要排序的对象列表
    recordList = []
    for data in myData:
        recordList.append(record(data, data ** 2))

    # 输出未排序列表
    print([rec.key for rec in recordList])
    # insert_sort(recordList)
    # select_sort(recordList)
    # bubble_sort(recordList)
    quick_sort(recordList)
    print([rec.key for rec in recordList])
