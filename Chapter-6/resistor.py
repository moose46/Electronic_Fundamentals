# Chapter-6/resistor.py

"""
# - Contains functions to calculate series and parallel voltages, current and total resistance
# - serve this page by using python -m mkdocs serve from the command line

"""
from dataclasses import fields
import traceback


class Resistor:
    """Attributes of one resistor
    """

    def __init__(self, ohms: [int, float]):
        """
        Parameters:
            ohms[int | float]: Value of the resistor in ohms

        Examples:
        >>> r1 = Resistor(ohms=100)

        >>> r1.current(25)
        0.25

        >>> r1.voltage_drop(1000,10)
        1.0

        >>> r1.power(10)
        1.0

        >>> r1.ohms
        100
    """

        self._ohms = ohms
        self._volts = 10
        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        self._def_name = text[:text.find('=')].strip()

    @property
    def symbol(self):
        return self._def_name

    @property
    def ohms(self):
        return self._ohms

    def current(self, voltage):
        return round(float(voltage / self._ohms), 2)

    @property
    def volts(self, volts):
        self._volts = volts

    @volts.setter
    def volts(self, value):
        self._volts = value

    def voltage_drop(self, total_resistance, voltage):
        """
        # Voltage drop equals the resistance divided by the  total resistance multiplied by the voltage
        - vd = r/rt * v
        :param total_resistance:
        :param voltage:
        :return:
        """
        return float((self._ohms / total_resistance) * voltage)

    def power(self, voltage):
        """
        ## Power equals current squared times resistance
        - P = I * I * R
        Examples:
            >>> Ri = Resistor(100)

            >>> Ri.ohms
            100
        """
        return round(float(self.current(voltage) ** 2 * self._ohms), 2)


class Series:
    """
    ## Passed a list of resistor values, and voltages, it will calculate voltage drop across each resistor , total resistance and total current
    """

    def __init__(self, resistors: list[Resistor], vs: [int, float]):
        """
        - resistors is a list of resistors in ohms
        - vs is the voltage source in volts
        Examples:
            >>> r10 = Resistor(10)
            >>> s2 = Series([r10,r10],10)
            >>> s2.volts # volts
            10

        param resistors:list[int,float]
        param volts:[int,float]
        """
        self._resistors = resistors
        self._volts = vs
        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        self._def_name = text[:text.find('=')].strip()

    @property
    def rt(self):
        """
        rt = r1 + r2 + r3 + r...
        Examples:
            >>> r33 = Resistor(33)
            >>> r68 = Resistor(68)
            >>> s3 =Series([r33, r68], 10)
            >>> s3.rt
            101

        return: Total Ohms in the series circuit
        """
        rt = 0
        [rt := rt + r.ohms for r in self._resistors]
        return rt

    @property
    def it(self):
        """
        it = volts/rt
        Examples:
            >>> r100 = Resistor(100)
            >>> s4 = Series([r100,r100], 10)
            >>> s4.it
            0.05

        return: Total Current in the series circuit
        """
        it = self._volts / self.rt
        return round(it, 2)

    @property
    def voltage_drops(self):
        """
        voltage_drop = resistance/rt * volts
        Examples:
            >>> R100 = Resistor(100)
            >>> R200 = Resistor(200)
            >>> s5 = Series([R100,R200],100)
            >>> s5.voltage_drops
            {'R100=100Ω': 33.33, 'R200=200Ω': 66.67}

        {'R1=100Ω': 5.0, 'R2=100Ω': 5.0}

        return: Voltage drop dictionary, for each resitor in the circuit
        """
        drops = dict()
        n = 1
        for r in self._resistors:
            drops[f'{r.symbol.upper()}={r.ohms}\u03A9'] = round((r.ohms / self.rt) * self.volts, 2)
            n += 1
        return drops

    @property
    def volts(self):
        """
        Examples:

        :return:
        """
        return self._volts

    @volts.setter
    def volts(self, value):
        self._volts = value

    def __repr__(self):
        return f"rt={self.rt} \u03A9" \
               f"\nvolts({self._volts})={self.voltage_drops}" \
               f"\nit={self.it}"


class Parallel:
    """Class will calculate current, total ohms for parallel resistors"""

    def __init__(self, resistors: list[Resistor], volts: [int | float] = 1):
        self._resistors = resistors
        self._volts = volts

        for r in self._resistors:
            r.volts = self._volts

    def rt(self) -> float:
        total = 0
        [total := total + r.ohms ** -1 for r in self._resistors]
        return round(float(total ** -1), 2)


r33 = Resistor(33)
r68 = Resistor(68)
r3 = Resistor(100)
r4 = Resistor(47)
r5 = Resistor(10)
x = Series([r33, r68, r3, r4, r5], 10)
print(x)

r6 = Resistor(100)
s1 = Series([r6, r6], 10)
print(s1)

p1 = Parallel([r3, r3])
print(p1.rt())
