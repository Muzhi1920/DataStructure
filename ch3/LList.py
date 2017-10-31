from LNode import LNode

#单链表
class LList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    # 前向添加
    def prepend(self, elem):
        self.head = LNode(elem, self.head)

    # 删掉首结点
    def pop(self):
        if self.head is None:
            raise ValueError
        e = self.head.elem
        self.head = self.head.next
        return e

    # 后向添加
    def append(self, elem):
        if self.head is None:
            self.head = LNode(elem, None)
            return
        p = self.head  # 一般必须获取指针
        while p.next is not None:  # 循环指到最后
            p = p.next
        p.next = LNode(elem, None)  # 添加新的结点

    # 删除最后一个结点
    def poplast(self):
        if self.head is None:  # empty list
            raise ValueError
        p = self.head
        if p.next is None:  # 单结点；删除后返回
            e = p.elem
            self.head = None
            return e
        while p.next.next is not None:  # till p.next be last node
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 查找结点
    def find(self, pred):
        p = self.head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next
        return None

    def printall(self):
        p = self.head
        while p is not None:
            print(p.elem)
            p = p.next

    # 遍历数据，操作
    def for_each(self):
        p = self.head  # 得到首结点，指针
        while p is not None:
            print(p.elem * 10)  # 获取该节点元素
            p = p.next  # 该节点next对象赋给p。p即为下一个结点

    # 汇聚对象的数据，构造迭代器
    def elements(self):
        p = self.head
        while p is not None:
            if p.elem % 2 == 0:  # 添加条件汇聚
                yield p.elem
            p = p.next

    def filter(self, pred):
        p = self.head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    # 自定义函数1:定位插入  3的倍数后添加一个自定义结点
    def udf_insert(self, data):
        p = self.head
        while p is not None:
            if p.elem % 3 == 0:
                # 方式二
                # nextNode = p.next  # 获取下一结点
                # p.next = LNode(data, None)  # 新结点链接到该结点
                # p = p.next
                # p.next = nextNode
                # 方式一
                p.next = LNode(data, p.next)
                p = p.next
            p = p.next

    # 自定义函数2:删除某给定元素
    def udf_del(self, data):
        p = self.head
        while p.next is not None:
            # 判断首元素
            if self.head.elem == data:
                self.head = self.head.next
                p = self.head
            elif p.next.elem == data:
                p.next = p.next.next
            else:
                p = p.next

    def rev(self):
        p = None
        while self.head is not None:
            q = self.head
            self.head = q.next
            q.next = p   #取出截断列表的首元素，将其下一结点设置为之前的p。
            p = q    #更新p
        self.head = p


if __name__ == '__main__':
    # 构建空链表
    mlist1 = LList()

    for i in range(10):
        mlist1.prepend(i)

    for i in range(11, 20):
        mlist1.append(i)

    # mlist1.udf_insert('NB')
    # mlist1.prepend('NB')
    # mlist1.prepend('NB')
    # mlist1.udf_del('NB')
    mlist1.printall()
    mlist1.rev()
    mlist1.printall()
    # # mlist1.for_each()
    # for x in mlist1.elements():
    #     print(x)
