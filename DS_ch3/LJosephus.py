from LCList import LCList
#表的应用

def JosephusA(n, k, m):
    people = list(range(1, n + 1))
    num, i = 0, k - 1
    for num in range(n):
        count = 0
        while count < m:  # 够数出去一人，再执行一次，一共执行n次，直至所有人出去
            if people[i] > 0:  # 此人未退出
                count += 1
            if count == m:  # 到该人退出
                print(people[i], end="")
                people[i] = 0
            i = (i + 1) % n  # 在0-n之间递增，而且循环
        if num < n - 1:
            print(", ", end="")
        else:
            print("")
    return


def JosephusL(n, k, m):
    people = list(range(1, n + 1))
    if k < 1 or k > n:
        raise ValueError

    num, i = n, k - 1
    for num in range(n, 0, -1):
        i = (i + m - 1) % num
        print(people.pop(i), end="")
        if num > 1:
            print(", ", end="")
        else:
            print("")
    return


class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self.rear = self.rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1) #指向起始结点
        #因为循环单链表，所以一直移动，抛出，直至为空
        while not self.isEmpty():
            self.turn(m - 1)
            print(self.pop(), end="")
            if not self.isEmpty():
                print(", ", end="")
            else:
                print("")


# end class Josephus

if __name__ == '__main__':
    s = input("Josephus parameters (n k m): ")
    n, k, m = map(int, s.split())
    # JosephusA(n, k, m)
    # JosephusL(n, k, m)
    Josephus(n, k, m)
