if __name__ == '__main__':
    # 1
    my_dict = {'name': '张三', 'age': 18, 'score': 100}
    print(my_dict['name'])  # 输出: 张三
    # 访问不存在的key，会报错KeyError: 'city'
    # print(my_dict['city'])

    # 2
    my_dict = {'name': '张三', 'age': 18, 'score': 100}
    city = my_dict.get('city')
    print(city)  # 输出: None
    city = my_dict.get('city', 'unknown')
    print(city)  # 输出: unknown

    # 3
    my_dict = {'name': '张三', 'age': 18, 'score': 100}
    key = 'city'
    if key in my_dict:
        value = my_dict[key]
    else:
        print(f'{key} is not in dict')  # 会执行这一句
