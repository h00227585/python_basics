class MyContextManager:
    def __enter__(self):
        print("Entering MyContextManager")
        print('open resources')
        return self  # 返回的对象可以通过as赋值

    def do_something(self):
        print('use resources')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting MyContextManager")
        print('close resources')
        if exc_type:
            print(f"Exception occurred: {exc_val}")
            return True  # 异常被抑制，不向外传播
        return False  # 异常正常传播（默认行为）


with MyContextManager() as cm:
    cm.do_something()


# 输出结果如下:
# Entering MyContextManager
# open resources
# use resources
# Exiting MyContextManager
# close resources
