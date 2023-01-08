"""


"""
from utils import *

inf = "inf"


class TropicalValue(object):

    def __init__(self, value, isint=False):
        if value == inf or value == float(inf):
            self.is_num = False
            self.is_int = isint
            self.value = float(inf)
        elif isint and not isinstance(value, int):
            raise Exception(str(value) + " is not an integer.")
        elif is_number(value):
            self.is_num = True
            self.is_int = isint
            self.value = value
        else:
            raise Exception(str(value) + " is not an accurate tropical value.")

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return TropicalValue(min(self.value, other.value))

    def __mul__(self, other):
        return TropicalValue(self.value + other.value)

    def __pow__(self, power, modulo=None):
        return self.value * power


tropical_0 = TropicalValue(inf)
tropical_1 = TropicalValue(0)


def correct_tropical_value(value, isint=False):
    try:
        TropicalValue(value, isint)
    except:
        return False
    else:
        return True
