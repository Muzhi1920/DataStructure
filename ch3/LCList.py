from LNode import LNode


# 循环单列表类，仅引入结点对象
class LCList:  # class of Circular Linked List
    def __init__(self):
        self.rear = None  # 只有一个尾结点域

    def isEmpty(self):
        return self.rear is None

    def prepend(self, elem):  # add element in the front end
        p = LNode(elem, None)
        if self.rear is None:
            p.next = p  # initiates circle
            self.rear = p
        else:
            p.next = self.rear.next  # p下一个是首结点
            self.rear.next = p  # p 来做首结点

    def append(self, elem):  # add element in the rear end
        self.prepend(elem)  # 添加一个结点
        self.rear = self.rear.next  # 添加完之后，尾结点往后移，做尾结点

    def pop(self):  # pop out head element
        if self.rear is None:
            raise ValueError
        p = self.rear.next  # 获取首结点
        if self.rear is p:
            self.rear = None  # 首尾相同时，清空结束
        else:
            self.rear.next = p.next  # 首结点跨越指向首结点的下一个结点
        return p.elem

    def printall(self):
        p = self.rear.next  # 获取首结点
        while True:
            print(p.elem)
            if p is self.rear:  # 后移到当首尾相同时跳出
                break
            p = p.next  # 首结点后移


if __name__ == '__main__':
    mlist = LCList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    # mlist.prepend('a')
    # mlist.printall()
    #
    while not mlist.isEmpty():
        print(mlist.pop())
    #弹出后为空
    print(mlist.rear)
