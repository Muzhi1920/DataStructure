# 结点元素为数据，结点的next是下一个结点

#create Node class
class LNode:
    def __init__(self, elm, nxt):
        self.elem = elm
        self.next = nxt


if __name__ == '__main__':
    llist1 = LNode(1, None)  # 建立表首结点
    pnode = llist1  # 表指针指向首结点

    for i in range(2, 11):
        pnode.next = LNode(i, None)  # 该结点指向————>下一个结点
        pnode = pnode.next  # 表指针指向该节点

    pnode = llist1  # 链表建立完毕，指针指向首结点

    while pnode:  # when not null
        print(pnode.elem)
        pnode = pnode.next
