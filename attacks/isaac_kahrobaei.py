"""


"""
from protocols.grigorie_shpilrain_2019 import *
from attacks.attacks_utils import *


def isaac_kahrobaei(M,H,A,B):
    M_now = M

    prevoius_D = []
    prevoius_M = [None]

    D = None
    o=1
    #TODO: deal with special cases: check if (M,H)^a == (A,*)
    while D not in prevoius_D:
        M_before = M_now
        M_now = semidirect_product_1st(M_before,None,M,H)
        prevoius_D.append(D)
        prevoius_M.append(M_before)
        #print("M"+str(o+1) + "-M" + str(o) + "=")
        #print(M_now)
        #print("-")
        #print(M_before)
        D = matrix_difference(M_now, M_before)
        print("D" + str(o)+ ":\n"+str(D))
        o+=1
        print("------------")

    for k in range(2):
        M_before = M_now
        M_now = semidirect_product_1st(M_before, None, M, H)
        D = matrix_difference(M_now, M_before)
        print("D" + str(o+k) + ":\n" + str(D))


    d = prevoius_D.index(D)
    rho = len(prevoius_D) - d
    print("d=" + str(d))
    print("rho=" + str(rho))
    prevoius_D.append(D)

    print("A=\n"+str(A))
    Y = matrix_difference(A,prevoius_M[d+1])
    print("M_" + str(d+1) +"=\n"+ str(prevoius_M[d+1]))
    sum = matrix_sum([prevoius_D[i+1] for i in range(d,d+rho)])
    print("Y=\n"+str(Y))
    print("sum=\n"+str(sum))

    for k in range(1,rho+1):
        partial_sum = matrix_sum([prevoius_D[i] for i in range(d+1,d+k+1)],D.rows)
        print("partial sum for " + str(k) + ", d's: ")
        for l in range(d+1,d+k+1):
            print(l)
        print(partial_sum)
        diff = matrix_difference(Y,partial_sum)
        print("diff for k="+str(k))
        print(diff)
        if is_zero_modulo(diff,sum):
            print("work")
            break

    #TODO: check this
    print("k="+str(k))
    x=(diff.values[0][0]).value // (sum.values[0][0]).value
    print("x="+str(x))
    m = d + x * rho + k
    print("power is: " +str(m))
    Hm = semidirect_power_2nd(M, H, m)

    return semidirect_product_1st(B, None, A, Hm)


M =TropicalMatrix([[ -275,  -23357,   0 ],[ -31,  -1609,  -7003 ],[ -61,  84,   31  ]])
H =TropicalMatrix([[ -2985,  388875,  -6230984],[ 18,   6702,  12  ],[ 80006,   53,  -56 ]])

A = semidirect_power_1st(M,H,11)
B = semidirect_power_1st(M,H,3)

#isaac_kahrobaei(M,H,A,B)