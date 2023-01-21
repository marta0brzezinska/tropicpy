"""


"""
from tropical_matrix import *


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
        tmp_product = semidirect_power(self.M, self.H, self.m)
        self.A = tmp_product[0]
        self.Hm = tmp_product[1]
        return self.A

    def set_Key(self, B):
        self._K = (B @ self.Hm) + self.A

    def get_Key(self):
        return self._K

    def check_Key(self, check_K):
        return check_K == self._K

# TODO: implementacja ataku rudy_monico()

# TODO: implementacja ataku isaac_kahrobae()

# TODO: implementacja ataku muanalifah_sergeev()
