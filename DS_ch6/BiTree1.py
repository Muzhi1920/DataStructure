# 用python类实现二叉树

class BiTNodeError(ValueError):
    pass


class BiTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


# 获取二叉树的所有的结点数
def count_BiTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BiTNodes(t.left) + count_BiTNodes(t.right)


# 获取二叉树的所有数据之和
def sum_BiTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BiTNodes(t.left) + sum_BiTNodes(t.right)


# …………………………深度优先遍历……………………
# 先根序 遍历二叉树的递归函数
def preorder(t, proc=print):
    if t is None:
        return
    # assert (isinstance(t, BiTNode))
    proc(t.data)
    preorder(t.left)
    preorder(t.right)


# 中根序 默认是输出该值
def inorder(t, proc=print):
    if t is None: return
    inorder(t.left)
    proc(t.data)
    inorder(t.right)


# 中根序 默认是输出该值
def postorder(t, proc=print):
    if t is None: return
    postorder(t.left)
    postorder(t.right)
    proc(t.data)


# ………………宽度优先遍历………………
from SQueue import *


def levelorder(t, proc):
    q = SQueue()
    q.enqueue(t)
    while not q.is_empty():
        n = q.dequeue()
        if t is None:
            continue
        q.enqueue(t.left)
        q.enqueue(t.right)
        proc(t.data)


from SStack import *


def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # go down along left chain
            s.push(t.right)  # push right branch into stack
            proc(t.data)
            t = t.left
        t = s.pop()  # left chain ends, backtrack


def preorder_iter(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            yield t.data
            t = t.left
        t = s.pop()


def inorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left
        t = s.pop()
        proc(t.data)
        t = t.right


def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:  # iterate until top has no child
            s.push(t)
            t = t.left if t.left is not None else t.right
            # if we can go left, go, otherwise, go right
        t = s.pop()  # get the node to be access
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right  # end of left visit, turn right
        else:
            t = None  # end of right visit, force to backtrack


def print_BiTNodes(t):
    if t is None:
        print("^", end="")
        return
    print("(" + str(t.data), end="")
    print_BiTNodes(t.left)
    print_BiTNodes(t.right)
    print(")", end="")


class BiTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def preorder_iter(self):
        t, s = self._root, SStack()
        while t is not None or not s.is_empty():
            while t is not None:
                s.push(t.right)
                yield t.data
                t = t.left
            t = s.pop()


if __name__ == '__main__':
    pass
