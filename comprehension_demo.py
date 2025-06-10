if __name__ == '__main__':
    # 1. 列表推导式

    # 生成包含偶数的列表
    evens = [i for i in range(10) if i % 2 == 0]
    print(evens)  # 输出: [0, 2, 4, 6, 8]

    # 生成包含奇数的列表
    odds = [i for i in range(10) if i % 2 == 1]
    print(odds)  # 输出: [1, 3, 5, 7, 9]

    # 2. 集合推导式

    # 生成包含偶数的集合
    evens = {i for i in range(10) if i % 2 == 0}
    print(evens)  # 输出: {0, 2, 4, 6, 8}

    # 生成包含奇数的集合
    odds = {i for i in range(10) if i % 2 == 1}
    print(odds)  # 输出: {1, 3, 5, 7, 9}

    # 3. 字典推导式

    # 生成一个字典，值(value)为键(key)的平方
    my_dict = {i: i**2 for i in range(3)}
    print(my_dict)  # 输出: {0: 0, 1: 1, 2: 4}

    # 4. 生成器推导式

    # 生成一个包含偶数的生成器
    evens = (i for i in range(10) if i % 2 == 0)
    print(type(evens))  # 输出: <class 'generator'>
    print(next(evens))  # 输出: 0
    print(next(evens))  # 输出: 2

    # 5. 嵌套推导式

    # 生成一个二维列表
    matrix = [[i + j for j in range(3)] for i in range(2)]
    print(matrix)  # 输出: [[0, 1, 2], [1, 2, 3]]

    # 6. 推导式最多只应该写两个子表达式

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 直接阅读可能不好理解
    filtered_matrix = [[elem for elem in row if elem % 3 == 0] for row in matrix if sum(row) > 10]
    print(filtered_matrix)  # 输出: [[6], [9]]

    # 进行适当的拆分
    filtered_matrix = []
    for row in matrix:
        # 选择总和大于10的行
        if sum(row) > 10:
            # 保留行中能被3整除的元素
            filtered_matrix.append([elem for elem in row if elem % 3 == 0])
    print(filtered_matrix)  # 输出: [[6], [9]]

    # 7. 如果推导式中有重复计算，可以考虑使用赋值表达式

    my_list = list(range(1, 6))
    print(my_list)  # 输出: [1, 2, 3, 4, 5]

    # 使用赋值表达式之前，计算i的三次方执行了两次。
    # 输出: [27, 64, 125]
    print([i ** 3 for i in my_list if i ** 3 > 10])

    # 使用赋值表达式之后，计算i的三次方执行了一次。
    # 输出: [27, 64, 125]
    print([cube for i in my_list if (cube := i ** 3) > 10])
