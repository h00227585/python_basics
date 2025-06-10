class Example:  # 没有定义__str__()，定义__repr__(), 打印对象时调用__repr__()
    def __repr__(self) -> str:
        return "This is __repr__"


if __name__ == '__main__':
    obj = Example()
    print(obj)  # 输出 This is __repr__
