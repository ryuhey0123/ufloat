""" ***************************
    単位 = [分子, 分母]
    分子 = [係数, [文字列]]
    分母 = [係数, [文字列]]
    みたいに定義
*************************** """
m = [[1, ["m"]], [1, [1]]]
s = [[1, ["s"]], [1, [1]]]
N = [[1, ["N"]], [1, [1]]]


class Ufloat(object):

    def __init__(self, value, unit):
        self.value = float(value)
        self.unit = unit

    def __str__(self):
        """分子と分母の文字列"""
        new_unit_above = ""
        new_unit_under = ""

        """分子の係数"""
        for i in range(len(self.unit[0]) - 1):  # 配列[分子]の最後は必ず[文字列]なので -1
            if self.unit[0][i] != 1:
                new_unit_above += self.unit[0][i]

        """分子の文字列"""
        for i in range(len(self.unit[0][len(self.unit[0])])):
            # [文字列]は必ず最後はなのでlen(unit[0])番目
            new_unit_above += self.unit[0][len(self.unit[0])][i]

        """分母も同様に"""
        for i in range(len(self.unit[1]) - 1):
            if self.unit[1][i] != 1:
                new_unit_under += self.unit[1][i]

        for i in range(len(self.unit[1][len(self.unit[1])])):
            if self.unit[1][len(self.unit[1])][i] != 1:
                new_unit_under += self.unit[1][len(self.unit[1])][i]

        if new_unit_under == "":
            new_unit = new_unit_above
        else:
            new_unit = new_unit_above + "/" + new_unit_under

        return str(self.value) + " " + new_unit

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        distance = 1.0
        if isinstance(other, Ufloat):
            for i in range(len(other[0]) - 1):
                distance *= other[0][i]
            for i in range(len(other[1]) - 1):
                distance /= other[1][i]
        try:
            ans = self.value + other.value * distance
        finally:
            pass
        return Ufloat(ans, self.unit)

    def __sub__(self, other):
        distance = 1.0
        if isinstance(other, Ufloat):
            for i in range(len(other[0]) - 1):
                distance *= other[0][i]
            for i in range(len(other[1]) - 1):
                distance /= other[1][i]
        try:
            ans = self.value - other.value * distance
        finally:
            pass
        return Ufloat(ans, self.unit)

    def __mul__(self, other):
        new_unit_above = [1]
        new_unit_above_ary = [1]
        new_unit_under = [1]
        new_unit_under_ary = [1]
        new_unit = []

        """分母分子の係数被り削除"""
        for i in range(min(len(self.unit[0]), len(other.unit[1]))):
            if len(self.unit[0]) <= len(other.unit[1]):
                for j in range(len(self.unit[0]) - 1):
                    if self.unit[0][j] in len(other.unit[1]):
                        del self.unit[0][j]
                        del other.unit[1][other.unit[1].index(self.unit[0][j])]
            if len(self.unit[0]) > len(other.unit[1]):
                for j in range(len(other.unit[1]) - 1):
                    if other.unit[1][j] in len(self.unit[0]):
                        del other.unit[1][j]
                        del self.unit[0][self.unit[0].index(other.unit[1][j])]

        for i in range(min(len(self.unit[1]), len(other.unit[0]))):
            if len(self.unit[1]) <= len(other.unit[0]):
                for j in range(len(self.unit[1]) - 1):
                    if self.unit[1][j] in len(other.unit[0]):
                        del self.unit[1][j]
                        del other.unit[0][other.unit[0].index(self.unit[1][j])]
            if len(self.unit[1]) > len(other.unit[0]):
                for j in range(len(other.unit[0]) - 1):
                    if other.unit[0][j] in len(self.unit[1]):
                        del other.unit[0][j]
                        del self.unit[1][self.unit[1].index(other.unit[0][j])]

        """分母分子の単位被り削除"""
        for i in range(min(len(self.unit[0][len(self.unit[0])]),
                len(other.unit[1][len(other.unit[1])]))):
            if len(self.unit[0][len(self.unit[0])]) <= len(
                    other.unit[1][len(other.unit[1])]):
                for j in range(len(self.unit[0][len(self.unit[0])])):
                    if self.unit[0][len(self.unit[0])][j] in len(
                            other.unit[1][len(other.unit[1])]):
                        del self.unit[0][len(self.unit[0])][j]
                        del other.unit[1][other.unit[1].index(
                            self.unit[0][len(self.unit[0])][j])]
            if len(self.unit[0][len(self.unit[0])]) > len(
                    other.unit[1][len(other.unit[1])]):
                for j in range(len(other.unit[1][len(other.unit[1])])):
                    if other.unit[1][len(other.unit[1])][j] in len(
                            self.unit[0][len(self.unit[0])]):
                        del other.unit[1][len(other.unit[1])][j]
                        del self.unit[0][self.unit[0].index(
                            other.unit[1][len(other.unit[1])][j])]

        for i in range(min(len(self.unit[1][len(self.unit[1])]),
                len(other.unit[0][len(other.unit[0])]))):
            if len(self.unit[1][len(self.unit[1])]) <= len(
                    other.unit[0][len(other.unit[0])]):
                for j in range(len(self.unit[1][len(self.unit[1])])):
                    if self.unit[1][len(self.unit[1])][j] in len(
                            other.unit[0][len(other.unit[0])]):
                        del self.unit[1][len(self.unit[1])][j]
                        del other.unit[0][other.unit[0].index(
                            self.unit[1][len(self.unit[1])][j])]
            if len(self.unit[1][len(self.unit[1])]) > len(
                    other.unit[0][len(other.unit[0])]):
                for j in range(len(other.unit[0][len(other.unit[0])])):
                    if other.unit[0][len(other.unit[0])][j] in len(
                            self.unit[1]):
                        del other.unit[0][len(other.unit[0])][j]
                        del self.unit[1][self.unit[1].index(
                            other.unit[0][len(other.unit[0])][j])]

        for i in range(len(self.unit[0]) - 1):
            new_unit_above.append(self.unit[0][i])
        for i in range(len(other.unit[0]) - 1):
            new_unit_above.append(other.unit[0][i])

        for i in range(len(self.unit[1]) - 1):
            new_unit_above.append(self.unit[1][i])
        for i in range(len(other.unit[1]) - 1):
            new_unit_above.append(other.unit[1][i])

        new_unit_above_ary = self.unit[0][len(self.unit[0])] + other.unit[0][
            len(other.unit[0])]
        new_unit_under_ary = self.unit[1][len(self.unit[1])] + other.unit[1][
            len(other.unit[1])]

        new_unit_above.append(new_unit_above_ary)
        new_unit_under.append(new_unit_under_ary)
        new_unit.append(new_unit_above).append(new_unit_under)

        ans = self.value * other.value

        return Ufloat(ans, new_unit)

    def __truediv__(self, other):
        new_unit_above = [1]
        new_unit_above_ary = [1]
        new_unit_under = [1]
        new_unit_under_ary = [1]
        new_unit = []

        """分母分子の係数被り削除"""
        for i in range(min(len(self.unit[0]), len(other.unit[0]))):
            if len(self.unit[0]) <= len(other.unit[0]):
                for j in range(len(self.unit[0]) - 1):
                    if self.unit[0][j] in len(other.unit[0]):
                        del self.unit[0][j]
                        del other.unit[1][other.unit[0].index(self.unit[0][j])]
            if len(self.unit[0]) > len(other.unit[0]):
                for j in range(len(other.unit[0]) - 1):
                    if other.unit[0][j] in len(self.unit[0]):
                        del other.unit[0][j]
                        del self.unit[0][self.unit[0].index(other.unit[0][j])]

        for i in range(min(len(self.unit[1]), len(other.unit[1]))):
            if len(self.unit[1]) <= len(other.unit[1]):
                for j in range(len(self.unit[1]) - 1):
                    if self.unit[1][j] in len(other.unit[1]):
                        del self.unit[1][j]
                        del other.unit[1][other.unit[1].index(self.unit[1][j])]
            if len(self.unit[1]) > len(other.unit[1]):
                for j in range(len(other.unit[1]) - 1):
                    if other.unit[1][j] in len(self.unit[1]):
                        del other.unit[1][j]
                        del self.unit[1][self.unit[1].index(other.unit[1][j])]

        """分母分子の単位被り削除"""
        for i in range(min(len(self.unit[0][len(self.unit[0])]),
                len(other.unit[0][len(other.unit[0])]))):
            if len(self.unit[0][len(self.unit[0])]) <= len(
                    other.unit[0][len(other.unit[0])]):
                for j in range(len(self.unit[0][len(self.unit[0])])):
                    if self.unit[0][len(self.unit[0])][j] in len(
                            other.unit[0][len(other.unit[0])]):
                        del self.unit[0][len(self.unit[0])][j]
                        del other.unit[0][other.unit[0].index(
                            self.unit[0][len(self.unit[0])][j])]
            if len(self.unit[0][len(self.unit[0])]) > len(
                    other.unit[1][len(other.unit[1])]):
                for j in range(len(other.unit[0][len(other.unit[0])])):
                    if other.unit[0][len(other.unit[0])][j] in len(
                            self.unit[0][len(self.unit[0])]):
                        del other.unit[0][len(other.unit[0])][j]
                        del self.unit[0][self.unit[0].index(
                            other.unit[0][len(other.unit[0])][j])]

        for i in range(min(len(self.unit[1][len(self.unit[1])]),
                len(other.unit[1][len(other.unit[1])]))):
            if len(self.unit[1][len(self.unit[1])]) <= len(
                    other.unit[1][len(other.unit[1])]):
                for j in range(len(self.unit[1][len(self.unit[1])])):
                    if self.unit[1][len(self.unit[1])][j] in len(
                            other.unit[1][len(other.unit[1])]):
                        del self.unit[1][len(self.unit[1])][j]
                        del other.unit[1][other.unit[1].index(
                            self.unit[1][len(self.unit[1])][j])]
            if len(self.unit[1][len(self.unit[1])]) > len(
                    other.unit[1][len(other.unit[1])]):
                for j in range(len(other.unit[1][len(other.unit[1])])):
                    if other.unit[1][len(other.unit[1])][j] in len(
                            self.unit[1]):
                        del other.unit[1][len(other.unit[1])][j]
                        del self.unit[1][self.unit[1].index(
                            other.unit[1][len(other.unit[1])][j])]

        for i in range(len(self.unit[0]) - 1):
            new_unit_above.append(self.unit[0][i])
        for i in range(len(other.unit[0]) - 1):
            new_unit_above.append(other.unit[1][i])

        for i in range(len(self.unit[1]) - 1):
            new_unit_above.append(self.unit[1][i])
        for i in range(len(other.unit[1]) - 1):
            new_unit_above.append(other.unit[0][i])

        new_unit_above_ary = self.unit[0][len(self.unit[0])] + other.unit[1][
            len(other.unit[1])]
        new_unit_under_ary = self.unit[1][len(self.unit[1])] + other.unit[0][
            len(other.unit[0])]

        new_unit_above.append(new_unit_above_ary)
        new_unit_under.append(new_unit_under_ary)
        new_unit.append(new_unit_above).append(new_unit_under)

        ans = self.value / other.value

        return Ufloat(ans, new_unit)

    def __pow__(self, other):
        new_unit_above = [1]
        new_unit_above_ary = []
        new_unit_under = [1]
        new_unit_under_ary = []
        new_unit = []

        for i in range(other):
            for j in range(len(self.unit[0]) - 1):
                new_unit_above.append(self.unit[0][j])

            for i in range(len(self.unit[1]) - 1):
                new_unit_above.append(self.unit[1][i])

            new_unit_above_ary += self.unit[0][len(self.unit[0])]
            new_unit_under_ary += self.unit[1][len(self.unit[1])]

        new_unit_above.append(new_unit_above_ary)
        new_unit_under.append(new_unit_under_ary)
        new_unit.append(new_unit_above).append(new_unit_under)

        ans = self.value ** other

        return Ufloat(ans, new_unit)


if __name__ == '__main__':
    test = Ufloat(100, m)
    print(test)