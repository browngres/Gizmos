def find_differences(x, y):
    # 将数组转换为集合
    set_x = set(x)
    set_y = set(y)

    # 找出 x 有而 y 没有的元素
    only_in_x = set_x - set_y
    # 找出 y 有而 x 没有的元素
    only_in_y = set_y - set_x

    # 输出结果
    print(f"贪婪 有 {', '.join(map(str, sorted(only_in_x)))};")
    print(f"答案 有 {', '.join(map(str, sorted(only_in_y)))}")


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 19, 20, 25, 26, 27, 29, 30, 32, 34,
     35, 38, 40, 41, 43, 46, 47, 48, 49, 52, 56, 57]

y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 17, 19, 20, 25, 26, 27, 29, 30, 32, 34, 35,
     38, 40, 41, 43, 46, 48, 49, 50, 52, 56, 57]

find_differences(x,y)