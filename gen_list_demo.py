from typing import List

import numpy as np

from util.common_util import measure_time_with_log


def gen_list_by_concat(n: int) -> List[int]:
    """
    通过列表拼接生成从 0 到 n-1 的整数列表。
    注意：使用 `+=` 拼接列表效率较低，不推荐用于大规模数据。
    """
    elem_list = []
    for i in range(n):
        elem_list += [i]
    return elem_list


def gen_list_by_append(n: int) -> List[int]:
    """
    通过 `append` 方法生成从 0 到 n-1 的整数列表。
    比列表拼接更高效，适合小规模数据。
    """
    elem_list = []
    for i in range(n):
        elem_list.append(i)
    return elem_list


def gen_list_by_comprehension(n: int) -> List[int]:
    """
    通过列表推导式生成从 0 到 n-1 的整数列表。
    代码简洁且效率高，推荐使用。
    """
    return [i for i in range(n)]


def gen_list_by_list_range(n: int) -> List[int]:
    """
    通过 `range` 和 `list` 直接生成从 0 到 n-1 的整数列表。
    效率最高，代码最简洁，强烈推荐使用。
    """
    return list(range(n))


def gen_array_by_numpy_arange(n: int) -> np.ndarray:
    """
    通过 NumPy 的 `arange` 函数生成从 0 到 n-1 的数组。
    适用于需要与 NumPy 集成的场景。
    """
    return np.arange(n)


if __name__ == '__main__':
    measure_time_with_log(gen_list_by_concat, 120000)
    measure_time_with_log(gen_list_by_append, 120000)
    measure_time_with_log(gen_list_by_comprehension, 120000)
    measure_time_with_log(gen_list_by_list_range, 120000)
    measure_time_with_log(gen_array_by_numpy_arange, 120000)
