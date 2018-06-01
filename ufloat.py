from units import *


class ufloat(object):

    def __init__(self, x, unit):
        self.x = float(x)
        self.unit = unit

    def __str__(self):
        """ Return string, joining value and unit. """
        return str(self.x) + " " + str(self.unit)

    def __float__(self):
        """ Return only value for float."""
        return float.__float__(self.x)

    def __add__(self, other):
        """
        Value (without unit) adds. If other is not ufloat, transform it to
        float and add. In case, unit is overwrite by ufloat's unit.
        Adopted unit is self's.
        :param other: ufloat or float
        :return: ufloat
        """
        if other is ufloat:
            distance = other.unit / self.unit
        else:
            distance = 1.0
        try:
            ans = float(other) * distance + self.x
        finally:
            pass
        return ufloat(ans, self.unit)


if __name__ == '__main__':
    self = ufloat(100, Unit)
    other = ufloat(200, Unit)
    print(self + other)
