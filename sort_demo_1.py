from dataclasses import dataclass


@dataclass
class Student:
    """
    自定义学生类，包括姓名和年龄两个属性
    """
    name: str
    age: int


if __name__ == '__main__':
    # 1: list sorted()
    my_list = [8, 6, 4, 2, 5, 3, 7, 1]

    # 升序排列，输出: [1, 2, 3, 4, 5, 6, 7, 8]
    print(sorted(my_list))

    # 降序排列，输出: [8, 7, 6, 5, 4, 3, 2, 1]
    print(sorted(my_list, reverse=True))

    # 输出: [8, 6, 4, 2, 5, 3, 7, 1]，原来的列表没有改变内容
    print(my_list)

    # 2: list sort()
    my_list.sort()

    # 输出: [1, 2, 3, 4, 5, 6, 7, 8]，原来的列表已经改变内容
    print(my_list)

    # 3: str sorted()
    fruits = ['orange', 'banana', 'apple', 'grape']

    # 升序排列，依据字符串的自然顺序
    # 输出: ['apple', 'banana', 'grape', 'orange']
    print(sorted(fruits))

    # 升序排列，依据字符串的长度
    # ['apple', 'grape', 'orange', 'banana']
    print(sorted(fruits, key=len))

    # 4: dict sorted()
    my_dict = {'a': 300, 'b': 200, 'c': 100}

    # 根据字典的key排序，输出：[('a', 300), ('b', 200), ('c', 100)]
    print(sorted(my_dict.items(), key=lambda x: x[0]))

    # 根据字典的value排序，输出: [('c', 100), ('b', 200), ('a', 300)]
    print(sorted(my_dict.items(), key=lambda x: x[1]))

    # 5: object sorted
    # 创建三个学生对象
    s1 = Student('Tom', 19)
    s2 = Student('Bob', 19)
    s3 = Student('Jack', 20)
    students = [s1, s2, s3]

    # 根据姓名排序
    # 输出: [Student(name='Bob', age=19), Student(name='Jack', age=20), Student(name='Tom', age=19)]
    print(sorted(students, key=lambda x: x.name))

    # 根据年龄排序
    # 输出: [Student(name='Tom', age=19), Student(name='Bob', age=19), Student(name='Jack', age=20)]
    print(sorted(students, key=lambda x: x.age))

    # 多级排序，先根据年龄排序，再根据姓名排序
    # 输出: [Student(name='Bob', age=19), Student(name='Tom', age=19), Student(name='Jack', age=20)]
    print(sorted(students, key=lambda x: (x.age, x.name)))
