from LNode import LNode

#用链表来实现栈
class StackUnderflow(ValueError):
    pass


class LStack():  # stack implemented as a linked node list
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def top(self):
        if self.top is None:
            raise StackUnderflow
        return self.top.elem

    # 栈的添加操作就是链表的前向添加操作
    def push(self, elem):
        self.top = LNode(elem, self.top)

    def pop(self):
        if self.top is None:
            raise StackUnderflow
        e = self.top.elem
        self.top = self.top.next
        return e

    def printall(self):
        p = self.top
        while p.next is not None:
            print(p.elem)
            p = p.next


if __name__ == '__main__':
    lstack = LStack()
    print(lstack.top)
    for i in range(10):
        lstack.push(i)
    lstack.printall()