class Unit(object):

    def __init__(self, name, distance):
        self.name = str(name)
        self.distance = float(distance)

    def __str__(self):
        return self.name


# Length Define
m = Unit('m', 1)
km = Unit('km', 1000)

# TODO: 本当はそれぞれクラスで書きたい。名前空間が汚れるため。
# class m(Unit):
#
#     def __str__(self):
#         return 'm'
#
# ufloat(100, m()) とかの使い方は冗長なので、ufloat(100, m)とかで使いたい。
# しかし、インスタンス生成しないとメソッド使えないので str(m) としても <'class' m >となる。
# クラスメソッド化はありかも。→ ダメだった

# class N(Unit):
#
#     @staticmethod
#     def __str__():
#         return 'N'
#
# if __name__ == '__main__':
#     print(N)
#
# >>> <class '__main__.N'>
