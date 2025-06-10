if __name__ == '__main__':
    my_dict = {}
    my_dict['张三'] = {'性别': '男', '年龄': 19}
    my_dict[1] = 'one'
    # 输出:
    # {'张三': {'性别': '男', '年龄': 19}, 1: 'one'}
    print(my_dict)

    # 删除键值对
    del my_dict['张三']
    # 输出: {1: 'one'}
    print(my_dict)

    # 访问键值对
    # 输出: key: 1, value: one
    for key, value in my_dict.items():
        print(f'key: {key}, value: {value}')

    # Python 3.7 及以上的版本按照插入顺序进行存储
    my_dict['c'] = 'c'
    my_dict['a'] = 'a'
    my_dict['b'] = 'b'
    print(my_dict)
