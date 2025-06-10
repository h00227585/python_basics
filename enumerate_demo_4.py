from typing import List


def get_index_value(data: List[str], start_index=0) -> List[tuple]:
    return [(index, value) for index, value in enumerate(data, start=start_index)]


if __name__ == "__main__":
    my_list = ['one', 'two', 'three']
    index_value_list = get_index_value(my_list, start_index=1)
    # 输出：[(1, 'one'), (2, 'two'), (3, 'three')]
    print(index_value_list)
