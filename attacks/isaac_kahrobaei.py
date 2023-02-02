"""


"""
from protocols.grigorie_shpilrain_2019 import *
from attacks.attacks_utils import *


def isaac_kahrobaei(M,H,A,B):
    M_before = M
    M_now = semidirect_power_1st(M,H,2)

    prevoius_D = []
    D = matrix_difference(M_before,M_now)

    #TODO: deal with special cases: check if (M,H)^a == (A,*)
    while D not in prevoius_D:
        M_before = M_now
        M_now = semidirect_product_1st(M_before,None,M,H)

        prevoius_D.append(D)
        D = matrix_difference(M_before,M_now)

    d = prevoius_D.index(D)
    rho = len(prevoius_D) - d
    print("d=" + str(d))
    print("rho=" + str(rho))

    #TODO: find x and k

    Md = semidirect_power_1st(M,H,d)
    Y = matrix_difference(A,Md)

    print("D=\n" + str(D), end="\n--\n")
    print("Prevoius:")
    for m in prevoius_D:
        print(m,end="\n-\n")

    print("chosen:")
    for i in range(d,d+rho):
        print(i)

    sum = matrix_sum([prevoius_D[i] for i in range(d,d+rho)])
    print("full sum=\n" + str(sum))
    k=None
    for k in range(rho):
        partial_sum = matrix_sum([prevoius_D[i] for i in range(d,d+k+1)])
        print("partial sum=\n" + str(partial_sum))
        if is_zero_modulo(matrix_difference(Y,partial_sum),sum):
            break

    print("k="+str(k))
    print((Y.values[0][0]).value)
    print((sum.values[0][0]).value)
    x=(Y.values[0][0]).value // (sum.values[0][0]).value

    m = d + x * rho + k
    print("power is: " + str(m))
    Hm = semidirect_power_2nd(M, H, -m)
    return semidirect_product_1st(B, None, A, Hm)


M =TropicalMatrix([[ -275,  -23357,   0 ],[ -31,  -1609,  -7003 ],[ -61,  84,   31  ]])
H =TropicalMatrix([[ -2985,  3888975,  -6230984],[ 18,   6702,  12  ],[ 80006,   53,  -56 ]])

A = semidirect_power_1st(M,H,30)
B = semidirect_power_1st(M,H,23)

#isaac_kahrobaei(M,H,A,B)

print("a=")
print(attack(M,H,A))