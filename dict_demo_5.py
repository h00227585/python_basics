from collections import Counter

if __name__ == '__main__':
    my_list = [1, 1, 2, 2, 2, 3]
    my_counter = Counter(my_list)
    # 输出: 2 (1出现的次数为2)
    print(my_counter[1])
    # 输出: 3 (2出现的次数为3)
    print(my_counter[2])
    # 输出: 1 (3出现的次数为1)
    print(my_counter[3])

    my_str = 'hello world'
    my_counter = Counter(my_str)
    # 输出: 2 ('o'出现的次数为2)
    print(my_counter['o'])
