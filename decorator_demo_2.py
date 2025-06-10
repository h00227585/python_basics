class MyDecorator:
    def __init__(self, original_function):
        self.func = original_function

    def __call__(self, *args, **kwargs):
        # 调用原函数之前执行的代码，可以是其他代码
        print(f'enter {self.func.__name__}')
        # 调用原函数
        result = self.func(*args, **kwargs)
        # 调用原函数之后执行的代码，可以是其他代码
        print(f'exit {self.func.__name__}')
        return result

@MyDecorator
def some_function():
    print('execute some_function')

# 输出:
# enter some_function
# execute some_function
# exit some_function
some_function()
