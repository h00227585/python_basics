if __name__ == "__main__":
    my_list = ['one', 'two', 'three']
    for i, elem in enumerate(my_list, start=1):
        # 输出如下:
        # 1 one
        # 2 two
        # 3 three
        print(i, elem)
