"""


"""
from tropical.tropical_matrix import *


class GrigorieShpilrain2019:

    def __init__(self, M, H):
        if not isinstance(M, TropicalMatrix):
            raise Exception(str(M) + " is not an appropriate value.")
        elif not isinstance(H, TropicalMatrix):
            raise Exception(str(H) + " is not an appropriate value.")
        else:
            if M.rows != H.rows or M.columns != H.columns:
                raise Exception("Matrices M and H are of different dimensions.")
            elif M.rows != M.columns:
                raise Exception("Matrix M is not a square matrix.")
            elif H.rows != H.columns:
                raise Exception("Matrix H is not a square matrix.")

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
