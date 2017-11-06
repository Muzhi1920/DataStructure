# 用含尾结点的链表来实现队列
from LNode import *


class LList1:
    def __init__(self):
        self.head = None
        self.rear = None

    # 增加元素
    def append(self, data):
        if self.head is None:
            self.head = LNode(data, self.head)
            self.rear = self.head
        else:
            self.rear.next = LNode(data, None)
            self.rear = self.rear.next

    # 弹出元素
    def pop(self):
        if self.head is None:
            raise ValueError
        data = self.head.elem
        self.head = self.head.next
        return data

    def printAll(self):
        p = self.head
        while p is not None:
            print(p.elem)
            p = p.next


if __name__ == '__main__':
    llist = LList1()
    for i in range(5):
        llist.append(i)
    llist.printAll()
    print(llist.pop())
