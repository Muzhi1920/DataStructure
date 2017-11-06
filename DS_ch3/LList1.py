from LNode import LNode
from LList import LList
import random

#带尾结点的单链表
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self.rear = None

    # 前向添加
    def prepend(self, elem):
        self.head = LNode(elem, self.head)
        if self.rear is None:  # 从空表中添加，需要头==尾
            self.rear = self.head

    # 后向添加
    def append(self, elem):
        if self.rear is None:  # 从空表中添加，与前向添加一样
            self.prepend(elem)
        else:  # 非空表，后向添加，然后尾指针后移
            self.rear.next = LNode(elem, None)
            self.rear = self.rear.next

    # 前向弹出
    def pop(self):
        if self.head is None:
            raise ValueError
        # 首先获取元素
        e = self.head.elem
        # 删除结点
        if self.rear is self.head:  # 仅有一个结点
            self.rear = None
        self.head = self.head.next
        return e

    # 后向弹出
    def poplast(self):
        if self.head is None:#空表
            raise ValueError
        p = self.head

        if p.next is None: #单结点
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:#找到rear前一个结点
            p = p.next
        e = p.next.elem
        self.rear = p  #构造尾结点
        p.next = None #删除尾结点
        return e


if __name__ == '__main__':
    # mlist1 = LList1()
    # for i in range(10):
    #     mlist1.prepend(i)
    #
    # for i in range(11, 20):
    #     mlist1.append(i)
    #
    # mlist1.printall()
    mlist1 = LList1()
    mlist1.prepend(99)
    for i in range(1, 20):
        mlist1.append(random.randint(1, 20))
    mlist1.printall()
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    for x in mlist1.filter(lambda y: y % 2 == 0):
        print(x)
