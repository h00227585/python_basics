def access_local():
    v = 100  # 局部变量
    print(v)


def outer_func():
    def inner_func():
        print(v)  # 内部函数可以访问外部函数的变量

    v = 100
    inner_func()


v = 100  # 全局变量


def access_global():
    print(v)


x = 200


def access_local_x():
    x = 300
    print(x)


if __name__ == '__main__':
    # 1：局部作用域

    # 输出: 100
    access_local()

    # 以下语句会报错，因为v是access_local()的内部变量，外部不可见
    # print(v)

    # 2：嵌套作用域

    # 输出: 100
    outer_func()

    # 3：全局作用域

    # 输出: 100
    access_global()

    # 4: 内置作用域

    # 输出: __main__
    print(__name__)

    # 5: 查找变量的顺序

    # 输出: 300
    access_local_x()

    # 6: 函数内修改全局变量
    y = 1000


    def modify_global():
        global y  # 声明此处使用的变量 y 是全局变量
        y = 2000


    print(y)  # 输出: 1000
    modify_global()
    print(y)  # 输出: 2000

    # 7: 内部函数中修改外部函数的变量


    def outer_function():
        v = 100  # 外部函数的变量

        def inner_function():
            nonlocal v  # 声明此处使用的 v 是外部函数的变量
            v = 200  # 修改外部函数的变量

        print(v)  # 输出: 100
        inner_function()
        print(v)  # 输出: 200


    outer_function()
