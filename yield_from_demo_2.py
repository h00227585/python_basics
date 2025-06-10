if __name__ == '__main__':
    def generator1():
        yield 1
        yield 2
        yield 3

    def generator2():
        yield from generator1()
        yield 4
        yield 5

    # 输出:
    # 1
    # 2
    # 3
    # 4
    # 5
    for value in generator2():
        print(value)
