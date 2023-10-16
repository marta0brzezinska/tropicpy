"""


"""

from attacks.attacks_utils import *


def isaac_kahrobaei(M, H, A, B):
    m = 1

    D = None
    M_now = M

    previous_D = []
    previous_M = [None]

    while semidirect_power_1st(M, H, m) != A:

        additional_previous_D = []

        while D not in additional_previous_D:
            M_before = M_now
            M_now = semidirect_product_1st(M_before, None, M, H)
            additional_previous_D.append(D)
            previous_M.append(M_before)
            D = matrix_difference(M_now, M_before)

        previous_D = previous_D + additional_previous_D

        previous_D.reverse()
        d = len(previous_D) - previous_D.index(D) - 2
        previous_D.reverse()

        rho = len(previous_D) - (d + 1)
        print("d=" + str(d))
        print("rho=" + str(rho))

        if any(is_zero_matrix(prev_D) for prev_D in previous_D) or is_zero_matrix(D):
            m = d + 1
            break

        Y = matrix_difference(A, previous_M[d + 1])
        full_sum = matrix_sum([previous_D[i + 1] for i in range(d, d + rho)])

        for k in range(1, rho + 1):
            partial_sum = matrix_sum([previous_D[i] for i in range(d + 1, d + k + 1)], D.rows)
            diff = matrix_difference(Y, partial_sum)
            if is_zero_modulo(diff, full_sum):
                print("k=" + str(k))
                break

        x = (diff.values[0][0]).value // (full_sum.values[0][0]).value
        print("x=" + str(x))
        m = d + x * rho + k + 1

    print("Attack was succesfull!")
    print("m = " + str(m))
    Hm = semidirect_power_2nd(M, H, m)

    return semidirect_product_1st(B, None, A, Hm)
