class Example:  # 没有定义__str__()和__repr__(), 打印对象时调用__repr__()
    pass


if __name__ == '__main__':
    obj = Example()
    # 输出类似 <__main__.Example object at 0x000001159B597AF0>，表示对象的类型和地址
    print(obj)
