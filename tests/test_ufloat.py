from ufloat.ufloat import ufloat
from ufloat.units import m, km

# Working directory is project root directory.


class Test_ufloat:

    # インスタンスが正しく生成できるかの確認
    def test_make_instance(self):
        test = ufloat(100, m)
        assert isinstance(test, ufloat)

    def test_is_float_instance_by_float(self):
        test = ufloat(100.0, m)
        assert isinstance(test.x, float)

    def test_is_float_instance_by_int(self):
        test = ufloat(100, m)
        assert isinstance(test.x, float)

    def test_is_float_instance_by_str(self):
        test = ufloat('100', m)
        assert isinstance(test.x, float)

    # str()で正しく出力できるかの確認
    def test_str_func(self):
        test = ufloat(100.0, m)
        assert str(test) == '100.0 m'

    # 加算が正しく行われるかの確認
    # ufloat + ufloat
    def test_instance_add_by_ufloat_and_ufloat(self):
        test1 = ufloat(100, m)
        test2 = ufloat(1, km)
        ans = test1 + test2
        assert isinstance(ans, ufloat)

    def test_add_by_ufloat_and_ufloat(self):
        test1 = ufloat(100, m)
        test2 = ufloat(1, km)
        ans = test1 + test2
        assert str(ans) == '1100.0 m'

    # ufloat + float
    def test_instance_add_by_ufloat_and_float(self):
        test1 = ufloat(100, m)
        test2 = 1000.0
        ans = test1 + test2
        assert isinstance(ans, ufloat)

    def test_add_by_ufloat_and_float(self):
        test1 = ufloat(100, m)
        test2 = 1000.0
        ans = test1 + test2
        assert str(ans) == '1100.0 m'

    # ufloat + str
    def test_instance_add_by_ufloat_and_str(self):
        test1 = ufloat(100, m)
        test2 = '1000'
        ans = test1 + test2
        assert isinstance(ans, ufloat)

    def test_add_by_ufloat_and_str(self):
        test1 = ufloat(100, m)
        test2 = '1000'
        ans = test1 + test2
        assert str(ans) == '1100.0 m'

    # ufloat + bool
    def test_instance_add_by_ufloat_and_bool(self):
        test1 = ufloat(100, m)
        test2 = True
        ans = test1 + test2
        assert isinstance(ans, ufloat)

    def test_add_by_ufloat_and_bool(self):
        test1 = ufloat(100, m)
        test2 = True
        ans = test1 + test2
        assert str(ans) == '101.0 m'

    # ufloat + int
    def test_instance_add_by_ufloat_and_int(self):
        test1 = ufloat(100, m)
        test2 = 1000
        ans = test1 + test2
        assert isinstance(ans, ufloat)

    def test_add_by_ufloat_and_int(self):
        test1 = ufloat(100, m)
        test2 = 1000
        ans = test1 + test2
        assert str(ans) == '1100.0 m'
