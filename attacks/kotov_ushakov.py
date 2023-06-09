"""


"""
from attacks.attacks_utils import *

def kotov_ushakov(A, B, g, U, V, p_min, p_max):
    n = A.rows

    data = []

    for i in range(g+1):
        for j in range(g+1):
            matrix_min = min_of_matrix_difference((A ** i) * (B ** j), U * TropicalValue((-2) * -1000))
            if matrix_min[0].value <= 0:
                result = {}
                result["i"] = i
                result["j"] = j
                result["minval"] = matrix_min[0]
                result["inds"] = matrix_min[1]
                data.append(result)

    for record in data:
        print("For i=" + str(record["i"]) + " j=" + str(record["j"]))
        print("minimal value of " + str(record["minval"]))
        print("is acheived at: \n" + str(record["inds"]))
        print("")

    inds = [result["inds"] for result in data]
    C = minimal_set_covers(inds)
    print("minamal set covers:\n" + str(C))

    minimal_covers_ij=[]
    for cover in C:
        minimal_covers_ij.extend(list_cartesian([[[record["i"],record["j"]] for record in data if el == record["inds"]] for el in cover]))

    print(minimal_covers_ij)

    for ij in minimal_covers_ij:
        result = simplex(make_simplex_matrix(data,g,ij))
        polys = [[result[i]+p_min for i in range(g+1)],[result[g+1+ i]+p_min for i in range(g+1)]]
        if result:
            p1_A = tropical_matrix_0(n)
            p2_B = tropical_matrix_0(n)
            for (el1,el2,i) in zip(polys[0],polys[1],range(g+1)):
                p1_A += (A ** i) * TropicalValue(el1)
                p2_B += (B ** i) * TropicalValue(el2)
            return p1_A * V * p2_B

    return False

def kotov_ushakov_demo():
    print("Example of Kotov-Ushakov attack:")

    n=3

    A =TropicalMatrix([[ -6844059157,  5151562372  , 1977151082  ],[ 1675247741,   -2079685005,  -7947386719 ],[ -8293205090 ,-5149336598 , -3558159121 ]])
    B =TropicalMatrix([[ 7638858521  , -9463023213 , -617764241 ] , [ -3966713419 , 6414342109 ,  8449813899 ] , [ -475041357  ,  596839365  , 6775189016 ]])
    #A = TropicalMatrix([[ -8484113615 , -3525141732 , 4849675931 ],[ -8700334890 , 2832076767  , 5940548993 ],[ 8756763924   ,-2300113485 , 2623951354 ]])
    #B = TropicalMatrix([[ -6900308234 , -7167377685 , -8689388045 ],[ -9192786659 , -4369262160 , -3768719024 ],[ 2122385609  , -2991414787  ,-3988134310 ]])

    g=4

    print("Parameters:")
    print("A = \n" + str(A))
    print("B = \n" + str(B))
    print("g = " + str(g))

    p1 = [TropicalValue(-155),TropicalValue(-270), TropicalValue(47), TropicalValue(123), TropicalValue(127)]
    p2 = [TropicalValue(-637),TropicalValue(808), TropicalValue(-13), TropicalValue(-129),TropicalValue(-909)]


    result1 = tropical_matrix_0(n)
    result2 = tropical_matrix_0(n)
    for (el1, el2, i) in zip(p1,p2, range(g+1)):
        result1 += (A ** i) * el1
        result2 += (B ** i) * el2

    U = result1*result2
    print("U:")
    print(U)

    q1 = [TropicalValue(-130),TropicalValue(-814), TropicalValue(667), TropicalValue(762), TropicalValue(-123)]
    q2 = [TropicalValue(289),TropicalValue(505), TropicalValue(-90), TropicalValue(832), TropicalValue(-973)]

    result1 = tropical_matrix_0(n)
    result2 = tropical_matrix_0(n)
    for (el1, el2, i) in zip(q1, q2, range(g+1)):
        result1 += (A ** i) * el1
        result2 += (B ** i) * el2

    V=result1*result2
    print("V:")
    print(V)


    key = result1 * U * result2
    attack_key = kotov_ushakov(A,B,g,U,V,-1000,1000)

    match = (key==attack_key)
    print(match)