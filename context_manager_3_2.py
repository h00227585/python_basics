from contextlib import contextmanager


class ResourceManager:
    def __init__(self):
        print('open resources')

    def do_something(self):
        print('use resources')

    def close(self):
        print('close resources')


@contextmanager
def my_context_manager() -> ResourceManager:
    print("Entering my_context_manager")
    resource_manager = ResourceManager()
    try:
        # yield 之前的代码相当于 __enter__()，yield 之后的代码相当于 __exit__()
        yield resource_manager  # 这里可以返回值，相当于 `__enter__` 的返回值
        print("Exiting my_context_manager")
        resource_manager.close()
    except Exception as e:
        print(f"Exception occurred: {e}")


with my_context_manager() as cm:
    cm.do_something()

# 输出结果如下:
# Entering my_context_manager
# open resources
# use resources
# Exiting my_context_manager
# close resources
