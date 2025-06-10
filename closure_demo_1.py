# def f1():
#     def f2():
#         pass
#     f2()

def f1(x1):
    x2 = 2

    def f2(x3, x4):
        # 使用了外部函数的参数 x1 和变量 x2
        return x1 + x2 + x3 + x4

    return f2


total = 0
count = 0

def func(value):
    global total
    global count
    total += value
    count += 1
    return total, total / count


if __name__ == '__main__':
    f = f1(1)
    # 输出: 10, 即 1 + 2 + 3 + 4
    print(f(3, 4))
    # 输出: 73, 即 1 + 2 + 30 + 40
    print(f(30, 40))

    print(func(1))  # 输出: (1, 1.0)
    print(func(2))  # 输出: (3, 1.5)
    print(func(3))  # 输出: (6, 2.0)
