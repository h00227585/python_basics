if __name__ == '__main__':
    # 学生的姓名列表
    names = ['张三', '李四', '王五']
    # 学生的年龄列表
    ages = [18, 19, 20]
    # 学生的成绩列表
    scores = [98, 99, 100]
    # 将每个学生的姓名、年龄、成绩组合在一起
    zipped = zip(names, ages, scores)
    # 将迭代器zipped通过list()转换为可迭代对象，然后打印
    # 输出: [('张三', 18, 98), ('李四', 19, 99), ('王五', 20, 100)]
    print(list(zipped))
