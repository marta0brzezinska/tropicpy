"""


"""
from tropical.tropical_matrix import *

def value_difference(a, b):
    if b == tropical_0:
        return False
    elif a == tropical_0:
        return tropical_0
    else:
        return TropicalValue(a.value - b.value, a.is_int and b.is_int)


def matrix_difference(A,B):
    result = []
    tmp_isint = A.is_int and B.is_int
    for (row_a, row_b) in zip(A.values, B.values):
        tmp_row = []
        for (a, b) in zip(row_a, row_b):
            tmp_row.append(value_difference(a,b))
        result.append(tmp_row)

    return TropicalMatrix(result, tmp_isint)


def double_matrix_sum(A,B):
    result = []
    tmp_isint = A.is_int and B.is_int
    for (row_a, row_b) in zip(A.values, B.values):
        tmp_row = []
        for (a, b) in zip(row_a, row_b):
            tmp_row.append(a * b)
        result.append(tmp_row)

    return TropicalMatrix(result, tmp_isint)

def matrix_sum(matrix_table):
    R = matrix_table[0]
    matrix_table.pop()
    for M in matrix_table:
        R = double_matrix_sum(R,M)
    return R

def is_matrix_difference_constant(A, B):
    frst = True
    for (row_a, row_b) in zip(A.values, B.values):
        for (a, b) in zip(row_a, row_b):
            if frst:
                frst = False
                c = value_difference(a, b)
                if not c:
                    continue
            else:
                new_c = value_difference(a, b)
                if new_c:
                    if new_c != c:
                        return False
                    else:
                        c = new_c
    return c


def min_of_matrix_difference(A,B):
    result = {}
    t = tropical_0
    P = []
    for (row_a, row_b, i) in zip(A.values, B.values, range(A.rows)):
        for (a, b, j) in zip(row_a, row_b, range(A.columns)):
            c = value_difference(a, b)
            if t == c:
                P. append([i,j])
            elif t + c == c:
                t += c
                P = []
                P.append([i, j])
    result[t] = P
    return result

def is_zero_modulo(A,B):
    for (row_a, row_b) in zip(A.values, B.values):
        for (a, b) in zip(row_a, row_b):
            if a.value % b.value != 0:
                return False
    return True

def check_cover(main_set, dict_of_sets, cover):
    if dict_of_sets == {}:
        return False
    elif len(set(cover)) == len(main_set):
        return cover
    else:
        for t in dict_of_sets:
            tmp_dict = dict_of_sets.copy()
            tmp_dict.pop(t)
            cover[t]=dict_of_sets[t]
            return check_cover(main_set,tmp_dict,cover)
