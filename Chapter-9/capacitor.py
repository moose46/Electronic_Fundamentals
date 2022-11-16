__author__ = 'Robert W. Curtiss'
__project__ = 'Fluent Python'

#
# Author: Robert W. Curtiss
# capacitor.py was created on October 19, 2022 @ 7:18 PM
# Project: Electronic Fundamentals
# python -m pip install mkdocs
# python -m pip install "mkdocstrings[python]"
# python -m pip install mkdocs-material
#
import math

DEGREE_SYMBOL = "\u03B1"
class Capacitor:
    def __init__(self, capacitance: [int | float] = 2.2e-6, ohms: [int | float] = 10e3, volts: [int | float] = 50.0):
        self.capacitance = capacitance
        self.ohms = ohms
        self.volts: [int | float] = volts

    @property
    def get_volts(self):
        """ Returns volts
        Examples:
            >>> c = Capacitor()

            >>> c.volts
            50.0

            """
        return self.volts

    @get_volts.setter
    def set_volts(self, value: [int | float]):
        self.volts = value

    def discharge_time(self, time: [int | float]):
        return self.volts * (math.exp(-(time / self.time_constant)))

    def charge_time(self, time: [int | float]):
        return self.volts * (1 - math.exp(-(time / self.time_constant)))

    @property
    def time_constant(self):
        """ Returns 1 time constant for capacitance and ohms provided """
        return self.ohms * self.capacitance

    def __repr__(self):
        return f'{self.capacitance}\u03BCF {self.ohms:,}\u03A9 tc={self.time_constant:e} seconds'


# c = Capacitor(capacitance=4.7e-6, ohms=1e6)
# print(c)
#
# c = Capacitor(capacitance=3300e-12, ohms=270e3)
# print(c)
#
# print(c.charge_time(50e-6))

c = Capacitor(capacitance=.01e-6, ohms=8.2e3)
print(c)
print(f'Charge Time = {c.charge_time(10e-6):.3f} volts @ Time = {10e-6} ')
print(f'Charge Time = {c.charge_time(50e-6):.3f} volts @ Time = {50e-6}')
print(f'Discharge Time = {c.discharge_time(10e-6):.3f} volts @ Time = {10e-6}')
c = Capacitor(capacitance=2.2e-6, ohms=10e3, volts=10)
print(c.time_constant)
print(f'Discharge Time = {c.discharge_time(6e-3):.3f} volts @ Time = {10e-3}')
# Related problem 9-12 pp.406-407 2.2uF, 2.2K ohms and 1ms
c = Capacitor(capacitance=2.2e-6, ohms=2.2e3, volts=10)
print(c.time_constant)
print(f'Discharge Time = {c.discharge_time(1e-3):.3f} volts @ Time = {10e-3}')

# print(f'{c.charge_time(20e-6):.3f} volts')
# print(f'{c.charge_time(30e-6):.3f} volts')
# print(f'{c.charge_time(40e-6):.3f} volts')
# print(f'{c.charge_time(50e-6):.3f} volts')
# print(f'{c.charge_time(60e-6):.3f} volts')
# print(f'{c.charge_time(70e-6):.3f} volts')
# print(f'{c.charge_time(80e-6):.3f} volts')
# print(f'{c.charge_time(400e-6):.3f} volts')
#
# z = [(x, c.charge_time(x * 1e-6)) for x in range(10, 410, 10)]
# for x in z:
#     print(f'{x[0]},{x[1]}')
# print("==================")
# z = [(x, c.discharge_time(x * 1e-6)) for x in range(0, 410, 10)]
# for x in z:
#     print(f'{x[0]},{x[1]}')
