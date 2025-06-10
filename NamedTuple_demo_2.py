from typing import NamedTuple


class Student(NamedTuple):
    name: str   # 学生姓名
    age: int    # 学生年龄
    score: int  # 学生成绩

if __name__ == '__main__':
    student = Student('张三', 16, 99)
    print(student)       # 输出: Student(name='张三', age=16, score=99)
    print(student.name)  # 输出: 张三
    print(student.age)   # 输出: 16
    print(student.score) # 输出: 99