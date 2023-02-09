"""


"""
from protocols.grigorie_shpilrain_2019 import *
from attacks.attacks_utils import *


def isaac_kahrobaei(M,H,A,B):
    M_now = M

    prevoius_D = []
    D = None

    #TODO: deal with special cases: check if (M,H)^a == (A,*)
    while D not in prevoius_D:
        M_before = M_now
        M_now = semidirect_product_1st(M_before,None,M,H)
        prevoius_D.append(D)
        D = matrix_difference(M_now, M_before)

    d = prevoius_D.index(D)
    rho = len(prevoius_D) - d
    print("d=" + str(d))
    print("rho=" + str(rho))
    prevoius_D.append(D)

    Y = matrix_difference(A,M_now)
    sum = matrix_sum([prevoius_D[i+1] for i in range(d,d+rho)])

    for k in range(1,rho+1):
        partial_sum = matrix_sum([prevoius_D[i] for i in range(d,d+k)],D.rows)
        if is_zero_modulo(matrix_difference(Y,partial_sum),sum):
            break

    #TODO: check this
    k += 1
    print("k="+str(k))
    x=(Y.values[0][0]).value // (sum.values[0][0]).value
    print("x="+str(x))
    m = d + x * rho + k
    print("power is: " +str(m))
    Hm = semidirect_power_2nd(M, H, m)

    return semidirect_product_1st(B, None, A, Hm)


M =TropicalMatrix([[ -275,  -23357,   0 ],[ -31,  -1609,  -7003 ],[ -61,  84,   31  ]])
H =TropicalMatrix([[ -2985,  388875,  -6230984],[ 18,   6702,  12  ],[ 80006,   53,  -56 ]])

A = semidirect_power_1st(M,H,32)
B = semidirect_power_1st(M,H,23)

isaac_kahrobaei(M,H,A,B)