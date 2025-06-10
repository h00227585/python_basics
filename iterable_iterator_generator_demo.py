if __name__ == '__main__':
    # 1. 可迭代对象

    # 可以通过 for 循环访问
    my_list = list(range(6))
    for elem in my_list:
        print(elem)

    # 以下代码会报错，因为 my_list 不是迭代器，不能通过 next() 访问
    # print(next(my_list))

    # 可以重复遍历
    my_list = list(range(6))
    for elem in my_list:
        print(elem)  # 会执行这一句
    for elem in my_list:
        print(elem)  # 会执行这一句

    # 打印结果为所有元素
    my_list = list(range(6))
    print(my_list)  # 输出: [0, 1, 2, 3, 4, 5]

    # 2. 迭代器

    # 可以通过 for 循环和 next() 访问
    my_list = ['one', 'two', 'three']
    my_iterator = enumerate(my_list, start=1)
    # 输出: (1, 'one')
    print(next(my_iterator))
    # 输出:
    # (2, 'two')
    # (3, 'three')
    for elem in my_iterator:
        print(elem)

    # 只能单方向遍历，并且只能遍历一次
    my_list = ['one', 'two', 'three']
    my_iterator = enumerate(my_list, start=1)
    for elem in my_iterator:
        print(elem)  # 会执行这一句
    for elem in my_iterator:
        print(elem)  # 不会执行这一句

    my_list = ['one', 'two', 'three']
    my_iterator = enumerate(my_list, start=1)
    print(max(my_iterator))  # 输出: (3, 'three')
    for elem in my_iterator:
        print(elem)  # 不会执行这一句，因为 max() 已经单向遍历过 my_iterator 一次

    # 打印结果为对象的地址
    my_list = ['one', 'two', 'three']
    my_iterator = enumerate(my_list, start=1)

    # 输出类似 <enumerate object at 0x00000299B14B0680>
    print(my_iterator)

    # 3. 自定义可迭代对象和迭代器

    class MyIterator:
        """
        自定义迭代器
        """
        def __init__(self, begin, end):
            self.begin = begin
            self.end = end
            self.index = begin

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < self.end:
                result = self.index
                self.index += 1
                return result
            else:
                raise StopIteration


    class MyIterable:
        """
        自定义可迭代对象
        """
        def __init__(self, begin, end):
            self.begin = begin
            self.end = end

        def __iter__(self):
            # 返回一个迭代器对象
            return MyIterator(self.begin, self.end)

        def __repr__(self):
            return str(list(self))

    my_iterator = MyIterator(1, 3)

    # 输出:
    # 1
    # 2
    for elem in my_iterator:
        print(elem)

    my_iterable = MyIterable(1, 3)
    # 输出:
    # 1
    # 2
    for elem in my_iterable:
        print(elem)

    # 输出: [1, 2]
    print(my_iterable)

    # 4. 生成器

    # 生成 [begin, end)范围的整数
    def generate(begin, end):
        for i in range(begin, end):
            yield i
    my_generator = generate(6, 9)

    # 输出: 6
    print(next(my_generator))

    # 输出:
    # 7
    # 8
    for elem in my_generator:
        print(elem)

    # 输出: <class 'generator'>
    print(type(my_generator))
