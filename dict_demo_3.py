from collections import OrderedDict

if __name__ == '__main__':
    my_dict = OrderedDict()
    my_dict[3] = 'three'
    my_dict[2] = 'two'
    my_dict[1] = 'one'

    # 输出:
    # OrderedDict([(3, 'three'), (2, 'two'), (1, 'one')])
    print(my_dict)
