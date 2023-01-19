from judge import *

def could_be(i, j):
    cant_be = np.unique(this_20_ge(i, j))
    return np.setdiff1d(range(1, 10), cant_be)


'''
221121 1153 我发现用循环总是搞不定,因为这个could_num不是用for循环,没法在每次执行时继承
202211211304 成了
'''


def sudoku_solver(start_h, start_l):
    could_num = could_be(start_h, start_l)  # 列出可填
    if puzzle[start_l][start_h] == 0:  # 如果本格可填
        if could_num.any():  # 可填不空
            #     print(could_num)
            for z in could_num:
                puzzle[start_l][start_h] = z  # 填入第一个可填
                # print('({}，{})填入{}'.format(start_h,start_l,z))
                next_h, next_l = get_next(start_h, start_l)  # 找到下一个位置
                if next_h == -1:  # 没有下一个位置
                    print('OK')
                    return True
                else:
                    next_round = sudoku_solver(next_h, next_l)  # 进入下一轮
                if not next_round:  # 没有下一轮
                    puzzle[start_l][start_h] = 0
                # print('({}，{})填入{}'.format(start_h, start_l,0))
                else:
                    return True  # 调试半天原来是少了这句
        else:
            # print("no could")  # 没有可填
            return False


'''1st 版本
def sudoku_solver(start_h,start_l):
    could_num = could_be(start_h, start_l)  # 列出可填
    #if puzzle[start_l][start_h]==0: #如果本格可填
    if could_num.any():          # 可填不空
        print(could_num)
        puzzle[start_l][start_h] = could_num[0]   # 填入第一个可填
        next_h, next_l = get_next(start_h, start_l)   #找到下一位置
        if next_h==-1:                             #没有下一位置
            print('OK')
            return True
        else:
            next_round = sudoku_solver(next_h, next_l)  # 进入下一轮
            if not next_round:                         # 没有下一轮
                could_num = np.delete(could_num, 0)
                if could_num.any():
                    puzzle[start_l][start_h] = could_num[0]     # 再尝试填
                    next_round = sudoku_solver(next_h, next_l)  # 进入下一轮
                else:
                    return False
            else:
                return True

    else:
        print("no could")                          #没有可填
        return False
'''

sudoku_solver(1, 1)
print(puzzle)
check_all()
