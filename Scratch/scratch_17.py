from math import exp
from functools import singledispatchmethod
from series import Series
from fractions import Fraction
import math

OMEGA = '\u03A9'
MU = '\u03BC'
THETA = '\u03B8'


class ParallelResistorFactory:
    def __init__(self, ohms: [int | float | list] = 0):
        self._ohms = ohms
        self._resistors = list()
        self._total_resistance = Series(ohms)

    def __call__(self, base):
        self._resistors.append(base)
        total = 0
        for r in self._resistors:
            total += r ** -1
        self._total_resistance = 1 / total

        return self._total_resistance

    @property
    def resistors(self):
        return self._resistors

    @property
    def total(self):
        return self._total_resistance.value

    def __repr__(self):
        return (f"{self.__class__.__name__}(" \
                f'{self._total_resistance} \u03A9)')


class SeriesCapacitorFactory:
    def __init__(self, farads: [int | float] = 0):
        self._total = 0
        self._farads = farads
        self._capacitors = Series(farads)

    def __call__(self, base):
        self._capacitors.append(base)
        total = 0
        for c in self._capacitors:
            total += c ** -1
        self._total = 1 / total

        return self._total

    @property
    def capacitors(self):
        return self._capacitors

    @property
    def total(self):
        return self._total

    def __repr__(self):
        return f'{self._total} {MU}F'


class CapacitiveReactance:

    def __init__(self, farads=.0047e-6, frequency=1e3):
        """
        calculates capacitive reactance (Xc) when passed the farads and the frequency
        :param farads:
        :param frequency:
        """
        self._farads = farads
        self._frequency = frequency

    @property
    def Xc(self):
        """ return capacitive reactance"""
        return 1 / (2 * math.pi * self._farads * self._frequency)

    def I(self, voltage):
        """ return current at voltage level """
        return voltage / self.Xc

    def frequency(self, ohms):
        """ returns frequency of a """
        return 1 / (2 * math.pi * self._farads * ohms)

    def __repr__(self):
        return f'Xc={self.Xc:,.2f}'


class ImpedanceTriangle:
    """ Calculate phase angle and impedance of an ac rc circuit """

    def __init__(self, xc: [int | float] = 100.0, resistance: [int | float] = 47.0, current: [int | float] = 0,
                 volts: [int | float] = 0):
        """
        :xc: capacitive reactance
        :resistance: resistance
        """
        self._xc = xc
        self._r = resistance
        self._current = current
        self._volts = volts

    @property
    def current(self):
        # if self._current == 0:
        self._current = self._volts / self.impedance
        return self._current

    @current.setter
    def current(self, current: [int | float]):
        self._current = current

    @property
    def volts(self):
        return self._current * self.impedance

    def phase_angle(self):
        """ arctangent * xc / resistance """
        return math.degrees(math.atan(self._xc / self._r))

    @property
    def impedance(self):
        """ square root of xc 2 + resistance 2 """
        return math.sqrt(self._xc ** 2 + self._r ** 2)

    def __repr__(self):
        return f'{OMEGA} = {self.impedance:,.1f}  {THETA} = {self.phase_angle():.1f} volts={self.volts:,.2f}' \
               f' current={self.current:.2f}'


class Impedance:
    def __init__(self, xc: [int | float], ohms: [int | float]):
        self._xc = xc
        self._ohms = ohms

    @property
    def impedance(self):
        """ square root of xc 2 + resistance 2 """
        return math.sqrt(self._xc ** 2 + self._ohms ** 2)

    def __repr__(self):
        return f'Z={self.impedance}'

# x = ParallelResistorFactory()
# x(100)
# x(100)
# x(100)
# print(x.resistors)
# print(x)
# y = SeriesCapacitorFactory()
# y(.01e-6)
# y(.01e-6)
# y(.01e-6)
# print(y.capacitors)
# print(y)
# z = ParallelResistorFactory()
# z.from_list([100, 100, 100])
# print(z)
# print(ParallelResistorFactory(100))
# print(ParallelResistorFactory.from_list([100, 100]))
y = ParallelResistorFactory(100)

print(y.total)
y(200)
print(y)
y(200)
print(y)
x = ParallelResistorFactory([100, 100, 100, 400, 4.5])

print(f'x={Fraction(x.total)}')
x = CapacitiveReactance(farads=4700e-6, frequency=120)

print(f'{x.Xc:,} {OMEGA}')

x = CapacitiveReactance()
print(x.frequency(10e6))

ex915 = CapacitiveReactance(farads=.0056e-6, frequency=10e3)
print(ex915.Xc)
print(f'I = {ex915.I(voltage=5)} Amps')

example_10_1 = ImpedanceTriangle()
print(example_10_1)

i = ImpedanceTriangle(xc=50e3, resistance=33e3)
print(i)
example_10_2 = CapacitiveReactance(farads=.01e-6, frequency=1e3)
xc = example_10_2.Xc
print(example_10_2)
t = ImpedanceTriangle(xc=xc, resistance=10e3)
print(t)
print("Related Problem")
example_10_2 = CapacitiveReactance(farads=.01e-6, frequency=2e3)
xc = example_10_2.Xc
print(example_10_2)
t = ImpedanceTriangle(xc=xc, resistance=10e3)
t.current = 200e-6
print(t)
print("Example 10-3")
example_10_3 = CapacitiveReactance(farads=022e-6, frequency=1.5e3)
print(example_10_3)
z = Impedance(xc=example_10_3.Xc, ohms=2.2e3)
print(z)