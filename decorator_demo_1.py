def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # 调用原函数之前执行的代码，可以是其他代码
        print(f'enter {original_function.__name__}')
        # 调用原函数
        result = original_function(*args, **kwargs)
        # 调用原函数之后执行的代码，可以是其他代码
        print(f'exit {original_function.__name__}')
        return result
    return wrapper_function

@decorator_function
def some_function():
    print('execute some_function')

# 输出:
# enter some_function
# execute some_function
# exit some_function
some_function()

print(some_function.__name__)
