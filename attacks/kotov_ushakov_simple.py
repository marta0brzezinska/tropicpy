"""


"""
from protocols.grigorie_shpilrain_2014 import *
from attacks.attacks_utils import *

def kotov_ushakov_simple(A, B, g, U, V):
    for i in range(g + 1):
        for j in range(g + 1):
            c = is_matrix_difference_constant(U, (A ** i) * (B ** j))
            if c:
                print("Attack was succesfull!")
                print("c = " + str(c))
                print("i = " + str(i))
                print("j = " + str(j))

                return ((A ** i) * c) * V * (B ** j)
    return False

def kotov_ushakov_simple_demo():
    print("Example of Kotov-Ushakov Simple attack:")

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

    attack_K = kotov_ushakov_simple(A,B,g,U,V)

    if Alice.check_Key(attack_K):
        print("Key was found!")
        print("K = \n" + str(attack_K))
    else:
        print("Key doesn't match..")