"""


"""

from tropical.tropical_value import *
import random


class TropicalMatrix():

    def __init__(self, values, isint=False):

        tmp_rows = len(values)
        if tmp_rows == 0:
            tmp_columns = 0
        else:
            tmp_columns = len(values[0])
        tmp_values = []

        for (row, i) in zip(values, range(tmp_rows)):
            if len(row) != tmp_columns:
                raise Exception("Missing values in row no. " + str(i + 1) + ": " + str(row))

        for (row, i) in zip(values, range(tmp_rows)):
            tmp_row = []
            for value in row:
                if correct_tropical_value(value, isint):
                    tmp_row.append(TropicalValue(value, isint))
                elif isinstance(value, TropicalValue) and correct_tropical_value(value.value, isint):
                    tmp_row.append(value)
                else:
                    raise Exception(str(value) + " is not an accurate element of a tropical matrix.")
            tmp_values.append(tmp_row)

        self.is_int = isint
        self.rows = tmp_rows
        self.columns = tmp_columns
        self.values = tmp_values

    def __str__(self):
        if len(self.values) == 0:
            return "[]"

        result = ""
        column_widths = []
        for col_no in range(self.columns):
            column_widths += [max(len(str(row[col_no])) for row in self.values)]

        for (row, row_no) in zip(self.values, range(self.rows)):
            result += "["
            for (value, col_no) in zip(row, range(self.columns)):
                result += '{0:^{1}}'.format(str(value), column_widths[col_no] + 2)
            result += "]"
            if row_no != self.rows - 1:
                result += "\n"
        return result

    def __eq__(self, other):
        if isinstance(other, TropicalMatrix):
            if self.rows != other.rows:
                return False
            elif self.columns != other.columns:
                return False

            for (row_a, row_b) in zip(self.values, other.values):
                for (a, b) in zip(row_a, row_b):
                    if a != b:
                        return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        if self + other == self:
            return True
        else:
            return False

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise Exception("Different dimensions of matrices.")

        result = []
        for (row_a, row_b) in zip(self.values, other.values):
            tmp_row = []
            for (a, b) in zip(row_a, row_b):
                tmp_row.append(a + b)
            result.append(tmp_row)
        return TropicalMatrix(result, self.is_int and other.is_int)

    def __mul__(self, other):
        if isinstance(other, TropicalMatrix):
            if self.columns != other.rows:
                raise Exception("Mismatched dimensions of matrices.")

            result = []
            other_columns = []

            for col_no in range(other.columns):
                other_columns.append([row[col_no] for row in other.values])

            for row in self.values:
                tmp_row = []
                for col_no in range(self.columns):
                    times = list(map(TropicalValue.__mul__, row, other_columns[col_no]))
                    sum = tropical_0
                    for el in times:
                        sum += el
                    tmp_row.append(sum)
                result.append(tmp_row)
            return TropicalMatrix(result, self.is_int and other.is_int)
        elif isinstance(other, TropicalValue):
            result = []
            tmp_isint = self.is_int and other.is_int
            for row in self.values:
                tmp_row = []
                for value in row:
                    tmp_row.append(other * value)
                result.append(tmp_row)

            return TropicalMatrix(result, tmp_isint)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            if power == 0:
                return tropical_matrix_1(self.rows)
            elif power == 1:
                return self
            elif power % 2 == 0:
                return (self * self) ** (power >> 1)
            else:
                return self * ((self * self) ** ((power - 1) >> 1))
        else:
            raise Exception(str(power) + " is not an accurate power.")

    def __matmul__(self, other):
        if isinstance(other, TropicalMatrix):
            return self + other + (self * other)
        else:
            raise Exception("Cannot perform adjoint multiplication for type: " + str(type(other)))

    def __xor__(self, power):
        if power == 1:
            return self
        elif power % 2 == 0:
            return (self @ self) ^ (power >> 1)
        else:
            return self @ ((self @ self) ^ ((power - 1) >> 1))


def semidirect_product_1st(A, B, C, D):
    return (A @ D) + C


def semidirect_product_2nd(A, B, C, D):
    return B @ D

#todo: square-and-multiply method?
def semidirect_power_1st(A, B, n):
    if n == 1:
        return A
    else:
        I = tropical_matrix_1(A.rows)
        return ((A * (I + B)) + B) * ((I + B) ** (n - 2))


def semidirect_power_2nd(A, B, n):
    return B ^ n


def tropical_matrix_0(n):
    values = []
    for i in range(n):
        values.append([tropical_0] * n)
    return TropicalMatrix(values)

def kleene_star(F):
    n = F.rows
    result = tropical_matrix_1(n)
    tmp_F = F
    for i in range(1,n):
        result += tmp_F
        tmp_F *= tmp_F
    return result

def tropical_matrix_1(n):
    values = []
    for i in range(n):
        tmp_row = [tropical_0] * n
        tmp_row[i] = tropical_1
        values.append(tmp_row)
    return TropicalMatrix(values)

def generate_random_tropical_value(l,u,isint):
    return TropicalValue(random.randint(l, u), isint)

def generate_random_tropical_matrix(n, l, u, isint):
    values = []
    for i in range(n):
        tmp_row = []
        for j in range(n):
            tmp_row.append(generate_random_tropical_value(l,u,isint))
        values.append(tmp_row)
    return TropicalMatrix(values, True)


def tropical_demo():
    print("In tropical algebra we have:")

    print("0 = " + str(tropical_0))
    print("1 = " + str(tropical_1))

    print("0(3x3) \n=\n" + str(tropical_matrix_0(3)))
    print("1(3x3) \n=\n" + str(tropical_matrix_1(3)))

    print("Examples of tropical operations:")

    a = generate_random_tropical_value(-100, 100, False)
    b = generate_random_tropical_value(-100, 100, False)

    print("a) addition:")
    print("(" + str(a) + ")+(" + str(b) + ")=" + str(a+b))

    print("b) multiplication:")
    print("(" + str(a) + ")+(" + str(b) + ")=" + str(a*b))

    print("Examples of operations on tropical matrices:")

    e = generate_random_tropical_matrix(3, -100, 100, True)
    f = generate_random_tropical_matrix(3, -100, 100, False)

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