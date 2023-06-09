"""


"""
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