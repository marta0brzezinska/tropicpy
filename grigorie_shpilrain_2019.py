"""


"""
from tropical_matrix import *


class GrigorieShpilrain2019():

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

            #TODO: uzupełnić inicjalizacje protokołu GS2019


    def send_message(self):
        #TODO: generate message GS2019
        return self.m

    def set_Key(self, v):
        #TODO: ustalenie klucza dla GS2019
        self._K = 0

    def check_Key(self, check_K):
        return check_K == self._K

#TODO: implementacja ataku rudy_monico()

#TODO: implementacja ataku isaac_kahrobae()

#TODO: implementacja ataku muanalifah_sergeev()