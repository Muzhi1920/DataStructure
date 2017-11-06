class record:
    def __init__(self, key, datum):
        self.key = key
        self.datum = datum


# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1].key > x.key:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x


# 选择排序
def select_sort(lst):
    for i in range(len(lst) - 1):  # 确定范围，至倒数2
        k = i
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:  # 取i位置后的min
                k = j
        if i != k:  # 最小值不是首元素时
            lst[i], lst[k] = lst[k], lst[i]


# 冒泡排序
def bubble_sort(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                found = True
        if not found:
            break


# 归并排序
def merge(from_lst, to_lst, low, m, high):
    i, j, k = low, m, low
    while i < m and j < high:  # 反复复制两段首记录中较小的
        if from_lst[i].key <= from_lst[j].key:
            to_lst[k] = from_lst[i]
            i += 1
        else:
            to_lst[k] = from_lst[j]
            j += 1
        k += 1
    while i < m:  # 复制第一段剩余记录
        to_lst[k] = from_lst[i]
        i += 1
        k += 1
    while j < high:  # 复制第二段剩余记录
        to_lst[k] = from_lst[j]
        j += 1
        k += 1


def merge_pass(from_lst, to_lst, llen, slen):
    i = 0
    while i + 2 * slen < llen:  # 归并长len的两段
        merge(from_lst, to_lst, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:  # 剩下两段，后段长度小于 slen
        merge(from_lst, to_lst, i, i + slen, llen)
    else:  # 只剩下一段，复制到数组to
        for j in range(i, llen):
            to_lst[j] = from_lst[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)  # 结果存回原位
        slen *= 2


if __name__ == '__main__':

    myData = [3, 5, 2, 4, 6, 1, 9, 8, 0, 7]
    # 构造要排序的对象列表
    recordList = []
    for data in myData:
        recordList.append(record(data, data ** 2))

    # 输出未排序列表
    print([rec.key for rec in recordList])
    # 对列表中的对象进行排序
    # insert_sort(recordList) #插入排序
    # select_sort(recordList) #选择排序
    # bubble_sort(recordList)  # 冒泡排序
    merge_sort(recordList)
    # 打印对象数据
    print([rec.key for rec in recordList])
