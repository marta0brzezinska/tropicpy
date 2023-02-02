"""


"""
from tropical.tropical_matrix import *


class GrigorieShpilrain2019():

    def __init__(self, M, H):
        if not isinstance(M, TropicalMatrix):
            raise Exception(str(M) + " is not an appropriate value.")
        elif not isinstance(H, TropicalMatrix):
            raise Exception(str(H) + " is not an appropriate value.")
        else:
            if M.rows != H.rows or M.columns != H.columns:
                raise Exception("Matrices M and H are of different dimensions.")
            elif M.rows != M.columns:
                raise Exception("Matrice M is not a square metrix.")
            elif H.rows != H.columns:
                raise Exception("Matrice H is not a square metrix.")

            self.k = M.rows
            self.M = M
            self.H = H

            self.m = random.getrandbits(int(2 ** 200).bit_length())

            self.A = None
            self.Hm = None
            self._K = None

    def send_message(self):
        self.A = semidirect_power_1st(self.M, self.H, self.m)
        self.Hm = semidirect_power_2nd(self.M, self.H, self.m)
        return self.A

    def set_Key(self, B):
        self._K = (B @ self.Hm) + self.A

    def get_Key(self):
        return self._K

    def check_Key(self, check_K):
        return check_K == self._K

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
