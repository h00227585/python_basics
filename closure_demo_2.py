def outer_func():
    total = 0
    count = 0

    def inner_func(value):
        nonlocal total, count
        total += value
        count += 1
        return total, total / count

    return inner_func


if __name__ == '__main__':
    closure = outer_func()
    print(closure(1))  # 输出: (1, 1.0)
    print(closure(2))  # 输出: (3, 1.5)
    print(closure(3))  # 输出: (6, 2.0)
