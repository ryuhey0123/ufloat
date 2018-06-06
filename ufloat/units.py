class Unit(object):
    """ Unitクラスを定義する.

    任意の単位について、基本単位に何を乗じればその値になるか(これをfactorとしている)
    を探すことがメイン。ufloatの演算体系では、factorを用いて一度演算対象を基本単位系に直して
    から演算し、元に戻すという作業を行う。

    一度Unitで単位系を定義してあげれば再計算の必要がなくなるので、パフォーマンス的に期待できる。
    また、SI単位に関わらないユーザー単位（例えばfeetや条など）も対応が容易。

    Usage:
        Unit(単位名称, factor, alias)
        でUnitインスタンスの生成が可能。定数と考えて差し支えないので、それぞれsetterなしの
        propertyとして、擬似ReadOnlyとしている。
        factor, aliasは省略可能。

    Property:
        .name: 単位名称
        .factor: 基本単位に乗じる係数
        .base_unit: 比較した基本単位
        .alias: 別名
    """

    def __init__(self, name, factor=None, alias=None):
        """
        Args:
            name (str):
                Unit name.
            factor (int or float or None):
                それを乗じれば基本単位になる数値.
                例えば 'km' であれば、
                    1 km = 1000 m
                より、factor = 1000となる. 省略すれば、nameより自動計算.
            alias (Unit):
                単位の別名。例えば、Pa = N/m2.
        """
        self._name = str(name)
        self._base_unit, self._factor = self.__set_factor(self.name)
        self._alias = alias

    @staticmethod
    def __set_factor(name):
        """
        Called when factor is None. Calculate factor and return.
        """
        base_unit = None
        if name in BASE_UNITS.keys():
            base_unit = BASE_UNITS[name]
        elif name in DERIVED_UNITS.keys():
            base_unit = DERIVED_UNITS[name]
        return base_unit, base_unit.factor

    @property
    def name(self):  # ReadOnly
        return self._name

    @property
    def factor(self):  # ReadOnly
        return self._factor

    @property
    def alias(self):  # ReadOnly
        return self._alias

    @property
    def base_unit(self):  # ReadOnly
        return self._base_unit

    def __str__(self):
        """ Called when str(), print() """
        return self.name

    def __mul__(self, other):
        """ Unit * Unit
        Args:
            other (Unit): Value after operator '*'.
        Returns:
            float: Ex) kN * N returns 1000.0
        """
        return float(self.factor * other.factor)

    def __truediv__(self, other):
        """ Unit / Unit
        Args:
            other (Unit): Value after operator '/'.
        Returns:
            float: Ex) kN / N returns 0.001
        """
        return float(self.factor / other.factor)


# Reference https://en.wikipedia.org/wiki/International_System_of_Units

BASE_UNITS = {
    'm': Unit('m', 1),  # length
    'g': Unit('g', 1),  # mass
    's': Unit('s', 1),  # time
    'A': Unit('A', 1),  # electric current
    'K': Unit('K', 1),  # temperature
    'mol': Unit('mol', 1),  # amount of substance
    'cd': Unit('cd', 1)  # luminous
}

DERIVED_UNITS = {
    'rad': Unit('rad', 1),  # Angle
    'N': Unit('N', 1)
}

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
