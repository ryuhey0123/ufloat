# TODO: ディレクトリ構成が微妙。名前かぶりすぎ


class ufloat(object):

    def __init__(self, x, unit):
        self.x = float(x)
        self.unit = unit

    def __str__(self):
        """ str(),print()で呼び出される。値と単位を文字列に変換し,1スペースあけて出力 """
        return str(self.x) + " " + str(self.unit)

    def __float__(self):
        """ float()で呼び出される。値をfloat型に変換し値のみ出力 """
        return float.__float__(self.x)

    def __add__(self, other):
        """
        '+'演算子によって呼び出される。数値同士を計算し、単位をつけてufloat型で返す。
        優先単位は最初の項。otherがfloatの場合は、同一単位を解釈しselfの単位で出力。
        :param other: ufloat or other
        :return: ufloat
        """
        if isinstance(other, ufloat):
            distance = other.unit.distance * self.unit.distance
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
