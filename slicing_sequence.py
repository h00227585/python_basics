if __name__ == '__main__':
    # 生成一个list
    my_list = list(range(0, 8))
    print(my_list)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7]

    # 从前向后获取子序列，间隔2个获取元素
    print(my_list[0::2])  # 输出: [0, 2, 4, 6]

    # 从后向前获取子序列，间隔3个获取元素
    print(my_list[::-3])  # 输出: [7, 4, 1]

    # 省略start, stop和step，获取整个序列
    print(my_list[:])  # 输出: [0, 1, 2, 3, 4, 5, 6, 7]
    print(my_list[::])  # 输出: [0, 1, 2, 3, 4, 5, 6, 7]

    # 修改序列切片的内容，不会影响原来的序列
    my_sub_list = my_list[:2]
    print(my_sub_list)  # 输出: [0, 1]
    for i in range(len(my_sub_list)):  # 修改 my_sub_list
        my_sub_list[i] = -1
    print(my_sub_list)  # 输出: [-1, -1]
    print(my_list)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7], 即 my_sub_list 的修改不影响 my_list
