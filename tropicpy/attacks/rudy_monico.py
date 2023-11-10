"""

"""


def rudy_monico(M, H, A, B):
    r = 1
    tmp_M = semidirect_power_1st(M, H, r)
    while A <= tmp_M:
        r *= 2
        tmp_M = semidirect_power_1st(M, H, r)
    print("Upper bound found: \n" + str(r))
    upper = r
    lower = upper >> 1
    while upper >= lower:
        middle = (lower + upper) >> 1
        tmp_M = semidirect_power_1st(M, H, middle)
        if tmp_M == A:
            print("Attack was succesful!")
            break
        elif tmp_M <= A:
            upper = middle - 1
        else:
            lower = middle + 1

    print("m=" + str(middle))
    Hm = semidirect_power_2nd(M, H, middle)
    return semidirect_product_1st(B, None, A, Hm)
