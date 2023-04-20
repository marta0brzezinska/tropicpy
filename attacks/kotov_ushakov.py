"""


"""
from protocols.grigorie_shpilrain_2014 import *
from attacks.attacks_utils import *

def kotov_ushakov(A, B, g, U, V):
    result = {}
    n = A.rows
    for i in range(g+1):
        for j in range(g+1):
            result.update(min_of_matrix_difference((A ** i) * (B ** j),U))
    S = [[i,j] for i in range(n) for j in range(n)]
    for t in result:
        print(str(t) + ":" + str(result[t]))
        #TODO: znaleźć minimalne pokrycia S
        C = check_cover(S,result,dict([(t,result[t])]))
        print("cover:")
        for c in C:
            print(C[c])
    return False

def kotov_ushakov_demo():
    print("Example of Kotov-Ushakov attack:")

    n=3

    A = generate_random_tropical_matrix(n,-10 ** 10,10 ** 10,True)
    B = generate_random_tropical_matrix(n,-10 ** 10,10 ** 10,True)

    g=6

    print("Parameters:")
    print("A = \n" + str(A))
    print("B = \n" + str(B))
    print("g = " + str(g))

    Alice = GrigorieShpilrain2014(A,B,g)
    U = Alice.send_message()
    Bob = GrigorieShpilrain2014(A, B, g)
    V = Bob.send_message()

    Alice.set_Key(V)

    attack_K = kotov_ushakov(A,B,g,U,V)

    if Alice.check_Key(attack_K):
        print("Key was found!")
        print("K = \n" + str(attack_K))
    else:
        print("Key doesn't match..")