from functools import lru_cache

from util.common_util import measure_time_with_log


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    pre, cur = 0, 1
    for _ in range(2, n + 1):
        # 先计算=右边的结果，并赋值给临时变量，再将临时变量赋值给=左边的变量
        pre, cur = cur, pre + cur
    return cur


def fibonacci_cache(n: int, cache={}) -> int:
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_cache(n - 1, cache) + fibonacci_cache(n - 2, cache)
    cache[n] = result
    return result


@lru_cache(maxsize=None)  # maxsize=None 表示不限制缓存大小
def fibonacci_lru_cache(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)


if __name__ == '__main__':
    measure_time_with_log(fibonacci_recursive, 32)
    measure_time_with_log(fibonacci_iterative, 32)
    measure_time_with_log(fibonacci_cache, 32)
    measure_time_with_log(fibonacci_lru_cache, 32)
