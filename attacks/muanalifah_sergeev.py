"""


"""
from attacks_utils import *

def muanalifah_sergeev(M,H,A,B):
    lmbda = largest_tropical_eigenvalue(H)

    I = tropical_matrix_1(M.rows)
    F = I + H
    V = M * F + H

    K = (M + H) * kleene_star(H)

    if lmbda <= 0:
        if A == K or B == K:
            return K
        elif A == M or B == M:
            m = 1
            n = 1
        #TODO: find l1, l2
    else:
        if A == M or B == M:
            m = 1
            n = 1
        # TODO: find l1, l2

    #TODO: step 3.
    return 0

M = TropicalMatrix([[8, 7 ,2],[10, 3 ,6],[-10, -1 ,3]])
H = TropicalMatrix([[0,-3 ,-5],[-1,-2, 2],[1 ,-3 ,-4]])

m = 5
n = 8

A = semidirect_power_1st(M,H,m)
B = semidirect_power_1st(M,H,n)

muanalifah_sergeev(M,H,A,B)