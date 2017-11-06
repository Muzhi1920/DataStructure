""" 用list实现栈
类对象是栈
属性是列表
方法就是列表的对应的算法
"""

class StackUnderflow(ValueError):
    pass

#用python的标准库的list来实现栈
class SStack():
    def __init__(self):
        self.elem = []  # 栈类的属性就是一个列表

    def is_empty(self):
        return self.elem == []

    def top(self):
        if not self.elem:
            raise StackUnderflow
        return self.elem[len(self.elem) - 1]

    def push(self, elem):
        self.elem.append(elem)

    def pop(self):
        if self.elem == []:
            raise StackUnderflow
        return self.elem.pop()


if __name__ == '__main__':
    st = SStack()
    for i in range(0, 21, 5):
        st.push(i)
    print(st.is_empty())
    print(st.elem)
    print(st.top())
    for i in range(len(st.elem)):
        print(st.pop())
