"""


"""
from tropical.tropical_matrix import *


class GrigorieShpilrain2014():

    def __init__(self, A, B, g):
        if not isinstance(A, TropicalMatrix):
            raise Exception(str(A) + " is not an appropriate value.")
        elif not isinstance(B, TropicalMatrix):
            raise Exception(str(B) + " is not an appropriate value.")
        else:
            if A.rows != B.rows or A.columns != B.columns:
                raise Exception("Matrices A and B are of different dimensions.")
            elif A.rows != A.columns:
                raise Exception("Matrice A is not a square metrix.")
            elif B.rows != B.columns:
                raise Exception("Matrice B is not a square metrix.")

            self.n = A.rows
            self.A = A
            self.B = B
            self.g = g

            tmp_p1 = []
            tmp_p2 = []
            for i in range(g):
                tmp_p1.extend([TropicalValue(random.randint(-1000, 1000), True)])
                tmp_p2.extend([TropicalValue(random.randint(-1000, 1000), True)])

            self._p1 = tmp_p1
            self._p2 = tmp_p2

            result1 = tropical_matrix_0(self.n)
            result2 = tropical_matrix_0(self.n)
            for (el1, el2, i) in zip(self._p1, self._p2, range(self.g)):
                result1 += (self.A ** i) * el1
                result2 += (self.B ** i) * el2

            self._p_1_A = result1
            self._p_2_B = result2

            self.m = None
            self._K = None

    def send_message(self):
        self.m = self._p_1_A * self._p_2_B
        return self.m

    def set_Key(self, v):
        self._K = self._p_1_A * v * self._p_2_B

    def get_Key(self):
        return self._K

    def check_Key(self, check_K):
        return check_K == self._K

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