from collections import ChainMap

if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 20, 'c': 30}
    chain_map = ChainMap(dict1, dict2)

    # 输出: 1 (来自dict1)
    print(chain_map['a'])

    # 输出: 2 (来自dict1, 因为dict1中的'b'在dict2中的'b'前面)
    print(chain_map['b'])

    # 输出: 30 (来自dict2)
    print(chain_map['c'])
