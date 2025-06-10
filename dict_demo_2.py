from collections import defaultdict

if __name__ == '__main__':
    # int类型的默认值为0
    my_dict = defaultdict(int)
    my_dict['a'] += 1
    my_dict['b'] = my_dict['a'] + 1
    my_dict['c'] = my_dict['b'] + 1

    # 输出: defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})
    print(my_dict)

    # 输出: 0
    print(my_dict['d'])
