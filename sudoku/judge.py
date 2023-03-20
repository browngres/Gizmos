from input import puzzle
import itertools
import numpy as np

'''
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。
i=hang j=lie
puzzle[lie][hang]
'''


def which_house(i, j):  # 哪一宫
    if i < 4:
        for m in itertools.product([1, 2, 3], repeat=2):
            if m == (i, j):
                return 1
        for m in itertools.product([1, 2, 3], [4, 5, 6]):
            if (i, j) == m:
                return 2
        for m in itertools.product([1, 2, 3], [7, 8, 9]):
            if (i, j) == m:
                return 3
    if i > 6:
        for m in itertools.product([7, 8, 9], [1, 2, 3]):
            if (i, j) == m:
                return 7
        for m in itertools.product([7, 8, 9], [4, 5, 6]):
            if (i, j) == m:
                return 8
        for m in itertools.product([7, 8, 9], repeat=2):
            if (i, j) == m:
                return 9
    for m in itertools.product([4, 5, 6], [1, 2, 3]):
        if (i, j) == m:
            return 4
    for m in itertools.product([4, 5, 6], repeat=2):
        if (i, j) == m:
            return 5
    for m in itertools.product([4, 5, 6], [7, 8, 9]):
        if (i, j) == m:
            return 6


def this_house(house):
    all_num = []
    if house == 1:
        for (i, j) in itertools.product([1, 2, 3], repeat=2):
            all_num.append(puzzle[j][i])
    if house == 2:
        for (i, j) in itertools.product([1, 2, 3], [4, 5, 6]):
            all_num.append(puzzle[j][i])
    if house == 3:
        for (i, j) in itertools.product([1, 2, 3], [7, 8, 9]):
            all_num.append(puzzle[j][i])
    if house == 4:
        for (i, j) in itertools.product([4, 5, 6], [1, 2, 3]):
            all_num.append(puzzle[j][i])
    if house == 5:
        for (i, j) in itertools.product([4, 5, 6], repeat=2):
            all_num.append(puzzle[j][i])
    if house == 6:
        for (i, j) in itertools.product([4, 5, 6], [7, 8, 9]):
            all_num.append(puzzle[j][i])
    if house == 7:
        for (i, j) in itertools.product([7, 8, 9], [1, 2, 3]):
            all_num.append(puzzle[j][i])
    if house == 8:
        for (i, j) in itertools.product([7, 8, 9], [4, 5, 6]):
            all_num.append(puzzle[j][i])
    if house == 9:
        for (i, j) in itertools.product([7, 8, 9], repeat=2):
            all_num.append(puzzle[j][i])
    return all_num


def this_hang_6(i, j):
    house = which_house(i, j)
    hang_num = []
    if house == 1 or house == 6 or house == 7:
        for j in [4, 5, 6, 7, 8, 9]:
            hang_num.append(puzzle[j][i])
    if house == 2 or house == 5 or house == 8:
        for j in [1, 2, 3, 7, 8, 9]:
            hang_num.append(puzzle[j][i])
    if house == 3 or house == 6 or house == 9:
        for j in [1, 2, 3, 4, 5, 6]:
            hang_num.append(puzzle[j][i])
    return hang_num


def this_lie_6(i, j):
    house = which_house(i, j)
    lie_num = []
    if house == 1 or house == 2 or house == 3:
        for i in [4, 5, 6, 7, 8, 9]:
            lie_num.append(puzzle[j][i])
    if house == 4 or house == 5 or house == 6:
        for i in [1, 2, 3, 7, 8, 9]:
            lie_num.append(puzzle[j][i])
    if house == 7 or house == 8 or house == 9:
        for i in [1, 2, 3, 4, 5, 6]:
            lie_num.append(puzzle[j][i])
    return lie_num


def order_in_house(i, j):  # 判断位于宫中第几个
    q = 3 if i % 3 == 0 else i % 3
    p = 3 if j % 3 == 0 else j % 3
    return (q - 1) * 3 + p


def this_20_ge(i, j):  # 给出冲突域的20个(除去自己)
    ge20 = []
    for k in this_house(which_house(i, j)):
        ge20.append(k)
    ge20.pop(order_in_house(i, j) - 1)
    for k in this_hang_6(i, j):
        ge20.append(k)
    for k in this_lie_6(i, j):
        ge20.append(k)
    return ge20


def house_is_ok(n):  # 宫有无冲突
    house = np.array(this_house(n))
    for m in house:
        if m == 0:
            print("第{}宫不完整".format(n))
            return
    if house.sum() != 45:
        print("第{}宫有冲突/问题".format(n))
    else:
        print("第{}宫完整".format(n))


def hang_is_ok(n):  # 行有无冲突
    hang = np.array(puzzle.loc[n])
    for m in hang:
        if m == 0:
            print("第{}行不完整".format(n))
            return
    if hang.sum() != 45:
        print("第{}行有冲突/问题".format(n))
    else:
        print("第{}行完整".format(n))


def lie_is_ok(n):  # 行有无冲突
    lie = np.array(puzzle[n])
    for m in lie:
        if m == 0:
            print("第{}列不完整".format(n))
            return
    if lie.sum() != 45:
        print("第{}列有冲突/问题".format(n))
    else:
        print("第{}列完整".format(n))


def check_all():  # 检查所有
    for i in np.arange(1, 10):
        house_is_ok(i)
        hang_is_ok(i)
        lie_is_ok(i)


def get_next(i, j):  # 找到下一个空位
    for k in range(j + 1, 10):
        if puzzle[k][i] == 0:
            return i, k
    for j in range(i + 1, 10):
        for l in range(1, 10):
            if puzzle[l][j] == 0:
                return j, l
    return -1, -1


'''
print(puzzle[9][9])
print(which_house(9, 9))
print(this_house(which_house(9,9)))
print(this_hang_6(9,9))
print(this_lie_6(9,9))
print(order_in_house(8, 9))
print(this_20_ge(1, 1))
house_is_ok(1)
hang_is_ok(1)
lie_is_ok(3)
check_all()
print(get_next(9,8))
'''
