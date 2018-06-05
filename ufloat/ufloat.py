# TODO: ディレクトリ構成が微妙。名前かぶりすぎ
# from ufloat.units import Unit


class ufloat(object):

    def __init__(self, x, unit, factor=None):
        self.x = float(x)
        # self.unit = Unit(unit, factor) #調整中
        self.unit = unit

    def __str__(self):
        """ str(),print()で呼び出される。値と単位を文字列に変換し出力 """
        return '{} {}'.format(self.x, self.unit)

    def __float__(self):
        """ float()で呼び出される。値のみ出力 """
        return self.x

    def __add__(self, other):
        """
        '+'演算子によって呼び出される。数値同士を計算し、単位をつけてufloat型で返す。
        優先単位は最初の項。otherがfloatの場合は、同一単位を解釈しselfの単位で出力。
        :param other: ufloat or other
        :return: ufloat
        """
        if isinstance(other, ufloat):
            distance = other.unit.factor * self.unit.factor
        else:
            distance = 1.0
        try:
            ans = float(other) * distance + self.x
        finally:
            # TODO: 例外処理
            pass
        return ufloat(ans, self.unit)

    # TODO: 引き算
    # TODO: 掛け算(ヤバイ)
    # TODO: 割り算(ヤバイ)
    # TODO: 乗算(ヤバイ)
