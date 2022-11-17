# power.py

class CumulativePowerFactory:
    def __init__(self, exponent=2, *, start=0):
        self._exponent = exponent
        self.total = start

    def __call__(self, base):
        power = base ** self._exponent
        self.total += power
        return power


x1 = CumulativePowerFactory()
print(x1(21))
print(x1(42))
print(x1.total)
x3 = CumulativePowerFactory(exponent=2, start=3)
print(x3(3))
