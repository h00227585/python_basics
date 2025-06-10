if __name__ == '__main__':
    v = False
    if not v:
        print("v is False")  # 会执行这一句

    v = None
    if not v:
        print("v is None")  # 会执行这一句

    v = ""
    if not v:
        print("str is empty")  # 会执行这一句

    v = []
    if not v:
        print("list is empty")  # 会执行这一句

    v = ()
    if not v:
        print("tuple is empty")  # 会执行这一句

    v = {}
    if not v:
        print("dict is empty")  # 会执行这一句

    v = 0
    if not v:
        print("v is 0")  # 会执行这一句

    my_str = None
    if my_str is None or my_str == "":
        print('my_str is None or empty')  # 会执行这一句
    my_str = ""
    if my_str is None or my_str == "":
        print('my_str is None or empty')  # 会执行这一句

    my_str = None
    if not my_str:
        print('my_str is None or empty')  # 会执行这一句
    my_str = ""
    if not my_str:
        print('my_str is None or empty')  # 会执行这一句

