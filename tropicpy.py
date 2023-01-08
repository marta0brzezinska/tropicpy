"""


"""
from grigorie_shpilrain_2014 import *


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

tropical_demo()

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

    print("u \n= \n" + str(u))
    print("v \n= \n" + str(v))

    Alice.set_Key(v)
    Bob.set_Key(u)

    if Alice.get_Key() == Bob.get_Key():
        print("Alice and Bob share a secret!")
    else:
        print("Something went wrong!")


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

    attack_K = kotov_ushakov_simple(A,B,g,U,V)

    if attack_K == Alice.get_Key():
        print("Key was found!")
    else:
        print("Key doesn't match..")

#kotov_ushakov_simple_demo()