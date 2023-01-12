"""


"""
from tropical_matrix import *


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

    def check_Key(self, check_K):
        return check_K == self._K


def value_difference(a, b):
    if b == tropical_0:
        return False
    elif a == tropical_0:
        return tropical_0
    else:
        return TropicalValue(a.value - b.value, a.is_int and b.is_int)


def is_matrix_difference_constant(A, B):
    frst = True
    for (row_a, row_b) in zip(A.values, B.values):
        for (a, b) in zip(row_a, row_b):
            if frst:
                frst = False
                c = value_difference(a, b)
                if not c:
                    continue
            else:
                new_c = value_difference(a, b)
                if new_c:
                    if new_c != c:
                        return False
                    else:
                        c = new_c
    return c


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

def min_of_matrix_difference(A,B):
    result = {}
    t = tropical_0
    P = []
    for (row_a, row_b, i) in zip(A.values, B.values, range(A.rows)):
        for (a, b, j) in zip(row_a, row_b, range(A.columns)):
            c = value_difference(a, b)
            if t == c:
                P. append([i,j])
            elif t + c == c:
                t += c
                P = []
                P.append([i, j])
    result[t] = P
    return result

def check_cover(main_set, dict_of_sets, cover):
    if dict_of_sets == {}:
        return False
    elif len(set(cover)) == len(main_set):
        return cover
    else:
        for t in dict_of_sets:
            tmp_dict = dict_of_sets.copy()
            tmp_dict.pop(t)
            cover[t]=dict_of_sets[t]
            return check_cover(main_set,tmp_dict,cover)

def kotov_ushakov(A, B, g, U, V):
    result = {}
    n = A.rows
    for i in range(g+1):
        for j in range(g+1):
            result.update(min_of_matrix_difference((A ** i) * (B ** j),U))
    S = [[i,j] for i in range(n) for j in range(n)]
    for t in result:
        #TODO: znaleźć minimalne pokrycia S
        C = check_cover(S,result,dict([(t,result[t])]))
        print("cover:")
        for c in C:
            print(C[c])
    return False