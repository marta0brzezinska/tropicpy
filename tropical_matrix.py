"""


"""

from tropical_value import *
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
        if self.rows != other.rows:
            return False
        elif self.columns != other.columns:
            return False

        for (row_a, row_b) in zip(self.values, other.values):
            for (a, b) in zip(row_a, row_b):
                if a != b:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

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
            result = self
            for i in range(power - 1):
                result *= self
            return result
        else:
            raise Exception(str(power) + " is not an accurate power.")


def tropical_matrix_0(n):
    values = []
    for i in range(n):
        values.append([tropical_0] * n)
    return TropicalMatrix(values)


def tropical_matrix_1(n):
    values = []
    for i in range(n):
        tmp_row = [tropical_0] * n
        tmp_row[i] = tropical_1
        values.append(tmp_row)
    return TropicalMatrix(values)


def generate_random_tropical_matrix(n, l, u, isint):
    values = []
    for i in range(n):
        tmp_row = []
        for j in range(n):
            tmp_row.append(TropicalValue(random.randint(l, u), isint))
        values.append(tmp_row)
    return TropicalMatrix(values, True)

