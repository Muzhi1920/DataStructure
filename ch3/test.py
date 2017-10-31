# 构造单结点
class Node:
    def __init__(self, elm, nxt):
        self.elem = elm
        self.next = nxt

# 构造链表
class LList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = Node(data, None)

    def preappend(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e

    def popLast(self):
        if self.head is None:
            raise ValueError
        p = self.head
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def printAll(self):
        p = self.head
        while p is not None:
            print(p.elem)
            p = p.next


if __name__ == '__main__':
    lList = LList()
    for i in range(10):
        lList.preappend(i)
    lList.printAll()
    print(lList.pop())
    print(lList.popLast())
    # cList.printAll()
