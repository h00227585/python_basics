import time


def measure_time_with_log(func, *args, **kwargs):
    """
    测量函数执行时间并打印日志的通用函数。

    :param func: 要测量的函数
    :param args: 函数的位置参数
    :param kwargs: 函数的关键字参数
    :return: 函数的返回值
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("'{}' takes {:.2f} milliseconds".format(func.__name__, elapsed_time * 1000))
    return result
