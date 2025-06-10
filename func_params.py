def show_info(name: str, age: int, score: int):
    print(f'name:{name}, age:{age}, score:{score}')


# age的默认值为18, score的默认值为0
def show_info_with_default(name: str, age: int = 18, score: int = 0):
    print(f'name:{name}, age:{age}, score:{score}')


def func(*args, **kwargs):
    print(f'可变位置参数:{args}, 可变关键字参数:{kwargs}')


if __name__ == '__main__':
    # 1

    # 输出: name:张三, age:18, score:100
    show_info('张三', 18, 100)

    # 2

    # 输出: name:张三, age:18, score:100
    show_info(score=100, age=18, name='张三')

    # 3

    # 以下几种用法是等价的，都是输出: name:张三, age:18, score:100
    show_info('张三', age=18, score=100)
    show_info('张三', score=100, age=18)
    show_info('张三', 18, score=100)
    show_info('张三', 18, 100)

    # 以下用法是错误的
    # show_info(age=18, score=100, '张三')
    # show_info('张三', name='张三')

    # 4

    # 输出: name:张三, age:18, score:0
    show_info_with_default('张三')

    # 5

    # 输出: 可变位置参数:('张三',), 可变关键字参数:{'age': 18, 'score': 100}
    func('张三', age=18, score=100)

    # 输出: 可变位置参数:('张三', 18), 可变关键字参数:{'score': 100}
    func('张三', 18, score=100)
