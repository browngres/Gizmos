import pandas as pd

hang = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lie = [1, 2, 3, 4, 5, 6, 7, 8, 9]
blank = pd.DataFrame(index=hang, columns=lie, dtype=int)
puzzle = blank
puzzle[1] = [0, 0, 1, 0, 0, 8, 9, 0, 3]
puzzle[2] = [0, 3, 0, 9, 0, 1, 4, 0, 0]
puzzle[3] = [0, 9, 0, 0, 7, 3, 5, 0, 1]
puzzle[4] = [6, 7, 3, 2, 9, 5, 1, 4, 8]
puzzle[5] = [0, 1, 0, 3, 8, 6, 7, 0, 0]
puzzle[6] = [9, 8, 2, 7, 1, 4, 6, 3, 5]
puzzle[7] = [0, 0, 9, 8, 0, 7, 3, 1, 0]
puzzle[8] = [1, 0, 7, 0, 3, 2, 8, 0, 0]
puzzle[9] = [3, 0, 0, 1, 6, 9, 2, 5, 7]
puzzle = puzzle.T
ori_puzzle = puzzle
'''
puzzle[1] = [3, 4, 5, 0, 0, 2, 6, 7, 8]
puzzle[2] = [6, 7, 8, 0, 0, 5, 9, 1, 2]
puzzle[3] = [9, 1, 2, 6, 7, 8, 3, 0, 0]
puzzle[4] = [0, 2, 3, 0, 0, 9, 0, 0, 0]
puzzle[5] = [0, 0, 6, 0, 2, 0, 0, 0, 0]
puzzle[6] = [0, 0, 9, 0, 0, 0, 0, 2, 3]
puzzle[7] = [2, 0, 4, 0, 0, 0, 0, 0, 7]
puzzle[8] = [5, 0, 7, 2, 0, 0, 8, 0, 0]
puzzle[9] = [8, 0, 1, 0, 0, 7, 2, 0, 0]
'''
