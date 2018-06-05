class Unit(object):

    def __init__(self, name, factor=None):
        self.name = str(name)
        if factor == float or int:
            self.factor = float(factor)
        elif factor is None:
            self.__set_factor(self.name)

    def __str__(self):
        return self.name

    def __set_factor(self, name):
        """ factor が None のときに呼ばれる. デフォルト単位から指数を推定 """
        factor = None
        self.factor = factor

    def __mul__(self, other):
        """ Unit * Unit
        :param other: Unit
        """
        return float(self.factor * other.factor)

    def __truediv__(self, other):
        """ Unit / Unit
        :param other: Unit
        """
        return float(self.factor / other.factor)


# Length Define
m = Unit('m', 1)
km = Unit('km', 1000)

# Mass
g = Unit('g', 1)
kg = Unit('kg', 1000)

if __name__ == '__main__':
    test = g * m
    print(test)
    test = kg * m
    print(test)
    test = km / g
    print(test)
    test = kg / km
    print(test)
