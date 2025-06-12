
# 1. 访问单个元素，如果索引越界会提示异常。

# 一共6个元素，有效索引的范围是0到5
my_list = list(range(1, 7))

# 输出 [1, 2, 3, 4, 5, 6]
print(my_list)

# 抛出异常: IndexError: list index out of range
# print(my_list[8])


# 2. 通过切片访问子集，如果索引越界会返回切片范围和list元素范围的交集。

# 一共6个元素，有效索引的范围是0到5
my_list = list(range(1, 7))

# 输出 [1, 2, 3, 4, 5, 6]
print(my_list)

# 输出 [3, 4, 5, 6]
print(my_list[2:6])

# 输出 [3, 4, 5, 6], end索引已经越界
print(my_list[2:7])

# 输出 [], start索引和end索引都已经越界
print(my_list[6:12])
