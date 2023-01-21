"""


"""
from grigorie_shpilrain_2014 import *
from grigorie_shpilrain_2019 import *


def tropical_demo():
    print("In tropical algebra we have:")

    print("0 = " + str(tropical_0))
    print("1 = " + str(tropical_1))

    print("0(3x3) \n=\n" + str(tropical_matrix_0(3)))
    print("1(3x3) \n=\n" + str(tropical_matrix_1(3)))

    print("Examples of tropical operations:")

    a = TropicalValue(9)
    b = TropicalValue(inf)

    print("a) addition:")
    print(a, end="")
    print("+", end="")
    print(b, end="")
    print("=", end="")
    print(a + b)

    c = TropicalValue(2, True)
    d = TropicalValue(3, True)

    print("b) multiplication:")
    print(c, end="")
    print("*", end="")
    print(d, end="")
    print("=", end="")
    print(c * d)

    print("Examples of operations on tropical matrices:")

    e = TropicalMatrix([[1, 2], [5, -1]], isint=True)
    f = TropicalMatrix([[0, 3], [2, 8]])

    print("a) addition:")
    print(e)
    print("+")
    print(f)
    print("=")
    print(e + f)

    print("b) multiplication:")

    print(e)
    print("*")
    print(f)
    print("=")
    print(e * f)

    print("c) power")
    print(e)
    print("** 4\n=")
    print(e ** 4)

    print("d) adjoint multiplication:")

    print(e)
    print("@")
    print(f)
    print("=")
    print(e @ f)

    print("e) adjoint power")
    print(e)
    print("^3\n=")
    print(e ^ 3)


#tropical_demo()

def grigorie_shpilrain_2014_demo():
    print("Example of Grigorie-Shpilrain (2014) protocol:")

    n = 3
    A = generate_random_tropical_matrix(n,-10 ** 10,10 ** 10,True)
    B = generate_random_tropical_matrix(n,-10 ** 10,10 ** 10,True)

    g=6

    print("Parameters:")
    print("A = \n" + str(A))
    print("B = \n" + str(B))
    print("g = " + str(g))

    Alice = GrigorieShpilrain2014(A, B, g)
    Bob = GrigorieShpilrain2014(A, B, g)

    print("n = " + str(Alice.n))

    u = Alice.send_message()
    v = Bob.send_message()

    print("u = \n" + str(u))
    print("v = \n" + str(v))

    Alice.set_Key(v)
    Bob.set_Key(u)

    if Alice.get_Key() == Bob.get_Key():
        print("Alice and Bob share a secret!")
    else:
        print("Something went wrong!")

#grigorie_shpilrain_2014_demo()

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

#kotov_ushakov_simple_demo()

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

#kotov_ushakov_demo()

def grigorie_shpilrain_2019_demo():
    print("Example of Grigorie-Shpilrain (2019) protocol:")

    k = 3
    M = generate_random_tropical_matrix(k, -10 ** 10, 10 ** 10, True)
    H = generate_random_tropical_matrix(k, -10 ** 10, 10 ** 10, True)

    print("Parameters:")
    print("M = \n" + str(M))
    print("H = \n" + str(H))

    Alice = GrigorieShpilrain2019(M, H)
    Bob = GrigorieShpilrain2019(M, H)

    print("k = " + str(Alice.k))

    A = Alice.send_message()
    B = Bob.send_message()

    print("A = \n" + str(A))
    print("B = \n" + str(B))

    Alice.set_Key(B)
    Bob.set_Key(A)

    if Alice.check_Key(Bob.get_Key()):
        print("Alice and Bob share a secret!")
    else:
        print("Something went wrong!")

grigorie_shpilrain_2019_demo()

#TODO: rudy_monico_demo()
#rudy_monico_demo()

#TODO: isaac_kahrobae_demo()
#isaac_kahrobae_demo()

#TODO: muanalifah_sergeev_demo()
#muanalifah_sergeev_demo()