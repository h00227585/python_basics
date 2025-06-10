import numpy as np

if __name__ == '__main__':
    # 1. 一维数组的切片，和Python序列的切片方法类似

    # 生成一个一维数组
    arr1d = np.array(range(8))
    print(arr1d)  # 输出: [0 1 2 3 4 5 6 7]

    # 从倒数第2个元素开始切片
    print(arr1d[-2::])  # 输出: [6 7]

    # 2. 二维数组的切片

    # 生成一个二维数组
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # 输出:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    print(arr2d)

    # 选择前两行和前两列的元素
    sub_arr2d = arr2d[:2, :2]
    # 输出:
    # [[1 2]
    #  [4 5]]
    print(sub_arr2d)

    # 修改numpy数组切片的内容，会影响原来的数组
    sub_arr2d[:] = 0
    # 输出:
    # [[0 0 3]
    #  [0 0 6]
    #  [7 8 9]]
    print(arr2d)
