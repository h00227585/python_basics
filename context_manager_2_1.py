import threading
import time

num = 2
lock = threading.Lock()


def add_one():
    global num

    # 对num进行六次+1操作
    for _ in range(1, 7):
        lock.acquire()
        try:
            num += 1
            print(f"after add_one() num is {num}")
        finally:
            lock.release()
        time.sleep(0.3)  # 休眠0.2秒


def sub_one():
    global num

    # 对num进行六次-1操作
    for _ in range(1, 7):
        lock.acquire()
        try:
            num -= 1
            print(f"after sub_one() num is {num}")
        finally:
            lock.release()
        time.sleep(0.3)  # 休眠0.2秒


# 创建线程
t_add_one = threading.Thread(target=add_one)
t_sub_one = threading.Thread(target=sub_one)

# 启动线程
t_add_one.start()
t_sub_one.start()

# 等待线程完成
t_add_one.join()
t_sub_one.join()

# 输出结果示例
# after add_one() num is 3
# after sub_one() num is 2
# after add_one() num is 3
# after sub_one() num is 2
# after add_one() num is 3
# after sub_one() num is 2
# after sub_one() num is 1
# after add_one() num is 2
# after sub_one() num is 1
# after add_one() num is 2
# after sub_one() num is 1
# after add_one() num is 2
