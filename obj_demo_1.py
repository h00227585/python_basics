class Example:  # 同时定义__str__()和__repr__(), 打印对象时调用__str__()
    def __str__(self) -> str:
        return "This is __str__"

    def __repr__(self) -> str:
        return "This is __repr__"


if __name__ == '__main__':
    obj = Example()
    print(obj)  # 输出 This is __str__
