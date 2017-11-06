if __name__ == '__main__':
    mySet = set(['DataStructure'])
    mySet2 = set(['DataStructure', 'myclass'])
    print(mySet)
    print(mySet2)
    print(mySet2.difference(mySet))
    print(mySet2.union(mySet))
    print(mySet2.intersection(mySet))

