from itertools import islice

if __name__ == '__main__':
    my_list = list(range(8))
    print(my_list)  # 输出: [0, 1, 2, 3, 4, 5, 6, 7]

    my_sub_list = list(islice(my_list, 0, 2))
    print(my_sub_list)  # 输出: [0, 1]

    my_sub_list = list(islice(my_list, 1))  # stop为1
    print(my_sub_list)  # 输出: [0]

    my_sub_list = list(islice(my_list, 1, None))  # start为1
    print(my_sub_list)  # 输出: [1, 2, 3, 4, 5, 6, 7]
