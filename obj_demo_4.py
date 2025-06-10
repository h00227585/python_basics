class SimpleEquation:
    """
    最佳实践：同时定义__str__()和__repr__()

    __str__(): 用于返回用户友好的字符串表示，适合打印或显示给最终用户。
    __repr__(): 用于返回开发者友好的字符串表示，适合调试和开发。
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return 'x: {} y: {}'.format(self.x, self.y)

    def __repr__(self) -> str:
        return 'SimpleEquation(x={}, y={})'.format(self.x, self.y)


if __name__ == '__main__':
    obj = SimpleEquation(16, 16)
    print(obj)        # 打印结果: x: 16 y: 16
    print(repr(obj))  # 打印结果: SimpleEquation(x=16, y=16)
