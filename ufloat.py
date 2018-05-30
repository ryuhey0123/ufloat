class ufloat(float):

    def __init__(self, x):
        float.__init__(self, x)


if __name__ == '__main__':
    test = ufloat(100)
    print(test)
