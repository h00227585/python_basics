def format_output_by_str_concat(name: str, age: int) -> str:
    """
    以特定的格式返回包含 name 和 age 的字符串

    通过传统的字符串拼接实现，写起来相对麻烦。
    """
    formatted_string = "Name: " + name + ", Age: " + str(age)
    return formatted_string


def format_output_by_c_style(name: str, age: int) -> str:
    """
    以特定的格式返回包含 name 和 age 的字符串

    采用类似C语言风格的字符串格式化方法。
    """
    formatted_string = "Name: %s, Age: %d" % (name, age)
    return formatted_string


def format_output_by_str_format(name: str, age: int) -> str:
    """
    以特定的格式返回包含 name 和 age 的字符串

    使用 str.format() 进行字符串格式化。
    """
    formatted_string = "Name: {}, Age: {}".format(name, age)
    return formatted_string


def format_output_by_f_string(name: str, age: int) -> str:
    """
    以特定的格式返回包含 name 和 age 的字符串

    使用 f-string 进行字符串格式化。
    """
    formatted_string = f"Name: {name}, Age: {age}"
    return formatted_string


if __name__ == '__main__':
    name = "张三"
    age = 22

    print(format_output_by_str_concat(name, age))  # 输出: Name: 张三, Age: 22
    print(format_output_by_c_style(name, age))  # 输出: Name: 张三, Age: 22
    print(format_output_by_str_format(name, age))  # 输出: Name: 张三, Age: 22
    print(format_output_by_f_string(name, age))  # 输出: Name: 张三, Age: 22
