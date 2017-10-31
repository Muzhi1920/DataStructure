def hailStone(n):
    while n > 1:
        if n % 2 == 0:
            result.append(n)
            n = n / 2
            hailStone(n)
        else:
            result.append(n)
            n = 3 * n + 1
            hailStone(n)
        # 当包含1时结束
        if result.__contains__(1):
            break

    # 最后添加元素1
    if not result.__contains__(1):
        result.append(1)


def calcLength(n):
    length = 1
    while (n > 1):
        if (n % 2 == 1):
            n = 3 * n + 1
        else:
            n = n / 2
        length += 1
    return length


result = []
hailStone(42)

print(result)

length = calcLength(42)
print(length)
