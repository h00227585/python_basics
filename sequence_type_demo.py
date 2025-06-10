if __name__ == '__main__':
    # 字节数组: 可以修改元素
    v = bytearray(b'hello')
    v[0] = ord('H')  # 将字符转换为对应的ASCII码或Unicode数值
    print(v)  # 输出: bytearray(b'Hello')

    # 字节: 不能修改元素
    v = b'hello'
    print(v)

    # 范围: 不能修改元素
    v = range(6, 9)
    print(v)     # 输出: range(6, 9)
    print(v[0])  # 输出: 6


    # 容器序列
    my_list = [2, 'two', (2.0, 6.0)]
    print(my_list)  # 输出: [2, 'two', (2.0, 6.0)]
